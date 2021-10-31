def size_of_set(set):
  # return size of set  
  return len(set)


def is_elem_in_set(set, elem):
  # return true if elem exists in set, false otherwise
  return elem in set


def are_sets_equal(first_set, second_set):
  # return true if sets have the same elements inside, otherwise false
  return first_set == second_set


def add_elem_to_set(set, elem):
  # add elem to the set if elem does not exist in set, and return the set
  # if elem exists in set, return set
  if elem in set:
    return set
  else:
    set.add(elem)
  return set


def remove_elem_if_exists(set, elem):
  # remove elem from set if it exists, and return the set
  if elem in set:
    set.remove(elem)
  return set


def delete_first_element(set):
  # delete first elemenent of set
  set.pop()
  return set

# st = {"one", "two", "three"}
# st2 = {"one", "two", "three"}
# delete_first_element(st)
# print(st)
