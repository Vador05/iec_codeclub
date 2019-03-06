while(True):
    print("Are you Male or Female?")
    gender= input()
    if(gender=="female"):
	    print("Can you give me your phone number?")
	    phone=input()
	    if(phone!=""):
		    print("Do you like beer?")
		    beer=input()
    elif(gender=="male"):
	    print("Do you like beer?")
	    beer=input()
	    if(beer!=""):
		    print("Can you give me your phone number?")
		    phone=input()
    else:
	    print("I'm not interested thanks =)")
	    exit()
    print("#########New Person##########")
    print("Gender: "+gender)
    print("Phone: "+phone)
    print("Likes beer: "+beer)

