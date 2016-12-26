from bs4 import BeautifulSoup
import urllib
import string

###
# BUILD RECIPE DICTIONARY
###
recipe_dict = {}

root = "http://www.bbc.co.uk/food/recipes/"
recipe_file = map(lambda x: x.replace("\n", ""), open("recipes.txt", "r").readlines())
out_file = open("cookbook.txt", "w")

for line in recipe_file:
	print line

	link = root + line
	page = urllib.urlopen(link).read()
	soup = BeautifulSoup(page, "lxml")

	lis = soup.find_all("li", class_="recipe-ingredients__list-item")
	for item in lis:
		ing = item.find_all("a", class_="recipe-ingredients__link")
		if len(ing) > 0:
			ingredient = ing[0].contents[0]

			if line not in recipe_dict:
				recipe_dict[line] = []
			recipe_dict[line].append(ingredient)

	if line in recipe_dict:
		out_file.write(line)
		for item in recipe_dict[line]:
			out_file.write("," + item.encode("utf-8"))
		out_file.write("\n")
