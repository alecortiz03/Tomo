import serial
import time

# Set this to your ESP32's USB serial device (often /dev/ttyUSB0 or /dev/ttyACM0)
SERIAL_PORT = '/dev/ttyUSB0'  # Change as needed!
BAUD_RATE = 115200

with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
    # Turn LED on
    ser.write(b'LED_ON\n')
    print("LED ON command sent")

    time.sleep(3)

    # Turn LED off
    ser.write(b'LED_OFF\n')
    print("LED OFF command sent")
