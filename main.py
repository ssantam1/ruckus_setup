import serial
import time
import config

def send_command(ser: serial.Serial, command: str, sleep=1):
    ser.write((command + '\n').encode())
    time.sleep(sleep)
    response = ser.read_all().decode()
    return response

def send_command_with_wait(ser: serial.Serial, command, wait_for=None):
    response = send_command(ser, command)
    if wait_for:
        print(response, end='')
        while wait_for not in response:
            time.sleep(1)
            response = ser.read_all().decode()
    return response

def main():
    ser = serial.Serial(
        port=input('Enter COM port: '),
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )

    if ser.is_open:
        print("Serial connection established.")
    else:
        print("Failed to establish serial connection.")
        return

    commands = config.commands

    # Send a blank input to find out if we need to login or not
    response = send_command('')
    print(response, end='')

    # Send commands and print output as if you were doing it manually
    for command in commands:
        if isinstance(command, tuple):
            response = send_command_with_wait(ser, command[0], wait_for=command[1])
        else:
            response = send_command(ser, command)
        print(response, end='')

    ser.close()

if __name__ == "__main__":
    main()