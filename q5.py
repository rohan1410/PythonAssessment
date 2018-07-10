import json
from pprint import pprint
if __name__ == '__main__':
	with open('data.json') as jsonfile:
		data = json.load(jsonfile)   # Loading json file
	for i in data["Records"]:  # Iterating through records
		print (i["s3"]["bucket"]["arn"]) # Printing arn number