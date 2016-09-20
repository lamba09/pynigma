from Classes.EnigmaClass import Enigma

def Translate(text = None, once = True):
        myEnigma.Translate(text = text, once=once)

def ChangeWheelPositions():
        print "\n---------------------------"
        print "Choose the Wheel Pos."
        print "---------------------------"
        print "Type either: A, B, etc.."
        print "or: a, b, etc.."
        print "or: 1, 2, etc.."
        left = raw_input("Choose Left Letter: ")
        if len(left) != 3:
            middle = raw_input("Choose Middle Letter: ")
            right = raw_input("Choose Right Letter: ")
            numbers = [str(i+1) for i in xrange(26)]
            numbers += ["0"+str(i+1) for i in xrange(9)]
            if left in numbers:
                left = int(left)
            if middle in numbers:
                middle = int(middle)
            if right in numbers:
                right = int(right)
        else:
            middle = left[1]
            right = left[2]
            left = left[0]
        myEnigma.SetRotorStartPositions(left, middle, right)
        print "\nWheels moved. New Configuration:"
        myEnigma.ShowRotorWindow()

def ResetWheels():
        print "Wheels set to:"
        myEnigma.Reset()

def ChangeRotors():
        print "\n---------------------------"
        print "Choose the Rotors"
        print "---------------------------"
        print "Type either: I, II, etc.."
        print "or: 1, 2, etc.."
        left = raw_input("Choose Left Rotor: ")
        middle = raw_input("Choose Middle Rotor: ")
        right = raw_input("Choose Right Rotor: ")
        numbers = [str(i+1) for i in xrange(8)]
        if left in numbers:
            left = int(left)
        if middle in numbers:
            middle = int(middle)
        if right in numbers:
            right = int(right)
        myEnigma.SetRotors(left, middle, right)
        print "\nRotors changed. New Configuration:"
        myEnigma.ShowConfiguration()

def ChangeRingPositions():
        print "\n---------------------------"
        print "Change Ring Positions"
        print "---------------------------"
        print "Type either: A, B, etc.."
        print "or: a, b, etc.."
        print "or: 1, 2, etc.."
        left = raw_input("Set Left Ring Pos.: ")
        middle = raw_input("Set Middle Ring Pos.: ")
        right = raw_input("Set Right Ring Pos: ")
        numbers = [str(i+1) for i in xrange(26)]
        numbers += ["0"+str(i+1) for i in xrange(9)]
        if left in numbers:
            left = int(left)
        if middle in numbers:
            middle = int(middle)
        if right in numbers:
            right = int(right)
        myEnigma.SetRingPositions(left, middle, right)
        print "\nRings adjusted. New Configuration:"
        myEnigma.ShowConfiguration()

def ChangeReflector():
        print "\n---------------------------"
        print "Change Reflector"
        print "---------------------------"
        print "Type either: A, B, or C"
        reflector = raw_input("Choose Reflector: ")
        myEnigma.SetReflector(reflector, verbose=verbose)
        print "\nReflector chosen. New Configuration:"
        myEnigma.ShowConfiguration()

def NewPlugboardConfiguration():
        print "\n---------------------------"
        print "New Plugboard Configuration"
        print "---------------------------"
        myEnigma.plugboard.RemoveAll()
        myEnigma.plugboard.ShowSlots()
        myEnigma.PlugboardSetup()
        print "PLUGBOARD SETTING:"
        myEnigma.plugboard.ShowConfiguration()

def AddPair():
        print "\n---------------------------"
        print "Add a pair to the Plugboard"
        print "---------------------------"
        print "by typing two letters."
        print "(Example: `AK` or `ak`)"
        myEnigma.plugboard.ShowPlugs()
        pair = raw_input("Enter pair to add: ")
        myEnigma.plugboard.AddPair(pair=pair)
        myEnigma.plugboard.ShowPlugs()

def RemovePair():
        print "\n---------------------------"
        print "Remove a pair from the Plugboard"
        print "---------------------------"
        print "by typing two letters."
        print "(Example: `AK` or `ak`)"
        myEnigma.plugboard.ShowPlugs()
        pair = raw_input("Enter pair to remove: ")
        myEnigma.plugboard.RemovePair(pair=pair)
        myEnigma.plugboard.ShowPlugs()

def RemoveAllPairs():
        myEnigma.plugboard.RemoveAll()
        print "All Plugs removed:"
        myEnigma.plugboard.ShowSlots()


verbose = False
show_steps = False

myEnigma = Enigma(ShowSteps=show_steps, verbose=verbose)

possibilities = [41, 42, 51, 61, 62, 63, 64, 7, 8, 9, 4.1, 4.2, 5.1, 5.2, 6.1, 6.2, 6.3, 1, 2, 3, 4]
quit = False
while not quit:
    try:
        print "\n---------------------------"
        print "What do you want to do?"
        print "---------------------------"
        print "1 Enter Text"
        print "2 Change Wheel Positions"
        print "3 Reset Wheels"
        print "4 more.."
        choice = raw_input("--> Enter the Number or Text: ")
        try:
            if float(choice) in possibilities:
                if float(choice) % 1. == 0:
                    choice = int(float(choice))
                else:
                    choice = int(10*float(choice))
            else:
                choice = 99
                print "Seems like your parents are brothers and sisters. Try again."
        except ValueError:
            translateText = choice
            choice = 98


        if choice == 4:
            print "4 ROTORS:"
            print " 41 Change Rotors"
            print " 42 Change Ring Positions"
            print "5 REFLECTOR:"
            print " 51 Change Reflector"
            print "6 PLUGBOARD"
            print " 61 New Configuration"
            print " 62 Add Pair"
            print " 63 Remove Pair"
            print " 64 Remove All Pairs"
            print "7 New Configuration"
            print "8 Show Configuration"
            print "9 Quit"
            choice = raw_input("--> Enter the Number or Text: ")
            try:
                if float(choice) in possibilities:
                    if float(choice) % 1. == 0:
                        choice = int(float(choice))
                    else:
                        choice = int(10*float(choice))
                else:
                    choice = 99
                    print "Seems like your parents are brothers and sisters. Try again."
            except ValueError:
                translateText = choice
                choice = 98



        # Change Wheel Positions
        if choice == 2:
            ChangeWheelPositions()

        # Reset Wheels
        if choice == 3:
            ResetWheels()

        # Change Rotors
        if choice == 41:
            ChangeRotors()

        # Change Ring Positions
        if choice == 42:
            ChangeRingPositions()

        # Change Reflector
        if choice == 51:
            ChangeReflector()

        # New PlugBoard Configuration
        if choice == 61:
            NewPlugboardConfiguration()

        # Add Pair
        if choice == 62:
            AddPair()

        # Remove Pair
        if choice == 63:
            RemovePair()

        # Remove All Pairs
        if choice == 64:
            RemoveAllPairs()

        # New Configuration
        if choice == 7:
            ChangeRotors()
            ChangeRingPositions()
            ChangeReflector()
            NewPlugboardConfiguration()
            ChangeWheelPositions()
            print "New Configuration done.\n"

        # Show Configuration
        if choice == 8:
            pass

        # Quit
        if choice == 9:
            quit = True

        myEnigma.ShowConfiguration()

        # Enter TEXT
        if choice == 1:
            Translate(once=False)
        if choice == 98:
            Translate(text=translateText)
    except:
        print "\n\n\n\n\n\n ERROR \n\n\n\n\n\n\n"

print "Please come again..\n"