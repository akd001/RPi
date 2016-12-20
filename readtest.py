myvars = {}
with open("../data/maildata.txt") as myfile:
	for line in myfile:
		name, var = line.partition("=")[::2]
		myvars[name.strip()] = str(var.replace('\n', ''))
print myvars
