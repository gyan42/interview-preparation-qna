import heapq

def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]

print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
lst = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapq.heapify(lst)
print(lst)