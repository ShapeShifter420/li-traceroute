from core.try_data import TryData
import socket


def print_data(result: TryData):
    try:
        name = socket.gethostbyaddr(result.addr)[0]
    except socket.herror:
        name = 'Unknown server'
    finally:
        f_time = round(result.get_midle_sum() * 1000, 2)
        print(f'{result.addr:<15}    {name:<50}   {f_time} ms')
