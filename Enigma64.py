from string import ascii_letters, digits
import base64

class reflectors:
    saved = { 0:'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz5678901234/+=',
            1:'SVTvYO/NIxpDFnPkZ714Xd2jGM=BRl9my5iKJLzhfoUCacQb3ueq6swWtH0r+E8gA',
            2:'Zi2D+/7zbrsTVtXL0jknPR4MyhHCBdKJ9A1FEpx6=uYvUlSm8oQaqIc5w3NgWGefO',
            3:'fdnbZa8Jx5ND3cC6Q4B2A+ViLFusolYz7XPhRyMkTIqK9O0w/HEeU=tmrjpGgSvW1',
            4:'fDc04aV=A/UuoFmQ6CzMlY58NsiJrbEn91XBT7tyOWp3ZKkgPIvSdH+RewqLxG2jh',
            5:'UXGQqfBHNvt38J9DeZPkLj/CSR2gxpK5chYnEu6i+sdzy0aWVbIrT4Al1FM=moOw7'}

    def __init__(self, **kwargs):
        ''' version = 1-3\n
        defaults to preset 0 if version not specified\n
        '''
        if "version" in kwargs.keys():
            self.version = kwargs["version"]
            self.mapper(self.version)
        else:
            self.mapper()

    def __repr__(self):
        return f'Reflector Version: {self.version}\nReflections: {self.reflections}'

    def mapper(self, preset=0):
        '''Creates the reflector map from reflector key and saves it as self.reflections'''
        reflKey = reflectors.saved[preset]
        statorKey = ascii_letters + digits + "+/="
        map = {}
        reflMap = {}

        for i,char in enumerate(statorKey):
            map[char]=i
            map[i]=char
        for i in range(len(statorKey)):
            reflMap[map[statorKey[i]]] = map[reflKey[i]]
            self.reflections = reflMap

    def reflect(self, contact):
        ''' It takes contact number as argument and returns it's reflection'''
        return self.reflections[contact]

