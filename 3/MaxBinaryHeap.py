import random
from typing import List


class Heap:
    def __init__(self, array: List[int]):
        self.array = array
        self.heapify()

    def heapify(self):
        for i in range(len(self.array) // 2, -1, -1):
            self.sift_down(i)

    def sift_down(self, i: int):
        while 2 * i + 1 < len(self.array):
            left = 2 * i + 1
            right = 2 * i + 2
            j = left
            if right < len(self.array) and self.array[left] < self.array[right]:
                j = right
            if self.array[i] >= self.array[j]:
                break
            self.array[i], self.array[j] = self.array[j], self.array[i]
            i = j

    def __str__(self):
        return str(self.array)


if __name__ == '__main__':
    array = [random.randint(0, 100) for _ in range(10)]
    heap = Heap(array)
    print(heap)


