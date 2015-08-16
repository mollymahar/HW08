#!/usr/bin/python

import random

def printRoster(roster):
    """ prints entire roster """
    for x in roster:
        print x


def getRandomParticipantIndex(roster):
    """ Returns random index of person in roster """
    return random.randint(0, len(roster) - 1)


def getPerson(index, roster):
    """ Returns person (string) from roster """
    ### rewrite getPerson() to take an index and roster; return name at index #
    return roster[index]


def addPerson(name, roster):
    """ Adds person (string) to roster """
    ### rewrite addStudent() to take a name and roster; add name to roster #
    roster.append(name)


def get_excuse():
    excuses = [ "My dog ate my homework",
                "I drank too much beer last night.",
                "\"Bored to Death\" marathon",
                "Laptop went up in flames",
                "Ain't nobody got time for that!",
                "My plane got stuck in Vegas",
                "I was watching \"The Big Lebowski\"",
                "Wait, I was supposed to do something?"]

    return excuses[random.randint(0, len(excuses) - 1)]

            
def main():
    """ Main -- prints the bootcamp roster, adds Daniel, and then prints 
    excuses """
    bootcampParticipants = [ "Andrea", "Ankur", "Anne", "Astika", "Carlo", 
                             "Dina", "Emily", "Eric", "Hadrien", "Keshav",
                             "Laura", "Lynell", "Max", "Molly", "Neera", 
                             "Pooja", "Proxima", "Reema", "Richa", "Saikiran",
                             "Sasha", "Shirish" ]
                             
    ### your one line of code goes here to print roster #

    # add 'Daniel' to bootcampParticipants
    addPerson('Daniel', bootcampParticipants)

    ### Your Code Here ###
    # get random participant
    index = getRandomParticipantIndex(bootcampParticipants)
    
    # print person's name who has excuse today. 
    name = getPerson(index, bootcampParticipants)

    ###
    # print person's name who has excuse today. 
    print name + " said \'" + get_excuse() + '\''


if __name__ == "__main__":
    print("Excuse Generator") 
    main()
