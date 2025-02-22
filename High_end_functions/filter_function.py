#syntax
# filter(function,iterable)

# function return boolean value True or False

lst=[8,3,5,2,64,23,56,21,57,87,98]

# res=list(filter(lambda x:x%2==0,lst))
# print(res)

import time
import tracemalloc
import sys
numbers=list(range(100000))

tracemalloc.start()
start_time=time.time()
filter_number=list(filter(lambda x:x%2==0,numbers))
end_time=time.time()
print(f'memory consumed using filter:{tracemalloc.get_traced_memory()[1]/(1024*1024):.6f} MB')
tracemalloc.stop()



time_consumed=end_time-start_time
print(f'time consumed using filter:{time_consumed:.6f}s')

tracemalloc.start()
start_time=time.time()
filter_number=[x for x in numbers if x%2==0]
end_time=time.time()
print(f'memory consumed using list comprehension :{tracemalloc.get_traced_memory()[1]/(1024*1024):.6f} MB')
tracemalloc.stop()
time_consumed=end_time-start_time
print(f'time consumed with list comprehension:{time_consumed:.6f}s')
