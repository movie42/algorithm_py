# HEAP


class Heap:
    def __init__(self, data):
        self.heap_array = []
        self.heap_array.append(None)
        self.heap_array.append(data)

    def move_up(self, inserted_idx):
        if inserted_idx <= 1:
            return False
        if self.heap_array[inserted_idx] > self.heap_array[inserted_idx // 2]:
            return True
        else:
            return False

    def insert(self, data):
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)
        insert_idx = len(self.heap_array) - 1
        while self.move_up(insert_idx):
            parent_idx = insert_idx // 2
            if self.heap_array[insert_idx] > self.heap_array[parent_idx]:
                self.heap_array[insert_idx], self.heap_array[parent_idx] = (
                    self.heap_array[parent_idx],
                    self.heap_array[insert_idx],
                )
            insert_idx = parent_idx
        return True

    def pop(self):
        if len(self.heap_array) <= 1:
            return None

        pop_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        self.heap_array = self.heap_array[:-1]

        pop_idx = 1

        while pop_idx < len(self.heap_array):
            left = pop_idx * 2
            right = pop_idx * 2 + 1

            if left < len(self.heap_array) and right < len(self.heap_array):
                if self.heap_array[left] > self.heap_array[right]:
                    if self.heap_array[pop_idx] < self.heap_array[left]:
                        self.heap_array[pop_idx], self.heap_array[left] = (
                            self.heap_array[left],
                            self.heap_array[pop_idx],
                        )
                        pop_idx = left
                        left = pop_idx * 2
                    else:
                        break
                else:
                    if self.heap_array[pop_idx] < self.heap_array[right]:
                        self.heap_array[pop_idx], self.heap_array[right] = (
                            self.heap_array[right],
                            self.heap_array[pop_idx],
                        )
                        pop_idx = right
                        right = pop_idx * 2
                    else:
                        break
            elif (
                left < len(self.heap_array)
                and self.heap_array[left] > self.heap_array[pop_idx]
            ):
                self.heap_array[pop_idx], self.heap_array[left] = (
                    self.heap_array[left],
                    self.heap_array[pop_idx],
                )
                pop_idx = left
                left = pop_idx * 2
            elif (
                right < len(self.heap_array)
                and self.heap_array[right] > self.heap_array[pop_idx]
            ):
                self.heap_array[pop_idx], self.heap_array[right] = (
                    self.heap_array[right],
                    self.heap_array[pop_idx],
                )
                pop_idx = right
                right = pop_idx * 2
            else:
                break

        return pop_data


# Test
data_list = [23, 50, 100, 2, 4, 5, 8, 29, 44, 55, 76, 34]
heap = Heap(1)

for i in data_list:
    heap.insert(i)

print(heap.heap_array)

for i in range(len(data_list)):
    heap.pop()
    print(heap.heap_array)
