def size_of_list(list):
  # return size of list
  return len(list)


def add_elem_to_list(list, elem):
  # add elem to list and return the list
  list.append(elem)
  return list


def delete_elem_from_list(list, index = -1):
  # delete element from list, such that its index is index
  # if index is invalid, return empty list
  if len(list) < index:
    return []
  if index == -1:
    return list.pop(len(list) - 1)
  else:
    return list.pop(index)


def count_elements_in_list(list, x):
  # count elements in the list that are equal to x and return the count
  return list.count(x)


def sort_list(list):
  # return sorted list
  sorted_list = list.sort()
  return sorted_list


def reverse(list):
  # return reversed list
  reversed_list = list.reverse()
  return reversed_list


# random_int = random.randint(0, 40)
# print(random_int)
# print()
# lst = []
# for j in range (100):
#   if random.randint(0, 10) > 5:
#     lst.append(j)
# print(lst, end="\n")
# delete_elem_from_list(lst, random_int)
# print(lst)
