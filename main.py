import streamlit as st


def vigenere(
        text: str,
        key: str,
        alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя,."!@#$%^&*()_-+= ',
        encrypt=True
):
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
    return vigenere(text=text, key=key, encrypt=True)


def vigenere_decrypt(text, key):
    return vigenere(text=text, key=key, encrypt=False)


st.title('Шифр Виженера')

col1, col2 = st.columns(2)

with col1:
    st.subheader('Зашифровать слово')
    output = ''
    word = st.text_input('Слово', 'Hello world')
    key = st.text_input('Ключ', 'key')
    if st.button('Зашифровать'):
        output = vigenere_encrypt(word, key)
    st.markdown(f"Зашифрованное слово: {output}")


with col2:
    st.subheader('Расшифровать слово')
    output = ''
    shifre = st.text_input('Зашифрованное слово', 'Hello world')
    key = st.text_input('Ключ', '')
    if st.button('Расшифровать'):
        output = vigenere_decrypt(shifre, key)
    st.markdown(f"Расшифрованное слово: {output}")
