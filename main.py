import streamlit as st


alphabets = '0123456789' \
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ' \
            'abcdefghijklmnopqrstuvwxyz' \
            'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' \
            'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '

alphabets_light = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' \
                'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


def vigenere(text: str, key: str, alphabet, encrypt=True):
    result = ''
    for i in range(len(text)):
        letter_n = alphabet.index(text[i])
        key_n = alphabet.index(key[i % len(key)])

        if encrypt:
            value = (letter_n + key_n) % len(alphabet)
        else:
            value = (letter_n - key_n) % len(alphabet)

        result += alphabet[value]

    return result


def vigenere_encrypt(text, key):
    return vigenere(text=text, key=key, alphabet=alphabets, encrypt=True)


def vigenere_decrypt(text, key):
    return vigenere(text=text, key=key, alphabet=alphabets, encrypt=False)


st.title('Шифр Виженера')

col1, col2 = st.columns(2)

with col1:
    st.subheader('Зашифровать слово')
    output = ''
    word = st.text_input('Слово', 'Hello world')
    keys = st.text_input('Ключ', 'key')
    if st.button('Зашифровать'):
        output = vigenere_encrypt(word, keys)
    st.markdown(f"Зашифрованное слово: {output}")


with col2:
    st.subheader('Расшифровать слово')
    output = ''
    shifre = st.text_input('Зашифрованное слово', '')
    keys = st.text_input('Ключ', '')
    if st.button('Расшифровать'):
        output = vigenere_decrypt(shifre, keys)
    st.markdown(f"Расшифрованное слово: {output}")
