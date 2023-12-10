table = "".maketrans("abcdefghijklmnopqrstuvwxyz","cdefghijklmnopqrstuvwxyzab")
print("Gimme ur input kid.")
code = input()
print(code.translate(table))
