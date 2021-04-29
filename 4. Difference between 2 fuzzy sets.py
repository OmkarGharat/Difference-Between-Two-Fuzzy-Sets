# 4. Difference between 2 fuzzy sets

## formula :

# A | B = A n complement_of_B

# here , A and B are fuzzy sets and n is Intersection

# Example to Demonstrate the Difference Between Two Fuzzy Sets

A = dict()
B = dict()
Y = dict()

A = {"a": 1, "b": 0.3, "c": 0.5, "d": 0.2 }
B = {"a": 0.5, "b": 0.4, "c": 0.1, "d": 1 }

print('The First Fuzzy Set is :', A)
print('The Second Fuzzy Set is :', B)

for i, j in zip(A, B) :
 m = A[i]
 n = B[j]
 n = 1 - n

 if m < n :
     Y[i] = m
 else :
     Y[j] = n

print('Fuzzy Set Difference is :', Y) 
