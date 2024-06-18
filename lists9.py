thislists = ["apple", "banana", "cherry"]


n = input("Search items in lists: ")

if n in thislists:
    print(f"Yes,'{n}' is in the fruits lists")
else:
    print(f"No, '{n}' is not found in the fruit lists")

