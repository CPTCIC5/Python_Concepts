from collections import Counter

a= 'aaaabbbcccc'
counter = Counter(a)
print(counter)
print(counter.keys())
print(counter.values())
print(counter.most_common())
print(list(counter.elements()))