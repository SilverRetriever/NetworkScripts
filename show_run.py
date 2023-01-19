from netmiko import ConnectHandler

cisco_881 = {
    'device_type': 'cisco_ios',
    'host':   '10.0.0.50',
    'username': 'ciscotest',
    'password': 'ciscotest',

}

net_connect = ConnectHandler(**cisco_881)

output = net_connect.send_command('show run')
print(output)