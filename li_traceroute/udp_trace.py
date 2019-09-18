import time
import select
from li_traceroute.try_data import TryData
from li_traceroute.print_method import print_data
from li_traceroute.socket_maker import *

BASE_TRY_NUM = 3
DEFAULT_COUNT_BYTE = 1024
MAX_TIME = 3


def get_route(addr: str, hop: int, base_port: int) -> list:
    res_data = []
    complete = False
    for ttl in range(1, hop+1):
        if complete:
            print('Complete')
            break
        cur = None
        result = TryData()
        print(f'{str(ttl)+")":<6}', end='')

        for num_of_try in range(BASE_TRY_NUM):
            with make_socket_udp(ttl) as udp_socket,\
                    make_socket_icmp(ttl, base_port) as icmp_socket:
                udp_socket.sendto(''.encode(), (addr, base_port + ttl))
                send_time = time.time()
                try:
                    in_select_socket = select.select([icmp_socket], [], [],
                                                     MAX_TIME)
                    if not in_select_socket[0]:
                        break
                    _, cur = icmp_socket.recvfrom(DEFAULT_COUNT_BYTE)
                    recv_time = time.time()
                    cur = cur[0]
                    result.addr = cur
                    result.add(num_of_try, recv_time-send_time)
                except socket.timeout:
                    continue

        if not result.count_of_success:
            print('* * *')

        if cur is not None:
            print_data(result)
            res_data.append(result)

        if cur == addr:
            print('Complete')
            break

        if ttl == hop:
            print("End of max hop")
            break
    return res_data
