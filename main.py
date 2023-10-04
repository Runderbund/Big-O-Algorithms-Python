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

def repeated_names(name_list):
    pass

def sort_list(number_list):
    pass

# Even or Odd Tests
print(even_or_odd(2)) # True
print(even_or_odd(3)) # False
print(even_or_odd(4)) # True
print(even_or_odd(5.5)) # False, because not designed for floats

# Even or Odd Tests
print(less_than_100([2, 3, 4, 5])) # True
print(less_than_100([200, 3, 4, 5])) # False
print(less_than_100([2, 4, 98, 101])) # False