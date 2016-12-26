import string

out_file = open("recipes.txt", "w")
recipe_set = set()

###
# GENERATE LIST OF ALL RECIPES
###
for c in string.ascii_lowercase:
	in_file = open("data/" + c + ".txt", "r")
	data = in_file.readlines()
	if len(data) == 0:
		break

	for line in data:
		arr = line.split(",")
		arr.pop(0)

		for item in arr:
			if item not in recipe_set:
				recipe_set.add(item)
				out_file.write(item + "\n")