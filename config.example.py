hostname = 'TestHostname'
ip_address = '192.168.1.2'
subnet_mask = '255.255.255.0'
default_gateway = '192.168.1.1'

# Sample username and password
username = 'admin'
password = 'admin' 


# Configuration commands
commands = [
    {  # Enable privileged mode
        'command': 'enable',
        'validators': ['#'],  # Expect privileged prompt
    },
    {  # Enter config mode
        'command': 'conf t',
        'validators': ['(config)#'],  # Expect config prompt
    },
    {  # Set hostname
        'command': f'hostname {hostname}',
        'validators': [f'{hostname}(config)#'],
    },
    {  # Set IP address and subnet mask
        'command': f'ip address {ip_address} {subnet_mask}',
    },
    {  # Set default gateway
        'command': f'ip default-gateway {default_gateway}',
    },
    {  # Generate SSL certificate
        'command': 'crypto-ssl certificate generate',
        'wait_for': 'ssl-certificate creation is successful',  # Don't close connection until this is seen
        'validators': ['Creating certificate, please wait'],
    },
    {  # Create user for management
        'command': f'username {username} password {password}',
        'validators': ['User created successfully'],
    },
    {  # Generate RSA key pair
        'command': 'crypto key generate rsa',
        'validators': ['Key already exists. Please zeroize it', 'Creating RSA key pair, please wait'],
    },
    {  # Set timezone
        'command': 'clock timezone us Eastern',
    },
    {  # Enter interface configuration mode
        'command': 'int e1/1/1 to 1/1/24',
        'validators': ['(config-mif-1/1/1-1/1/24)#'],
    },
    {  # Set inline power priority
        'command': 'inline power priority 1 power-by-class 2\n',
    },
    {  # Return to config mode
        'command': 'exit',
        'validators': ['(config)#'],
    },
    {  # Return to privileged mode
        'command': 'exit',
        'validators': ['#'],
    }
]