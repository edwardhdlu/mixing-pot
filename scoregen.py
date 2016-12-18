in_file = map(lambda x: x.replace("\n", ""), open("freqs.txt").readlines())
out_file = open("scores.txt", "w")

###
# CALCULATE TOTALS
###
totals = {}

for line in in_file:
	arr = line.split(",")

	a = arr[0]
	b = arr[1]
	n = int(arr[2])

	if a not in totals:
		totals[a] = 0.0
	if b not in totals:
		totals[b] = 0.0

	totals[a] += n
	totals[b] += n

###
# CALCULATE CONDITIONAL PROBABILITIES AND MAX SCORE
###
lst = []
cur_max = 0
scores = []

for line in in_file:
	arr = line.split(",")

	a = arr[0]
	b = arr[1]
	n = int(arr[2])
	ta = totals[a]
	tb = totals[b]

	new_score = ((n / float(ta)) * (n / float(tb))) 
	cur_max = new_score if new_score > cur_max else cur_max

	scores.append(new_score)
	lst.append([a, b, new_score])

###
# CALCULATE DECILES
###
scores.sort()
deciles = []
k = len(scores)

for i in xrange(1, 10):
	m = int((float(i) / 10) * k)
	deciles.append(scores[m])

deciles.sort()
print deciles

###
# WRITE FINAL SCORES
###
score_table = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for item in lst:
	a = item[0]
	b = item[1]
	score = float(item[2])

	i = 0
	while i < 9 and score > deciles[i]:
		i += 1

	final_score = score_table[i]


	print a + " " + b + " " + str(final_score)
	out_file.write(a + "," + b + "," + str(final_score) + "\n")
	