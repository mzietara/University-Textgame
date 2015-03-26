from random import choice, randint, shuffle
import sys
import os
from time import sleep


def char_setup(s):
    '''This is the process of setting up the character that will be used. Return
    a list that contains the character name, starting level, starting health,
    and starting damage.'''
   
    name = raw_input("What would you like your character's name to be?\nName: ")
    
    lvl = 1.0
    char = [name, lvl]
    #These values are defaulted.
    hp = max_hp(char)
    dmg = damage(char)
    atk = ['Beat with stick', 'Smack', 'Throw homework']
    
    
    print "\nWelcome to the World of University, %s!" %(name)
    print "Let your adventure begin!"
    return [name, lvl, hp, dmg,atk]
    


def lvl_to_xp(lvl):
    '''level to exp points converter. For now, we will not use this.'''
    
    return 5*int(lvl)*(1 + int(lvl))
    


def max_hp(character):
    '''Return the int of the maximum hp calculated from level.'''
    
    return int(character[1]) * 5 + 20
    


def damage(character):
    '''how damage is calculated with respect to the level.'''
    start = int(character[1])*2 + 2
    end = start + 2*int(character[1]) + 2
    
    return range(start,end)
    

def evil_char(evil):
    '''Return the list of characteristics of the evil character. Evil is the
    name of the evil character as a string.
    0- Evil character name
    1- level
    2- hp
    3- damage
    4- list of what he/she does in battle. The first three things in the list
    are battle damage moves, then the next 2 do nothing.'''
    
    drunk_student = {'drunk_student': ['drunk_student', 1, 14, range(3,6), \
    ['Throw Random Stuff', 'Chuck used Textbooks', 'Fling Beer Bottles', \
     'Passed out shortly', 'Is getting really tipsy...', 'Drink Vodka']]}
    
    
    evil_dict = drunk_student
    
    if evil in evil_dict.keys():
        return evil_dict[evil]
    else:
        return []
    
    
    
    
    
    #GOTTA WRITE THIS!
    

def update_char(character, lvl_inc, diff_hp):
    '''Return character, but updated with respect to diff_hp, which is the
    int of increase or decrease of the character's hp, and lvl_inc which is
    the increase of the level.'''
    
    #update the character level.
    lvl_b4 = character[1]
    character[1] += lvl_inc
    
    if lvl_inc > 0:
        print 'you have gained ' + str(lvl_inc) + ' on your level!'
    
    if int(lvl_b4) != int(character[1]):
        print "LEVELLLL UPPPP!!!!!!!!!"
        character[3] = damage(character)
        character[2] = max_hp(character)
    
    
    #Define the maximum health with respect to the level.
    maximum_hp = max_hp(character)
    hp = character[2]
    
    #If the change hp results in a number greater than max_health, just
    #set the value to max health. Never let it go over. if health is under 0,
    #you are dead, and the game terminates.
    if maximum_hp >= hp + diff_hp > 0:
        character[2] += diff_hp
    elif maximum_hp < hp + diff_hp:
        character[2] = maximum_hp
    else:
        print "You have died!! :( \nBetter luck next time!"
        p = os.system("pause")
        sys.exit()
    
    
    
def current_stats(character):
    '''print out what the current stats of the character is. Bring user back to
    the choice screen after.'''
    
    print "\nYour current stats are:\n"
    
    print "Level: %.2f\tHP: %i/%i" %(character[1], character[2], max_hp(character))
    print "Damage: %i - %i" %(character[3][0], character[3][-1])
    
    choice_screen()
    
    
    
def choice_screen():
    '''This is the main choice screen. Depending on the input of the user will
    determine what happens next!'''
    blank = '____________________________________________________________________'
    print blank
    s = sleep(1)
    print '\nWhat would you like to do?\n'
    print '1: Keep exploring\t3: Terminate'
    print '2: Check stats\t'
    answer = raw_input('Enter Choice: ')
    
    if answer == '1':
        print blank
        explore()
    elif answer == '2':
        print blank
        current_stats(character)
    elif answer == '3':
        print blank
        print 'Thank you for playing!'
        p = os.system("pause")
        sys.exit()
        
    
    
    
