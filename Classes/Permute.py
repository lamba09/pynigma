import types as t
import ConfigParser

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


class PObject(object):

    def __init__(self, configuration = None, verbose=False):
        self.verbose = verbose
        self.alphabet_ABC = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.alphabet_abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.alphabet = self.alphabet_ABC + self.alphabet_abc
        self.name = ""
        self.type = ""
        self.configuration = {}
        self.SetConfiguration(configuration)

    def VerbosePrint(self, *args):
        if self.verbose:
            # Print each argument separately so caller doesn't need to
            # stuff everything to be printed into a single string
            for arg in args:
               print arg,
            print
        else:
            pass

    def SetConfiguration(self, configuration=None):
        if configuration == None:
            for i in xrange(26):
                self.configuration[i] = i
        else:
            letters = False
            numbers = False
            assert(len(configuration) == 26), "wrong length of configuration"
            for i in configuration:
                letters |= type(i) == t.StringType
                numbers |= (type(i) == t.IntType or type(i) == t.FloatType)
            assert((letters or numbers) and not (letters and numbers)), "Bad configuration content"
            if letters:
                listOfNumbers = self.StringToNumbers(configuration)
                self.SetConfiguration(listOfNumbers)
            else:
                for i in xrange(26):
                    self.configuration[i] = configuration[i]

    def LetterToNumber(self,letter):
        assert(type(letter) is t.StringType and letter in self.alphabet), "Bad letter input"
        nr = 0
        for i in self.alphabet:
            if i == letter:
                self.VerbosePrint("Letter found in alphabet: ", i, " == ", letter, " ; it has number ", nr, " in alphabet list. Return: ", nr%26)
                break
            nr += 1
        nr %= 26
        return  nr

    def NumberToLetter(self, number):
        assert(type(number) == t.IntType)
        number %= 26
        return self.alphabet_ABC[number]

    def StringToNumbers(self, string = None):
        if string != None:
            self.VerbosePrint("Converting String to Number; input: ", string)
        else:
            string = raw_input("Enter Text to convert to Numbers in alphabet (A..Z, a..z): ")
        numbers = []
        for letter in string:
            numbers.append(self.LetterToNumber(letter))
        if len(numbers) == 1:
            self.VerbosePrint("Output of String to number is single number: ", numbers[0])
            return numbers[0]
        else:
            return numbers

    def Rotate(self):
        pass

    def Translate(self,letter, backwards = False):
        if type(letter) == t.StringType:
            letter = self.StringToNumbers(letter)
        if not backwards:
            return self.configuration[letter]
        else:
            answer = -1
            for initial in self.configuration.keys():
                if letter == self.configuration[initial]:
                    answer = initial
                    break
            assert(answer>0), "Error 404: initial letter not found"
            return answer

    def ShowConfiguration(self):
        abc = ""
        config = ""
        for i in self.alphabet_ABC:
            abc += i
        for i in xrange(26):
            config += self.NumberToLetter(self.configuration[i])
        print "\nPermutation Configuration:"
        print abc
        print config

