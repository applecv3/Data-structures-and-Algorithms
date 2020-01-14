'''
Doubly Linked List using 2 classes
'''


class Node:

    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev #each node has one more pointer for the previous node!
        self.next = next


class NodeManager:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0 #to use when searching backward

    def add(self, data):#add new data from head

        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
            self.length += 1
        else:
            node = self.head

            while node.next:
                node = node.next
            #create and add the new node
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new#new node becomes tail
            self.length += 1

    def read_from_head(self):#print from the head
        if self.head is None:
            print('No data to print from')
            return
        node = self.head
        while node.next:
            print(node.data)
            node = node.next#go to the next node
        print(node.data)

    def read_from_tail(self):#print from the tail
        if self.tail is None:
            print('No data to print from')
            return
        node = self.tail
        while node.prev:
            print(node.data)
            node = node.prev
        print(node.data)

    def search_from_head(self, idx):#search the data of a certain node with index from the head
        if self.head is None:
            print('No data to search in')
            return
        node = self.head
        c = 0 #to count idx
        while node.next or c == 0:
            if idx == c:
                print(node.data)
                return
            else:
                c += 1
                node = node.next
        #when it's the last one
        if idx == c:
            print(node.data)
            return
        else:
            print('No such index in the list')

    def search_from_tail(self, idx):#search the data of a certain node with index from the tail
        if self.tail is None:
            print('No data to search in')
            return
        idx = self.length - idx - 1
        node = self.tail
        c = 0
        while node.prev or c == 0:
            if idx == c:
                print(node.data)
                return
            else:
                c += 1
                node = node.prev
        if idx == c:
            print(node.data)
            return
        else:
            print('No such index in the list')

    def delete_from_head(self, data):#delete a certain node by searching from head
        if self.head is None:
            print('No data to delete in')
            return
        if data == self.head.data:#when the data is data in the head
            self.head = self.head.next
            self.length -= 1
        else:
            node = self.head
            while node.next:
                if data == node.next.data and node.next.next is None:#when the data is the last one
                    node.next = None#delete the next node
                    self.tail = node#switch the tail to the current node
                    self.length -= 1
                    return
                elif data == node.next.data:#when the data is between
                    #switching nodes
                    node.next.next.prev = node
                    node.next = node.next.next
                    self.length -= 1
                    return
                else:
                    node = node.next
            print('No such data to delete')

    def delete_from_tail(self, data):#delete a certain node by searching from tail
        if self.tail is None:
            print('No data to delete in')
            return
        if data == self.tail.data:
            self.tail = self.tail.prev
            self.length -= 1
        else:
            node = self.tail
            while node.prev:
                if data == node.prev.data and node.prev.prev is None:
                    node.prev = None
                    self.head = node
                    self.length -= 1
                    return
                elif data == node.prev.data:
                    node.prev.prev.next = node
                    node.prev = node.prev.prev
                    self.length -= 1
                    return
                else:
                    node = node.prev
            print('No such data to delete')

    def insert_from_head(self, data_to_insert, before_data):#insert a new node before a certain data from going through head
        if self.head is None:
            print('No data to insert in')
            return
        if before_data == self.head.data:#when the data is in the head node
            new = Node(data_to_insert)
            #connecting nodes
            self.head.prev = new
            new.next = self.head
            self.head = new
            self.length += 1
            return
        else:
            node = self.head
            while node.next:
                if node.next.data == before_data:
                    new = Node(data_to_insert)
                    #insert the new node
                    new.next = node.next
                    new.prev = node
                    node.next.prev = new
                    node.next = new
                    self.length += 1
                    return
                else:
                    node = node.next
        print('No such data to insert before')

    def insert_from_tail(self, data_to_insert, after_data):#insert a new node after a certain data from going through head
        if self.head is None:
            print('No data to insert in')
            return
        if after_data == self.tail.data:
            new = Node(data_to_insert)
            self.tail.next = new
            new.prev = self.tail
            self.tail = new
            self.length += 1
            return
        else:
            node = self.tail
            while node.prev:
                if node.prev.data == after_data:
                    new = Node(data_to_insert)
                    new.prev = node.prev
                    new.next = node
                    node.prev.next = new
                    node.prev = new
                    self.length += 1
                    return
                else:
                    node = node.prev
        print('No such data to insert after')


linked_list = NodeManager()

for i in range(10):
    linked_list.add(i)
