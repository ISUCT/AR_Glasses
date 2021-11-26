import serial, sys
from serial import SerialException
from time import sleep

# serial configuration
serial_comm = serial.Serial()
serial_comm.baudrate = 9600
serial_comm.port = '/dev/cu.usbserial-110'
serial_comm.timeout = 10 #in seconds

def send_data_to_arduino(text_data):
    if serial_comm.isOpen():
        sleep(2)
        serial_comm.write(bytearray(text_data, 'utf-8'))
        serial_comm.flush()
        serial_comm.close()

def open_serial_connection():
    serial_comm.open()

def close_serial_connection():
    serial_comm.close()
