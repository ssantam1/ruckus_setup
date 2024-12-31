import serial
import time

hostname = 'TestHostname'
ip_address = '10.1.100.49'
subnet_mask = '255.255.255.0'
default_gateway = '10.1.100.1'

def send_command(ser: serial.Serial, command, sleep=1, wait_for=None):
    ser.write((command + '\n').encode())
    time.sleep(sleep)
    response = ser.read_all().decode()
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

    # Basic configuration commands
    commands = [
        '',  # Send newline to find out if it wants a login 
        'enable',  # Enter privileged exec mode
        'conf t',  # Enter global configuration mode
        'hostname ' + hostname,  # Set hostname
        'ip address ' + ip_address + ' ' + subnet_mask,  # Set IP address
        'ip default-gateway ' + default_gateway,  # Set default gateway
        ('crypto-ssl certificate generate', 'ssl-certificate creation is successful'),  # Generate RSA key and wait for prompt
        'exit',  # Exit global configuration mode
    ]

    # Send commands and print output as if you were doing it manually
    for command in commands:
        if isinstance(command, tuple):
            response = send_command(ser, command[0], wait_for=command[1])
        else:
            response = send_command(ser, command)
        print(response, end='')

    ser.close()

if __name__ == "__main__":
    main()