#!/usr/bin/env python3
from randcrack import RandCrack    # pip install randcrack
from pwn import *

def get_num(io):
    io.sendlineafter(b'> ', b'1')
    state = int(io.recvline_regex(r'STR: \d+').rpartition(b' ')[-1]) << 48
    state += int(io.recvline_regex(r'DEX: \d+').rpartition(b' ')[-1]) << 32
    state += int(io.recvline_regex(r'INT: \d+').rpartition(b' ')[-1]) << 16
    state += int(io.recvline_regex(r'LUK: \d+').rpartition(b' ')[-1])
    return state

def splithalf(num):
    # https://ctftime.org/writeup/14939  "getrandbits(64) you actually get getrandbits(32) << 32 | getrandbits(32)"
    lowerhalf = num & 0xffffffff
    upperhalf = num >> 32
    return upperhalf, lowerhalf

HOST="localhost"
PORT=8080
with remote(HOST, PORT) as io:
    
    cracker = RandCrack()
    for i in range(624 // 2):
        state = get_num(io)
        u, l = splithalf(state)
        cracker.submit(l)
        cracker.submit(u)

    guess = cracker.predict_getrandbits(64)

    #actual = get_num(io)
    #print("Guess: ", guess)
    #print("Actual: ", actual)
    #assert guess==actual, "RandCrack is not working."

    io.sendlineafter(b'> ', b'2')
    io.sendlineafter(b'Enter your lucky number: ', str(guess).encode())
    
    print(io.recvall().decode())
