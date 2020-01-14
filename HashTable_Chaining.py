'''
Hash table with chaining technique with linked list
when it collides at some point it goes thorugh a linked list to add the new data in the next
of the last node
'''

import hashlib


class Node:#to create each node

    def __init__(self, data, next=None):#data and a pointer to the next node
        self.data = data
        self.next = next


class HashTable:

    def __init__(self, size):
        self.size = size
        self.hashtable = [None for _ in range(self.size)]

    def get_key(self, data):
        hash_object = hashlib.sha256()
        hash_object.update(data.encode())
        hex_digit = hash_object.hexdigest()
        return int(hex_digit, 16)

    def hash_function(self, key):
        return key % self.size

    def save_data(self, data, value):#save a certain data in the hash table
        key = self.get_key(data)
        address = self.hash_function(key)
        if self.hashtable[address] is not None:#when this address has a value in it
            current_node = self.hashtable[address]#to explore the linked list
            while True:
                if current_node.data[0] == data:#if it finds the same key replace the value
                    current_node.data[1] = value
                    return
                if current_node.next is None:#when it is at the last node ends while loop
                    break
                else:#go to the next node
                    current_node = current_node.next
            current_node.next = Node([data, value])#append a new node
        else:
            self.hashtable[address] = Node([data, value])#simply add a new node(new data)

    def read_data(self, data):#print a certain data in the hash table
        key = self.get_key(data)
        address = self.hash_function(key)
        if self.hashtable[address] is not None:
            current_node = self.hashtable[address]
            while True:
                if current_node.data[0] == data:#when it finds the same key return the value
                    return current_node.data[1]
                if current_node.next is None:
                    break
                else:
                    current_node = current_node.next
            return None#when it can't find the same key return None
        else:
            return None#when the address has no data in the hashtable return None

    def delete_data(self, data):#delete a certain data in the hashtable
        key = self.get_key(data)
        address = self.hash_function(key)
        if self.hashtable[address] is not None:
            current_node = self.hashtable[address]
            if current_node.data[0] == data:#when the data to delete is in the head node
                self.hashtable[address] = None#delete
                del current_node
                return
            else:
                while current_node.next:#to explore following nodes
                    if current_node.next.data[0] == data:#when the data to delete is in the next node
                        current_node.next = current_node.next.next#connect the current node's next to next next node
                        return
                    else:
                        current_node = current_node.next
                print("Thers's no such data to delete")


hashtable = HashTable(10)
