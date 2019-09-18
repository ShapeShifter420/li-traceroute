import socket
import matplotlib.pyplot as plt
import matplotlib
import li_traceroute.udp_trace as udp_trace
import sys
import li_traceroute.icmp_trace as icmp_trace
import argparse
from li_traceroute.try_data import TryData

TRACE_METHOD = udp_trace.get_route
STANDART_DPI = 80


def main():

    parser = argparse.ArgumentParser(description='traceroute argument')
    parser.add_argument('addr', type=str, help='dest addr')
    parser.add_argument('hop', type=str, help='max hop count')
    parser.add_argument('-g', action='store_true', help='make graf')
    parser.add_argument('-I', '--ICMP', action='store_true',
                        help='use ICMP method')
    parser.add_argument('-p', '--base_port',
                        default='33434', help='give base port')
    namespaces = parser.parse_args()
    if sys.platform == 'win32':
        print('work on this platform is not supported')
        exit(0)
    if not check_correct(namespaces):
        print('Please use correct input')
        exit(0)
    addr = socket.gethostbyname(namespaces.addr)
    hop = int(namespaces.hop)
    res_data = TRACE_METHOD(addr, hop, int(namespaces.base_port))

    if namespaces.g:
        get_graf(res_data)


def check_correct(argv):
    try:

        global TRACE_METHOD
        if argv.ICMP:
            TRACE_METHOD = icmp_trace.get_route
        socket.gethostbyname(argv.addr)
        if int(argv.hop) > 255:
            return False
        int(argv.base_port)

    except socket.gaierror:
        print('Not correct dest adr')
        return False

    except ValueError:
        print('Not correct hop count')
        return False

    return True


def get_graf(res_data):
    if res_data == []:
        result = TryData()
        result.ddr = 'No_Data'
        res_data.append(result)
    dpi = STANDART_DPI
    coef = round(len(res_data) / 25)
    if coef == 0:
        coef = 1
    fig = plt.figure(dpi=dpi, figsize=(512 * coef / dpi, 480 * coef / dpi))
    matplotlib.rcParams.update({'font.size': 8})
    plt.title('Traceroute')

    xs = range(len(res_data))

    plt.bar([x + 0.05 for x in xs], [v.all_try[0] for v in res_data],
            width=0.2, color='red', alpha=0.7, label='first try',
            zorder=2)
    plt.bar([x + 0.3 for x in xs], [v.all_try[1] for v in res_data],
            width=0.2, color='blue', alpha=0.7, label='second try',
            zorder=2)
    plt.bar([x + 0.55 for x in xs], [v.all_try[2] for v in res_data],
            width=0.2, color='green', alpha=0.7, label='third try',
            zorder=2)
    plt.xticks(xs, [d.addr for d in res_data])

    fig.autofmt_xdate(rotation=90)

    plt.legend(loc='upper right')
    fig.savefig('trace.svg')


if __name__ == '__main__':
    main()
