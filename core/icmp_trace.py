import socket
import struct
import time
import select
import os
from core.try_data import TryData
from core.print_method import print_data
from core.socket_maker import make_socket_icmp

BASE_TRY_NUM = 3
DEFAULT_COUNT_BYTE = 2048
MAX_TIME = 3
ICMP_ANSWER = 0
ICMP_TRACE = 11
ICMP_NO_ROUTE = 3
ICMP_HEAD = 8


def get_route(addr: str, hop: int, base_port: int) -> list:
    res_data = []
    complete = False

    for ttl in range(1, hop+1):
        if complete:
            print('Complete')
            break
        print(f'{str(ttl) + ")":<6}', end='')
        result = TryData()
        cur = None

        for num_of_try in range(BASE_TRY_NUM):
            with make_socket_icmp(ttl, base_port) as icmp_socket:
                icmp_socket.sendto(get_pack(), (addr, base_port + ttl))
                send_time = time.time()

                try:
                    select_socket = select.select([icmp_socket], [], [],
                                                  MAX_TIME)
                    if not select_socket[0]:
                        break
                    rec_pack, cur = icmp_socket.recvfrom(DEFAULT_COUNT_BYTE)
                    cur = cur[0]
                    result.addr = cur
                    recv_time = time.time()
                except socket.timeout:
                    continue
                else:

                    icmp_type, *_ = struct.unpack("bbHHh", rec_pack[20:28])
                    if icmp_type == ICMP_TRACE or icmp_type == ICMP_NO_ROUTE:
                        result.add(num_of_try, recv_time - send_time)
                    elif icmp_type == ICMP_ANSWER:
                        col = struct.calcsize("d")
                        s_time = struct.unpack("d", rec_pack[28:28 + col])[0]
                        result.add(num_of_try, recv_time - s_time)
                        complete = True
                    else:
                        break

        if not result.count_of_success:
            print('* * *')
        if cur is not None:
            print_data(result)
            res_data.append(result)
        if cur == addr:
            complete = True
        if ttl == hop:
            print('End of max hop')
    return res_data


def get_pack():
    os_id = os.getpid() & 0xFFFF
    head = struct.pack("bbHHh", ICMP_HEAD, 0, 0, os_id, 1)
    body = struct.pack("d", time.time())
    control_sum = socket.htons(get_sum(head + body))
    head = struct.pack("bbHHh", ICMP_HEAD, 0, control_sum, os_id, 1)
    return head + body


# Вычисление контрольной суммы для пакета
def get_sum(data):
    sum_of_data = 0
    len_of_operation = (len(data) // 2) * 2
    place = 0

    while place < len_of_operation:
        temp = data[place + 1] * 256 + data[place]
        place += 2
        sum_of_data = sum_of_data + temp
        sum_of_data = sum_of_data & 0xffffffff

    if len_of_operation < len(data):
        sum_of_data += ord(data[-1])
        sum_of_data = sum_of_data & 0xffffffff

    sum_of_data = (sum_of_data >> 16) + (sum_of_data & 0xffff)
    sum_of_data = sum_of_data + (sum_of_data >> 16)
    control = ~sum_of_data & 0xffff
    final = control >> 8 | (control << 8 & 0xff00)

    return final
