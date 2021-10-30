def reverse_dict(dict):
  # swap keys and values within dict and return dict
  new_dict = {}
  for k, v in dict.items():
    new_dict[v] = k
  return new_dict


# dict = {1:'a', 2:'b', 3:'c'}
# print(reverse_dict(dict))
