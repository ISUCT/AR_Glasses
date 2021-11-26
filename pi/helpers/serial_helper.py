import serial, sys
from serial import SerialException
from time import sleep

# serial configuration
serial_comm = serial.Serial()
serial_comm.baudrate = 9600
serial_comm.port = '/dev/cu.usbserial-110'
serial_comm.timeout = 10 #in seconds

def send_data_to_arduino(text_data):
    try:
        if serial_comm.isOpen():
            sleep(2)
            serial_comm.write(bytearray(text_data, 'utf-8'))
            serial_comm.flush()
            serial_comm.close()
    except SerialException as ex:
        print(ex)

def open_serial_connection():
    try:
        serial_comm.open()
    except SerialException as ex:
        print(ex)

def close_serial_connection():
    try:
        serial_comm.close()
    except SerialException as ex:
        print(ex)