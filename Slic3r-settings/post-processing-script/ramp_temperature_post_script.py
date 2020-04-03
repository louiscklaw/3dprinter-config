#!/usr/bin/env python3
import os,sys,re
import math
from pprint import pprint
import decimal

temp = []


def float_range(start, stop, step):
  while start < stop:
    yield float(start)
    start += decimal.Decimal(step)

STEP='2'
RAMP_LAYER_START=3



START_TEMP=int(sys.argv[1])
FINAL_TEMP=int(sys.argv[2])
RAMP_TEMP = list(reversed(list(float_range(FINAL_TEMP,START_TEMP, STEP))+[START_TEMP]))

LAYER_START=1
RAMP_LAYER = list(range(RAMP_LAYER_START, RAMP_LAYER_START+len(RAMP_TEMP),1))

START_SPEED=int(sys.argv[3])
FINAL_SPEED=int(sys.argv[4])
RAMP_SPEED = list(range(START_SPEED, FINAL_SPEED, int(math.ceil((FINAL_SPEED-START_SPEED)/len(RAMP_TEMP)))))

print('start temp : {}'.format(START_TEMP))
print('final temp : {}'.format(FINAL_TEMP))
print('start speed: {}'.format(START_SPEED))
print('final speed: {}'.format(FINAL_SPEED))

def update_when_layer_change(in_gcode, layer_num):
  return "hellowlrd layer change"

def get_temp_table():
  output = []
  for i in range(0,len(RAMP_TEMP)):
    layer = RAMP_LAYER[i]
    temperature = RAMP_TEMP[i]
    # speed = RAMP_SPEED[i] if i <= len(RAMP_SPEED) else END_SPEED
    speed = RAMP_SPEED[i] if i < len(RAMP_SPEED) else FINAL_SPEED
    output.append([temperature, speed])
  return output

temp_table=get_temp_table()
layer_change=0
with open(sys.argv[-1],'r+') as fi:
  temp = fi.readlines()

  # layer changing to [layer_num]
  for i in range(0,len(temp)):
    if temp[i].find('layer changing to ') > 0:
      if layer_change < len(temp_table):
        change_comment=temp[i]
        layer_temperature = temp_table[layer_change][0]
        layer_speed = temp_table[layer_change][1]
        change_M220='M220 S'+ str(layer_speed)
        change_M104='M104 S'+ str(layer_temperature)

        temp[i]='\n'.join([change_comment, change_M220, change_M104])
        # print('findme {}'.format(i))
        # sys.exit()
        layer_change+=1
      else:
        change_comment=temp[i]+'\n; temp ramping done'
        temp[i]=change_comment

with open(sys.argv[-1],'w') as fo:
  fo.writelines(''.join(temp))
