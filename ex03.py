import socket

sites = [
    "www.google.com",
    "www.globo.com",
    "www.metropoledf.com.br",
    "www.olx.com.br",
    "www.ifrn.edu.br",
    "www.youtube.com",
    "www.tudoazul.com",
    "www.tjrn.jus.br",
    "www.udemy.com",
    "www.amazon.com"
]

def get_ip_addresses(hostname):
    try:
        ip_addresses = socket.gethostbyname_ex(hostname)
        return ip_addresses[2]
    except socket.gaierror:
        return []

for site in sites:
    ip_addresses = get_ip_addresses(site)
    if ip_addresses:
        print(f"Endereços IP para {site}:")
        for ip in ip_addresses:
            print(ip)
    else:
        print(f"Não foi possível obter os endereços IP para {site}")
        
