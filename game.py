from random import randint

ingredients = map(lambda x: x.replace("\n", ""), open("ingredients.txt").readlines())
scores_file = open("scores.txt").readlines()
scores = {}
cur_max = 0

for line in scores_file:
	arr = line.split(",")
	key = (arr[0], arr[1])

	score = int(arr[2])
	scores[key] = score
	cur_max = score if score > cur_max else cur_max

###
# RUN THE GAME
###
k = len(ingredients)
score = 0

a = randint(0, k - 1)
b = randint(0, k - 1)
c = randint(0, k - 1)

while b == a:
	b = randint(0, k - 1)
while c == b or c == a:
	c = randint(0, k - 1)

active = [ingredients[a], ingredients[b], ingredients[c]]

print "Here are your ingredients: "
print ingredients[a] 
print ingredients[b]
print ingredients[c]
print

print "Score: 0"
print "What do you want to add?"

while score >= -100:
	ans = raw_input()
	if ans in active:
		print "Already added, try again"
	elif ans in ingredients:
		for item in active:
			key = (ans, item) if ans < item else (item, ans)
			val = int(100 * scores[key] / cur_max if key in scores else -20)

			print ans + " + " + item + " : " + ("+" + str(val) if val >= 0 else str(val))
			score += val

		active.append(ans)

		for item in active:
			print item
		print
		print "Score: " + str(score)
		print "What do you want to add?"
	else:
		print "Not a valid ingredient, try again"
