def reverse_dict(dict):
  # swap keys and values within dict and return dict
  for k, v in dict.items():
    v:k
  return dict


# dict = {1:'a', 2:'b', 3:'c'}
# print(reverse_dict(dict))