class rotors:
    saved = {0:('QWERTYUIOPasdfghjklZXCVBNMqwertyuiopASDFGHJKLzxcvbnm0569832147/=+', [64]),
            1:('k4svlEXw1Yd3fnCSHAyhapOuIoPGezK+b2c9JZM07=mxQFTB5gNVrLWtiDU/jqR86',[25]),
            2:('ilQ2MpXcvftxTnSIOF8YJa+5srmVUwdzkH7ujobqL9EW13ZKRAhD0yBC6N=Pe4g/G',[38]),
            3:('IJwMfOj3ux8gK9C21Aozs/5NX0Sr64+dQLvpWVbRDn=GTqZylFUaePE7BthciHmYk',[21]),
            4:('mqc7FZlK0MOw9TGPBjXYtdxsnyA/SQLUebpRok3IDfJ1zC8i4r6Wh=VE5ag+uHvN2',[61]),
            5:('5inS1EG2KhWzFrNJyZ6wmVDA8X7=IQ/tM+30pqBf9kxYvuoPHC4sblTdOcReUjLga',[53]),
            6:('P=0zh56fT9pEMBtony8eZbV3kcDxGNwQRKCLg7YqIOrFal1u2d+/UJiv4jXHASmsW',[10]),
            7:('b4+8c6/JBzYP0ufOXrMj7g9T3=wqRyUiAZLsxed5KmlDhp1akG2QIntVCFESWNvoH',[27]),
            8:('0eG4VBFsoxmSiz/ZuIrCNpDYEHJTkhv5a7PLwX3U28bj6qdQf+9AM=gWclO1KytRn',[0]),
            9:('=wmlXfH765r2UQ3OpKavYnMJkWRidy4tTgjCesqF8z/xhIbcG0NBo+PDLZA1VSE9u',[55]),
            10:('07XNej8fEROB9mPvotAgl5Zn/+QYDxzFTGqV6wb3pIW2dHhiKCL1Mur4akcSsJy=U',[2]),
            11:('zBmkKbvhsSu2gUrleDJX8=F3xa9cIiHwTNjyA0Vn7WYE5+dLt/CQROM4qopfZ1G6P',[44]),
            12:('/Lqzfx6DiMUJtChwgjInuFmGsorBTb078H+=5PYcXvWRNy1Qdel43ZAk9KEaVOp2S',[53])}
    rotorSequence = {}

    def __init__(self, **kwargs):

        """ rotor_num = 1-3, preset = 1-5, position = 0-64, offset = 0-64 """

        # default values
        self.preset = 0
        self.offset = 0
        self.position = 0

        # switching to given values
        if "rotor_num" in kwargs: self.rotor_num = kwargs["rotor_num"] # regarding sequence of rotors
        if "preset" in kwargs: self.preset = kwargs["preset"] # choosing rotor from presets given
        if "offset" in kwargs: self.offset = kwargs["offset"] # ring setting
        if "position" in kwargs: self.position = kwargs["position"] # position (in window) according to new ring setting
        if "notches" in kwargs: self.notches = kwargs["notches"] # notches of a rotor
        else: self.notches = rotors.saved[self.preset][1] # load from preset

        # setting up remaining properties
        rotors.rotorSequence[self.rotor_num] = self # listing the rotor in "rotors(class) > rotorSequence(array)"
        self.mapper(self.preset) # applying wiring from saved sets
        self.notch_found = False

    def __repr__(self):
        return f'<Rotor no. {self.rotor_num}, Preset: {self.preset}, Position: {self.position}, Offset: {self.offset}>'
    def mapper(self, preset=0):
        '''takes preset number as an arguments and maps the\n
        rotor wiring accordingly'''
        statorKey = ascii_letters + digits + "+/="
        rotorKey = rotors.saved[preset][0]
        map = {}
        rotorMap = {}
        for i,char in enumerate(statorKey):
            map[char]=i
            map[i]=char
        for i in range(len(statorKey)):
            rotorMap[i] = [map[rotorKey[i]]]
        for i in range(len(statorKey)):
            temp = rotorMap[map[rotorKey[i]]]
            rotorMap[map[rotorKey[i]]] = (temp[0], i)
        rotorMap["wiring"] = rotorKey

        self.wiring = rotorMap
    def rotate(self):
        '''rotates the rotorset once (for each keypress)'''
        # should this rotor make the next rotor rotate?
        if self.position in self.notches and self.rotor_num < len(rotors.rotorSequence):
            rotors.rotorSequence[self.rotor_num + 1].notch_found = True
        # to rotate or not to rotate
        if self.rotor_num == 1:
            self.position +=1
        ## Double Shift [Deactivated for better security]
        # elif self.position in self.notches and self.rotor_num < len(rotors.rotorSequence): # double shift
        # self.position +=1
        elif self.notch_found:
            self.position += 1
            self.notch_found = False     
        # Completion of rotation >>> Reset
        self.position %= 65
    def passLeft(self, contact):
        '''takes contact from right and sends to left\n
        meanwhile taking care of rotation in the\n
        forward cycle'''
        self.rotate() # Rotation prior to connection
        # self.position (offset) >>> truPos
        # input SCN (truPos) >>> input CLN
        # input CLN (wiring) >>> output CLN (LCLN)
        # output CLN (truPos) >>> output SCN (LSCN)
        # Finding truePos from position and offset - position according to rotors fixed central line number
        # truPos = (self.position - self.offset)%65 # actual rotational position of rotor
        # ## if truPos < 0: truPos += 65
        # # finds the CLN (Central line number) for input SCN
        # CLN = (truPos + contact)%65
        # ## if CLN > 64: CLN -= 65 #25 and 26
        # # finds the rotors LCLN from input CLN
        # LCLN = self.wiring[CLN][0]
        # # finds the LSCN from LCLN
        # LSCN = (LCLN - truPos)%65
        # ## if LSCN < 0: LSCN +=65
        ### TODO Maybe I can optimise by separating left right pass tuple
        LSCN = (self.wiring[(self.position-self.offset+contact)%65][0] - (self.position-self.offset))%65
        return LSCN
            
    def passRight(self, contact):
        
        '''takes contact from right and sends to left\n
        without any rotation'''
        
        # Rotation is not required
        
        # self.position (offset) >>> truPos
        # input SCN (truPos) >>> input CLN
        # input CLN (wiring) >>> output CLN (RCLN)
        # output CLN (truPos) >>> output SCN (RSCN)
        
        # Finding truePos from position and offset - position according to rotors fixed central line number
        
        # truPos = (self.position - self.offset)%65 # actual rotational position of rotor
        # # if truPos < 0: truPos += 65
        
        # # finds the CLN (Central line number) for input SCN
        # CLN = (truPos + contact)%65
        # if CLN > 64: CLN -= 65 # 25 and 26 before
        
        # # finds the rotors RCLN from input CLN
        # RCLN = self.wiring[CLN][1]
        
        # # finds the RSCN from RCLN
        # RSCN = (RCLN - truPos)%65
        # # if RSCN < 0: RSCN +=65
        
        RSCN = (self.wiring[(self.position-self.offset+contact)%65][1] - (self.position-self.offset))%65
        return RSCN


class steckerbrett:
    def __init__(self, **kwargs):

        '''phrase = "aK JY cD ... uf"\n
        OR phrase = "any alphabetical word/phrase"\n
        phrase can be omitted if no letter swaps to be made
        '''
        
        self.mapper() # setting statorKey map and default steckerbrett map with no swaps    
        
        # Swapping letters according to the given phrase
        if "phrase" in kwargs.keys():
            temp = []
            self.swaps = temp
            for i in kwargs["phrase"].replace(" ", ""):
                if i not in temp:
                    temp.append(i)
                else: continue
            if len(temp) >= 2:
                for i in range(1, len(temp), 2):
                    self.pairs[temp[i]] = temp[i-1]
                    self.pairs[temp[i-1]] = temp[i]
            del temp

    def __repr__(self):
        return f'Steckerbrett : {self.swaps}'

    def mapper(self):
        statorKey = ascii_letters + digits + "+/="
        self.pairs = {}
        self.map = {}

        for i,char in enumerate(statorKey):
            self.map[char]=i
            self.map[i]=char
            self.pairs[char]= char

    def connect(self, char):
        # SCN = self.map[self.pairs[input]]
        return self.map[self.pairs[char]]

    def disconnect(self, contact):
        return self.pairs[self.map[contact]]

