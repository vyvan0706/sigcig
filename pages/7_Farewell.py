import streamlit as st
import time

st.set_page_config(
    page_title="Home",
    page_icon="👋",
    initial_sidebar_state="collapsed"
)
st.markdown("""
            <style>
            [data-testid="stSidebar"] {
                display: none
            }

            [data-testid="collapsedControl"] {
                display: none
            }
            </style>
            """, unsafe_allow_html=True)
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
<h1 style="font-family: 'EB Garamond', serif; font-size: 80px; color: #344E41; text-align: left;">Farewell</h1>
<h2 style="font-family: 'EB Garamond', serif; font-size: 20px; opacity: 0.7; color: #EBE3D5; text-align: left;">Posted on 29-2-2004</h2>
<p style="font-family: 'EB Garamond', serif; font-size: 22px; color: #EBE3D5 ;text-shadow: 2px 2px 4px black;">
Marina darling, five days by your bedside, and on day six, you were here no more. I thought it was just a nightmare, 
but when I woke up, you had gone somewhere - somewhere to never be found again. But everything about you is still here. 
Our pictures on the wall, your dresses, favorite vase, the sweet scent of purple daisies still wafts from your shirt... 
You fell asleep so peacefully just in a blink and never to wake up again. The more effortlessly it is for you to leave, 
the greater the pain of losing you. I don't know what my future will be like when you are no longer in my life.  
<br> Oh, life forces us to be like this, we have to endure it. I do not know what to do. The contradictions in life, 
the pain we thought we couldn't understand.
<br> But living in this world, everyone doesn't have to experience pain. Different trees have different flowers and 
different families have different situations. Face it, accept it and live with it... I'm still trying every day, every hour.
<br> I also had times when I found my smile again. But behind every smile is a bitterness and sourness because you are no 
longer here, also because I can no longer share this smile with you.
</p>
"""

navigation_links = """
<div style="margin-top: 10px; font-family: 'EB Garamond', serif; font-size: 22px; color: #EBE3D5;">
    <div style="float: left;">
        <a id="blog-link" class="navigation-link" href="/Journey" target="_self" style="color: #EBE3D5;"> ⬅Return to last entry </a>
    </div>
    <div style="float: right;">
        <a id="contact-link" class="navigation-link" href="/Work" target="_self" style="color: #EBE3D5;"> Next Entry⮕ </a>
    </div>
    <div style="clear: both;"></div>
</div>
"""

# Display content and navigation links
st.markdown(content + navigation_links, unsafe_allow_html=True)
