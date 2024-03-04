import streamlit as st
import base64
from PIL import Image
import time

from streamlit_extras.stoggle import stoggle 
st.set_page_config(
    page_title="Blog entries",
    page_icon="🔥",
    layout= 'wide',
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
st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://i.ibb.co/0QM5dwk/z5212839788226-60ccf9d2215e9e2187e0cf9535d04290.jpg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
st.markdown(
    """
    <div style="position: fixed; top: 63px; left: 64px;">
        <img src="https://khothietke.net/wp-content/uploads/2021/03/freepng1633-dieu-thuoc-la-khong-hut-thuoc-2.png" width="80">
    </div>
    """,
    unsafe_allow_html=True
)

col1, col23, col4,col5,col6 = st.columns([2,17,3,3,3])
#set logo
st.markdown(
    """
    <div style="position: fixed; top: 63px; left: 64px;">
        <img src="https://khothietke.net/wp-content/uploads/2021/03/freepng1633-dieu-thuoc-la-khong-hut-thuoc-2.png" width="80">
    </div>
    """,
    unsafe_allow_html=True
)
#for col 1
with col1:
    with open('wave.css') as css:
        files = css.read()
    st.markdown(f'<style>{files}</style>', unsafe_allow_html=True)
    st.markdown(
        """
        <body>
            <div class="patterns" style="width: 100%; height: 100vh; justify-content: center; align-items: center;">
                  <defs>
                    <style>
                      @import url("https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400..800;1,400..800&display=swap");
                      text {
                        font-family: "EB Garamond", serif !important;
                        font-optical-sizing: auto;
                        font-weight: 800;
                        font-style: normal;
                        font-size: 2rem;
                        cursor: pointer;
                        fill: #F55F5F; /* Adjust the fill color */
                        transform: rotate(270deg); /* Rotate the text */
                        transform-origin: center; /* Set rotation origin to center */
                        position: fixed;
                        top: 193px; left: 24px;
                      }
                    </style>
                    <circle fill="#be9ddf" cx="25" cy="25" r="2"></circle>
                  </defs>
                  <text x="20" y="40%" text-anchor="middle">     Blog by Lev     </text>
              </div>
            </body>
        """,
        unsafe_allow_html=True
    )
#for col5
with col5:
    navigation_link = '<a id="about-link" class="navigation-link" href="/Home" target="_self" style="color: #EBE3D5;top: 63px; right: 400px;"><span style="color: #F55F5F;">&#8226;</span> home</a>'
    st.markdown(navigation_link, unsafe_allow_html=True)

with col6:
    navigation_link2 = '<a id="blog-link" class="navigation-link" href="/Blog" target="_self" style="color: #EBE3D5;top: 63px; right: 275px;"><span style="color: #F55F5F;">&#8226;</span> blog</a>'
    st.markdown(navigation_link2, unsafe_allow_html=True)

navigation_link3 = '<a id="contact-link" class="navigation-link" href="/your-contact-page" target="_self" style="color: #EBE3D5;top: 63px; right: 120px;"><span style="color: #F55F5F;">&#8226;</span> contact</a>'
st.markdown(navigation_link3, unsafe_allow_html=True)


st.markdown(
    """
    <h1 <span style="font-family: 'EB Garamond', serif;font-size: 80px;
color: #EBE3D5; position: fixed; top: 80px; left: 350px;">About me</span><span style="color: #F55F5F;"> :</span></h1>
    """ 
, unsafe_allow_html=True)
st.markdown("""
<p style="color: #EBE3D5;font-size: 22px; position: fixed; top: 200px; left: 350px;right: 120px;">Nice to meet you here. I'm Lev.<br>
Just hopped off a big old bus in London town. Exciting, right? <br> Well, kinda.
<br> See, I'm here to find a job. My family back home needs some real <br> help with money , so I gotta step up and bring home the bacon. <br>
London's a whole new world for me. Big buildings, lots of <br> people rushing around. But I'm ready to roll up my sleeves and <br> get to work. Gotta make that cash.
Hopefully, I'll find something <br> soon and be able to send some money back home. That's the plan,<br> at least. 
<br> So yeah, that's me. Just a guy from somewhere else, trying to  make <br> it work here in London.
</p>""",unsafe_allow_html=True)
# with col22:
#     st.markdown(
#     """
#     <h1 <span style="color: #EBE3D5;">My interests</span><span style="color: #F55F5F;"> :</span></h1>
#     """ 
# , unsafe_allow_html=True)
#     stoggle(
#         "Click me!",
#         """🥷 Surprise! Here's some additional content""",
#     )
with open("text-animation.css", "r") as file:
    css_code = file.read()

# Display CSS animation code
st.markdown(f'<style>{css_code}</style>', unsafe_allow_html=True)

# Image URL
# image_url = "https://i.ibb.co/RD2bK96/Screenshot-2024-03-03-122415.png"

# # Markdown string for the image with fixed positioning
# image_markdown = f'<div style="position: fixed; bottom: 130px; right: 100px;">' \
#                  f'<img src="{image_url}" alt="Screenshot" width="400px">' \
#                  f'</div>'

# Markdown string for the text with fixed positioning
text_markdown = f"""<h1 style="
                    font-family: 'EB Garamond', serif;
                    font-optical-sizing: auto;
                    font-weight: 300;
                    font-style: italic;
                    font-size: 60px;
                    color: #F55F5F; 
                    position: fixed; 
                    bottom: 330px; 
                    right: 180px;
                    "> \
                <span style="color: #F55F5F;">If</span> \
                <span>only</span> \
                <span>we</span><br> \
                <span>were</span> \
                <span>stork</span> \
                </h1>"""

# Display the markdown for the image and text
# st.markdown(image_markdown, unsafe_allow_html=True)
st.markdown(text_markdown, unsafe_allow_html=True)
















instagram_image_url = "https://www.karliky.com/instagram.7cafa855.svg"  
instagram_image_url2 = "https://www.karliky.com/twitter.61c8a55c.svg"  

# Instagram account URL
instagram_account_url = "https://www.instagram.com/tunhaycuoi/"  
instagram_account_url2 = "https://twitter.com/realDonaldTrump"  
#link acc
st.markdown(
    f"""
    <style>
    .instagram-link {{
        position: fixed;
        bottom: 50px;
        left: 86px;
        z-index: 9999;
    }}
    </style>
    <a href="{instagram_account_url}" target="_blank" class="instagram-link">
        <img src="{instagram_image_url}" style="width: 30px; height: auto;">
    </a>
    """,
    unsafe_allow_html=True
)
st.markdown(
    f"""
    <style>
    .instagram-link2 {{
        position: fixed;
        bottom: 100px;
        left: 86px;
        z-index: 9999;
    }}
    </style>
    <a href="{instagram_account_url2}" target="_blank" class="instagram-link2">
        <img src="{instagram_image_url2}" style="width: 30px; height: auto;">
    </a>
    """,
    unsafe_allow_html=True)