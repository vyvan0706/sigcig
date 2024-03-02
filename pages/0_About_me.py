import streamlit as st
import base64
from PIL import Image
st.set_page_config(
    page_title="Blog entries",
    page_icon="🔥",
    layout='wide'
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
image_path = 'https://i.ibb.co/NsRKnGR/99-F9-EFCE-60-DF-403-C-8199-FAB105-CDC089.png'
# Define HTML with CSS styling to set the width
html_str2 =  f"""
<div style='width: 1080px; height: 200px;'>
    <img src='{image_path}' alt='Blog Banner' style='width:100%; height:100%; object-fit: cover;'>
</div>
"""
st.markdown(html_str2, unsafe_allow_html=True)
t1,t2,t3,t4,t5,t6,t7=st.tabs(['Blog1','Blog2','Blog3','Blog4','Blog5','Blog6','Blog7'])
with t1:

    text = """
<span style='color:black;'>
Today I went to the sulphur spring at Jor with my love - Marina. The sky was blue, just like a turquoise love letter, where the sunlights are countless words I want you to know. In the sky, I saw a flock of storks flew gracefully overhead, and some were finding food for the little storks waiting for their parents. I hope nature can cure what I have lost, but now, the most wonderful scenery can’t even pull myself together… 

I watched you immersed your body obediently in the scummy water. You were laining there, following your eyesight towards a female stork returning to its high nest. If only we were storks

Your voice waked me up from my daydream. Why d’you say that? I asked. Because you never see a stork dying. It’s as though they didn’t die

My dear, i hope i didn’t misunderstand you. I wish I could know how much time you have left with me. I wish I could do something to help you.
</span>
"""
    st.markdown(text, unsafe_allow_html=True)
with t2:
    text2 = """
<span style='color:black;'>
Today is probably the worst day of my life, Marina.
I don't understand why life is so unfair to you. 
you are a beautiful woman, a filial daughter, a good wife and a gentle mother, 
But why did God give you that terrible disease? leukemia. That makes me keep thinking since I received that shocking news, 
I don't know how much time I can still be with you, but no matter what, I still love you with all my heart. 
My love, I will try to be positive, work hard to help pay for medicine and take care of our family more. 
I only hope that you will be healthy and happy in the future.

</span>
"""
    st.markdown(text2, unsafe_allow_html=True)
with t3:
    text3 = """
<span style='color:black;'>
Marina darling, I'm returning home after days of being by your side without leaving. I thought it was just a nightmare, 
but when I woke up, you were gone from this world.But everything about you still exists here. The sweet scent of purple 
daisies still wafts from your shirt... you fell asleep so peacefully just in a blink and couldn't wake up again. The more 
effortlessly it is for you to go, the greater the pain of losing you.

</span>
"""
    st.markdown(text3, unsafe_allow_html=True)
with t4:
    text4 = """
<span style='color:black;'>
The Baryn sawmill officially closed today. I don't know how long can i live like this. My daughter and I have to depend entirely on my mother. My daughter, she's our precious gem, and she deserves to be happy, not suffer like this. My daughter deserves nothing but the best, and I will stop at nothing to give her the life she deserves.

</span>
"""
    st.markdown(text4, unsafe_allow_html=True)