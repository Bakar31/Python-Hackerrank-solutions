import re
string = input()
output = re.search(r'((\w(?!_))\2)', string)
if output:
    print(string[output.start()])
else:
    print(-1)