def getSettings():

    '''Asks the user for the initial settings for Enigma,\n
    returns those settings as a dictionary file required
    to setup The Enigma.\n
    It also saves such settings in a predefined settings
    variable named "settings."
    '''

    settings['version'] = int(input('Enter Reflector version (1-5) >>> '))
    settings['phrase'] = input('Enter Plugboard swaps as a phrase consisting (a to z, A to B, 0 to 9, +/=)\n>>> ')
    num = int(input('How many rotors do you want? >>> '))

    settings['rotors']['sequence'] = []
    for i in range(num):
        rotor_num = int(input(f'Enter number of rotor {i+1} from 1-12 >>> '))
        settings['rotors']['sequence'].append(rotor_num)    

    settings['rotors']['positions'] = []
    for i in range(num):
        position = int(input(f'Enter position of rotor {i+1} from 0-64 >>> '))
        settings['rotors']['positions'].append(position)

    settings['rotors']['offset'] = []
    for i in range(num):
        offset = int(input(f'Enter offset of rotor {i+1} from 0-64 >>> '))
        settings['rotors']['offset'].append(offset)

    return settings

def Enigma(settings):

    '''settings - settings saved in a dictionary\n
    returns (reflector, plugboard, rotorSet) which can be used\n
    as instance of enigma machine while encrypting.'''

    reflector = reflectors(version = settings['version'])
    plugboard = steckerbrett(phrase = settings['phrase'])
    sequence = settings['rotors']['sequence']
    positions = settings['rotors']['positions']
    offsets = settings['rotors']['offset']
    rotorSet = {}
    for i in range(len(sequence)):
        rotorSet[i] = rotors(rotor_num=i+1, preset=sequence[i], position=positions[i], offset=offsets[i])

    return reflector, plugboard, rotorSet

def Encrypt(message, enigma):

    '''message - base64-string which will be encrypted\n
    enigma - instance of the enigma machine\n
    returns the encrypted message.'''

    reflector, plugboard, rotorSet = enigma
    encrypted = ''

    for char in message:
        contact = plugboard.connect(char)
        for i in range(1, len(rotors.rotorSequence)+1):
            contact = rotors.rotorSequence[i].passLeft(contact)
        contact = reflector.reflect(contact)
        for i in range(len(rotors.rotorSequence), 0, -1):
            contact = rotors.rotorSequence[i].passRight(contact)
        char = plugboard.disconnect(contact)
        encrypted += char
    return encrypted

def test(size,settings):

    '''used to test if the machine is working properly\n
    by comparing original message with a message\n
    encrypted and derypted. The string is just the letter "a"\n
    repeated "size" times.\n
    size - length of message to be tested with\n
    settings - settings to be tested with'''

    message = 'a'*size
    enigma = Enigma(settings)
    enc = Encrypt(message, enigma)
    enigma = Enigma(settings)
    dec = Encrypt(enc, enigma)
    if message==dec:
        count=0
        for i,j in zip(message,enc):
            if i == j: count+=1
        return f'Matched & has {count} out of {size} letters encoded as themselves'
    else: return 'Unmatched'

def fileEncrypt(filename, saveas, enigma):

    '''filename - path for the file to be encrypted\n
    saveas - path for the encrypted file to save to\n
    enigma - instance of the enigma machine'''

    print('\nWorking on it... Please Wait..')
    with open(filename, "rb") as f:
        b64b = base64.b64encode(f.read())
    b64s = b64b.decode()
    b64sn = Encrypt(b64s, enigma)
    b64bn = b64sn.encode()

    with open(saveas, "wb") as f:
        f.write(b64bn)
    print(f'The encrypted file has been saved successfully as "{saveas}"\n')

def fileDecrypt(filename, saveas, enigma):
    '''filename - path for the file to be decrypted\n
    saveas - path for the decrypted file to save to\n
    enigma - instance of the enigma machine'''
    print('\nWorking on it... Please Wait..')
    with open(filename, "rb") as f:
        b64b = f.read()
    b64s = b64b.decode()
    b64sn = Encrypt(b64s, enigma)
    b64bn = b64sn.encode()
    plain_bn = base64.b64decode(b64bn)

    with open(saveas, "wb") as f:
        f.write(plain_bn)
    print(f'The decrypted file has been saved successfully as "{saveas}"\n')


# Settings for The Enigma
settings = {'version':0,
            'phrase':"Anyth1nG RanD0M Go3S HeR=E 69 And HWa+t CtuaLFck39875/",
            'rotors':{'sequence':[7,3,5],
            'positions':[4,15,28],
            'offset':[15,2,31]}}