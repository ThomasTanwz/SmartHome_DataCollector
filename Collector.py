# This program monitors a serial port that Arduino prints to; Collects the data and stores it in a CSV file
# Credit: https://github.com/Chams123456/Arduino_to_python/blob/master/DHT11_Arduino_to_Python.py

import schedule
import serial
import time
import csv
from kafka import KafkaProducer


# single_listen: listens to a port and outputs the data, then closes the port
def single_listen():
    # 9600 BAUD speed; port: ttyACM0(See platformIO project for specific parameters)
    port = "/dev/ttyACM0"
    baudrate = 9600
    ser = serial.Serial(port, baudrate)
    data = ser.readline()

    # start from index 0 but first character may be some weird stuff
    # TODO: data cleaning for csv
    decoded_values = data[0:len(data)].decode("ISO-8859-1").strip()
    list_values = decoded_values.split(' ')
    # sometimes the first character of serial output is a foreign character, we dont want that
    for items in list_values:
        if not items[0].isdecimal():
            list_values[0] = list_values[0][1:]
    print(f'Collected readings from Arduino: {list_values}')
    # producer = KafkaProducer(bootstrap_servers="10.32.143.242:9092", acks=1)
    # liststr = ''.join(list_values)
    # producer.send("utilizations", value=bytes(liststr, encoding="ascii"))
    # producer.flush()
    writedb("./DB.csv", list_values)
    list_values.clear()
    ser.close()


# listen: runs single listen in an infinite while loop with timeout
def listen():
    schedule.every(1).seconds.do(single_listen)
    while True:
        schedule.run_pending()
        time.sleep(1)


# writedb: write a single line(a list) to target file(CSV file)
def writedb(filename, listasline):
    with open(filename, 'a', newline='') as database:
        write = csv.writer(database)
        write.writerow(listasline)

listen()
