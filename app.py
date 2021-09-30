import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt


#HEADER

html_header="""
<head>
<title>DataJobMarketAnalysis</title>
<meta charset="utf-8">
<meta name="keywords" content="Python Project, dashboard, Data Field, DSTI">
<meta name="description" content="DataJobMarketAnalysis Dashboard">
<meta name="author" content="Nelson Lopez - Virgile Sarniguet">
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<h1 style="font-size:300%; color:#008080; text-align: center; font-family:Arial"> Data Field Job Market Analysis<br>
 <h2 style="color:#008080; font-family:Arial"> Dashboard</h3> <br>
 <hr style= "  display: block;
  margin-top: 0.5em;
  margin-bottom: 0.5em;
  margin-left: auto;
  margin-right: auto;
  border-style: inset;
  border-width: 1.5px;"></h1>
"""


st.set_page_config(page_title="Project Dashboard", page_icon="", layout="wide")

st.markdown('<style>body{background-color: #fbfff0}</style>',unsafe_allow_html=True)
st.markdown(html_header, unsafe_allow_html=True)

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

st.markdown("<h5 style='text-align: center; color: #008080; font-family:Arial'>Summary of data job market in France, analysing Job Offers of 2 of the most important job sites in France (Welcome to the Jungle and Indeed</h5>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center; color: #008080; font-family:Arial'>Filter Options</h2>", unsafe_allow_html=True)

#READING DATA

#SIDEBAR
st.sidebar.multiselect('Select Role or Roles', ['Data Analyst','Data Engineer','Data Scientist'])
st.sidebar.multiselect('Select Industry', ['Industry 1','Industry 2','Industry 3'])
st.sidebar.multiselect('Select WebSite', ['Welcome to the Jungle','Indeed'])

#BODY

html_card_header1="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #75a8ae; padding-top: 5px; width: 200px;
   height: 50px;">
    <h3 class="card-title" style="background-color:#75a8ae; color:#25545b; font-family:Arial; text-align: center; padding: 0px 0;">Total</h3>
  </div>
</div>
"""
html_card_footer1="""
<div class="card">
  <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #75a8ae; padding-top: 1rem;; width: 200px;
   height: 50px;">
    <p class="card-title" style="background-color:#75a8ae; color:#25545b; font-family:Arial; text-align: center; padding: 0px 0;">Offers</p>
  </div>
</div>
"""
html_card_header2="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #75a8ae; padding-top: 5px; width: 200px;
   height: 50px;">
    <h3 class="card-title" style="background-color:#75a8ae; color:#25545b; font-family:Arial; text-align: center; padding: 0px 0;">Top 10</h3>
  </div>
</div>
"""
html_card_footer2="""
<div class="card">
  <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #75a8ae; padding-top: 1rem;; width: 200px;
   height: 50px;">
    <p class="card-title" style="background-color:#75a8ae; color:#25545b; font-family:Arial; text-align: center; padding: 0px 0;">Companies Demanding</p>
  </div>
</div>
"""
html_card_header3="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #75a8ae; padding-top: 5px; width: 200px;
   height: 50px;">
    <h3 class="card-title" style="background-color:#75a8ae; color:#25545b; font-family:Arial; text-align: center; padding: 0px 0;">Top 10</h3>
  </div>
</div>
"""
html_card_footer3="""
<div class="card">
  <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #75a8ae; padding-top: 1rem;; width: 200px;
   height: 50px;">
    <p class="card-title" style="background-color:#75a8ae; color:#25545b; font-family:Arial; text-align: center; padding: 0px 0;">Skills Demanded</p>
  </div>
</div>
"""
html_card_header4="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #75a8ae; padding-top: 5px; width: 200px;
   height: 50px;">
    <h3 class="card-title" style="background-color:#75a8ae; color:#25545b; font-family:Arial; text-align: center; padding: 0px 0;">Top 5</h3>
  </div>
</div>
"""
html_card_footer4="""
<div class="card">
  <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #75a8ae; padding-top: 1rem;; width: 200px;
   height: 50px;">
    <p class="card-title" style="background-color:#75a8ae; color:#25545b; font-family:Arial; text-align: center; padding: 0px 0;">Contract Types</p>
  </div>
</div>
"""

html_br="""
<br>
"""

with st.container():
    col1, col2, col3, col4, col5, col6, col7 = st.columns([1,2,1,2,1,2,1])
    with col1:
        st.write("")
    with col4:
        st.markdown(html_card_header1, unsafe_allow_html=True)
#Figure
        st.markdown(html_card_footer1, unsafe_allow_html=True)
        
st.markdown(html_br, unsafe_allow_html=True)

#Block 2 highlight numbers

with st.container():
    col1, col2, col3, col4, col5, col6, col7 = st.columns([1,2,1,2,1,2,1])
    with col1:
        st.write("")
    with col2:
        st.markdown(html_card_header2, unsafe_allow_html=True)
