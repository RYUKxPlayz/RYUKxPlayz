import streamlit as st

st.title("A Cute Question for You ❤️")
st.subheader("Will you be mine?")

if st.button("Yes"):
    st.success("Yay! You said YES! 😍")

if st.button("No"):
    st.error("No nahi bolne dete 😜")
