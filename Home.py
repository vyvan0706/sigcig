import streamlit as st
import base64
from PIL import Image
from streamlit_extras.buy_me_a_coffee import button
from streamlit_extras.switch_page_button import switch_page
st.set_page_config(
    page_title="Home",
    page_icon="👋",
    layout="wide"
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
_LOREM_IPSUM ='''Hello, I'm Lev. I'm on a journey, traveling from place to place, seeking something elusive yet essential. This blog will document my experiences and reflections along the way. Join me as I navigate through the twists and turns of life's unpredictable road.'''
def stream_data():
    for word in _LOREM_IPSUM.split():
        yield word + " "
        time.sleep(0.5)
st.write_stream(stream_data)
def example2():
    want_to_contribute = st.button("Blog entries")
    if want_to_contribute:
        switch_page("Blog entries")
example2 ()
