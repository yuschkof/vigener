import streamlit as st
from vigenere import Vigenere

alphabets = '0123456789' \
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ' \
            'abcdefghijklmnopqrstuvwxyz' \
            'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' \
            'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '

st.title('Шифр Виженера')

col1, col2 = st.columns(2)

with col1:
    st.subheader('Зашифровать слово')
    output = ''
    word = st.text_input('Слово', 'Hello world')
    keys = st.text_input('Ключ', 'Key')
    if st.button('Зашифровать'):
        abc = Vigenere(word, keys, True)
        output = abc.algoritm(alphabets)
    st.markdown(f"Зашифрованное слово: {output}")


with col2:
    st.subheader('Расшифровать слово')
    output = ''
    shifre = st.text_input('Зашифрованное слово', '')
    keys = st.text_input('Ключ', '')
    if st.button('Расшифровать'):
        abc = Vigenere(shifre, keys, False)
        output = abc.algoritm(alphabets)
    st.markdown(f"Расшифрованное слово: {output}")
