import random
import sys
import time
import datetime

chances = 3
minimum = 0
maximum = 0
powitanie="\nWelcome to this pretty easy game\nYour task is to guess the magic number(which is randomly generated) from following ranges\n(keep in mind that amount of your guesses is limited):\n"
zakresy="\n1. <0;15> Chances: 3\n2. <0;30> Chances: 3\n3. <0;50> Chances: 5\n4. Randomly generated range \n0. Change parameters\n"
menu="\nPlease, state your choice:"
czas = 0.015


def ChancesLeft():
    print"Chances left: "
    print chances

def DzienDobry():
    sys.stdout.write('Loading')
    for i in xrange(random.randint(1,100)):
        time.sleep(czas)
        sys.stdout.write(".")

def Wypisz(co, ile):
    for a in range(len(co)):
        sys.stdout.write(co[a])
        time.sleep(ile)
        
def WannaStay():
    print "Do you want to try again?(y/n)"
    wannastay = raw_input()
    if  wannastay == "y":
        #CLEAR!
        main()
    elif wannastay == "n":
            print "Bye...!"
            sys.exit(0)
     
def Menu():
    global minimum
    global maximum
    global chances
    Wypisz(powitanie, czas)
    Wypisz(zakresy, czas)
    Wypisz(menu, czas)
    opcja = int(raw_input())
    if opcja == 1:
        minimum = 0
        maximum = 15
        chances = 3
        #DEBUG: print minimum, maximum, chances
    elif opcja == 2:
        minimum = 0
        maximum = 30
        chances = 3
    elif opcja == 3:
        minimum = 0
        maximum = 50
        chances = 5
    elif opcja == 4:
        minimum = 0
        maximum = random.randint(0,1000)
        chances = random.randint(3,100)
    elif opcja == 0:
        print "\nRange min.: "
        minimum = int(raw_input())
        print "\nRange max.: "
        maximum = int(raw_input())
        if minimum<0 or maximum<0 or minimum>maximum:
            print "Impossible. Try again"
            #CLS!
            main()
        print "\nChances available: "
        chances = int(raw_input())
        if chances<= 0:
            print "Impossible. Try again"
            #CLS!
            main()
    else:
        print "Ship has sailed, capitan!"
        sys.exit(0)
        
def gra():
    global chances
    guess = 0
    MagicNumber = random.randint(minimum, maximum)
    print 'Range is from:', minimum, 'to:', maximum,'.'
    beggining = datetime.datetime.now()
    while guess!=MagicNumber and chances>0:
        sys.stdout.write("Take your guess: ")
        guess = int(raw_input())
        if guess == MagicNumber:
            print "That's it! Congratulations, you guessed it!\n Your magic number is:", MagicNumber
            break
        if guess>MagicNumber:
            print "Too much!"
            chances-=1
        if guess<MagicNumber:
            print "Not enough!"
            chances-=1
    ending = datetime.datetime.now()
    if chances<=0:
        print "Sorry... out of chances :-("
    print "You played for:", (ending-beggining).seconds,"point",(ending-beggining).microseconds, " seconds"   
    WannaStay()
    
        
def main():
    Menu()
    gra()
    
DzienDobry()
main()
