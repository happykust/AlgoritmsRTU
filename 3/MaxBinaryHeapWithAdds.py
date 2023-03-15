# Create a class "Binary heap" (maximum heap). Implement for class
# a constructor that forms a heap from an arbitrary array, a constructor by
# default (create an empty heap). For a class, implement methods: lookup
# maximum, removing the maximum, adding a new element to the heap, merging
# two heaps

class BinaryHeap:
    def __init__(self, array=None):
        if array is None:
            self.heap = []
        else:
            self.heap = array
            for i in range(len(self.heap) // 2, -1, -1):
                self.sift_down(i)

    def sift_down(self, i):
        while 2 * i + 1 < len(self.heap):
            left = 2 * i + 1
            right = 2 * i + 2
            j = left
            if right < len(self.heap) and self.heap[left] < self.heap[right]:
                j = right
            if self.heap[i] >= self.heap[j]:
                break
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j

    def sift_up(self, i):
        while i > 0 and self.heap[i] > self.heap[(i - 1) // 2]:
            self.heap[i], self.heap[(i - 1) // 2] = self.heap[(i - 1) // 2], self.heap[i]
            i = (i - 1) // 2

    def add(self, item):
        self.heap.append(item)
        self.sift_up(len(self.heap) - 1)

    def extract_max(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        max = self.heap.pop()
        self.sift_down(0)
        return max

    def get_max(self):
        return self.heap[0]

    def merge(self, other):
        self.heap.extend(other.heap)
        for i in range(len(self.heap) // 2, -1, -1):
            self.sift_down(i)

    def __str__(self):
        return str(self.heap)


if __name__ == "__main__":
    heap = BinaryHeap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(heap)
    heap.add(11)
    print(heap)
    heap.extract_max()
    print(heap)
    heap.merge(BinaryHeap([12, 13, 14, 15, 16, 17, 18, 19, 20]))
    print(heap)
