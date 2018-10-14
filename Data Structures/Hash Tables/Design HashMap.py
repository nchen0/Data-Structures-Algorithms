# 706. Design HashMap: https://leetcode.com/problems/design-hashmap/description/

"""
Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

Example:

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);         
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1 
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found) 

Note:

All keys and values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashMap library.
"""


class MyHashMap(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 100001
        self.map = [None] * self.capacity

    def hash_function(self, key):
        new_hash = 0
        for char in str(key):
            new_hash += ord(char)
        return new_hash % self.capacity

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        index = key
        pair = [key, value]
        if self.map[index] is None:
            self.map[index] = pair
        else:
            self.map[index][1] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = key
        if self.map[index] is None:
            return -1
        else:
            return self.map[index][1]

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        index = key
        if self.map[index] is None:
            return -1
        else:
            self.map[index] = None