class Rotor(PObject):

    def __init__(self, name, rotorposition="A", ringposition="A", verbose=False):
        names = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", 1, 2, 3, 4, 5, 6, 7, 8]
        assert(name in names), "Rotor "+str(name)+" not found"
        if type(name) is t.IntType:
            name = names[name - 1]
        PObject.__init__(self, None, verbose)
        self.type = "Rotor"
        self.name = name
        self.ConfigParser = ConfigParser.ConfigParser()
        self.ConfigParser.read("Configurations/Rotors/ROTOR_"+self.name+".cfg")
        self.SetRingPosition(ringposition)

        notch = self.ConfigParser.get("ROTOR", "notch")
        if len(notch)>1:
            self.notch = [notch[0], notch[2]]
            self.notchNr = [(self.LetterToNumber(self.notch[0]) + 0)%26, (self.LetterToNumber(self.notch[1]) + 0)%26]
        else:
            self.notch = notch
            self.notchNr = [(self.LetterToNumber(self.notch) + 0)%26]

        self.SetRotorStartPosition(rotorposition)

        self.VerbosePrint("Initialisation complete Rotor ", self.name, ". In Position: ", self.rotorPosition)
        if self.verbose:
            self.ShowConfiguration()

    def SetRingPosition(self, ringposition = "A"): # set ring possitions bevore rotors would be nice
        self.initialConfiguration = self.ConfigParser.get("ROTOR","wiring")
        if type(ringposition) is t.StringType:
            self.ringPositionNr = self.LetterToNumber(ringposition)
        elif type(ringposition) is t.IntType and ringposition > 0:
            self.ringPositionNr = ringposition - 1
        else:
            assert(False), "Incompatible ringposition"
        self.ringPosition = self.NumberToLetter(self.ringPositionNr)
        self.initialConfiguration = self.initialConfiguration[-self.ringPositionNr:]+self.initialConfiguration[:-self.ringPositionNr]
        if hasattr(self, "rotorPosition"):
            self.SetRotorStartPosition(self.rotorPosition)
        else:
            self.SetConfiguration(self.initialConfiguration)


    def SetRotorStartPosition(self, rotorposition):
        self.SetConfiguration(self.initialConfiguration)
        self.rotorPosition = "A"
        self.rotorPositionNr = 0
        if type(rotorposition) is t.IntType:
            rotorposition = self.alphabet_ABC[rotorposition - 1]
        for i in xrange(self.LetterToNumber(rotorposition)):
            self.Rotate()

    def Translate(self,letter, backwards = False):
        #print "rot pos: ", self.rotorPositionNr
        self.VerbosePrint("Translating Letter ", letter, " trough Rotor ", self.name, "...")
        if type(letter) == t.StringType:
            self.VerbosePrint("Letter is String type (", letter, "). Will converte to Number...")
            letter = self.StringToNumbers(letter)
        else:
            letter %= 26
        if not backwards:
            self.VerbosePrint("Start Translating Letter number ", letter, " in forward direction through Rotor ", self.name)
            result = (self.configuration[letter] - self.rotorPositionNr + self.ringPositionNr) % 26
            self.VerbosePrint("TRANSLATE RETURN: ({0} - {1} + {2}) % 26 = {3}".format(self.configuration[letter],self.rotorPositionNr, self.ringPositionNr, result))
            return result
        else:
            self.VerbosePrint("Start Translating Letter number ", letter, " in reversed direction through Rotor ", self.name)
            self.VerbosePrint("letter + rotorpositionNr - ringPositionNr: ", letter, " + ", self.rotorPositionNr, " - ", self.ringPositionNr, " = ", (letter + self.rotorPositionNr - self.ringPositionNr)%26)
            letter = letter + self.rotorPositionNr - self.ringPositionNr # this is the left letter on the rotor (abc) on position "letter"
            letter %= 26
            answer = -1
            self.VerbosePrint("looking for ", letter, " in configuration keys, s.t. ",letter," == configuration[?]")
            for initial in self.configuration.keys():
                if letter == self.configuration[initial]:
                    answer = initial
                    break
            assert(answer>=0), "Error 404: initial letter not found"
            self.VerbosePrint("Translation output: ", answer)
            return answer

    def Rotate(self, reversed = False):
        #print "rotate ", self.rotorPosition
        rotateNextRotor = False
        if self.rotorPositionNr in self.notchNr: # Notch number not anymore valid if ringposition changed !
            rotateNextRotor = True
        configuration = []
        for i in xrange(26):
            configuration.append(self.configuration[i])
        if reversed: # [ABCD...XYZ] --> [ZABC...WXY]  WRONG direction !
            configuration = [configuration[25]]+configuration[:-1]
            self.rotorPositionNr += 1
        else: # [ABCD...XYZ] --> [BCDE...YZA]
            firstElement = configuration[0]
            configuration = configuration[-25:]
            configuration.append(firstElement)
            self.rotorPositionNr += 1
        self.SetConfiguration(configuration)
        self.rotorPositionNr %= 26
        self.rotorPosition = self.NumberToLetter(self.rotorPositionNr)
        self.VerbosePrint("Rotor ",self.name," rotated. New position: ", self.rotorPosition, " i.e. number ",self.rotorPositionNr)
        if self.verbose:
            print "New Configuration of Rotor ", self.name
            self.ShowConfiguration()
        return rotateNextRotor


class Reflector(PObject):

    def __init__(self, name, verbose = False):
        PObject.__init__(self,verbose=verbose)
        assert(name in ["A", "B", "C", "a", "b", "c"]), "Reflector "+str(name)+" not found"
        if name in ["a", "b", "c"]:
            name = self.NumberToLetter(self.LetterToNumber(name))
        parser = ConfigParser.ConfigParser()
        parser.read("Configurations/Reflectors/REFLECTOR_"+name+".cfg")
        configuration = parser.get('REFLECTOR','wiring')
        self.SetConfiguration(configuration)
        self.name = name
        self.type = "Reflector"

    def SetConfiguration(self, configuration):
        error = False
        super(Reflector, self).SetConfiguration(configuration)
        # testing if configuration is allowed (i.e. has only loops of length 2)
        for key in self.configuration.keys():
            start = key
            out1 = self.configuration[start]
            out2 = self.configuration[out1]
            error |= not (start == out2) # true if e.g. S->F, F->X instead of S->F, F->S
        assert(not error), self.type+" configuration not compatible. It has to have just loops like e.g. A-F and F-A"

    def SetReflector(self, name):
        pass

