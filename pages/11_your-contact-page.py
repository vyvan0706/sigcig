import streamlit as st
import base64
from PIL import Image
import time
import streamlit.components.v1 as components

from streamlit_extras.stoggle import stoggle 
st.set_page_config(
    page_title="Blog entries",
    page_icon="🔥",
    layout= 'wide',
    initial_sidebar_state="collapsed"
)
custom_scrollbar_css = """
<style>
/* Hide scrollbar */
body*  {
    overflow: hidden !important;
}
::-webkit-scrollbar {
    display: none;
}
</style>
"""

# Render the CSS
st.markdown(custom_scrollbar_css, unsafe_allow_html=True)
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
             background: url("https://i.ibb.co/5L9yJX5/Screenshot-2024-03-04-002913.png");
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

col1, col2,col3, col4,col5,col6 = st.columns([2,13,5,2,2,3])

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
    navigation_link2 = '<a id="blog-link" class="navigation-link" href="/About_me" target="_self" style="color: #EBE3D5;top: 63px; right: 255px;"><span style="color: #F55F5F;">&#8226;</span> about</a>'
    st.markdown(navigation_link2, unsafe_allow_html=True)

navigation_link3 = '<a id="contact-link" class="navigation-link" href="/Blog" target="_self" style="color: #EBE3D5;top: 63px; right: 120px;"><span style="color: #F55F5F;">&#8226;</span> blog</a>'
st.markdown(navigation_link3, unsafe_allow_html=True)
st.markdown(
    """
    <div style="position: fixed; top: 150px; left: 290px;">
        <img src="https://i.ibb.co/3777gSb/z5213912693174-c1f7a8a2fac66b82fc6c99c7732aa857.jpg" width="350">
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <h1 <span style="font-family: 'EB Garamond', serif;font-size: 80px;
color: #EBE3D5; position: fixed; top: 100px; right: 270px;">Contact me </span><span style="color: #F55F5F;"> :</span></h1>
    """ 
, unsafe_allow_html=True)
st.markdown(
    """
    <p <span style="font-family: 'EB Garamond', serif;font-size: 30px;
color: #EBE3D5; position: fixed; top: 300px; right: 250px;">Contact </span></p>
    """ 
, unsafe_allow_html=True)
st.markdown(
    """
    <p <span style="font-family: 'EB Garamond', serif;font-size: 25px;
color: #EBE3D5; position: fixed; top: 350px; right:53px;">levgobigorgohome@blog.com </span></p>
    """ 
, unsafe_allow_html=True)
with col3: 
# Define form fields
   st.write('')
   st.write('')
   st.write('')
   st.write('')
   st.write('')
   st.write('')
   st.write('')
   st.write('')
   st.write('')
   st.write('')
   st.write('')
   st.write('')
   st.write('')
   st.write('')

   name = st.text_input("Name")
   email = st.text_input("Email")
   message = st.text_area("Message")

# Render the submit button
   submit_clicked = st.button("Submit")

# If submit button is clicked, display submission message
   if submit_clicked:
      st.success("Thanks for contacting me!")


instagram_image_url = "https://www.karliky.com/instagram.7cafa855.svg"  
instagram_image_url2 = "https://www.karliky.com/twitter.61c8a55c.svg"  

# Instagram account URL

instagram_account_url = "https://www.instagram.com/tunhaycuoi/"  
instagram_account_url2 = "https://twitter.com/realDonaldTrump"    # Replace with your Instagram account URL
#link acc
st.markdown(
    f"""
    <style>
    .instagram-link {{
        position: fixed;
        bottom: 260px;
        right : 310px;
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
        bottom: 263px;
        right : 260px;
        z-index: 9999;
    }}
    </style>
    <a href="{instagram_account_url2}" target="_blank" class="instagram-link2">
        <img src="{instagram_image_url2}" style="width: 30px; height: auto;">
    </a>
    """,
    unsafe_allow_html=True)