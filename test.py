string = " 🧍 "
print(string)
string = list(string)



if string[0] == " ":
    string[0] = ""
result = "".join(string)
print(result)