def explore():
    print "\nyou continue walking...\n"
    
    #for each option, attach a number which will increase the chance of that
    #certain option occuring.
    opt1 = 35*['Nothing exciting happened.']
    opt2 = 15*['You found Timmies! Would you like to buy a donut?']
    opt3 = 15*['Bathroom break...\n...\n...\n...\nAlright! Moving on...']
    opt4 = 5*["Look! You've spotted a TA! His wisdom grants you 5xp."]
    opt5 = 35*['An evil drunken student wants to fight!!!!!!']
    opt6 = 15*["OH NO! IT'S THE SECURITY GUARD!! Fight him!!"]
    all_opt = opt1 + opt2 + opt3 + opt4 + opt5 #+ opt6
    
    what_happens = choice(all_opt)
    
    if what_happens in opt1:
        print what_happens
        choice_screen()
    
    elif what_happens in opt2:
        print what_happens
        answer = raw_input("Yes or no: ")
        if answer.lower() == "yes":
            choices = ["You bought you a donut! you have gained 5 hp.", "ICK!! All that sugar got you sick. You have lost 5hp."]
            happen = choice(choices)
            if happen == choices[0]:
                print happen
                update_char(character, 0, 5)
            elif happen == choices[1]:
                print happen
                update_char(character, 0, -5)
        else:
            print "Too bad for you! Maybe next time!"
       
        choice_screen()
        
    elif what_happens in opt3:
        print what_happens
        choice_screen()
    
    elif what_happens in opt4:
        print what_happens
        update_char(character, 0.2, 0)
        choice_screen()
    
    elif what_happens in opt5:
        print what_happens
        evil = 'drunk_student'
        battle(evil)


    
def battle(evil):
    '''This initiates a battle.'''
    evil = evil_char(evil)
    bat = "***********BATTLE!******************BATTLE!************"
    print bat
    print '\n%s is about to battle %s!\n' %(character[0], evil[0])
    

    
    while evil[2] > 0 and character[2] > 0:
        print '\nCurrent health: %i' %(character[2])
        print 'Current opponent health: %i' %(evil[2])
        print '\nWhat would you like to do in this battle?\n'
        print '1: Attack moves      2: Run from battle'
        answer = raw_input('Enter Choice: ')
        if answer == '1':
            for i in range(0, len(character[4])-1, 2):
                print character[4][i] + "      " + character[4][i+1]
            move = raw_input("\nChoose a move: ")
            damage = choice(character[3])
            evil[2] += -damage
            print "\nYou have done %i HP of damage!" %(damage)
            move = choice(evil[4])

            if move in evil[4][0:3]:
                damage = choice(evil[3])
                update_char(character, 0, -damage)
                print '\n%s has used the move %s\n!' %(evil[0], move)
                print 'You have taken ' + str(damage) + "hp of damage!"
            elif move in evil[4][3:5]:
                print evil[0] + " " + move + "!"
                
            elif move in evil[4][5]:
                evil[2] += 5
                print '\n%s has used the move %s!\n' %(evil[0], move)
                print "%s has healed for 5hp!" %(evil[0])


        
        elif answer == '2':
            print "Can't run from this battle!"
        
        print "_______________________________________________________________"
            
    if evil[2] <= 0:
        print '%s has died! You are victorious!' %(evil[0])
        lvl_inc = choice([0.1, 0.2, 0.3])
        update_char(character, lvl_inc, 0)
        
    
    #STILL HAVE TO WRITE THIS!
    
    choice_screen()
    
    
    
    
    

if __name__ == '__main__':
    print '\n \n \nCreated By Mark Zietara.\n \nWelcome to UNIVERSITY ADVENTURES!!'
    print 'This is an interactive rpg based around University.'
    print 'Are you ready to begin your adventure?'
    ready = raw_input("Yes or no: ")
    while ready.lower() != 'yes':
        print choice(['That sucks... how about now?', 'Well then Hurry! Are you ready now?', "Well we don't have all day... so are you ready now?"])
        ready = raw_input("Yes or no: ")
    print "GREAT! Let's get started! \n \n \n"
    
    character = char_setup("")
    
    #Write an intro storyline.
    while character[1] < 2:
        choice_screen()
