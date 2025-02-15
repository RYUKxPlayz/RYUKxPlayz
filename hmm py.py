# import tkinter as tk
# import random

# # Create main window
# root = tk.Tk()
# root.title("A Cute Question for You")
# root.geometry("400x300")

# # Display the question
# question_label = tk.Label(root, text="Will you be mine? ❤️", font=("Helvetica", 18))
# question_label.pack(pady=20)

# # Button click action
# def yes_clicked():
#     response_label.config(text="Yay! You said YES! 😍")

# def no_hover(event):
#     # Move the 'No' button to a random position
#     x = random.randint(50, 300)
#     y = random.randint(100, 250)
#     no_button.place(x=x, y=y)

# # Yes Button
# yes_button = tk.Button(root, text="Yes", font=("Helvetica", 14), command=yes_clicked)
# yes_button.pack(pady=10)

# # No Button (moves on hover)
# no_button = tk.Button(root, text="No", font=("Helvetica", 14))
# no_button.place(x=150, y=150)
# no_button.bind("<Enter>", no_hover)

# # Response Label
# response_label = tk.Label(root, text="", font=("Helvetica", 16))
# response_label.pack(pady=10)

# # Run the app
# root.mainloop()

import streamlit as st

st.title("A Cute Question for You ❤️")
st.subheader("Will you be mine?")

if st.button("Yes"):
    st.success("Yay! You said YES! 😍")

if st.button("No"):
    st.error("No nahi bolne dete 😜")