import serial

# Change '/dev/ttyUSB0' if needed to match your device
SERIAL_PORT = '/dev/ttyUSB0'   # or '/dev/ttyACM0'
BAUD_RATE = 115200             # Must match Serial.begin() on ESP32

try:
    with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
        print(f"Connected to {SERIAL_PORT} at {BAUD_RATE} baud.")
        while True:
            line = ser.readline()
            if line:
                # decode bytes to string and remove trailing newline
                print(line.decode(errors='replace').strip())
except Exception as e:
    print(f"Could not open serial port: {e}")
