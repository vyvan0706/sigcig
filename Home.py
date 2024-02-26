import streamlit as st
import base64
from PIL import Image
from streamlit_extras.buy_me_a_coffee import button
from streamlit_extras.switch_page_button import switch_page
st.set_page_config(
    page_title="Home",
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
st.title('_Blog_ by :blue[lev] :sunglasses:')
st.write('1 + 1 = ')
def example():
    button(username="fake-username", text= 'Donate if you want!', width=221, coffee_color='#DDA15E', font='Roboto')
example()
def example2():
    want_to_contribute = st.button("Blog entries")
    if want_to_contribute:
        switch_page("Blog entries")
example2 ()
