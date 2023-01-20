from napalm import get_network_driver
import json

driver = get_network_driver('ios')
device = driver('10.0.0.50', 'ciscotest', 'ciscotest')
device.open()
print(json.dumps(device.get_bgp_neighbors(), indent=2))
device.close()