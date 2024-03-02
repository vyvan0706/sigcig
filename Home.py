import streamlit as st
import base64
import time
import numpy
from PIL import Image
from streamlit_extras.buy_me_a_coffee import button
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.markdownlit import mdlit
st.set_page_config(
    page_title="Home",
    page_icon="👋",
    layout= 'wide'
)

#animation etc
with open('wave.css') as f:
    csss = f.read()
st.markdown(f'<style>{csss}</style>', unsafe_allow_html=True)

#ẩn header footer
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

#đặt logo cho page
st.markdown(
        f"""
            <style>
                [data-testid="stSidebar"] {{
                    background-image: url(https://khothietke.net/wp-content/uploads/2021/03/freepng1633-dieu-thuoc-la-khong-hut-thuoc-2.png);
                    background-repeat: no-repeat;
                    padding-top: 80px;
                    background-position: 20px 20px;
                    background-size: 115px 130px
                }}
            </style>
            """,
        unsafe_allow_html=True,
    )

# đặt banner
image_path = 'https://i.ibb.co/xgxpWMf/B76-C7813-950-B-410-B-85-A2-E62-DEFC4-C805.png'
html_str2 =  f"""
<div style='width: 1080px; height: 200px;'>
    <img src='{image_path}' alt='Blog Banner' style='width:100%; height:100%; object-fit: cover;'>
</div>
"""
st.markdown(html_str2, unsafe_allow_html=True)

#đặt font
with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
html_str = """
<h1 class="animated-text" style='font-size: 100px; text-align: center; color: #776B5D ;'>
    BLOG BY LEV
</h1>
"""
st.markdown(html_str, unsafe_allow_html=True)

#phần dưới
col1, col2 = st.columns([2, 2])
col1.markdown('<h2 style="color: #344955;">About me</h2><hr style="border-top: 1px solid black; margin-top: 0.5em;">', unsafe_allow_html=True)

#st.markdown("<h1 style='color: black;'><span style='color: black;font-style: italic;'>Blog</span> <span style='color: black;'>by</span> <span style='color: blue;'>lev</span> 😎</h1>", unsafe_allow_html=True)

#_LOREM_IPSUM ='''Hello, I'm Lev. I'm on a journey, traveling from place to place, seeking something elusive yet essential. This blog will document my experiences and reflections along the way. Join me as I navigate through the twists and turns of life's unpredictable road.'''
#def stream_data():
#    for word in _LOREM_IPSUM.split():
#        yield word + " "
#        time.sleep(0.05)
#st.write_stream(stream_data)
_LOREM_IPSUM = '''<p><span style="color: black;">Hello, I'm Lev. I'm on a journey, traveling from place to place, seeking something elusive yet essential. This blog will document my experiences and reflections along the way. Join me as I navigate through the twists and turns of life's unpredictable road.</span></p>'''
col1.markdown(_LOREM_IPSUM, unsafe_allow_html=True)
col2.image('levtheguy.jpg',caption='This is me!',use_column_width=True )
col1.page_link("pages/0_Blog_entries.py", label=":grey[→ Blog entries here]")
