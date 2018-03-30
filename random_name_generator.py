import random
def main():

	firstnames = ['Beecher', 'Jimmy', 'Kyle', 'Pearson', 'George', 'Jacob', 'Adam', 'Joel', 'Baizley', 'Ryan']

	lastnames = ['Jones', 'Brown', 'Idol', 'Williams', 'Smithers', 'Miller', 'Davis', 'Clarkson', 'Moore', 'Hill']

	middlenames = ['Anthony', 'Alexander', 'Charles', 'Dash', 'David', 'Edward', 'Jose', 'Finn', 'Francis', 'Henry']

	printHeader()
	while True:
		selection = getuserselection()
		if selection == 0:
			print ("                     ")
			generatefirstname(firstnames)
			generatelastname(lastnames)
			print ("                     ")
		elif selection == 1:
			print ("                     ")
			generatefirstname(firstnames)
			generatemiddlename(middlenames)
			generatelastname(lastnames)
			print ("                     ")
		elif selection == 9:
			print ("TERMINATING COMMAND")
			break
		else:
			print("INPUT NOT RECOGNIZED")

inputquestions = [
"RANDOM FIRST AND LAST NAME - PRESS 0",
"RANDOM FIRST, MIDDLE AND LAST NAME - PRESS 1",
"TO END PROGRAM - PRESS 9",
] 

def printHeader():
	print ("RANDOM NAME GENERATOR")

def getuserselection():
	for inputquestion in inputquestions:
		print ("                      ")
		print (inputquestions[0])
		print (inputquestions[1])
		print (inputquestions[2])
		print ("                      ")
		return int(input("ENTER SELECTION HERE: "))

def generatefirstname(firstnames):
	print (random.choice(firstnames), end=' ')

def generatelastname(lastnames):
	print (random.choice(lastnames), end='')

def generatemiddlename(middlenames):
	print (random.choice(middlenames), end=' ')

main()

