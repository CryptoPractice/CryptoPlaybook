#!/usr/bin/env python3

import random

from pwn import *

HOST = "127.0.0.1"
PORT = 8080

N = 624
M = 397
MATRIX_A = 0x9908B0DF
UPPER_MASK = 0x80000000
LOWER_MASK = 0x7FFFFFFF


def tempering(y):
    y ^= y >> 11
    y ^= (y << 7) & 0x9D2C5680
    y ^= (y << 15) & 0xEFC60000
    y ^= y >> 18
    return y


def untempering(y):
    y ^= y >> 18
    y ^= (y << 15) & 0xEFC60000
    y ^= (((y << 7) & 0x9D2C5680) ^ ((y << 14) & 0x94284000) ^ ((y << 21) & 0x14200000) ^ ((y << 28) & 0x10000000))
    y ^= (y >> 11) ^ (y >> 22)
    return y


def generate(mt, kk):
    mag01 = [0x0, MATRIX_A]
    y = (mt[kk] & UPPER_MASK) | (mt[(kk + 1) % N] & LOWER_MASK)
    mt[kk] = mt[(kk + M) % N] ^ (y >> 1) ^ mag01[y & 0x1]


def genrand_int32(mt, mti):
    generate(mt, mti)
    y = mt[mti]
    mti = (mti + 1) % N
    return tempering(y), mti


def getrandbits(mt, mti, bits):
    assert bits == 32
    mt, mti = genrand_int32(mt, mti)
    return mt >> (32 - bits), mti


def get_mt_state(io):
    io.sendlineafter(b'> ', b'1')
    state = int(io.recvline_regex(b'STR: \d+').rpartition(b' ')[-1]) << 48
    state += int(io.recvline_regex(b'DEX: \d+').rpartition(b' ')[-1]) << 32
    state += int(io.recvline_regex(b'INT: \d+').rpartition(b' ')[-1]) << 16
    state += int(io.recvline_regex(b'LUK: \d+').rpartition(b' ')[-1])
    return state & 0xffffffff, state >> 32


def crack_next(states: list, n: int=32):
    assert len(states) == N

    mt = [0] * N
    mti = 0
    for state in states:
        mt[mti] = untempering(state)
        mti = (mti + 1) % N

    rand = random.Random()
    rand.setstate((rand.VERSION, tuple(mt + [N]), None))
    return rand.getrandbits(n)


if __name__ == "__main__":
    with remote(HOST, PORT) as io:
        states = [state for _ in range(N//2) for state in get_mt_state(io)]
        next_state = crack_next(states, 64)

        io.sendlineafter(b'> ', b'2')
        io.sendlineafter(b'Enter your lucky number: ', str(next_state).encode())
        print(io.recvall().decode())
