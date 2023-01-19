from netmiko import ConnectHandler

cisco_881 = {
    'device_type': 'cisco_ios',
    'host':   '10.0.0.50',
    'username': 'ciscotest',
    'password': 'ciscotest',

}

net_connect = ConnectHandler(**cisco_881)

config_commands = [ 'config t',
                    'interface e0/2',
                    'no shut',
                    'ip add 6.6.6.6 255.255.255.0',
                    'no logging console' ]
output = net_connect.send_config_set(config_commands)

output = net_connect.send_command('show run | section Ethernet0/2')

print(output)