import socket, sys

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        resultado = sock.connect_ex((host, port))

        if resultado == 0:
            print(f"A porta {port} está aberta")
        else:
            print(f"A porta {port} está fechada")

        sock.close()
    except socket.error:
        print(f"Erro ao conectar à porta {port}")

def main():
    host = input("Digite o endereço do host: ")
    try:
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("Não foi possível resolver o nome do host.")
        return

    ports = [22, 23, 25, 80, 443, 8080]

    for port in ports:
        scan_port(ip, port)

if __name__ == "__main__":
    main()

