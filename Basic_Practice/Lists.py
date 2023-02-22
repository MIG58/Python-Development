# Lists
# 1. It allows multiple data types
# 2. Values can be changed later in code

lang = ["Java", "C prog", "Python"]

lang.append("Go")  # Insert value at the last of the lists

print(lang)
lang.pop()  # delete value from the lists
print(lang)
lang.remove('C prog')  # delete specified value from the lists
print(lang)

lang.append(8)
print(type(lang))
