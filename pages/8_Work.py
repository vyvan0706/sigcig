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
<h1 style="font-family: 'EB Garamond', serif; font-size: 80px; color: #344E41; text-align: left;">Workplace Closure</h1>
<h2 style="font-family: 'EB Garamond', serif; font-size: 20px; opacity: 0.7; color: #EBE3D5; text-align: left;">Posted on 26-3-2006</h2>
<p style="font-family: 'EB Garamond', serif; font-size: 22px; color: #EBE3D5;">
What a tragic day… The Baryn sawmill has completely been shut down, leaving this man jobless. Why, God? What have I done wrong that you’re playing the karmas on me? I’m so desperate right now. What should I do? Marina, please, tell me, what should I do?<br>
…<br>
I just talked with my bud about this. He suggested going to the UK - London to be specific - since there’s always some sort of job to do.. I thought that was a terrible idea, but… I guess it’s the only path for me. I’ve decided. <span style="color:black;font-weight: 800;"> I will go to London. </span>
</p>
"""

navigation_links = """
<div style="margin-top: 10px; font-family: 'EB Garamond', serif; font-size: 22px; color: #EBE3D5;">
    <div style="float: left;">
        <a id="blog-link" class="navigation-link" href="/Farewell" target="_self" style="color: #EBE3D5;"> ⬅Return to last entry </a>
    </div>
    <div style="float: right;">
        <a id="contact-link" class="navigation-link" href="/London" target="_self" style="color: #EBE3D5;"> Next Entry⮕ </a>
    </div>
    <div style="clear: both;"></div>
</div>
"""

# Display content and navigation links
st.markdown(content + navigation_links, unsafe_allow_html=True)
