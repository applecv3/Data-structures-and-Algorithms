'''
Hash table with linearprobing technique
when it collides at some point it goes through all the slots to find an empty address to save
a new data from the current address
'''


import hashlib


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

    def save_data(self, data, value):
        key = self.get_key(data)
        current_address = self.hash_function(key)
        c = 0#to check how many times it moved to find an empty slot to save a new data
        while c != self.size:#when it moved size-1 times it ends
            if self.hashtable[current_address] is None:#when the slot is empty just add
                self.hashtable[current_address] = [data, value]
                return
            else:
                if self.hashtable[current_address][0] == data:#when it has the same key replace the value
                    self.hashtable[current_address][1] = value
                    return
                else:
                    c += 1#count 1
                    if current_address == self.size - 1:#when the address reached the last idx, to go to the first idx
                        current_address -= self.size - 1
                    else:
                        current_address += 1#to go to the next slot
        print('No more room to save data')

    def read_data(self, data):#visit from the current address to the entire slots to find the data.
        key = self.get_key(data)
        current_address = self.hash_function(key)
        c = 0
        while c != self.size:
            #when it has the same key return the value
            if self.hashtable[current_address] and self.hashtable[current_address][0] == data:
                return self.hashtable[current_address][1]
            c += 1
            if current_address == self.size - 1:
                current_address -= self.size - 1
            else:
                current_address += 1
        return None#when not finding such data

    def delete_data(self, data):
        key = self.get_key(data)
        current_address = self.hash_function(key)
        c = 0
        while c != self.size:
            #when it has the same key delete the data
            if self.hashtable[current_address] and self.hashtable[current_address][0] == data:
                self.hashtable[current_address] = None
                return
            c += 1
            if current_address == self.size - 1:
                current_address -= self.size - 1
            else:
                current_address += 1
        print('No such data to delete')#when not finding such data


hashtable = HashTable(3)
