from random import randint

idlist = []

def idgen(ids):
	idlist = ids
	while True:
		r = hex(randint(1,68719476736)) #64**6
		print("trying ",r)
		if r not in idlist:
			idlist.append(r)
			print(r," appended")
			return r
