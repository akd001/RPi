myvars = {}
with open("../data.txt") as myfile:
	for line in myfile:
		name, var = line.partition("=")[::2]
		myvars[name.strip()] = float(var)
print myvars["var3"]