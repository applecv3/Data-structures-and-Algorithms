'''
Basic Linked List using 2 classes
'''


class Node:#to create each node

    def __init__(self, data, next=None):#data and a pointer to the next node
        self.data = data
        self.next = next


class NodeManager:

    def __init__(self):
        self.head = None#empty head

    def add(self, data):#add value at the end of the linked list

        if self.head is None:
            self.head = Node(data)

        else:
            node = self.head
            while node.next:#it ends at the last node
                node = node.next
            node.next = Node(data)

    def read(self):#print data in each node in order

        if self.head is None:
            print('No data to print')

        else:
            node = self.head
            while node.next:
                print(node.data)
                node = node.next
            print(node.data)#print the last one

    def search(self, idx):#search a node with index
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

    def insert(self, data_to_insert, before_data):#insert a new node before a certain data
        if self.head is None:
            print('No data to insert in')
            return
        if before_data == self.head.data:#when the data is in the head node
            new = Node(data_to_insert)
            #connecting nodes
            new.next = self.head
            self.head = new
            return
        else:
            node = self.head
            while node.next:
                if node.next.data == before_data:
                    new = Node(data_to_insert)
                    #insert the new node
                    new.next = node.next
                    node.next = new
                    return
                else:
                    node = node.next
        print('No such data to insert before')

    def delete(self, data):#delete a node with a certain value
        if self.head is None:
            print('No data to delete from')
            return
        if self.head.data == data:#when the data is data in the head
            self.head = self.head.next

        else:#it handles when the data is in the middle of the linked list or the last one both.

            node = self.head

            while node.next:
                if data == node.next.data:
                    node.next = node.next.next
                    return
                else:
                    node = node.next

            print('No such data to delete')


LinkedList = NodeManager()

for i in range(10):
    LinkedList.add(i)
