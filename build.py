void = ["cakes and baking", "unleavened bread"]
ingredients_set = set()
recipe_dict = {}

cookbook_file = map(lambda x: x.replace("\n", ""), open("cookbook.txt").readlines())
for line in cookbook_file:
	arr = line.split(",")
	key = arr[0]
	arr.pop(0)	
	# print arr

	recipe_dict[key] = []
	for item in arr:
		item = item.lower()
		recipe_dict[key].append(item)
		ingredients_set.add(item)

###
# BUILD LIST OF INGREDIENTS
###
ingredients = list(ingredients_set)
ingredients.sort()
out_file = open("ingredients.txt", "w")

for item in ingredients:
	if item != "" and item + "s" not in ingredients and item not in void:
		out_file.write(item + "\n")

for item in ingredients:
	if item + "s" in ingredients or item in void:
		ingredients.remove(item)

###
# BUILD FINAL PAIR DICTIONARY
###
freq_dict = {}

for i in ingredients:
	for j in ingredients:
		if (i < j):
			pair = (i, j)
			freq_dict[pair] = 0

for key in recipe_dict.keys():
	for i in recipe_dict[key]:
		for j in recipe_dict[key]:
			if (i < j):
				pair = (i, j)

				if pair not in freq_dict:
					if (i + "s", j) in freq_dict:
						pair = (i + "s", j)
					elif (i, j + "s") in freq_dict:
						pair = (i, j + "s")
				else:
					freq_dict[pair] += 1

###
# WRITE TO FILE
###
out_file = open("freqs.txt", "w")

for key in freq_dict.keys():
	if freq_dict[key] != 0:
		print key[0] + " " + key[1] + " " + str(freq_dict[key])
		out_file.write(key[0] + "," + key[1] + "," + str(freq_dict[key]) + "\n")