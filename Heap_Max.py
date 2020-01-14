"""
Max heap with a list.
It's designed to get the biggest value in a heap (list)
"""


class Heap:

    def __init__(self):
        self.list = None

    def insert(self, data):
        if self.list is None:
            self.list = [None]#to make the first index '1' for convinence
            self.list.append(data)#and then append the data
        else:
            self.list.append(data)#once append
            last_idx = len(self.list) - 1
            while True:
                if last_idx == 1:#when it's right to the right of the head (None)
                    break
                parent_idx = last_idx // 2
                if self.list[last_idx] > self.list[parent_idx]:#when the parent is smaller than the newly added one
                    self.list[last_idx], self.list[parent_idx] = self.list[parent_idx], self.list[last_idx]
                    last_idx = parent_idx#change last one to parent idx and goes while loop again
                else:
                    break

    def get(self):
        if self.list is None:
            print('No data to get')
        else:
            data = self.list[1]
            self.list[1] = self.list[-1] #last one goes to head
            del self.list[-1] #delete the last one
            current_idx = 1
            while True:
                left_child = current_idx * 2
                right_child = current_idx * 2 + 1
                if left_child >= len(self.list) and right_child >= len(self.list):#when it has no children
                    break
                elif right_child >= len(self.list):#when it has only left child
                    if self.list[current_idx] < self.list[left_child]:
                        self.list[current_idx], self.list[left_child] = self.list[left_child], self.list[current_idx]
                        current_idx = left_child
                    else:
                        break
                else:#when it has both children
                    if self.list[left_child] >= self.list[right_child]:#get the greater child
                        child_to_swap = left_child
                    else:
                        child_to_swap = right_child
                    if self.list[current_idx] < self.list[child_to_swap]:#when it's smaller than greater child
                        self.list[current_idx], self.list[child_to_swap] = self.list[child_to_swap], self.list[current_idx]
                        current_idx = child_to_swap
                    else:#otherwise stop!
                        break
            return data


heap = Heap()