class Plugboard(Reflector):

    def __init__(self, configuration = None, verbose = False):
        PObject.__init__(self, configuration, verbose)
        self.name = "Plugboard"
        self.type = "Plugboard"

    def Setup(self):
        print "Add a new pair to the Plugboard by"
        print "typing two letters. (Example: `AK`"
        print "or `ak`). Type `.q` if done."
        for i in xrange(10):
            newPair = raw_input("Add pair to connect: ")
            if newPair == ".q":
                break
            self.AddPair(newPair)
            self.ShowSlots()
        self.ShowPlugs()

    def AddPair(self, pair = None):
        assert(len(pair) == 2 and pair[0] in self.alphabet and pair[1] in self.alphabet), "Bad pair"
        if self.CheckIfFreeSlots(pair):
            self.configuration[self.LetterToNumber(pair[0])] = self.LetterToNumber(pair[1])
            self.configuration[self.LetterToNumber(pair[1])] = self.LetterToNumber(pair[0])
        else:
            print "slots not free:"
            print pair[0], "-->", self.NumberToLetter(self.configuration[self.LetterToNumber(pair[0])])
            print pair[1], "-->", self.NumberToLetter(self.configuration[self.LetterToNumber(pair[1])])
            self.ShowPlugs()

    def RemovePair(self, pair):
        if self.CheckIfPairConnencted(pair):
            self.configuration[self.LetterToNumber(pair[0])] = self.LetterToNumber(pair[0])
            self.configuration[self.LetterToNumber(pair[1])] = self.LetterToNumber(pair[1])
        else:
            print pair, " is not a connected pair."

    def RemoveAll(self):
        for i in xrange(26):
            self.configuration[i] = i
        if hasattr(self, "pairs"):
            self.pairs = ""
        self.VerbosePrint("All Plugs removed.")

    def CheckIfFreeSlots(self,pair):
        if self.configuration[self.LetterToNumber(pair[0])] == self.LetterToNumber(pair[0]) and self.configuration[self.LetterToNumber(pair[1])] == self.LetterToNumber(pair[1]):
            return True
        else:
            return False

    def CheckIfPairConnencted(self, pair):
        if self.configuration[self.LetterToNumber(pair[0])] == self.LetterToNumber(pair[1]) and self.configuration[self.LetterToNumber(pair[1])] == self.LetterToNumber(pair[0]):
            return True
        else:
            return False


    def ShowPlugs(self, before="", after="", printResult = True, buildString = True):
        self.pairs = ""
        self.found_letternumbers = []
        self.freeSlots = ""
        for i in xrange(26):
            tmp1 = self.configuration[i]
            tmp2 = self.configuration[tmp1]
            if i != tmp1 and i == tmp2 and i not in self.found_letternumbers and tmp1 not in self.found_letternumbers:
                self.pairs += (self.NumberToLetter(i) + self.NumberToLetter(tmp1) + " ")
                self.found_letternumbers.append(i)
                self.found_letternumbers.append(tmp1)
            elif i == tmp1:
                self.freeSlots += self.NumberToLetter(i)+" "
            else:
                pass
        if buildString:
            pairsString = "Pairs: "+self.pairs
            if len(self.pairs) <= 15:
                pairsString = ExtendStringTo(pairsString, 24)
                pairsString = before+pairsString+after
            else:
                pairsString1 = "Pairs: "+(self.pairs[:15])
                pairsString2 = "       "+(self.pairs[15:])
                pairsString1 = ExtendStringTo(pairsString1, 24)
                pairsString2 = ExtendStringTo(pairsString2, 24)
                pairsString = before+pairsString1+after+"\n"+before+pairsString2+after
            slotsString = "Free Slots:"
            slotsString = ExtendStringTo(slotsString, 24)
            slotsString = before + slotsString + after
            plugboardString = self.ShowSlots(before=before, after=after, printResult=False)
            plugConfigString = pairsString+"\n"+slotsString+"\n"+plugboardString
            if printResult:
                print pairsString
                print slotsString
            return plugConfigString

    def ShowSlots(self, before="", after="", printResult=True):
        self.ShowPlugs(printResult=False, buildString = False)
        Letters = before+" __________________     "+after+"\n"+before+"|Q W E R T Z U I O |    "+after+"\n"+before+"| A S D F G H J K  |    "+after+"\n"+before+"|P Y X C V B N M L |    "+after+"\n"+before+" ==================     "+after
        LetterList = list(Letters)
        for letter in list(self.pairs):
            if letter in LetterList and letter != " " and letter != "\n":
                index = LetterList.index(letter)
                LetterList[index] = "_"
        Letters = "".join(LetterList)
        if printResult:
            print Letters
        return Letters
        

    # def ShowConfiguration(self):
    #     pass


# from random import shuffle
# from Permute import PObject
# rot1 = PObject()
# a = [i+1 for i in xrange(26)]
# shuffle(a)
# rot1.SetConfiguration(a)
# rot1.ShowConfiguration()