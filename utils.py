import streamlit as st

def setup():
    st.sidebar.text('made by 모코코더')
    st.sidebar.text('for streamlit test')
    st.markdown(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Titillium+Web&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap');
            *{                
                # font-family:'Nanum Gothic', sans-serif;
                font-family: 'Titillium Web', sans-serif;
            }
            # [data-testid="stSidebarNav"]::before {
            #     content: "Loa";
            #     margin-left: 20px;
            #     margin-top: 20px;
            #     font-size: 30px;
            #     font-weight: 600;
            #     position: relative;
            #     top: 70px;
            #     bottom: 70px;
            # }
            .css-79elbk ul .css-j7qwjs{
                padding-bottom:3px;
                transform:translatex(0px) translatey(0px);
            }
            [data-testid="stSidebar"][aria-expanded="true"]{
                min-width: 200px;
                max-width: 230px;
            }           
            #MainMenu {visibility: hidden;}
            .css-15zrgzn {visibility: hidden;}
            .css-z5fcl4 {
                padding-top: 1rem;
                padding-bottom: 10rem;
                padding-left: 5rem;
                padding-right: 5rem;
            }
            .dataframe tr a{
                text-align:center;
                font-size:13px;
                font-family:'Nanum Gothic', sans-serif;
            }
            .css-ocqkz7 div h3{
                padding-top:0px;
            }
            .css-k7vsyb h3 span{
                margin-top:-12px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
