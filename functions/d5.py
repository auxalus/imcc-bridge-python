def calculator(a , b , operation):
  if operation == ("add"):
    return a + b
  elif operation == ("sub"):
    return a-b
  elif operation == ("multi"):
    return a*b 
  elif operation == ("divide"):
    return a/b
  else:
    print("invalid response")

here = calculator(7,1 ,"divide")
print(here)