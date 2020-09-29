#========================
# Cipher
#========================

class Cipher():
    def __init__(self, message):
        self.message = message

    def __Basic_Cipher(self):
        vowels = 'aeiou'
        consonants = 'bcdfghjklmnpqrstvwxyz'
        secret = ''
        updatedMessage = self.message.lower()

        for element in updatedMessage:
            if element in vowels:
                secret += vowels[(vowels.find(element) + 8) % 5]
            elif element in consonants:
                secret += consonants[(consonants.find(element) + 40) % 21]
            else:
                secret += element
        secret = secret.upper()

        return secret

    def __Upgraded_Cipher(self):

        privateDict = {'a': '4', 'b': '13', 'c': 'U', 'd': 'P', 'e': '3', 'g': '6', 'h': '#', 'i': '!',
                       'j': '?', 'k': '<', 'l': '7', 'm': 'W', 'n': 'Z', 'o': '0', 'p': 'D', 'q': ' & ', 'r': '12',
                       's': '8', 't': 'X', 'u': 'C', 'v': 'Y', 'w': 'M', 'x': '+', 'y': 'V', 'z': 'N',
                       '1': 'I', '2': '5', '3': 'E', '4': 'A', '5': '2', '6': 'G', '7': 'L', '8': 'S', '9': '@', '0': 'O',
                       '!': 'i', '?': 'j'}

        m_lower = self.message.lower()
        stringlist = list(m_lower)
        f_count = 0
        keys = privateDict.keys()
        secretMessage = ''

        for value in stringlist:
            if value == ' ':
                secretMessage += ' '
            elif value == 'f':
                f_count += 1
                if f_count % 2 == 0:
                    secretMessage += ']'
                else:
                    secretMessage += '['
            elif value not in keys:
                secretMessage += '(%s)' % (value)
            else:
                for element in privateDict.keys(): 
                    if value == element:
                        secretMessage += privateDict[element]

        if f_count % 2 != 0:
            secretMessage += '_]'

        return secretMessage
    
    def get_Basic_Cipher(self):
        return self.__Basic_Cipher()
    
    def get_Upgraded_Cipher(self):
        return self.__Upgraded_Cipher()
