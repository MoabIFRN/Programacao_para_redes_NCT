import struct
import time

def write_tcpdump_file(file_name, packet_data_list):
    # Cabeçalho do arquivo
    magic_number = 0xa1b2c3d4
    major_version = 2
    minor_version = 4
    reserved1 = 0
    reserved2 = 0
    snap_len = 65535
    fcs = 1
    link_type = 1

    header = struct.pack('IHHIIII', magic_number, major_version, minor_version,
                         reserved1, reserved2, snap_len, (fcs << 24) | link_type)

    with open(file_name, 'wb') as file:
        file.write(header)

        for packet_data in packet_data_list:
            # Informações do pacote
            timestamp_seconds = int(time.time())
            timestamp_microseconds = int((time.time() - timestamp_seconds) * 1000000)
            captured_packet_length = len(packet_data)
            original_packet_length = len(packet_data)

            packet_header = struct.pack('IIII', timestamp_seconds, timestamp_microseconds,
                                        captured_packet_length, original_packet_length)

            file.write(packet_header)
            file.write(packet_data)

# Exemplo de uso
packet_data_list = [b'\x01\x02\x03\x04', b'\x05\x06\x07\x08']
write_tcpdump_file('exemplo.cap', packet_data_list)

# Indicar que o script foi executado com sucesso
print("Script executado com sucesso!")


