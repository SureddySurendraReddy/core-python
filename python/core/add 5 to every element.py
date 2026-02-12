nested_list = [[1, 2], [3, 4], [5, 6]]

result = list(map(lambda sub: list(map(lambda x: x + 5, sub)), nested_list))

print(result)
