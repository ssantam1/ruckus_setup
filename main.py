import serial
import serial.tools.list_ports
import time
import config
from enum import Enum

class AccessLevel(Enum):
    LOGGED_OUT = 0
    USER = 1
    PRIVILEGED = 2
    CONFIG = 3

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

        # Send newline to get a prompt and check current access level
        response = self.send_command('')
        self.access_level = self.check_access_level(response)

        if self.access_level is AccessLevel.LOGGED_OUT:
            response = self.login(response=response)
            self.access_level = self.check_access_level(response)

        assert self.access_level is not AccessLevel.LOGGED_OUT

    def check_access_level(self, response: str):
        if response.endswith('(config)#'):
            return AccessLevel.CONFIG
        elif response.endswith('#'):
            return AccessLevel.PRIVILEGED
        if response.endswith('>'):
            return AccessLevel.USER
        else:
            return AccessLevel.LOGGED_OUT
        
    def login(self, response:str=''):
        # We may need to cycle through a few prompts to get to the username prompt
        for _ in range(5):
            if 'Please Enter Login Name:' in response:
                break
            response = self.send_command('')
        else:
            raise Exception('Could not find login prompt')

        response = self.send_command(config.username)
        assert 'Please Enter Password:' in response
        response = self.send_command(config.password)
        assert 'User login successful' in response

        return response

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
    ports = serial.tools.list_ports.comports()
    if not ports:
        print('No COM ports found')
        return
    
    if len(ports) == 1:
        port = ports[0].device
    else:
        print('Multiple COM ports found:')
        print('\n'.join([('  ' + port.device) for port in ports]))
        port = input("Enter the desired COM port: ")
    
    print(f'Using COM port: {port}')
    conn = Connection(port)

    commands = config.commands

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