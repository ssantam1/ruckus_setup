import serial
import time
import config
from enum import Enum

class AccessLevel(Enum):
    LOGGED_OUT = 0
    USER = 1
    PRIVILEGED = 2
    CONFIG = 3

    def __lt__(self, other):
        if isinstance(other, AccessLevel):
            return self.value < other.value
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, AccessLevel):
            return self.value <= other.value
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, AccessLevel):
            return self.value > other.value
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, AccessLevel):
            return self.value >= other.value
        return NotImplemented

class Connection:
    def __init__(self, port):
        self.ser = serial.Serial(
            port=port,
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )

    def send_command(self, command: str, sleep=1):
        self.ser.write((command + '\n').encode())
        time.sleep(sleep)
        response = self.ser.read_all().decode()
        return response


    def send_command_with_wait(self, command: str, wait_for=None):
        response = self.send_command(command)
        if wait_for:
            print(response, end='')
            while wait_for not in response:
                time.sleep(1)
                response = self.ser.read_all().decode()
        return response
    
    def close(self):
        self.ser.close()

def main():
    port = input("Enter the COM port: ")
    conn = Connection(port)

    commands = config.commands

    # Send a blank input to find out if we need to login or not
    response = conn.send_command('')
    print(response, end='')


    # Send commands and print output as if you were doing it manually
    for command in commands:
        if isinstance(command, tuple):
            response = conn.send_command_with_wait(command[0], wait_for=command[1])
        else:
            response = conn.send_command(command)
        print(response, end='')

    conn.close()

if __name__ == "__main__":
    main()