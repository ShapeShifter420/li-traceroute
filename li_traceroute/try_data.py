class TryData:

    def __init__(self, count_of_try: int = 3):
        self.count_of_success = 0
        self.all_try = []
        for num_of_try in range(count_of_try):
            self.all_try.append(0.0)
        self.addr = ''

    def add(self, num_of_try: int, value: float):
        self.all_try[num_of_try] = value
        self.count_of_success += 1

    def get_midle_sum(self):
        sum_all = 0
        for value in self.all_try:
            sum_all += value
        if not self.count_of_success:
            return 0.0
        return sum_all / self.count_of_success
