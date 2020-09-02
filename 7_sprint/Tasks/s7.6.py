class HackerLanguage:
    def __init__(self):
        self.message = ""

    def write(self, text):
        self.message += text

    def delete(self, N):
        self.message = self.message[:-N]

    def send(self):
        self.encrypted_text = ''
        for char in self.message:
            if char.isalpha():
                self.encrypted_text += str(bin(ord(char)))[2:]
            elif char.isdigit():
                self.encrypted_text += char
            elif char == ' ':
                self.encrypted_text += '1000000'
            elif char in ['.', ':', '!', '?', '@', '$', '%']:
                self.encrypted_text += char
        return self.encrypted_text

    def read(self, text):
        self.normal_text = ''
        start = 0
        end = 7
        while end <= len(text):
            if text[start:end] == '1000000':
                self.normal_text += ' '
                start += 7
                end += 7
            elif text[start:end].isdigit():
                if self.isNumber(text[start:end]):
                    self.normal_text += chr(int(text[start:end], 2))
                    start += 7
                    end += 7
            elif text[start].isdigit():
                if self.isData(text[start:end + 3]):
                    self.normal_text += text[start:end + 3]
                    start += 10
                    end += 10
                elif self.isTime(text[start:end - 2]):
                    self.normal_text += text[start:end - 2]
                    start += 5
                    end += 5
                else:
                    self.normal_text += text[start]
                    start += 1
                    end += 1
                # check is data
            elif self.isAnyOtherChar(text[start]):
                self.normal_text += text[start]
                start += 1
                end += 1
        return self.normal_text

    def isData(self, str1):
        indexRange = [0, 1, 3, 4, 6, 7, 8, 9]

        isData = True
        for i in indexRange:
            if not str1[i].isDigit():
                return False
        return isData and str1[2] == '.' and str1[5] == '.'

    def isTime(self, str2):
        indexRange = [0, 1, 3, 4]

        isTime = True
        for i in indexRange:
            if not str2[i].isDigit():
                return False
        return isTime and str2[2] == ':'

    def isNumber(self, str4):
        for char in str4:
            if int(char) > 1:
                return False
        return True

    def isAnyOtherChar(self, anyChar):
        if anyChar not in ['.', ':', '!', '?', '@', '$', '%']:
            return False
        return True

message_1 = HackerLanguage()
message_1.write('Remember: 21.07.2018 at 11:11AM')
message_1.delete(2)
message_1.write('PM')
print(message_1.send())



message_2 = HackerLanguage()
print(message_2.read(
    '10011011111001100000011001011101101110000111010011101100100000011010011110011100000011011011110010.11100101101111110001011011111110100@11001111101101110000111010011101100.110001111011111101101'))
