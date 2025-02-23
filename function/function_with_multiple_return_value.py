def get_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return total,average,numbers

lst=[10, 20, 30, 40]
res= get_stats(lst)
print(type(res))
print(f'total sum:{res[0]}')
print(f'total average:{res[1]}')

# Output: Total: 100, Average: 25.0

total_sum,average=get_stats(lst)

print(f'total_sum sum:{total_sum}')
print(f'total average:{average}')