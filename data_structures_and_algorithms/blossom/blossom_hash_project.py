'''
In this project, we are going to implement a hash map to relate the names of flowers to their meanings. 
In order to avoid collisions when our hashing function collides the names of two flowers, 
we are going to use separate chaining. 
We will implement the Linked List data structure for each of these separate chains.
'''
from linked_list import Node, LinkedList
from blossom_lib import flower_definitions
class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for i in range(self.array_size)]
  def hash(self, key):
    return sum(key.encode())

  def compress(self, hash_code):
    return hash_code%self.array_size

  def assign(self, key, value):
    hash_code = self.hash(key)
    array_index = self.compress(hash_code)
    payload = Node([key,value])

    list_at_array = self.array[array_index]
    for item in list_at_array:
      if item[0] == key:
        item[1] = value
    list_at_array.insert(payload)

  def retrieve(self, key):
    hash_code = self.hash(key)
    array_index = self.compress(hash_code)
    list_at_index = self.array[array_index]
    for item in list_at_index:
      if item[0] == key:
        return item[1]
    return None
    payload = self.array[array_index]
    if pay_load is not None and payload[0] == key:
      return payload[1]
    else:
      return None

blossom = HashMap(len(flower_definitions))
for element in flower_definitions:
  blossom.assign(element[0], element[1])

print(blossom.retrieve('daisy'))