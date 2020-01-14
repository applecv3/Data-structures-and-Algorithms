'''
Basic hash table with SHA
'''


import hashlib


class HashTable:

    def __init__(self, size):
        self.size = size#size of the tabel
        self.hashtable = [None for _ in range(self.size)]

    def get_key(self, data):
        hash_object = hashlib.sha256()#declare a hash object to use SHA256
        hash_object.update(data.encode())#encode 'data' into byte form and update
        hex_digit = hash_object.hexdigest()#get a str object of hexadecimal number
        return int(hex_digit, 16)

    def hash_function(self, key):
        return key % self.size#use the remainder as hash address

    def save_data(self, data, value):
        key = self.get_key(data)#convert the data into a str object of hexadecimal number
        address = self.hash_function(key)#get an address
        self.hashtable[address] = value#save the data in the hashtable

    def read_data(self, data):
        key = self.get_key(data)
        address = self.hash_function(key)
        if self.hashtable[address] is None:#if this address doesn't have any value return None
            return None
        else:
            return self.hashtable[address]#return the value

    def delete_data(self, data):
        key = self.get_key(data)
        address = self.hash_function(key)
        if self.hashtable[address] is None:#when there's no data to delete
            print("Thers's no such data to delete")
        else:
            self.hashtable[address] = None#delete!


hashtable = HashTable(8)


