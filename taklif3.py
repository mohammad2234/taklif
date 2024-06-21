class min_Heap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.heapify_up(len(self.heap) - 1)

    def get_min(self):
        if self.heap:
            return self.heap[0]
        return None

    def del_min(self):
        if len(self.heap) > 1:
            self._swap(0, len(self.heap) - 1)
            min_val = self.heap.pop()
            self.heapify_down(0)
            
        elif self.heap:
            min_val = self.heap.pop()
            
        else:
            min_val = None
        return min_val

    def heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self._swap(index, parent_index)
            self.heapify_up(parent_index)

    def heapify_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self._swap(index, smallest)
            self.heapify_down(smallest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

def heap_sort(list_of_numbers):
    heap = min_Heap()
    sorted_list = []

    for number in list_of_numbers:
        heap.insert(number)

    while heap.heap:
        sorted_list.append(heap.del_min())

    return sorted_list

