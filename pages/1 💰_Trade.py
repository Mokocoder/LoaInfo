import streamlit as st
import utils as ut
import requests

ut.setup()

s = requests.Session()

def serach_code(item):    
    return s.get('https://lostarkapi.ga/tradeplus/'+item).json()

def search_item(code):
    return s.get('https://lostarkapi.ga/trade/'+str(code)).json()

search_str = st.columns(1)[0].text_input(" ",key="search_str",placeholder="거래소에 검색할 아이템")
with st.expander("Filter"):
    grade_choices = st.multiselect("등급 필터",["일반","고급","희귀","영웅","전설","유물","고대","에스더"])

st.divider()

if search_str:
    data = serach_code(search_str)
    if data['Result'] == "Success" and len(data['Data']) > 0:
        codes = {}
        codes[data['FirstItem']['name']] = {'id':data['FirstItem']['id'], 'count':data['FirstItem']['BundleCount']}
        st.caption("탭 스크롤 : Shift + 스크롤")
        if grade_choices:
            temp_filtered = []
            for item in data['Data']:
                if str(item.split(' ')[0]) in grade_choices:
                    temp_filtered.append(item)
            data['Data'] = temp_filtered
        if len(data['Data']) > 0:
            itemtab = st.tabs(data['Data'])

            for i,tab in enumerate(itemtab):
                with tab:
                    if not data['Data'][i] in codes:
                        temp_serach = serach_code(data['Data'][i])
                        codes[data['Data'][i]] = {'id':temp_serach['FirstItem']['id'], 'count':temp_serach['FirstItem']['BundleCount']}

                    if data['Data'][i] in codes:
                        result = search_item(codes[data['Data'][i]]['id'])
                        if result['Result'] == "Success":
                            bar = {}
                            for j,chart in enumerate(result['Pricechart']):
                                result['Pricechart'][j]['Amount'] = int(chart['Amount'].replace(",",""))/int(codes[data['Data'][i]]['count'])
                                bar[str(chart['Price'])] = result['Pricechart'][j]['Amount']

                            st.caption("["+str(codes[data['Data'][i]]['count'])+"개 단위]")

                            cols = st.columns([7,1,15])
                            with cols[0]:
                                st.dataframe(result['Pricechart'])
                            with cols[2]:                                
                                st.bar_chart({"Price":bar})
        else:
            st.warning("Not Found")
    else:
            st.warning("Not Found")