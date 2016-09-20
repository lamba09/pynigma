
from random import shuffle
import ConfigParser
from Helpers.enigma_logo import enigma_logo
from Permute import PObject, Rotor, Reflector, Plugboard

def ExtendStringTo(string, number):
    length = len(string)
    if length > number:
        pass
    else:
        spaces = [" " for i in xrange(number-len(string))]
        space = "".join(spaces)
        string += space
    return string

def PrintOnMachine(before, string, after):
    string = before+ExtendStringTo(string, 26)+after
    print string

class Enigma(object):

    def __init__(self, ShowSteps = True, verbose = False):
        self.verbose = verbose
        self.showSteps = ShowSteps

        self.initialConfiguration = {
            "LeftRotor": "I",
            "MiddleRotor": "II",
            "RightRotor": "III",
            "Reflector": "A",
            "LeftRotorStartposition": "A",
            "MiddleRotorStartposition": "A",
            "RightRotorStartposition": "A"
        }
        # self.SetRotors(LeftRotor, MiddleRotor, RightRotor, verbose = self.verbose)
        # self.SetReflector(reflector, verbose = self.verbose)
        self.plugboard = Plugboard(verbose = self.verbose)
        # self.SetRotorStartPositions(LeftRotorStartposition, MiddleRotorStartposition, RightRotorStartposition)

        self.LoadConfig()

        self.WelcomeMessage()

    def LoadConfig(self):
        Parser = ConfigParser.ConfigParser()
        Parser.read("Configurations/ENIGMA.cfg")

        rotors = Parser.get("ROTOR", "Rotors")
        rot_L = int(rotors[0])
        rot_M = int(rotors[2])
        rot_R = int(rotors[4])
        self.SetRotors(rot_L, rot_M, rot_R, verbose=self.verbose)

        ringPositions = Parser.get("ROTOR", "RingPositions")
        r_L = int(ringPositions[0:2])
        r_M = int(ringPositions[3:5])
        r_R = int(ringPositions[6:])
        self.SetRingPositions(r_L, r_M, r_R)

        wheels = Parser.get("ROTOR", "WheelPositions")
        w_L = wheels[0]
        w_M = wheels[2]
        w_R = wheels[4]
        self.SetRotorStartPositions(w_L, w_M, w_R,show=False)

        reflector = Parser.get("REFLECTOR", "Reflector")
        self.SetReflector(reflector, verbose=self.verbose)

        plugs = Parser.get("PLUGBOARD", "Pairs")
        numberOfPairs = 1.*(len(plugs)+1)/3.
        if numberOfPairs%1. == 0:
            numberOfPairs = int(numberOfPairs)
            for i in xrange(numberOfPairs):
                pair = plugs[0+i*3:2+i*3]
                self.plugboard.AddPair(pair)
        elif len(plugs) == 0:
            pass
        else:
            print "Bad Plugboard Configuration. Enter Manually:"
            self.PlugboardSetup()

    def VerbosePrint(self, *args):
        if self.verbose:
            # Print each argument separately so caller doesn't need to
            # stuff everything to be printed into a single string
            for arg in args:
               print arg,
            print
        else:
            pass
    
    def WelcomeMessage(self):
        print enigma_logo
        self.ShowConfiguration()
    
    def Reset(self):
        self.SetRotorStartPositions(self.initialConfiguration["LeftRotorStartposition"],
                              self.initialConfiguration["MiddleRotorStartposition"],
                              self.initialConfiguration["RightRotorStartposition"], show=False)
        self.ShowRotorWindow()

    def ShowRotorWindow(self, extended=False):
        if extended:
            extension = "|"
            extensionR = "|  |"
            extension_corner = "+  |"
        else:
            extension = ""
            extensionR = ""
            extension_corner = ""
        print extension+"---------------------------"+extension_corner
        print (extension+"----|{0}|-----|{1}|-----|{2}|----"+extensionR).format(self.leftRotor.rotorPosition, self.middleRotor.rotorPosition, self.rightRotor.rotorPosition)
        print extension+"---------------------------"+extensionR

    def ShowConfiguration(self):
        before = "| "
        after = "|  |"
        print "  +--------------------------- +\n /                           / |"
        self.ShowRotorWindow(extended=True)
        PrintOnMachine(before, "Rotors:", after)
        PrintOnMachine(before, "      "+self.leftRotor.name+" "+self.middleRotor.name+" "+self.rightRotor.name, after)
        PrintOnMachine(before, "Ring Positions:", after)
        PrintOnMachine(before, "        "+self.leftRotor.ringPosition+"   "+self.middleRotor.ringPosition+"   "+self.rightRotor.ringPosition, after)
        PrintOnMachine(before, "      ({0:02d})({1:02d})({2:02d})".format(self.leftRotor.ringPositionNr + 1, self.middleRotor.ringPositionNr + 1, self.rightRotor.ringPositionNr + 1), after)
        PrintOnMachine(before, "Reflector: "+self.reflector.name, after)
        self.ShowPlugboardConfig(before=before, after=after)
        print "|                           | /\n+---------------------------+"

    def ShowPlugboardConfig(self, before="", after=""):
        print before+"PLUGBOARD                 "+after
        print self.plugboard.ShowPlugs(before=before+"  ", after=after, printResult=False)

    def SetRotors(self, left, middle, right, verbose = False):
        self.leftRotor = Rotor(left, verbose=verbose)
        self.middleRotor = Rotor(middle, verbose=verbose)
        self.rightRotor = Rotor(right, verbose=verbose)
        self.initialConfiguration["LeftRotor"] = left
        self.initialConfiguration["MiddleRotor"] = middle
        self.initialConfiguration["RightRotor"] = right

    def SetReflector(self, reflector, verbose=False):
        self.reflector = Reflector(reflector, verbose=verbose)
        self.initialConfiguration["Reflector"] = reflector

    def SetRingPositions(self, left, middle, right):
        self.leftRotor.SetRingPosition(left)
        self.middleRotor.SetRingPosition(middle)
        self.rightRotor.SetRingPosition(right)

    def SetRotorStartPositions(self, left, middle, right, show = True):
        self.leftRotor.SetRotorStartPosition(left)
        self.middleRotor.SetRotorStartPosition(middle)
        self.rightRotor.SetRotorStartPosition(right)
        self.initialConfiguration["LeftRotorStartposition"] = left
        self.initialConfiguration["MiddleRotorStartposition"] = middle
        self.initialConfiguration["RightRotorStartposition"] = right
        if show:
            self.ShowRotorWindow()
    
    def PlugboardSetup(self):
        self.plugboard.Setup()
    
    def Translate(self, text = None, once = False):
        inputtext = text
        quit = False
        while not quit:
            if once:
                quit = True
                quittext = ""
            else:
                quittext = " (`.q` for Quit)"

            if inputtext == None:
                text = raw_input("Enter Text"+quittext+": ")
                if text == ".q":
                    quit = True
                    print "quitting.."
                    continue
            else:
                quit = True

            #self.ShowRotorWindow()
            answer = ""
            for letter in text:
                if letter != " ":
                    # rotate + 1

                    if self.rightRotor.rotorPositionNr in self.rightRotor.notchNr or self.middleRotor.rotorPositionNr in self.middleRotor.notchNr:
                        rotate_middle = True
                    else:
                        rotate_middle = False
                    if self.middleRotor.rotorPositionNr in self.middleRotor.notchNr:
                        rotate_left = True
                    else:
                        rotate_left = False

                    self.rightRotor.Rotate()
                    if rotate_middle:
                        self.middleRotor.Rotate()
                    if rotate_left:
                        self.leftRotor.Rotate()

                    if self.showSteps: self.ShowRotorWindow()
                    pb1 = self.plugboard.Translate(letter)
                    r1 = self.rightRotor.Translate(pb1)
                    self.VerbosePrint(letter+" -> "+self.rightRotor.NumberToLetter(r1)+"\n")
                    r2 = self.middleRotor.Translate(r1)
                    self.VerbosePrint(self.rightRotor.NumberToLetter(r1)+" -> "+self.rightRotor.NumberToLetter(r2)+"\n")
                    r3 = self.leftRotor.Translate(r2)
                    self.VerbosePrint(self.rightRotor.NumberToLetter(r2)+" -> "+self.rightRotor.NumberToLetter(r3)+"\n")
                    ref = self.reflector.Translate(r3)
                    self.VerbosePrint(self.rightRotor.NumberToLetter(r3)+" -> "+self.rightRotor.NumberToLetter(ref)+"\n")
                    b3 = self.leftRotor.Translate(ref,backwards=True)
                    self.VerbosePrint(self.rightRotor.NumberToLetter(ref)+" -> "+self.rightRotor.NumberToLetter(b3)+"\n")
                    b2 = self.middleRotor.Translate(b3,backwards=True)
                    self.VerbosePrint(self.rightRotor.NumberToLetter(b3)+" -> "+self.rightRotor.NumberToLetter(b2)+"\n")
                    b1 = self.rightRotor.Translate(b2,backwards=True)
                    self.VerbosePrint(self.rightRotor.NumberToLetter(b2)+" -> "+self.rightRotor.NumberToLetter(b1)+"\n")
                    pb2 = self.plugboard.Translate(b1)
                    if self.showSteps: print letter+" -> "+self.rightRotor.NumberToLetter(pb2)+"\n"
                    answer += self.rightRotor.NumberToLetter(pb2)

            print "\n\n===========OUTPUT=========="
            print answer
            print "===========================\n\n"
            self.ShowRotorWindow()