import streamlit as st
import utils as ut
import requests
import pandas as pd

s = requests.Session()

def load_notice():
    return s.get('http://152.70.248.4/notice/').json()

def load_adventure():
    return s.get('http://152.70.248.4/adventureisland/').json()

def load_total_adventure():
    return s.get('http://152.70.248.4/adventure_calendar/').json()

ut.setup()

st.markdown("""
    <style>
        .st-bf .st-bx input[type=text]{
            border-color:#645b5b;
                border-width:1px;
                border-style:solid;
            }
    </style>""",
    unsafe_allow_html=True
)

cols = st.columns([5,1,5])

with cols[0] :
    st.title('Notice')
    df = pd.DataFrame.from_dict({'Notice': load_notice()})
    st.write(df.to_html(escape=False, index=False, show_dimensions=False, justify="center"), unsafe_allow_html=True,)

with cols[2] :
    st.title('Calendar')
    data = load_adventure()

    if (data['Result'] == "Success"):
        st.markdown(f"**:blue[{data['IslandDate'].replace('시작','')}]**")
        st.dataframe(data['Island'])

st.divider()            

total_calen = load_total_adventure()
if (total_calen['Result'] == "Success"):
    date = []
    for element in total_calen:
        if element != "Result":
            if not str(element[:10]) in date:
                date.append(str(element[:10]))

    cal_tabs = st.tabs(date)

    for i,tab in enumerate(cal_tabs):
        with tab:
            temp = {}
            for element in total_calen:
                if date[i] in str(element):
                    temp[str(element).replace(date[i]+"T","")] = (total_calen[element])
                    
            st.dataframe(temp)