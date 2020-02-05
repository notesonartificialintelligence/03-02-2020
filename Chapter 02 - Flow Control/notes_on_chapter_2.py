#Gabriel Abraham
#notesonartificialintelligence
#Automate The Borning Stuff With Python - Chapter 2
#I've covered most of these things alreaady; as such I'll create the example without using the code of the #author. If something is to be learnt; I'll implement it.

#Break Statements allows the program execution to break out of a while loop.


while True:
	print("Please type your name.")
	name = input()
	
	if name.lower() == "tim":
		break
print("Thank you!")

#Continue Statements; these statements are used inside loops, when it's reached the program
#execution immediately jumps back to the start of the loop, and reevaluated the loops condition.

while True:
	print("Who are you?")
	name = input()
	if name != "Joe":
		continue
	print("Hello, Joe. What is the password? (It is a fish.)")
	password = input()
	if password == "swordfish":
		break
print("Access granted.")

#If the users name is not the same as joe, the program flow will immdeiately jump to the start
#of the loop.

#Not nuch for today.