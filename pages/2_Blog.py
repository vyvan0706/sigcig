import streamlit as st
import base64
from PIL import Image
import streamlit as st
import time
import streamlit.components.v1 as components
#layout for page
st.set_page_config(
    page_title="Home",
    page_icon="👋",
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


#columns
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

with col5:
    navigation_link = '<a id="about-link" class="navigation-link" href="/Home" target="_self" style="color: #EBE3D5;top: 63px; right: 400px;"><span style="color: #F55F5F;">&#8226;</span> home</a>'
    st.markdown(navigation_link, unsafe_allow_html=True)

with col6:
    navigation_link2 = '<a id="blog-link" class="navigation-link" href="/About_me" target="_self" style="color: #EBE3D5;top: 63px; right: 275px;"><span style="color: #F55F5F;">&#8226;</span> about</a>'
    st.markdown(navigation_link2, unsafe_allow_html=True)

navigation_link3 = '<a id="contact-link" class="navigation-link" href="/your-contact-page" target="_self" style="color: #EBE3D5;top: 63px; right: 120px;"><span style="color: #F55F5F;">&#8226;</span> contact</a>'
st.markdown(navigation_link3, unsafe_allow_html=True)
st.markdown(
    """
    <h1 <span style="font-family: 'EB Garamond', serif;font-size: 80px;
color: #EBE3D5; position: fixed; top: 80px; left: 300px;">Blog</span><span style="color: #F55F5F;"> :</span></h1>
    """ 
, unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .scrollable-images {
        position: fixed;
        top: 230px;
        left: 300px;
        width: 1000px; /* Adjust width as needed */
        max-height: 70vh; /* Set maximum height for scrolling */
        overflow-y: auto;
    }
    .image-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
    }
    .image-box {
        width: 30%; /* Adjust width for each image box */
        margin-bottom: 20px;
    }
    .image-box img {
        width: 100%;
    }
    @import url('https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400..800;1,400..800&display=swap');
    .image-title {
        font-family: 'EB Garamond';
        text-align: center;
        font-size: 24px;
        color: #EBE3D5 !important;
        margin-top: 5px;
    }
    .scrollable-images a {
        color: #EBE3D5 !important;
        text-decoration: none; /* Remove default underline */
        transition: text-decoration 0.3s; /* Smooth transition */
    }
    .scrollable-images a:hover {
        text-decoration: underline; /* Underline on hover */
    }
    </style>
    
    <div class="scrollable-images">
        <div class="image-container">
            <div class="image-box">
                <a href="/Daughter_Arrival" target="_self">
                    <img src="https://us.images.westend61.de/0001348148pw/close-up-tired-newborn-baby-boy-sleeping-HOXF06195.jpg" alt="newborn">
                </a>
                <div class="image-title">
                    <a href="/Daughter_Arrival" target="_self">Daughter's Arrival</a>
                </div>
            </div>
            <div class="image-box">
                <a href="/Cancer" target="_self">
                    <img src="https://i.ibb.co/9c3FM6H/Screenshot-2024-03-03-172439.png" alt="cancer">
                </a>
                <div class="image-title">
                    <a href="/Cancer" target="_self">Cancer Diagnosis</a>
                </div>
            </div>
            <div class="image-box">
                <a href="/Journey" target="_self">
                    <img src="https://i.ibb.co/0tnNLq0/428321598-1196100685109035-7544325101553350177-n.jpg" alt="spring day">
                </a>
                <div class="image-title">
                    <a href="/Journey" target="_self">one hope left...</a>
                </div>
            </div>
        </div>
        <div class="image-container">
            <div class="image-box">
                <a href="/Farewell" target="_self">
                    <img src="https://images.unsplash.com/photo-1463947628408-f8581a2f4aca?q=80&w=1770&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="farewell">
                </a>
                <div class="image-title">
                    <a href="/Farewell" target="_self">Farewell</a>
                </div>
            </div>
            <div class="image-box">
                <a href="/Work" target="_self">
                    <img src="https://cdn1.epicgames.com/ue/product/Screenshot/Sawmill---closed-area0017HighresScreenshot00006-1920x1080-a45dae7a6b9a9ccf89738e60ac0ca739.png?resize=1&w=1920" alt="workplace closure">
                </a>
                <div class="image-title">
                    <a href="/Work" target="_self">Workplace Closure</a>
                </div>
            </div>
            <div class="image-box">
                <a href="/London" target="_self">
                    <img src="https://ohheyiceland.files.wordpress.com/2017/07/cityoflondon2.jpg" alt="london calling">
                </a>
                <div class="image-title">
                    <a href="/London" target="_self">London Calling</a>
                </div>
            </div>
        </div>
        <div class="image-container">
            <div class="image-box">
                <a href="/Moving_Forward" target="_self">
                    <img src="https://recruitment-agency.london/wp-content/uploads/2023/12/Kitchen-Porter-Agency-London.jpg" alt="workplace closure">
                </a>
                <div class="image-title">
                    <a href="/Moving_Forward" target="_self">Moving Forward</a>
                </div>
            </div>
        </div>
    </div>
    """
    ,
    unsafe_allow_html=True
)


    
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





