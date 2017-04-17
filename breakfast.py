"""Breakfast"""

print("get ingredients")
print("mix")
print("pour into the pan")
print("flip the other side")
breakfast = "---yummy egg---"
print (breakfast)


print("get ingredients")
print("mix")
print("pour into the pan")
print("flip the other side")
breakfast = "---yummy pancake---"
print (breakfast)

def make_breakfast(item):
    print("get ingredients")
    print("mix")
    print("pour into the pan")
    print("flip the other side")
    breakfast = "---yummy +item+ ---"
    return breakfast

print(make_breakfast("egg"))
print(make_breakfast("pancake"))
