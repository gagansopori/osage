"""This file will contain all the constants & what-not that will be used across this application.
"""
# System Constants
CPU_TEMPERATURE_FILE = '/sys/class/thermal/thermal_zone0/temp'

# Sensor Specific Constants
OXIDIZING_GASES = 'in0/gnd'
REDUCING_GASES = 'in1/gnd'
NH3_AMMONIA = 'in2/gnd'
TMP_36 = 'ref/gnd'
MICS6814_HEATER_PIN = 24

# Generic Constants
WARM_UP_TIME = 600
