from bs4 import BeautifulSoup
import urllib
import string

root = "http://www.bbc.co.uk/food/"

###
# BUILD FULL LIST OF INGREDIENTS
###

for c in string.ascii_lowercase:
	ingredient_dict = {}

	letter_page = urllib.urlopen(root + "ingredients/by/letter/" + c).read()
	soup = BeautifulSoup(letter_page, "lxml")
	ings = soup.find_all("li", class_="resource food")

	for ing in ings:
		ext = ing.find_all("a")[0]["href"]

		name = ext.split("/")[2].replace("_", " ")
		print name

		ingredient_dict[name] = []

		# ITERATE OVER PAGES
		count = 1
		while True:
			recipe_page = urllib.urlopen(root + "recipes/search?page=" + str(count) + "&keywords=" + name).read()
			soup = BeautifulSoup(recipe_page, "lxml")

			# TERMINATE ON NONEXISTENT PAGE
			if soup.find_all("h3", class_="error"):
				break

			print name + " pg." + str(count)

			items = soup.find_all("li", class_="article with-image") + soup.find_all("li", class_="article no-image")

			for item in items:
				recipe = item.find_all("a")[0]["href"].split("/")[3]
				print recipe

				if name in ingredient_dict:
					ingredient_dict[name].append(recipe)

			count += 1

	out_file = open(c + ".txt", "w")
	for key in ingredient_dict.keys():
		out_file.write(key)

		for val in ingredient_dict[key]:
			out_file.write("," + val)
		out_file.write("\n")
