# now we will add stramlit by its command  of importing 
import streamlit as st
# we use st as streamlit shortcut
# the next modulr which is random  and it is also a builtin module in python  and same string
import random
import string


#  now for password generator we will create one function
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  
    

    if use_digits:
        characters += string.digits  # Adds numbers (0-9) if selected

    if use_special:
        characters += (
            string.punctuation
        ) 
         #  for Adding the special characters (!@#$%^&* etc.) if user selected

    # Generate a password by randomly selecting characters based on the length provided
    return "".join(random.choice(characters) for _ in range(length))



st.title("Password Generator") 


# User input: password length (slider to select length between 6 and 12 characters)
length = st.slider("Select password length:", min_value=6, max_value=12, value=9)

# Checkbox options for including numbers and special characters in the password
use_digits = st.checkbox("Include numbers") 
 # Checkbox for numbers (0-9)
use_special = st.checkbox(
    "Include special characters"
)
# button for generate the code
if st.button("Generate Password"):
    password = generate_password(
        length, use_digits, use_special
    )  
    # we create write-space or input for password
    st.write(f"Generated Password: {password}")