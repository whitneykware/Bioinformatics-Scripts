import matplotlib.pyplot as plt
import time
import random


class Lists:
    length = []
    time = []

    def __init__(self, num):
        self.num = num

    def create_list(self):
        for _ in range(1, self.num+1):
            random_int = random.randint(1, 100)
            random_list = [random.randint(1, 100) for _ in range(random_int)]
            self.length.append(len(random_list))
            start = time.time()
            random_list.sort()
            end = time.time()
            total_time = end-start
            self.time.append(total_time)

    def get_info(self):
        print(self.length, self.time)

    def plot_time(self):
        plt.scatter(self.length, self.time)
        plt.title('Time Spent to Sort List')
        plt.xlabel('List Length')
        plt.ylabel('Time(s)')
        plt.xlim(0, max(self.length))
        plt.ylim(0, max(self.time))
        plt.show()


x = Lists(1000)
x.create_list()
x.plot_time()
