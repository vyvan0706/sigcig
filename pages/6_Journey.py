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
<h1 style="font-family: 'EB Garamond', serif; font-size: 80px; color: #344E41; text-align: left;">one hope left...</h1>
<h2 style="font-family: 'EB Garamond', serif; font-size: 20px; opacity: 0.7; color: #EBE3D5; text-align: left;">Posted on 27-6-2004</h2>
<p style="font-family: 'EB Garamond', serif; font-size: 22px; color: #EBE3D5;">
Today, as Marina requested, we visited the famous sulfur springs at Jor. We were lucky, as the springs were not too crowded and the weather was just perfect. There were no clouds at all, yet the sunlight was mellow and warm. What a beautiful day, isn’t it? I sat on the rocks and felt the sun on my skin, while Marina immersed herself into the hot water. She laid there relaxingly, her gorgeous eyes stuck to a female stork returning to its nest on a tremendously tall tree.<br>
<span style="font-style: italic; font-weight: 800; color:#E6E6FA;">
“If only we were storks”</span> <br>
Her voice woke me up from my daydream. I asked her what she meant with confusion. <br>
“Because you never see a stork dying. It’s as though they didn’t <span style="font-style: italic; font-weight: 700;">
die </span>” - she smiled and turned away. I was speechless, looked up, trying not to burst into tears. In the sky, I saw a flock of storks flew gracefully overhead, and some were finding food for the little storks waiting for their parents. I hope nature can cure what I have lost, but now, the most wonderful scenery can’t even pull myself together… 
</p>
"""

navigation_links = """
<div style="margin-top: 10px; font-family: 'EB Garamond', serif; font-size: 22px; color: #EBE3D5;">
    <div style="float: left;">
        <a id="blog-link" class="navigation-link" href="/Cancer" target="_self" style="color: #EBE3D5;"> ⬅Return to last entry </a>
    </div>
    <div style="float: right;">
        <a id="contact-link" class="navigation-link" href="/Farewell" target="_self" style="color: #EBE3D5;"> Next Entry⮕ </a>
    </div>
    <div style="clear: both;"></div>
</div>
"""

# Display content and navigation links
st.markdown(content + navigation_links, unsafe_allow_html=True)
