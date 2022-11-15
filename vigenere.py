class Vigenere:

    def __init__(self, text, key):
        self.text = text
        self.key = key

    def vigenere_encrypt(self):
        return vigenere(text=self.text, key=self.key, alphabet=alphabets, encrypt=True)

    def vigenere_decrypt(self):
        return vigenere(text=self.text, key=self.key, alphabet=alphabets, encrypt=False)


alphabets = '0123456789' \
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ' \
            'abcdefghijklmnopqrstuvwxyz' \
            'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' \
            'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '

alphabets_light = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' \
                'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


def vigenere(text, key, alphabet, encrypt=True):
    result = ''
    for i in range(len(text)):
        letter_n = alphabet.index(text[i])
        key_n = alphabet.index(key[i % len(key)])

        if encrypt:
            value = (letter_n + key_n) % len(alphabet)
        else:
            value = ((letter_n - key_n) - len(alphabet)) % len(alphabet)

        result += alphabet[value]

    return result


