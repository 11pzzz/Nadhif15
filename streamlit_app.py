import streamlit as st


st.image("BC048F02-5A9D-4FB7-9FB9-BA5759CC84BB.jpeg",width=500)

st.title("1pzzz app👀")
st.header("Mengecek bilangan Ganjil dan Genap")
angka = st.number_input("Tulis sebuah angka:", value=0, step=1)


if(angka % 2) == 0:
    st.write(f"{angka} Adalah bilangan genap")
else:
    st.write(f"{angka} adalah bilangan ganjil")       

    
