hostname = 'TestHostname'
ip_address = '192.168.1.2'
subnet_mask = '255.255.255.0'
default_gateway = '192.168.1.1'

# Basic configuration commands
commands = [
    'enable',  # Enter privileged exec mode
    'conf t',  # Enter global configuration mode
    'hostname ' + hostname,  # Set hostname
    'ip address ' + ip_address + ' ' + subnet_mask,  # Set IP address
    'ip default-gateway ' + default_gateway,  # Set default gateway
    ('crypto-ssl certificate generate', 'ssl-certificate creation is successful'),  # Generate RSA key and wait for prompt
    'exit',  # Exit global configuration mode
]