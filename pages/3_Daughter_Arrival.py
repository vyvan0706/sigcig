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
<h1 style="font-family: 'EB Garamond', serif; font-size: 80px; color: #344E41; text-align: left;">Daughter's Arrival</h1>
<h2 style="font-family: 'EB Garamond', serif; font-size: 20px; opacity: 0.7; color: #EBE3D5; text-align: left;">Posted on 29-5-2002</h2>
<p style="font-family: 'EB Garamond', serif; font-size: 22px; color: #EBE3D5;">
Today is probably one of the best days ever. <br> Welcome to the world,<span style=" font-style: italic;font-weight: 700; color:pink"> Maya</span>. <br> The moment when the nurse gave me my baby, my entire body and soul filled with eternal happiness - happier than holding any treasures. <br> Yet, today is also one of the worst days ever.<br> Seeing Marina going through all the worst pains to bring Maya to this life is so heartbreaking, and it hurts even more when I can’t do anything to share the pain with her. When the doctors pulled her bed out, I couldn’t hold my tears back anymore. She looked so vulnerable, yet she still had a smile full of happiness on her pale face. They said that she will have fully recovered in about a week. I can’t wait to see our family living happily ever after, so excited that every recent night, I pictured me and Marina taking care of our daughter, seeing her footsteps in life while we grow old together. I love them so so much.
</p>
"""

navigation_links = """
<div style="margin-top: 10px; font-family: 'EB Garamond', serif; font-size: 22px; color: #EBE3D5;">
    <div style="float: left;">
        <a id="blog-link" class="navigation-link" href="/Blog" target="_self" style="color: #EBE3D5;"> ⬅Return to Blog preview </a>
    </div>
    <div style="float: right;">
        <a id="contact-link" class="navigation-link" href="/Cancer" target="_self" style="color: #EBE3D5;"> Next Entry⮕ </a>
    </div>
    <div style="clear: both;"></div>
</div>
"""

# Display content and navigation links
st.markdown(content + navigation_links, unsafe_allow_html=True)
