import math   
def get_hypotenuse(catet1, catet2):  
  # calculate hypotenuse of right triangle based on 2 catets and return it
  c = catet1 * catet1 + catet2 * catet2
  return math.sqrt(c)


# print(get_hypotenuse(3, 4))
