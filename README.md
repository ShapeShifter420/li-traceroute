### Простой трассировщик использующий UDP(как в linux) или ICMP(как в windows) протокол. Ключи ставятся перед адресом и максимальным количеством прыжков.
+ "sudo python3 li-trace -g www.yandex.ru 30" - рисует график
* "sudo python3 li-trace -I www.yandex.ru 30" - использует ICMP протокол
* "sudo python3 li-trace -I -g www.yandex.ru 30" - использует ICMP протокол и рисует график
* "sudo python3 li-trace --help" - вызывает помощь
* "sudo python3 li-trace -p 33434 www.yandex.ru 30" - указать интересующий порт

#### Дополнительные возможности:
* Создание графика на основе полученных данных
