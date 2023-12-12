selfIp = '10.100.200.1'
hosts = [f'h{i}' for i in range(1, 7)]
ports = [f'900{i}' for i in range(6)]
addrs = ['10.10.101.2', '10.10.101.3', '10.10.102.2', '10.10.102.3', '10.10.103.2', '10.10.103.3']
nets = ['10.10.1.1', '10.10.2.1', '10.10.3.1']

def grab_config():
    return selfIp, hosts, ports, addrs, nets