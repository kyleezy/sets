set1={2,3,4,5,6,7,8,8,9,10,9,9,10,2,1}
print(set1)
set1.add(11)
print(set1)
set1.remove(11)
print(set1)

set1={1,2,3,4}
set2={3,4,5,6}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))
print(set1.symmetric_difference(set2))