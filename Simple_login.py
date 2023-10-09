import streamlit as st
import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader
with open("passwords.yaml") as file:
    config = yaml.load(file, Loader = SafeLoader)

authenticator = stauth.Authenticate(config["credentials"], config['cookie']['name'], config['cookie']['key'], config['cookie']['expiry_days'])
name, authentication_status, username = authenticator.login('Login')
if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'sidebar')
    st.sidebar.write(f'Welcome *{st.session_state["name"]}*')

elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')
