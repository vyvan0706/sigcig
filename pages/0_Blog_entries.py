import streamlit as st
import base64
from PIL import Image
st.set_page_config(
    page_title="Blog entries",
    page_icon="👋",
)
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

tab1,tab2,tab3=st.tabs(['Blog1','Blog2','Blog3','Blog4','Blog5','Blog6','Blog7'])
