def start():
    print "up or down"

    option = raw_input(">")

    if option == "up":
        ghost()

    if option == "down":
        sandwich()

def ghost():
    print "there is a ghost"
    print "it is in front of u"
    print "what do u want to do?"

    option1= raw_input(">")

    if option1 == "scream":
        print "ghost bit ur neck"
        print "you are dead"

    elif option1 == "kill it":
        print "you killed the ghost"
        print "you enter into dinning hall"

        sandwich()

    else :
        print "try again"


def sandwich():
    print "enter no. of sandwiches you need"
    food = raw_input(">")
    bread = int(food)

    if bread >  50 :
        print "you are glutton"
        print "greedy..!"
        print " you lose"

    elif bread < 50:
        print "you are not greedy "
        print "you enter the gold room"

        goldroom()

    else:
        print "try again"


def goldroom():
    print "you ecieve agold coin"
    print "do you need a pot full of gold?"

    option2 = raw_input(">")

    if option2 == "yes":
        print "greedy man you lose"

    elif option2 == "no":
        print "you are sincere"
        print "you are rewarded with pot full of gold"



start()