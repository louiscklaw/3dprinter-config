#!/usr/bin/env python3

import os,sys,re
import math

import decimal

def float_range(start, stop, step):
  while start < stop:
    yield float(start)
    start += decimal.Decimal(step)

STEP='0.2'
RAMP_LAYER_START=3

START_TEMP=210; END_TEMP=193; RAMP_TEMP = list(reversed(list(float_range(END_TEMP,START_TEMP, STEP))))

LAYER_START=3;
RAMP_LAYER = list(range(RAMP_LAYER_START, RAMP_LAYER_START+len(RAMP_TEMP),1))

START_SPEED=65; END_SPEED=200; RAMP_SPEED = list(range(START_SPEED, END_SPEED, int(math.ceil((END_SPEED-START_SPEED)/len(RAMP_TEMP)))))



RAMP_TEMP.append(END_TEMP)
RAMP_SPEED.append(END_SPEED)
RAMP_LAYER.append(RAMP_LAYER[-1]+1)
from pprint import pprint

# pprint(list(RAMP_TEMP))
# pprint(list(RAMP_SPEED))
# pprint(list(RAMP_LAYER))

# pprint(len(list(RAMP_TEMP)))
# pprint(len(list(RAMP_SPEED)))
# pprint(len(list(RAMP_LAYER)))

# sys.exit()

print(';RAMP START')
print('{if layer_num < 2}')
print('   M220 S65')
print('   M104 S210')
# for temperature, layer, speed in zip(RAMP_TEMP, RAMP_LAYER, RAMP_SPEED):
for i in range(0,len(RAMP_TEMP)):
  layer = RAMP_LAYER[i]
  temperature = RAMP_TEMP[i]
  # speed = RAMP_SPEED[i] if i <= len(RAMP_SPEED) else END_SPEED
  speed = RAMP_SPEED[i] if i < len(RAMP_SPEED) else END_SPEED

  print('{elsif layer_num < '+str(layer)+'}')
  print(f'   ; M118 setting change: T{temperature} L{layer} S{speed}')
  print('   M220 S'+str(speed))
  print('   M104 S'+str(temperature))
  print()

print('{else}')
print('   M118 RAMPING DONE')
print('{endif}')