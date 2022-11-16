class Vigenere:

    def __init__(self, text, key, encrypt):
        self.text = text
        self.key = key
        self.encrypt = encrypt

    def algoritm(self, alphabet):
        result = ''
        for i in range(len(self.text)):
            letter_n = alphabet.index(self.text[i])
            key_n = alphabet.index(self.key[i % len(self.key)])
            if self.encrypt:
                value = (letter_n + key_n) % len(alphabet)
            else:
                value = ((letter_n - key_n) - len(alphabet)) % len(alphabet)
            result += alphabet[value]
        return result

