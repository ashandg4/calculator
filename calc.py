import sys

from help import help
from sum import sum
from sub import sub

arguments = sys.argv[1:]

length = len(arguments)

if length == 0:
    help()
elif length >= 1:
    if arguments[0] == "help":
        help()
    elif arguments[0] == "sum":
        if length == 3:
            try:
                num1 = int(arguments[1])
                num2 = int(arguments[2])
                print(f"{num1} + {num2} = {sum(num1, num2)}")
            except Exception as error:
                print(error)
        else:
            print("need 2 numbers")
    elif arguments[0] == "sub":
        if length == 3:
            try:
                num1 = int(arguments[1])
                num2 = int(arguments[2])
                print(f"{num1} - {num2} = {sub(num1, num2)}")
            except Exception as error:
                print(error)
        else:
            print("need 2 numbers")
    else:
        print("command not found")
