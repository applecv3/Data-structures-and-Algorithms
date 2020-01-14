"""
Min heap with a list.
It's designed to get the smallest value in a heap (list)
"""


class Heap:

    def __init__(self):
        self.list = None

    def insert(self, data):
        if self.list is None:
            self.list = [None]#to make the first value's idx 1 for convinence
            self.list.append(data)#add the new data
        else:
            self.list.append(data)#once add!
            current_idx = len(self.list) - 1
            while True:
                if current_idx == 1:#when the current value is right next to the 'None' stop
                    break
                parent_idx = current_idx // 2#to compare with its parent
                if self.list[current_idx] < self.list[parent_idx]:#if current is smaller than its parent swap!
                    self.list[current_idx], self.list[parent_idx] = self.list[parent_idx], self.list[current_idx]
                    current_idx = parent_idx
                else:#otherwise stop
                    break

    def get(self):
        data = self.list[1]#data to return
        self.list[1] = self.list[-1]#lift up the last value
        del self.list[-1]#delete
        current_idx = 1
        while True:
            left_child = current_idx * 2
            right_child = current_idx * 2 + 1
            if left_child >= len(self.list) and right_child >= len(self.list):#when the current one has no children stop!
                break
            elif right_child >= len(self.list):#when it has only left child
                if self.list[current_idx] > self.list[left_child]:
                    self.list[current_idx], self.list[left_child] = self.list[left_child], self.list[current_idx]
                    current_idx = left_child
                else:
                    break
            else:#when it has both children
                if self.list[left_child] <= self.list[right_child]:#get the smaller child to compare with
                    child_to_swap = left_child
                else:
                    child_to_swap = right_child
                if self.list[current_idx] > self.list[child_to_swap]:#swap
                    self.list[current_idx], self.list[child_to_swap] = self.list[child_to_swap], self.list[current_idx]
                    current_idx = child_to_swap
                else:#stop
                    break

        return data


head = Heap()
