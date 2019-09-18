### Простой трассировщик исплоьзующий UDP(как в linux) или ICMP(как в windows) протокол. Ключи ставятся перед адрессом и максималны количеством прыжков.
+ "sudo python3 traceroute.py -g www.yandex.ru 30" - рисует график
* "sudo python3 traceroute.py -I www.yandex.ru 30" - использует ICMP протокол
* "sudo python3 traceroute.py -I -g www.yandex.ru 30" - использует ICMP протокол и рисует график
* "sudo python3 traceroute.py --help" - вызывает помошь
* "sudo python3 traceroute.py -p 33434 www.yandex.ru 30" - указать интерисующий порт

#### Дополнительные возможности:
* Создание граффика на основе полученных данных
