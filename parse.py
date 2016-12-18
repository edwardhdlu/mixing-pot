import string

###
# BUILD RECIPE DICTIONARY
###
recipe_dict = {}
ingredients = []
void = ["cakes and baking", "unleavened bread"]

for c in string.ascii_lowercase:
	in_file = open("data/" + c + ".txt", "r")
	data = in_file.readlines()
	if len(data) == 0:
		break

	for line in data:
		arr = line.split(",")

		ing = arr[0]
		if ing in void:
			break

		ingredients.append(ing)
		arr.pop(0)

		for item in arr:
			if item not in recipe_dict:
				recipe_dict[item] = []
			recipe_dict[item].append(ing)

###
# BUILD LIST OF INGREDIENTS
###
ingredients.sort()
out_file = open("ingredients.txt", "w")

for item in ingredients:
	if item != "":
		out_file.write(item + "\n")

###
# BUILD FINAL PAIR DICTIONARY
###
score_dict = {}

for key in recipe_dict.keys():
	for i in recipe_dict[key]:
		for j in recipe_dict[key]:
			if (i < j):
				pair = (i, j)

				if pair not in score_dict:
					score_dict[pair] = 0
				score_dict[pair] += 1

###
# WRITE TO FILE
###
out_file = open("freqs.txt", "w")

for key in score_dict.keys():
	out_file.write(key[0] + "," + key[1] + "," + str(score_dict[key]) + "\n")
