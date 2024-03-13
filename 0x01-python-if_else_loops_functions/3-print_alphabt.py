#!/usr/bin/python3
for char in range(ord('a'), ord('z') + 1):
    # Skip 'q' and 'e' by checking their ASCII codes
    if chr(char) not in ('q', 'e'):
        print(chr(char), end="")
