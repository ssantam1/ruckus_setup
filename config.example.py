hostname = 'TestHostname'
ip_address = '192.168.1.2'
subnet_mask = '255.255.255.0'
default_gateway = '192.168.1.1'

# Sample username and password
username = 'admin'
password = 'admin' 


# Configuration commands
commands = [
    {
        'command': 'enable',
        'validators': ['#'],  # Expect privileged prompt
    },
    {
        'command': 'conf t',
        'validators': ['(config)#'],  # Expect config prompt
    },
    {
        'command': f'hostname {hostname}',
        'validators': [f'{hostname}(config)#'],
    },
    {
        'command': f'ip address {ip_address} {subnet_mask}',
        'validators': ['Interface IP address is set'],
    },
    {
        'command': f'ip default-gateway {default_gateway}',
        'validators': ['Default gateway is set'],
    },
    {
        'command': 'crypto-ssl certificate generate',
        'wait_for': 'ssl-certificate creation is successful',  # Don't close connection until this is seen
        'validators': ['Creating certificate, please wait'],
    },
    {
        'command': 'exit',
        'validators': ['#'],  # Expect privileged prompt
    },
]