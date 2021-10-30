def reverse_dict(dict):
  # swap keys and values within dict and return dict
  old_dict = dict
  new_dict = {}
  for k, v in dict.items():
    if v in new_dict:
      new_dict[v].append(k)
    else:
      new_dict[v]=k
  return new_dict


# dict = {1:'a', 2:'b', 3:'c'}
# print(reverse_dict(dict))
