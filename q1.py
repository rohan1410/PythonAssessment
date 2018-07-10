import re
import logging 
def validate(s):
	l = ['$','#','@']
	logging.basicConfig(filename='invalid.log',level=logging.DEBUG, filemode = "w")
	if not re.search(r'[A-Z]+',s):
		logging.debug('No uppercase letter')
		return False
	if not re.search(r'[a-z]+',s):
		logging.debug('No lowercase letter')
		return False
	if not re.search(r'[0-9]+',s):
		logging.debug('No digits ')
		return False
	flag = 0
	for t in l:
		if t in s:
			flag = 1
			break
	if not flag:
		logging.debug('No special character')
		return False
	if len(s) < 6 or len(s) > 12:
		logging.debug('Password should be of minimum length of 6 and maximum length of 12')
		return False
	return True


def main():
	s = raw_input()
	if validate(s):
		print "valid"
	else:
		print "not valid"

if __name__ == '__main__':
	main()
