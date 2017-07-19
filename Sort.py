from random import *
import sys

sys.setrecursionlimit(2000)


class Sort:
    def __init__(self):
        self.data_list = []

    def __len__(self):
        return len(self.data_list)

    def swap(self, index1, index2):
        temp = self.data_list[index1]
        self.data_list[index1] = self.data_list[index2]
        self.data_list[index2] = temp

    def selection_sort(self):
        if not self.data_list:
            return
        n = len(self)
        for i in range(n):
            for j in range(n):
                if self.data_list[j] > self.data_list[i]:
                    self.swap(i, j)

    def quick_sort(self, first, last):
        if first >= last:
            return
        i = first
        j = last - 1
        pivot = self.data_list[last]
        while True:
            while self.data_list[i] <= pivot and i <= last-1:
                i += 1
            while self.data_list[j] > pivot and j > first:
                j -= 1
            if i >= j:
                break
            self.swap(i, j)
            i += 1
            j -= 1
        if self.data_list[j] < pivot:
            j += 1
        self.swap(j, last)
        self.quick_sort(j+1, last)
        self.quick_sort(first, j-1)

    def merge_sort(self, first, last):
        if first >= last:
            return
        middle = int((first + last)/2)
        self.merge_sort(first, middle)
        self.merge_sort(middle + 1, last)
        self.merge(first, middle, last)

    def merge(self, first, middle, last):
        n1 = middle - first + 1
        n2 = last - middle
        temp_list1 = []
        temp_list2 = []
        for i in range(n1):
            temp_list1.append(self.data_list[first + i])
        for i in range(n2):
            temp_list2.append(self.data_list[i + middle + 1])
        i = 0
        j = 0
        k = first
        while True:
            if i < n1:
                if j < n2:
                    if temp_list1[i] < temp_list2[j]:
                        self.data_list[k] = temp_list1[i]
                        i += 1
                        k += 1
                    else:
                        self.data_list[k] = temp_list2[j]
                        j += 1
                        k += 1
                else:
                    self.data_list[k] = temp_list1[i]
                    k += 1
                    i += 1
            else:
                if j < n2:
                    self.data_list[k] = temp_list2[j]
                    j+=1
                    k+=1
                else:
                    break

    def heap_sort(self):
        n = len(self)
        for i in range(int(n/2) - 1, -1, -1):
            self.heapify(i, n)
        count = 0
        for i in range(n-1, -1, -1):
            count+=1
            self.swap(i, 0)
            self.heapify(0, n-count)

    def heapify(self, i, n):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < n and self.data_list[left] > self.data_list[largest]:
            largest = left
        if right < n and self.data_list[right] > self.data_list[largest]:
            largest = right
        if largest == i:
            return
        else:
            self.swap(largest, i)
            self.heapify(largest, n)




new_list = []
for i in range(20):
    new_int = randint(1, 80)
    new_list.append(new_int)
print(new_list)

my_sort = Sort()
my_sort.data_list = new_list
my_sort.heap_sort()
print(my_sort.data_list)

