from json import dumps, loads


def push(data, destination="noteid.json"):
	file = open(destination, "r+")
	print(destination," opened...")
	file.write(dumps(data))
	print(destination, " data converted to JSON...")
	file.close()
	print(destination, " data processed!")

def pull(destination="noteid.json"):
	print("pulling ", destination,)
	return loads(open(destination, "r+").read())

def add(data, destination="noteid.json"):
	print("adding to ", destination)
	push({'idlist': {**pull(destination)['idlist'], **data}}, destination="noteid.json")