#Figure
        st.markdown(html_card_footer2, unsafe_allow_html=True)
    with col3:
        st.write("")
    with col4:
        st.markdown(html_card_header3, unsafe_allow_html=True)
#Figure
        st.markdown(html_card_footer3, unsafe_allow_html=True)
    with col5:
        st.write("")
    with col6:
        st.markdown(html_card_header4, unsafe_allow_html=True)
#Figure
        st.markdown(html_card_footer4, unsafe_allow_html=True)
    with col7:
        st.write("")

st.markdown(html_br, unsafe_allow_html=True)
st.markdown(html_br, unsafe_allow_html=True)
st.markdown(html_br, unsafe_allow_html=True)
st.markdown(html_br, unsafe_allow_html=True)


### Block 3#########################################################################################
html_card_header5="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #75a8ae; padding-top: 5px; width: 625px;
   height: 30px;">
    <h3 class="card-title" style="background-color:#75a8ae; color:#25545b; font-family:Arial; text-align: center; padding: 5px 0;">Job Offers Location</h3>
  </div>
</div>
"""


with st.container():
    col1, col2, col3, col4, col5, col6, col7 = st.columns([1,2,1,2,1,2,1])
    with col2:
        st.markdown(html_card_header5, unsafe_allow_html=True)
#Figure

    with col6:
        st.write("Little Paragraph or Selection Module")
    with col3:
        st.write("")

st.markdown(html_br, unsafe_allow_html=True)
st.markdown(html_br, unsafe_allow_html=True)

### Block 4#########################################################################################
html_card_block4_header="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #75a8ae; padding-top: 5px; width: 625px;
   height: 30px;">
    <h3 class="card-title" style="background-color:#75a8ae; color:#25545b; font-family:Arial; text-align: center; padding: 5px 0;">Word Cloud</h3>
  </div>
</div>
"""


with st.container():
    col1, col2, col3, col4, col5, col6, col7 = st.columns([1,2,1,2,1,2,1])
    with col4:
        st.markdown(html_card_block4_header, unsafe_allow_html=True)
#Figure
    with col2:
        st.write("Little Paragraph")
    with col3:
        st.write("")

st.markdown(html_br, unsafe_allow_html=True)

### Block 5#########################################################################################
html_line_block5="""
<br>
<br>
<br>
<br>
<hr style= "  display: block;
  margin-top: 0.5em;
  margin-left: auto;
  margin-right: auto;
  border-style: inset;
  border-width: 1.5px;">
"""
html_card_block51_header="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #75a8ae; padding-top: 5px; width: 450px;
   height: 30px;">
    <h3 class="card-title" style="background-color:#75a8ae; color:#25545b; font-family:Arial; text-align: center; padding: 5px 0;">Role Comparisson</h3>
  </div>
</div>
"""
html_card_block52_header="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #75a8ae; padding-top: 5px; width: 450px;
   height: 30px;">
    <h3 class="card-title" style="background-color:#75a8ae; color:#25545b; font-family:Arial; text-align: center; padding: 5px 0;">Skill Comparisson</h3>
  </div>
</div>
"""

st.markdown(html_line_block5, unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; color: #008080; font-family:Arial'>Interactive Data Comparisson</h3>", unsafe_allow_html=True)

with st.container():
    col1, col2, col3, col4, col5, col6, col7 = st.columns([1,2,1,2,1,2,1])

    with col2:
        st.multiselect('Select Role to Compare', ['Data Analyst','Data Engineer','Data Scientist'])
    with col6:
        st.multiselect('Select Skills to Compare', ['SQL','Python','Machine Learning'])


with st.container():
    col1, col2, col3, col4, col5, col6, col7 = st.columns([1,2,1,2,1,2,1])

    with col1:
        st.markdown(html_card_block51_header, unsafe_allow_html=True)
    with col5:
        st.markdown(html_card_block52_header, unsafe_allow_html=True)

st.markdown(html_br, unsafe_allow_html=True)
st.markdown(html_br, unsafe_allow_html=True)
st.markdown(html_br, unsafe_allow_html=True)
st.markdown(html_br, unsafe_allow_html=True)
st.markdown(html_br, unsafe_allow_html=True)



html_br="""
<br>
"""



#FOOTER

html_line="""
<br>
<br>
<br>
<br>
<hr style= "  display: block;
  margin-top: 0.5em;
  margin-left: auto;
  margin-right: auto;
  border-style: inset;
  border-width: 1.5px;">
<div style="color: #008080; font-family:Arial; text-align: right;">Designed by Nelson Lopez and Virgile Sarniguet</div>
<div style="color: #008080; font-family:Arial; text-align: right;">DSTI Project - Python Labs</div>
"""
st.markdown(html_line, unsafe_allow_html=True)