import time
import streamlit as st
st.set_page_config(
    page_title="Home",
    page_icon="👋",
    initial_sidebar_state="collapsed"
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
<h1 style="font-family: 'EB Garamond', serif; font-size: 80px; color: #344E41; text-align: left;">Moving Forward</h1>
<h2 style="font-family: 'EB Garamond', serif; font-size: 20px; opacity: 0.7; color: #EBE3D5; text-align: left;">Posted on 14-10-2007</h2>
<p style="font-family: 'EB Garamond', serif; font-size: 22px; color: #EBE3D5;">
Nearly a month has passed without me knowing it. Lately, I’ve been breaking my back to make our ends meet. 
It isn’t a problem anyways. I’m still so glad that I got a job right on day one. However, that kebab shop is so 
poorly paid that, despite the kindness of the owner, I had to switch jobs after a few days. But luck is still with me 
- I got another job pretty easily. Being a kitchen porter is surely exhausting, still, the busy and wearying schedule 
cannot stop me from thinking about my loved ones. I missed little Maya so much - I just can’t get her off my mind. I hope 
Mother is still doing okay and still able to take good care of Maya. Tomorrow will be the day that I receive my wages. It’s
nothing close to a good payout, but at least, it’s enough to provide me with a basic life on this foreign land. My dear 
Marina, do you see me from up there? I hope you’re still watching us and giving us your blessings. I and our family miss 
you and love you so much, always.
<br> Half past midnight.. I think I should go to bed. Tomorrow will be another long, busy and tiring day.  


</p>
"""

navigation_links = """
<div style="margin-top: 10px; font-family: 'EB Garamond', serif; font-size: 22px; color: #EBE3D5;">
    <div style="float: left;">
        <a id="blog-link" class="navigation-link" href="/London" target="_self" style="color: #EBE3D5;"> ⬅Return to last entry </a>
    </div>
    <div style="float: right;">
        <a id="contact-link" class="navigation-link" href="/Blog" target="_self" style="color: #EBE3D5;"> Return to Blog preview ⮕</a>
    </div>
    <div style="clear: both;"></div>
</div>
"""

# Display content and navigation links
st.markdown(content + navigation_links, unsafe_allow_html=True)
