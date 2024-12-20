logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)

def add(a, b):
  return a + b
def sub(a, b):
  return a - b
def mul(a, b):
  return a * b
def div(a, b):
  return a / b
  
def calculator():
  continue1 = True
  while continue1:
    continue2 = True
    operations = {
      "+": add,
      "-": sub,
      "*": mul,
      "/": div,
    }
    a = float(input("write a first number \n"))
    while continue2 == True:
      print("Choose an operation")
      for key in operations:
        print(key)
      op = input()
      b = float(input("write a second number \n"))
      c = operations[op](a,b)
      print(f"{a} {op} {b} = {round(c, 3)}")
      ans = input(f"Type \n 'y'   to continue with {round(c, 3)} \n 'n'   to start with a new clculation \n 'e'   to exit \n ")
      if ans == "y":
        continue1 = False
        a = c
      elif ans == "n":
        continue1 = True
        continue2 = False
      elif ans == "e":
        print("bye bye")
        continue1 = False
        continue2 = False
        

calculator()