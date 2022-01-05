strings = [(2, 0), (3, 1), (1, 2)]

strings.sort(key = lambda x : x[0])
string_sorted = sorted(strings, key = lambda x : x[1])
print(string_sorted)