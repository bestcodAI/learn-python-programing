fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlists = [x if x != "banana" else "orange" for x in fruits]

print(newlists)
