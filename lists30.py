fruites = ["apple", "banana", "orange", "cherry", "kiwi", "mango"]

# using if condition if x == "a"
alists = [m for m in fruites if "a" in m]

# using if condition

newlists = [x for x in fruites if x != "apple"]


# not using if condition

xlists = [t for t in fruites]

print(f"If 'a' insert to alists : {alists}")
print(f"Using condition: {newlists}")
print(f"Not using condition: {xlists}")

