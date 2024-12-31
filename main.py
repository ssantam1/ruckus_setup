import serial
import time

def send_command(ser, command, sleep=1):
    ser.write((command + '\n').encode())
    time.sleep(sleep)
    response = ser.read_all().decode()
    return response

def main():
    # Configure the serial connection
    ser = serial.Serial(
        port=input('Enter COM port: '),  # Replace with your serial port
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )

    if ser.isOpen():
        print("Serial connection established.")
    else:
        print("Failed to establish serial connection.")
        return

    # Basic configuration commands
    commands = [
        'enable',
        'configure terminal',
        'hostname TestHostname',
        'exit'
    ]

    for command in commands:
        response = send_command(ser, command)
        print(f"Sent: {command}\nResponse: {response}")

    ser.close()

if __name__ == "__main__":
    main()