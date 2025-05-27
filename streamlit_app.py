import streamlit as st


st.image("BC048F02-5A9D-4FB7-9FB9-BA5759CC84BB.jpeg",width=500)

st.title("1pzz app")
st.header("Mengecek Bilangan Ganjil Dan Genap”)
angka = st.number_input(“Tulis Sebuah Angka:”, value= 0, step= 1) 


if(angka % 2) == 0:
    st.write(f”{angka} Adalah Bilangan Genap”) 
else:
    st.write(f”{angka} Adalah Bilangan Ganjil”)         

    
