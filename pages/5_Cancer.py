import streamlit as st
import time

st.set_page_config(
    page_title="Home",
    page_icon="👋",
    initial_sidebar_state="collapsed"
)
st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)
#hide header footer
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
#reduce header height
reduce_header_height_style = """
    <style>
        div.block-container {padding-top:0.0000000001rem;}
    </style>
"""
st.markdown(reduce_header_height_style, unsafe_allow_html=True)
#background
st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://i.ibb.co/7tJRryb/Helo-b-d-11.png");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
content = """
<h1 style="font-family: 'EB Garamond', serif; font-size: 80px; color: #344E41; text-align: left;">Cancer Diagnosis</h1>
<h2 style="font-family: 'EB Garamond', serif; font-size: 20px; opacity: 0.7; color: #EBE3D5; text-align: left;">Posted on 22-2-2003</h2>
<p style="font-family: 'EB Garamond', serif; font-size: 22px; color: #EBE3D5;">
Today is surely the worst day of my life, Marina. I don't understand.<br> Why? Why does God have to do that? Why is life so unfair to <span style='font-style:italic;font-weight: 700;'>you</span> ? A beautiful woman, a filial daughter, a good wife and a gentle mother, but fate decided to give you the worst illness ever: leukemia. Since the day I got the news, I can hardly sleep at night but think about my wife. I cannot imagine how much pain she has gone through. Why, Lev, why didn't you notice anything? Why didn't you give more attention and care to your wife? What a bad husband I am, right? Don't worry, Marina, I promise not to let you go, I believe we'll get through all this together. God, please give us strength to stay strong and fight this. I can’t lose my Marina. <br> <span style="font-style: italic; font-weight: 700;color:#000080">Please, God, please..
</p>
"""

navigation_links = """
<div style="margin-top: 10px; font-family: 'EB Garamond', serif; font-size: 22px; color: #EBE3D5;">
    <div style="float: left;">
        <a id="blog-link" class="navigation-link" href="/Daughter_Arrival" target="_self" style="color: #EBE3D5;"> ⬅Return to last entry </a>
    </div>
    <div style="float: right;">
        <a id="contact-link" class="navigation-link" href="/Journey" target="_self" style="color: #EBE3D5;"> Next Entry⮕ </a>
    </div>
    <div style="clear: both;"></div>
</div>
"""

# Display content and navigation links
st.markdown(content + navigation_links, unsafe_allow_html=True)
