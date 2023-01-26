import random

phonebook = {}
phonebook = {"Chris": "555−1111", "Katie": "555−2222", "Joanne": "555−3333"}

""""
print()
print("*****  start section 1 - print dictionary ********")
print()

print(phonebook)
print(type(phonebook))
print(len(phonebook))

mydictionary = dict(m=1, n=2)
print(mydictionary)

print(phonebook["Chris"])
print(phonebook["chris"])

print()
print("*****  end section 1 ********")
print()





print()
print("*****  start section 2 - search dictionary ********")
print()

name = "chris"

# looks thtough all the keys in the phonebook
if name in phonebook:
    print(phonebook[name])
else:
    print(f"{name} is not in the phonebook")
    #dont get the key error


print()
print("*****  end section 2 ********")
print()


print()
print("*****  start section 3 - edit/append dictionary ********")
print()

print(phonebook)

#if you try to create a duplicate key, it updates the key (phone number in this case)
phonebook["Chris"] = "555-0123"
#auto append to the end of the dictionary
phonebook["Joe"] = "555-4444"
print(phonebook)

print()
print("*****  end section 3 ********")
print()



print()
print("*****  start section 4 - delete/remove from dictionary ********")
print()

del phonebook["Chris"]
print(phonebook)


print()
print("*****  end section 4 ********")
print()


print()
print("*****  start section 5 - iterate through keys, values, items ********")
print()

for key in phonebook:
    print(key)
    print(phonebook[key])

for v in phonebook.values():
    print(v)

mydict = {"mylist": [1, 2, 3, 4]}

for v in mydict.values():
    for ele in v:
        print(ele)
    print(v)


print()
print("*****  end section 5 ********")
print()



for key, value in phonebook.items():
    print(f"Name: {key} and their phone number: {value}")

for ph_tuple in phonebook.items():
    print(ph_tuple)


print()
print("*****  start section 6 - using get and clear ********")
print()

phone = phonebook.get("chris", "key not found")
print(phone)

phonebook.clear()
print(phonebook)


print()
print("*****  end section 6 ********")
print()


print()
print("*****  start section 7 - using pop method ********")
print()

remove = phonebook.pop("Chris", "not found")
print(remove)
print(phonebook)

print()
print("*****  end section 7 ********")
print()


print()
print("*****  start section 8 - using popitem ********")
print()

a = phonebook.popitem()

print(a)
print(phonebook)

print()
print("*****  end section 8 ********")
print()

"""

print()
print("*****  start section 9 - using random and converting to list ********")
print()

list_of_keys = list(phonebook)
print(list_of_keys)
random_key = random.choice(list_of_keys)
print(phonebook[random_key])


# shortened to one line of code
print(phonebook[random.choice(list(phonebook))])


print()
print("*****  end section 9 ********")
print()
