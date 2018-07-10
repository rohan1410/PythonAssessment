if __name__ == '__main__':
	f = open("input.txt","r")
	m = {} #Dictionary to for distinct words and their count
	text = f.read()
	for line in text.split(" "):
		if not line.isalnum():
			continue
		if line in m:
			m[line] += 1
		else:
			m[line] = 1
	f.close()

	f = open("output.txt","w+")
	for key,value in sorted(m.items()):
		f.write(str(key) + " " + str(value) + "\n")