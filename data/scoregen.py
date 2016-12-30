in_file = map(lambda x: x.replace("\n", ""), open("freqs.txt").readlines())

###
# CREATE FREQUENCY DICT
###
freqs_dict = {}

for line in in_file:
	arr = line.split(",")
	a = arr[0]
	b = arr[1]
	n = int(arr[2])

	freqs_dict[(a,b)] = n

###
# FIND QUINTILE OF COUNT
###
out_file = open("scores.txt", "w")

for key in freqs_dict.keys():
	a = key[0]
	b = key[1]
	n = freqs_dict[key]
	arr = []

	for item in freqs_dict.keys():
		if item[0] == a or item[0] == b or item[1] == a or item[1] == b:
			arr.append(freqs_dict[item])

	arr.sort()
	k = len(arr) - 1
	quintiles = []

	for i in range(0,5):
		m = int((float(i) / 4) * k)
		quintiles.append(arr[m])

	scores_table = [-10, 0, 10, 20, 30]
 	i = 0
 	while i < 5 and n > quintiles[i]:
 		i += 1

 	score = scores_table[i]

 	print a + " " + b + " " + str(score)
 	out_file.write(a + "," + b + "," + str(score) + "\n")
	