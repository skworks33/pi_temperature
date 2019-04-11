#coding: utf-8

##################
# sensor: DS18D20
##################

import datetime
import csv

DATA_DIR = 'log/'
DEVICE_ID = '00-ffffffffffff'

record_datetime = datetime.datetime.now()
record_filename = 'temp_data_' + record_datetime.strftime('%Y%m%d') + '.csv'
record_datetime = record_datetime.strftime('%Y-%m-%d %H:%M:%S')

# get temperature
temp_file = open("/sys/bus/w1/devices/" + DEVICE_ID + "/w1_slave")
w1_slave_text = temp_file.read()
temp_file.close()
temp_data = w1_slave_text.split("\n")[1].split(" ")[9]
temperature = float(temp_data[2:]) / 1000
print record_datetime + ',' + str(temperature)

# save csv
csv_file = open(DATA_DIR + record_filename, 'a')  # append mode
writer = csv.writer(csv_file, lineterminator='\n')
writer.writerow([record_datetime, temperature])
csv_file.close()
