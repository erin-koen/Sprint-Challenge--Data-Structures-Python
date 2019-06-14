import time

start_time = time.time()

f = open('./names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('./names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

hash = {}
for name1 in names_1:
    hash[name1] = True
for name2 in names_2:
    if name2 in hash:
        duplicates.append(name2)

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

'''
Understand
----------
current code runs in quadratic time. should be able to shrink that with a chache. 

Plan 
----
- put all names from first list in a hash 0(n). loop through all names in second list and check if they're int the hash O(n)  If they are, append to the duplicates list.          

Execute
-------
.0056 seconds

Analyze
-------

seems like O(n) time complexity. 

first loop - n * 1 (hash insert) 
second loop - n * 1 (lookup) * 1 (append)

n * 1 + ( n * 1 * 1) = n + n = 2n






'''
