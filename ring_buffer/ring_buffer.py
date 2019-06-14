'''
Understand
----------
- Ring Buffers are an array of a fixed length. 
- While there's space, New items will be added to the array at the last available index.
- In the case where the array is full, the oldest item in the array is removed, and the new item is inserted in its place.
- The class contains a 'current' property which is initialized to zero, and likely needs to be incremented or decremented upon insertion, to tell the function where the next oldest element is. 
- 
- what's the complexity of the pop method? O(n) i think because it needs to move all the elements to the right of the element down.
- Get method 


Plan 
----
    - append: 
        - handle case where there's room in the buffer.
        - if the buffer is full, check self.current to see the element of the list to overwrite.
            - if self.current = self.capacity - 1: self.current = 0. Else self.current += 1. THis means it's looping through the list.
    - get:
        - return the array in self.storage. Looks like the tests need me to strip out the 'none' that the constructor throws in there. 
            

Execute
-------


Analyze
-------




'''


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            self.storage[self.current] = item
            if self.current < self.capacity - 1:
                self.current += 1
            else:
                self.current = 0


    def get(self):
        get_arr =[]
        for item in self.storage:
            if item is not None:
                get_arr.append(item)
        return get_arr