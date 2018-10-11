# Hash tables are what are dictionaries, and objects in python/js.
# Hash tables employ the use of a hash function to map general keys to corresponding indices in a table. Ideally, keys will be well distributed in the range from 0 to N - 1 by a hash function, but in practice there may be two or more distinct keys that get mapped to the same index.
# As a result, we will conceptualize our table as a bucket array where the bucket may manage a collection of items that are sent to a specific index by the hash functions.


"""
Hash Functions:
- The goal of a hash function is to map each key k to an integer in the range 0 to N - 1, where N is the capacity of the bucket array for a hash table. We store the item (key, value) in the bucket A[h(key)] with h being the hash function. 
- If there are two or more keys with the same hash value, then two different items will be mapped to the same bucket in A. In that case, we can say that a collision has occurred. 
- When dealing with hash functions, we can split it into two portions, a hash code that maps a key k to an integer (this integer does not have to be within N - 1, it can be a large number or even negative) and a compression function that maps the hash code to an integer within a range of indices 0 to N - 1. 
- Hashing functions are typically deterministic, meaning, same values will be hashed to the same integers, and are typically one way, and lastly, has to be N - 1 range. You cannot take a hash value result and turn that around and get the original data back. Deterministic means that two objects that are equal SHOULD return the same hash value. The flip side is that two equal hash may not be from the same objects. 
    - Say an object with Sam, Jones, 04/04/1990 gets a hash value of 2075. Any object with those exact figures will get the same hash value, but say an object Fay Adams comes along with different values, different birthday and just happen to have the same hash value. That would be collision. 
- The point of using a hash function is that we can take some complicated object and turn it into a simple integer representation, and with that we can use it to get to a certain location. 

Hash Tables:
- The big advantages of hash tables over arrays and linked lists is that they're very fast. Finding, inserting, deleting. 
- A hash table begins with multiple "buckets" waiting for content. We want to add a key value pair to the hash table. We are thus always adding in pairs.
- When we are inputting a function, the hash table takes the key, runs it through the hash function, then compresses it to fit one of our buckets. When we are trying to look up that item at a later time, it does exactly the same thing, and it goes directly to the bucket in which that contains the value we're looking for. So there's no binary/linear etc search. We go directly to that value. 
