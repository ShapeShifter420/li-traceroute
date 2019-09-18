import unittest
from unittest import TestCase
import li_traceroute.traceroute as t
import li_traceroute.udp_trace as udp
import li_traceroute.icmp_trace as icmp
import socket
from li_traceroute.try_data import TryData


class Test_makegraf(TestCase):
    def test_justmake(self):
        r_data = []
        result = TryData()
        result.add(0, 0.2)
        result.add(1, 0.01)
        result.add(2, 0.1)
        result.addr = '111.111.111.111'
        for i in range(15):
            r_data.append((result))
        t.get_graf(r_data)

    def test_makemanyseconds(self):
        r_data = []
        result = TryData()
        result.add(0, 3)
        result.add(1, 0.01)
        result.add(2, 3)
        result.addr = '111.111.111.111'
        for i in range(15):
            r_data.append(result)
        t.get_graf(r_data)

    def test_makelowseconds(self):
        r_data = []
        result = TryData()
        result.add(0, 0.003)
        result.add(1, 0.01)
        result.add(2, 0.000001)
        result.addr = '111.111.111.111'
        for i in range(15):
            r_data.append(result)
        t.get_graf(r_data)

    def test_nodata(self):
        r_data = []
        t.get_graf(r_data)

    def test_makesmany(self):
        r_data = []
        result = TryData()
        result.add(0, 0.2)
        result.add(1, 0.01)
        result.add(2, 0.1)
        result.addr = '111.111.111.111'
        for i in range(255):
            r_data.append((result))
        t.get_graf(r_data)

    def test_shortip(self):
        r_data = []
        result = TryData()
        result.add(0, 0.2)
        result.add(1, 0.01)
        result.add(2, 0.1)
        result.addr = '1.1.1.1'
        for i in range(15):
            r_data.append((result))
        t.get_graf(r_data)


# class Test_Just(TestCase):
#    def test_yandex30(self):
#        addr = socket.gethostbyname('yandex.ru')
#        udp.get_route(addr, 30, 33434)

#    #def test_yandex1(self):
#        #addr = socket.gethostbyname('yandex.ru')
#        #udp.get_route(addr, 1, 33434)

#    #def test_wikipedia(self):
#       #addr = socket.gethostbyname('ru.wikipedia.org')
#        #udp.get_route(addr, 30, 33434)

#    #def test_i_yandex30(self):
#        #addr = socket.gethostbyname('yandex.ru')
#        #icmp.get_route(addr, 30, 33434)

#    #def test_i_yandex1(self):
#       #addr = socket.gethostbyname('yandex.ru')
#        #icmp.get_route(addr, 1, 33434)

#    #def test_i_wikipedia(self):
#        #addr = socket.gethostbyname('ru.wikipedia.org')
#        #icmp.get_route(addr, 30, 33434)

if __name__ == '__main__':
    unittest.main()
