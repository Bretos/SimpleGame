#
# SimpleGame -> just guess that f...ing number! Child of Boredom
#
# Copyright (C) 2013  Bretos
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
import random
import sys
import time
import datetime
import os

chances = 3
minimum = 0
maximum = 0
powitanie = "\nWelcome to this pretty easy game\nYour task is to guess the magic number(which is randomly generated) from following ranges\n(keep in mind that amount of your guesses is limited):\n"
zakresy = "\n1. <0;15> Chances: 3\n2. <0;30> Chances: 3\n3. <0;50> Chances: 5\n4. Randomly generated range \n0. Change parameters\n-1. Quit"
menu = "\nPlease, state your choice: "
czas = 0.015


def ChancesLeft():
    print"Chances left: "
    print chances


def DzienDobry():
    sys.stdout.write('Loading')
    for i in xrange(random.randint(1, 100)):
        time.sleep(czas)
        sys.stdout.write(".")


def Wypisz(co, ile):
    for a in range(len(co)):
        sys.stdout.write(co[a])
        time.sleep(ile)


def WannaStay():
    print "Do you want to try again?(y/n)"
    wannastay = raw_input()
    if wannastay == "y":
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
        maximum = random.randint(0, 1000)
        chances = random.randint(3, 100)
    elif opcja == 0:
        print "\nRange min.: "
        minimum = int(raw_input())
        print "\nRange max.: "
        maximum = int(raw_input())
        if minimum < 0 or maximum < 0 or minimum > maximum:
            print "Impossible. Try again"
            #CLS!
            main()
        print "\nChances available: "
        chances = int(raw_input())
        if chances <= 0:
            print "Impossible. Try again"
            #CLS!
            main()
    elif opcja == -1:
        print "Bye bye!"
        exit()
    else:
        print "Ship has sailed, capitan!"
        sys.exit(0)


def gra():
    global chances
    guess = 0
    MagicNumber = random.randint(minimum, maximum)
    print 'Range is from:', minimum, 'to:', maximum, '.'
    beggining = datetime.datetime.now()
    while guess != MagicNumber and chances > 0:
        sys.stdout.write("Take your guess: ")
        guess = int(raw_input())
        if guess == MagicNumber:
            print "That's it! Congratulations, you guessed it!\n Your magic number is: ", MagicNumber
            break
        if guess > MagicNumber:
            print "Too much! "
            chances -= 1
        if guess < MagicNumber:
            print "Not enough! "
            chances -= 1
    ending = datetime.datetime.now()
    if chances <= 0:
        print "Sorry... out of chances :-("
        print "Your magic number was: ", MagicNumber, "!"
    print "You played for:", (ending - beggining).seconds, ".", ((ending - beggining).microseconds / 10000), " seconds"
    WannaStay()


def main():
    Menu()
    gra()


DzienDobry()
main()
