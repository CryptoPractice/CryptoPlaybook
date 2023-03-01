# Jagacha

## Introduction

A challenge that exploits the random function implementation of CPython using the Mersenne Twister algorithm.

## Info for Participants

### Challenge Description

As a wise man once said, there is no greater happiness in life than to hit a homerun with your SSS-tier gacha pulls on the first try. However, reality is not that easy. Therefore, we are providing a chance for you to pull the SSS-rarity flag if you can guess the number correctly. However, if you are still unsure of your chances of guessing it right, you're always welcome to do a random gacha pull until you change your mind.

Note: Submit the flag in all caps.

### Additional Information

Serve the files in `dist/` as an attachment for participants

## Info for HTB

### Access

None.

### Key Processes

- Source code can be found in the `src/` directory

### Automation / Crons

None

### Firewall Rules

Allow port `8080` as it is the exposed port used by the container.

### Docker

- [Dockerfile](./server/Dockerfile)

### Other

The flag is `STF22{W@IFU5_L@1FU5}`.

## Writeup

See `xpl.py`. Similar writeups are available online for other mersenne twister challenges generating 32-bit random numbers. The only difference is that this challenge generates 64-bit numbers instead, thereby needing only half the 624 random rolls (312 rolls) is needed to recreate the Mersenne Twister memory state.
