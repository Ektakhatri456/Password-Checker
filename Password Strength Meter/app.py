#Project-3: Password Strength Meter

import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔒", layout="centered", initial_sidebar_state="expanded")

#Building profile:
st.sidebar.image("https://avatars.githubusercontent.com/u/170619187?s=400&u=f758c87ccd8a92db5993514049855df20f7d80aa&v=4", width=100)
st.sidebar.markdown("### Ekta Khatri")
st.sidebar.markdown("💼 **Developer**")
st.sidebar.markdown("[🔗 Streamlit] (https://share.streamlit.io/user/ektakhatri456)")
st.sidebar.markdown("[🔗 LinkedIn] (https://www.linkedin.com/in/ekta-khatri-7b6b4a1a8/)")

st.title("🔐Password Strength Checker")
st.write(" ## This app checks the strength of your password and suggests improvements.")
st.write("Enter your password below:")
password = st.text_input("Password", type="password")

st.markdown(""" 
<style>
        .main{text-align : center;}
        .stTextInput{margin : auto; width : 60% !important;}
        .stButton button{width : 50%; background-color #4CAF50; font-size : 20px; color : black; }
        .stButton button : hover {background-color : red; color : white;}            
        </style>
        """, unsafe_allow_html=True)

# To check the strength of the password:

def password_strength(password):
    value = 0
    output = []

    if len(password) >= 10:
        value += 1
    else:
        output.append("⚠Your password should contain at least 10 characters**.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        value += 1  # value will be gradually increased if the password contains uppercase and lowercase letters.
    else:
        output.append("⚠Your password should be in **both uppercase and lowercase letters**.")

    if re.search(r"\d", password):  # '\d' is to check if there is a digit in the password.
        value += 1
    else:
        output.append("⚠Your password should contain at least one **digit**.")
    
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        value += 1
    else:
        output.append("⚠ At least one **special character is required**.")

    if value == 4:
        output.append("☑ **Password Secured** Your password is strong.")
    elif value == 3:
        st.info("⚠**Not strong enough!** Add some more characters.")  # st.info() is used to display the information message.
    else:
        st.error("⚠**Weak Password!** Please follow the suggestions.")  # display error message on the screen.

    expander_label = " 🔍Improve Password" if value < 4 else "✅ Strong Password"

    if output:
        with st.expander(expander_label):
            for suggestion in output:
                st.write(suggestion)
    else:
        st.success("☑**Strong Password!**")

# Now getting input from the user:
if st.button("Check"):
    if password:
        password_strength(password)
    else:
        st.warning("⚠**Please enter your password**.") # for displaying warning.