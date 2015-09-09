# coding=utf-8
#David sitt zork. SuggerAgurk
from sys import exit
def print_line():
    print "\n------------------------------------<<>>-------------------------------------\n"

def about_you():
    name = raw_input("Who are you?\n> ")
    print_line()
    return { "name" : name, "luck" : 1, "gun" : False, "goldenKey": False, "hiddenWall" : False }

def start_text(player):
    print "Hello there %s, how are you?" % player["name"]
    print "I'm terrebly sorry to tell you this."
    print "But you are a dumb guy! Also, stuck in this dark room."
    print "This pyramid is one of the legends."
    print "Whatever, we do not have time for this you need to get out"
    print "This place is haunted, so keep an eye open. (Just read everything!)"
    print_line()
    start_room()

def start_room():
    print "In front of you is a door and too your left is another door."
    print "What too do? So many Decissions"

    decide = raw_input("> ")

    if decide == "left":
        dead("You tripped on a line and fell into the spikes.")
        print_line()
    elif decide == "forward":
        print_line()
        one_room()
    elif decide == "right" and player["hiddenWall"] == False:
        print "This does not even look like a solid wall? What is this?"
        brkWll = raw_input("> ")
        if brkWll == "push":
            print_line()
            print "The wall fell down! You find a three cloves. \nLuck +1"
            player["hiddenWall"] = True
            luck_up()
            print_line()
            start_room()
        else:
            print_line()
            print "I do not know what you mean by that, whatever."
            print_line()
            start_room()
    elif decide == "right" and player["hiddenWall"] == True:
        print "You have already broken the wall. Move on!\n"
        print_line()
        start_room()
    else:
        dead("you can not spell.")

def dead(why):
    if player["luck"] <= 0:
        print_line()
        print "You died since,", why
        print ""
        exit(0)
    else:
        print_line()
        print "You shuld have died since,", why
        print "But you are lucky"
        #current_room() Må lage current room funksjon som følger med hvor spiller er.

def luck_up():
    player["luck"] += 1

def luck_down():
    player["luck"] -= 1
    
player = about_you()


start_text(player)
