import socket
import struct

MAX_TIME = 3


def make_socket_udp(num):
    proto_u = socket.getprotobyname('udp')
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, proto_u)
    udp_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, num)
    return udp_socket


def make_socket_icmp(num, base_port):
    icmp_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW,
                                socket.getprotobyname("icmp"))
    icmp_socket.setsockopt(socket.IPPROTO_IP, socket.IP_TTL,
                           struct.pack('I', num))
    icmp_socket.settimeout(MAX_TIME)
    icmp_socket.bind(('', base_port + num))
    return icmp_socket
