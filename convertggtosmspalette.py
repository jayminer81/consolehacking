#!/usr/bin/env python

# This is a simple program to convert from Game Gear palette format
# to the Master System format. It simply skips the least significant
# bits so some manual tweaking might improve the result.

# Usage: ./convertggtosmspalette.py <entry1> <entry2> ...

# Example: ./convertggtosmspalette.py FF0F 370A 0F00 will give the
# result 3F 21 03

# Todo: Add error-checking and a description of the command if no
# argument is given.

import sys

length = len(sys.argv)

for loop in range (1, length):
  x = int(sys.argv[loop], 16)
  r = (x & 0x0f00) >> 10
  g = (x & 0xf000) >> 14
  b = (x & 0x000f) >> 2

  smsg = g << 2
  smspal = b << 4
  smspal = smspal | r | smsg

  print format(smspal,'02X'),
