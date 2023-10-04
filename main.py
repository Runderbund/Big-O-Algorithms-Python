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
    return False

# Time complexity O(n^2)
def sort_list(number_list):
    sorted = False
    n = len(number_list)-1

    while not sorted:
        sorted = True
        for i in range(0, n):
            if number_list[i] > number_list[i+1]:
                number_list[i], number_list[i+1] = number_list[i+1], number_list[i]
                sorted = False
    return number_list

# even_or_odd Tests
print("Even or Odd:")
print(even_or_odd(2)) # True
print(even_or_odd(3)) # False
print(even_or_odd(4)) # True
print(even_or_odd(5.5)) # False, because not designed for floats
print ("\n")

# less_than_100 Tests
print("Less than 100:")
print(less_than_100([2, 3, 4, 5])) # True
print(less_than_100([200, 3, 4, 5])) # False
print(less_than_100([2, 4, 98, 101])) # False
print ("\n")

# repeated_names Tests
print("Repeated names:")
print(repeated_names(["Alice", "Bob", "Charlie"]))  # False
print(repeated_names(["Alice", "Bob", "Charlie", "Alice"]))  # True
print(repeated_names(["Alice", "Alice", "Alice"]))  # True
print(repeated_names(["Alice"]))  # False
print(repeated_names([]))  # False
print ("\n")

# repeated_names_set Tests
print("Repeated names set:")
print(repeated_names_set(["Alice", "Bob", "Charlie"]))  # False
print(repeated_names_set(["Alice", "Bob", "Charlie", "Alice"]))  # True
print(repeated_names_set(["Alice", "Alice", "Alice"]))  # True
print(repeated_names_set(["Alice"]))  # False
print(repeated_names_set([]))  # False
print("\n")

# sort_list Tests
print("Sort list:")
print(sort_list([4, 2, 8, 5, 1]))  # [1, 2, 4, 5, 8]
print(sort_list([1, 2, 3, 4, 5]))  # [1, 2, 3, 4, 5]
print(sort_list([5, 4, 3, 2, 1]))  # [1, 2, 3, 4, 5]
print(sort_list([1]))  # [1]
print(sort_list([]))  # []
print("\n")

