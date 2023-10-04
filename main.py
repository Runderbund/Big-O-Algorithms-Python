# Time complexity O(1)
def even_or_odd(number):
    if number % 2 == 0:
        return True
    return False


# Time complexity O(n)
def less_than_100(number_list):
    for n in number_list:
        if n > 100:
            return False
    return True

# Time complexity O(n^2)
def repeated_names(name_list):
    new_name_list = []
    for name in name_list:
        if name in new_name_list:
            return True
        new_name_list.append(name)
    return False

# Time complexity O(n) (set is O(1), better than new list)
def repeated_names_set(name_list):
    name_set = set()
    for name in name_list:
        if name in name_set:
            return True
        name_set.add(name)


def sort_list(number_list):
    pass

# even_or_odd Tests
print("Even or Odd:")
print(even_or_odd(2)) # True
print(even_or_odd(3)) # False
print(even_or_odd(4)) # True
print(even_or_odd(5.5)) # False, because not designed for floats
print ("/n")

# less_than_100 Tests
print("Less than 100:")
print(less_than_100([2, 3, 4, 5])) # True
print(less_than_100([200, 3, 4, 5])) # False
print(less_than_100([2, 4, 98, 101])) # False
print ("/n")

# repeated_names Tests
print("Repeated names:")
print(repeated_names(["Alice", "Bob", "Charlie"]))  # False
print(repeated_names(["Alice", "Bob", "Charlie", "Alice"]))  # True
print(repeated_names(["Alice", "Alice", "Alice"]))  # True
print(repeated_names(["Alice"]))  # False
print(repeated_names([]))  # False
print ("/n")
