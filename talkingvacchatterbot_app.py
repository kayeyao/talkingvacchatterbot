import warnings


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from PIL import Image
from streamlit import caching

import talkingvacchatterbot_appbody as body

warnings.filterwarnings('ignore')


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
            
local_css("style.css") #for styling, contains css for the background and the button style



st.markdown("""<style>.css-1aumxhk {background-color: #efede8; background-image: none; color: #efede8}</style>""", unsafe_allow_html=True) # changes background color of sidebar #


## Side Bar Information
image = Image.open('Image/TalkingVac logo 2.png')
st.sidebar.image(image, caption='', width=200)


## Create Select Box and options
add_selectbox = st.sidebar.radio(
	"Chatbot",
	("COVID-19 FAQs","COVID-19 Vaccine FAQs","COVID-19 Statistics","QA Chatbot")
)


if add_selectbox == 'COVID-19 FAQs':	
	st.title("Frequently Asked Questions")
	st.title("On COVID-19")
	st.markdown('<div style="color: #efede8;">.</div>',unsafe_allow_html=True) # space #
	st.markdown('<div style="color: #efede8;">.</div>',unsafe_allow_html=True) # space #
	
	body.covid_info()


if add_selectbox == 'COVID-19 Vaccine FAQs':
	st.title("Frequently Asked Questions")
	st.title("On COVID-19 Vaccines")
	st.markdown('<div style="color: #efede8;">.</div>',unsafe_allow_html=True) # space #
	st.markdown('<div style="color: #efede8;">.</div>',unsafe_allow_html=True) # space #
	
	body.vaccine_info()


if add_selectbox == 'COVID-19 Statistics':
	st.title("COVID-19 Statistics")
	st.markdown('<div style="color: #efede8;">.</div>',unsafe_allow_html=True) # space #
	st.markdown('<div style="color: #efede8;">.</div>',unsafe_allow_html=True) # space #
	
	body.covid_statistics_table()
	st.markdown('<div style="font-style: italic;">Source: Our World in Data - https://covid.ourworldindata.org/data/owid-covid-data.csv</div>',unsafe_allow_html=True)
	st.write('')	
	body.covid_statistics()
	st.markdown('<div style="font-style: italic;">Source: Our World in Data - https://covid.ourworldindata.org/data/owid-covid-data.csv</div>',unsafe_allow_html=True)


if add_selectbox == 'QA Chatbot':
	st.subheader("Your guide for your COVID-19 vaccine queries.")
	st.markdown('<div style="font-style: italic;">This version is made using Chatterbot.</div>',unsafe_allow_html=True)
	
	
	st.markdown('<div style="color: #efede8;">.</div>',unsafe_allow_html=True) # space #
	st.markdown('<div style="color: #efede8;">.</div>',unsafe_allow_html=True) # space #

	st.subheader("Hi! How may I help you?")	
	body.chatterbot()

	
st.sidebar.markdown("""<a style='display: block; text-align: left;color:#efede8;text-decoration: none;'>.</a>""",unsafe_allow_html=True)	
st.sidebar.markdown("""<a style='display: block; text-align: left;color:#efede8;text-decoration: none;'>.</a>""",unsafe_allow_html=True)	
st.sidebar.markdown("""<a style='display: block; text-align: left;color:#696969;text-decoration: none;'> TalkingVac is a capstone project of Eskwelabs Cohort 6 Data Science Fellows.</a>""",unsafe_allow_html=True)
st.sidebar.markdown("""<a style='display: block; text-align: left;color:#84a3a7;text-decoration: none;' href="https://talkingvac.herokuapp.com">Click here to know 	more.</a>""",unsafe_allow_html=True)