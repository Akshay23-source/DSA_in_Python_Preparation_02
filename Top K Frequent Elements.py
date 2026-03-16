from collections import Counter
import heapq
a=[1,1,1,2,2,3]
print(heapq.nlargest(2,Counter(a),key=Counter(a).get))





import heapq
a=[7,3,9,1]
print(heapq.nsmallest(2,a))