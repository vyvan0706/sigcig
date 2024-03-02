import streamlit as st
import base64
from PIL import Image
import streamlit as st
st.set_page_config(
    page_title="Home",
    page_icon="👋",
    layout= 'wide'
)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

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
             background: url("https://i.ibb.co/2c5PF35/z5210644115108-99ed313083d7406016deded000186acd.jpg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )



col1, col23, col4,col5,col6 = st.columns([2,17,3,3,3])
st.markdown(
    """
    <div style="position: fixed; top: 63px; left: 64px;">
        <img src="https://khothietke.net/wp-content/uploads/2021/03/freepng1633-dieu-thuoc-la-khong-hut-thuoc-2.png" width="80">
    </div>
    """,
    unsafe_allow_html=True
)

with col1:
    with open('wave.css') as css:
        files = css.read()
    st.markdown(f'<style>{files}</style>', unsafe_allow_html=True)
    st.markdown(
        """
        <body>
            <div class="patterns" style="width: 100%; height: 100vh; display: flex; justify-content: center; align-items: center;">
                <svg width="100%" height="100%" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid meet">
                  <defs>
                    <style>
                      @import url("https://fonts.googleapis.com/css2?family=EB+Garamond:wght@800&display=swap");
                      text {
                        font-family: "EB Garamond", serif !important;
                        font-optical-sizing: auto;
                        font-weight: 800;
                        font-style: normal;
                        font-size: 5rem;
                        cursor: pointer;
                        fill: #F55F5F; /* Adjust the fill color */
                        transform: rotate(270deg); /* Rotate the text */
                        transform-origin: center; /* Set rotation origin to center */
                      }
                    </style>
                    <circle fill="#be9ddf" cx="25" cy="25" r="2"></circle>
                  </defs>
                  <text x="300" y="40%" text-anchor="middle">     Blog by Lev     </text>
                </svg>
              </div>
            </body>
        """,
        unsafe_allow_html=True
    )
with col5:
    navigation_link = '<a class="navigation-link" href="/your-navigation-page" style="color: #EBE3D5;top: 63px; right: 400px;"><span style="color: #F55F5F;">&#8226;</span> about</a>'
    st.markdown(navigation_link, unsafe_allow_html=True)

with col6:
    navigation_link2 = '<a class="navigation-link" href="/your-navigation-page" style="color: #EBE3D5;top: 63px; right: 275px;"><span style="color: #F55F5F;">&#8226;</span> blog</a>'
    st.markdown(navigation_link2, unsafe_allow_html=True)
navigation_link = '<a class="navigation-link" href="/your-navigation-page" style="color: #EBE3D5;top: 63px; right: 120px;"><span style="color: #F55F5F;">&#8226;</span> contact</a>'
st.markdown(navigation_link, unsafe_allow_html=True)
import streamlit.components.v1 as components
# Define the HTML content00
with col23:

   html_content5 = """
<div class="word"></div>
"""

# Define the CSS styles
   css_styles = """
<style>
html {
  height: 100%;
}

.word {
  margin: auto;
  position:absolute;
  top:190px;
  left:80px;
  color: black;
  font: 700 normal 5em 'Eb Garamond';
  text-shadow: 5px 2px #EBE3D5, 2px 4px #EBE3D5, 3px 5px #EBE3D5;
}
</style>
"""

# Define the JavaScript code
   javascript_code = """
<script>
var words = ["Hi I'm Lev", "I'm from Europe", "I'm currently working in London"],
    part,
    i = 0,
    offset = 0,
    len = words.length,
    forwards = true,
    skip_count = 0,
    skip_delay = 15,
    speed = 70;
var wordflick = function () {
  setInterval(function () {
    if (forwards) {
      if (offset >= words[i].length) {
        ++skip_count;
        if (skip_count == skip_delay) {
          forwards = false;
          skip_count = 0;
        }
      }
    }
    else {
      if (offset == 0) {
        forwards = true;
        i++;
        offset = 0;
        if (i >= len) {
          i = 0;
        }
      }
    }
    part = words[i].substr(0, offset);
    if (skip_count == 0) {
      if (forwards) {
        offset++;
      }
      else {
        offset--;
      }
    }
    document.querySelector('.word').innerText = part;
  },speed);
};

wordflick();
</script>
"""
   custom_component = f"{css_styles}\n{html_content5}\n{javascript_code}"
   components.html(custom_component, height=500)

col11, col22 = st.columns([3, 2],gap='large')
# with col11:
#     with open("text-animation.css", "r") as file:
#          css_code = file.read()
#     st.markdown(f'<style>{css_code}</style>', unsafe_allow_html=True)
#     html_content = """
# <h2 style="color: #475058; position: fixed; top: 250px; left: 160px;">
#   <span>Hi</span>
#   <span>there👋</span>
#   <span>I'm</span>
#   <span>Lev!</span>
#   <span>I'm</span>
#   <span>from</span>
#   <span>an</span>
#   <span>Eastern</span><br>
#   <span>European country</span>
#   <span>country</span>
# </h2>
# """
# Display the HTML content
    # st.markdown(html_content, unsafe_allow_html=True)

# with col22:
#     st.markdown("""
#         <div style="display: flex; justify-content: center; position: fixed; bottom: 0px; right: 64px;">
#             <img src="https://i.ibb.co/VHJXY5D/levtheguy-ai-brush-removebg-502gwv2h.png" style="max-width:90%; height:auto; transform: scaleX(-1);">
#         </div>
#     """, unsafe_allow_html=True)





instagram_image_url = "https://www.karliky.com/instagram.7cafa855.svg"  
# Replace with your Instagram logo URL
instagram_image_url2 = "https://www.karliky.com/twitter.61c8a55c.svg"  

# Instagram account URL
instagram_account_url = "https://www.instagram.com/your_account/"  # Replace with your Instagram account URL

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
    <a href="{instagram_account_url}" target="_blank" class="instagram-link2">
        <img src="{instagram_image_url2}" style="width: 30px; height: auto;">
    </a>
    """,
    unsafe_allow_html=True
)
# Render linked images
# st.markdown(
#     f"""
#     <style>
#     .instagram-link {{
#         position: fixed;
#         bottom: 50px;
#         left: 86px;
#         z-index: 9998;
#     }}
#     .instagram-link img {{
#         margin-top: 10px;
#     }}
#     </style>
#     <a href="{instagram_account_url}" target="_blank" class="instagram-link">
#         <img src="{instagram_image_url}" style="width: 30px; height: auto;">
#         <img src="{instagram_image_url2}" style="width: 30px; height: auto;">
#     </a>
#     """,
#     unsafe_allow_html=True
# )