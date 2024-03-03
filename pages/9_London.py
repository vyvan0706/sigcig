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
<h1 style="font-family: 'EB Garamond', serif; font-size: 80px; color: #344E41; text-align: left;">London Calling</h1>
<h2 style="font-family: 'EB Garamond', serif; font-size: 20px; opacity: 0.7; color: #EBE3D5; text-align: left;">Posted on 23-9-2007</h2>
<p style="font-family: 'EB Garamond', serif; font-size: 22px; color: #EBE3D5;">
It's my first night in London. I was lucky enough to have found a cheap yet convenient shared hostel, 9 miles away from 
central London. Lying in my bed, I can't help but think about them - my mother, my daughter Maya, and my beloved wife.
How's my mother doing? When I was still at home, I could help her with the chores and keep an eye on Maya. Now she has 
to do all of that alone. She is getting old, and I, her only son, can't do anything for her and still have to ask for help.
What a terrible son I am. And how is little Maya doing? Is she healthy? What is she doing there? How does she react to my
disappearance? When I left, she was still asleep. Mom told me she would tell her that i'm coming back soon, but i don't
know. There are very few chances that the economic conditions there are getting better. I would never want to see my daughter growing up without both of her parents, but what else could I do? I miss my wife so much. If only Death hadn't taken her away from me and from our family. Now that she's gone, I can't help but grieving over her and the family we built every single day. Even the smell of a random woman's boiled egg reminded me of our first vacation together to the sulfur springs at Jor. It was definitely one of my favorite memories ever. She was so gorgeous that I could hardly take my eyes off her. I remembered her saying "If only we were storks." At that moment, I simply thought she was silly. Now that I think again, I should've agreed with her.<span style="font-style: italic; font-weight: 800; color:#E6E6FA;"> If only we were storks.</span>
<br> 11p.m.. I think I should get some sleep. It's been a long and exhausting day. I hope tomorrow I will be able to get a 
job somewhere around here. 
<br> Father, as I lie down for sleep tonight, wash over me with the warmth of Your love. In Your mercy, soothe my pain, whether in my body, mind or soul. Grant me a restful night of sleep so that when I awake, I'm strengthened to do Your will. Amen.
</p>
"""

navigation_links = """
<div style="margin-top: 10px; font-family: 'EB Garamond', serif; font-size: 22px; color: #EBE3D5;">
    <div style="float: left;">
        <a id="blog-link" class="navigation-link" href="/Work" target="_self" style="color: #EBE3D5;"> ⬅Return to last entry </a>
    </div>
    <div style="float: right;">
        <a id="contact-link" class="navigation-link" href="/Moving_Forward" target="_self" style="color: #EBE3D5;"> Next Entry ⮕</a>
    </div>
    <div style="clear: both;"></div>
</div>
"""

# Display content and navigation links
st.markdown(content + navigation_links, unsafe_allow_html=True)
