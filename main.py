# Iterating through different datastructures using a for loop
def p():
  print("# --------------------------------------------")
# --------------------------------------------
# 1. Iterating through a list with mixed types of entries 
list1 = ["ila", 99, {"city": "chennai"}, [1, 2, 3]]
for i in list1:
  print(f"Entry: {i} <-> Type of entry: {type(i)}")
p()
# Results:
# Entry: ila <-> Type of entry: <class 'str'>
# Entry: 99 <-> Type of entry: <class 'int'>
# Entry: {'city': 'chennai'} <-> Type of entry: <class 'dict'>
# Entry: [1, 2, 3] <-> Type of entry: <class 'list'>
# --------------------------------------------
# 2. Iterating through a dictionary
dict1 = {"country": "spain", "city": "madrid", "population": 45343, "location": "europe"}
for i in dict1:
  print(f"Entry: {i} <-> Type of entry: {type(i)}")
  print(dict1[i])
# Results:
# Entry: country <-> Type of entry: <class 'str'>
# Entry: city <-> Type of entry: <class 'str'>
# Entry: population <-> Type of entry: <class 'str'>
# Entry: location <-> Type of entry: <class 'str'>
# --------------------------------------------
p()  
# 3. Iterating through a list of dictionaries
ld1 = [{"country": "France"}, {"govt": "democracy"}]
for d in ld1:
  print(f"Entry: {d} <-> Type of entry: {type(d)}")
  for k in d:
    print(f"key: {k} -> value: {d[k]}")
  # for k in i:
  #   print(f"key: {k} -> value: {dict1[k]}")
# Results:
# Entry: {'country': 'France'} <-> Type of entry: <class 'dict'>
# key: country -> value: France
# Entry: {'govt': 'democracy'} <-> Type of entry: <class 'dict'>
# key: govt -> value: democracy
# Learn more at https://stackoverflow.com/questions/17117912/python-accessing-values-in-a-list-of-dictionaries
# https://docs.python.org/2/tutorial/controlflow.html

p()