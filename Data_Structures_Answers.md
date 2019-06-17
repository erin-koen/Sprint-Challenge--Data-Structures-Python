Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
- needs to loop through to count len, but everything else is 0(1) so runtime complexity is 0(n) where n is limited to `self.capacity` 

2. What is the space complexity of your ring buffer's `append` function?
- Needs to hold `self.storage` in memory to measure against `self.capacity`, so O(n). 

3. What is the runtime complexity of your ring buffer's `get` method?
- Needs to loop through all of `self.storage` to weed out the `None`. O(n) 

4. What is the space complexity of your ring buffer's `get` method?
- potentially needs to hold two lists of length `n`. O(2n)
 == O(n).

5. What is the runtime complexity of the provided code in `names.py`?
- O(n^2)

6. What is the space complexity of the provided code in `names.py`?
- 0(n^2)

7. What is the runtime complexity of your optimized code in `names.py`?
- O(n)

8. What is the space complexity of your optimized code in `names.py`?
- O(2n) => O(n)