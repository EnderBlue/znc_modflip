# flip.py

import os
import znc

# Create a ~/.fliptable with:
#  user: myuser
# in order to set your username (until you update znc...)
f = open(os.path.expanduser("~") + "/.fliptable", 'r')
for line in f:
    if line.split()[0] == "user:":
        USER=line.split()[1]

class flip(znc.Module):
    description = "Example python3 module for ZNC"

    _dongers = {
        '\\f': '(╯°□°)╯︵ ┻━┻',
        '\\t': '(ノಠ益ಠ)ノ彡 ┻━┻',
        '\\c': ' ┬┬ ノ( ゜-゜ノ)',
        '\\s': '¯\_(ツ)_/¯',
        '\\b': '╭∩╮( ͡° ͜ʖ͡°)',
    }


    _upside_down_map = {
        'A' : 'ɐ', 'B' : 'q', 'C' : 'ɔ', 'D' : 'p',
        'E' : 'ǝ', 'F' : 'Ⅎ', 'G' : 'b', 'H' : 'ɥ',
        'I' : 'ı', 'J' : 'ظ', 'K' : 'ʞ', 'L' : 'l',
        'M' : 'ɯ', 'N' : 'u', 'O' : 'o', 'P' : 'd',
        'Q' : 'b', 'R' : 'ɹ', 'S' : 's', 'T' : 'ʇ',
        'U' : 'n', 'V' : 'ʌ', 'W' : 'ʍ', 'X' : 'x',
        'Y' : 'ʎ', 'Z' : 'z',
        'a' : 'ɐ', 'b' : 'q', 'c' : 'ɔ', 'd' : 'p',
        'e' : 'ǝ', 'f' : 'ɟ', 'g' : 'b', 'h' : 'ɥ',
        'i' : 'ı', 'j' : 'ſ', 'k' : 'ʞ', 'l' : 'l',
        'm' : 'ɯ', 'n' : 'u', 'o' : 'o', 'p' : 'd',
        'q' : 'b', 'r' : 'ɹ', 's' : 's', 't' : 'ʇ',
        'u' : 'n', 'v' : 'ʌ', 'w' : 'ʍ', 'x' : 'x',
        'y' : 'ʎ', 'z' : 'z',

        '!' : '¡',
        ',' : '`', '.' : '˙',
        '1' : '|', '2' : 'ᄅ',
        '3' : 'Ɛ', '4' : 'ㄣ',
        '5' : 'ϛ', '6' : '9',
        '7' : 'ㄥ', '8' : '8',
        '9' : '6', '0' : '0',
        ';' : ';', '?' : '¿',
        '(' : ')', '[' : ']',
        '{' : '}', '<' : '>',
        '>' : '<', ' ' : ' ',
        '_' : '‾'
        }

    def _flipit(self, text):
        flipped = ''

        if text:
            for x in text:
                if x in self._upside_down_map:
                    flipped = self._upside_down_map[x] + flipped
                else:
                    flipped = x + flipped
        else:
            flipped = ' ^t  ^t^a ^t '

        return flipped


    def OnUserMsg(self, target, message):
        outIRC = ""
        outUser = ""
        outRet = znc.CONTINUE
        outReverse = ""

        m = message.s
        c = m[:2]

        if self._dongers[c]:
#            disable for now..
#            if c == '\\f' or c == '\\t':
#                if len(m) > 2:
#                    outReverse = "  " + self._flipit(c)
            outIRC = ("PRIVMSG {0} : " + self._dongers[c]).format(target) + outReverse
            outUser = (":" + USER + " PRIVMSG {0} :" + self._dongers[c]).format(target) + outReverse
            outRet = znc.HALT


        if outIRC != "":
            self.PutIRC(outIRC)

        if outUser != "":
            self.PutUser(outUser)

        return outRet

#    def OnUserTextMessage(self, message):
#        self.PutModule("UserTextMessage said {0}".format(message))

