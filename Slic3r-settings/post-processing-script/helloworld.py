#!/usr/bin/env python3

import sys
INCOMING_GCODE_FILE = sys.argv[1]
OUTPUT_GCODE_FILE = INCOMING_GCODE_FILE+'.out'

print ('This is the name of your G-Code file: {0}'.format(INCOMING_GCODE_FILE))
print("output file: {0}".format(OUTPUT_GCODE_FILE))

temp = []
with open(INCOMING_GCODE_FILE) as fi:
  temp = fi.readlines()
  # print(''.join(fi.readlines()))


  temp.append('helloworld')

with open(OUTPUT_GCODE_FILE, "w") as fo:
  fo.writelines(temp)