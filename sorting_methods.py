import matplotlib.pyplot as plt
import time
import random
import copy


class SortList:
    bub_time = []
    ins_time = []
    merge_time = []
    tim_time = []
    length = []
    lists = []

    def __init__(self, num):
        self.num = num
        print("Original Lists: ")
        for i in range(1, num+1):
            random_list = random.sample(range(200), i)
            self.lists.append(random_list)
            self.length.append(len(random_list))
            print(random_list)

    def display(self):
        print("Original Lists: {}".format(self.lists))

    def bubble_sort(self):
        print("Bubble Sort: ")
        bub_list = copy.deepcopy(self.lists)
        for x in bub_list:
            start = time.time()
            n = len(x)
            for i in range(n):
                swapped = False
                for j in range(0, n-i-1):
                    if x[j] > x[j+1]:
                        x[j], x[j+1] = x[j+1], x[j]
                        swapped = True
                if swapped == False:
                    break
            end = time.time()
            self.bub_time.append(end-start)
            print(x)

    def insertion_sort(self):
        print("Insertion Sort: ")
        ins_list = copy.deepcopy(self.lists)
        for x in ins_list:
            start = time.time()
            for i in range(1, len(x)):
                key = x[i]
                j = i - 1
                while j >= 0 and key < x[j]:
                    x[j+1] = x[j]
                    j = j - 1
                x[j+1] = key
            end = time.time()
            self.ins_time.append(end-start)
            print(x)

    def merge_sort_method(self, a_list):
        if len(a_list) > 1:
            mid = len(a_list) // 2
            left = a_list[:mid]
            right = a_list[mid:]

            self.merge_sort_method(left)
            self.merge_sort_method(right)

            i = 0
            j = 0
            k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    a_list[k] = left[i]
                    i = i + 1
                else:
                    a_list[k] = right[j]
                    j = j + 1
                k = k + 1
            while i < len(left):
                a_list[k] = left[i]
                i = i + 1
                k = k + 1
            while j < len(right):
                a_list[k] = right[j]
                j = j + 1
                k = k + 1

    def merge_sort(self):
        print("Merge Sort: ")
        mer_list = copy.deepcopy(self.lists)
        for x in mer_list:
            start = time.time()
            self.merge_sort_method(x)
            end = time.time()
            self.merge_time.append(end-start)
            print(x)

    def tim_sort(self):
        print("TimSort: ")
        tim_list = copy.deepcopy(self.lists)
        for x in tim_list:
            start = time.time()
            x = sorted(x)
            end = time.time()
            self.tim_time.append(end-start)
            print(x)

    def plot_time(self):
        fig, pl = plt.subplots()
        pl.plot(self.length, self.bub_time, 'b', label='Bubble Sort')
        pl.plot(self.length, self.ins_time, 'k', label='Insertion Sort')
        pl.plot(self.length, self.merge_time, 'g', label='Merge Sort')
        pl.plot(self.length, self.tim_time, 'r', label='TimSort')
        pl.legend()
        pl.set_title('Time Spent to Sort List')
        pl.set_xlabel('List Length')
        pl.set_ylabel('Time(s)')
        pl.set_xlim(1, self.num)
        plt.show()


a = SortList(50)

a.bubble_sort()
a.insertion_sort()
a.merge_sort()
a.tim_sort()
a.plot_time()
