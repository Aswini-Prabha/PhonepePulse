import json
import pandas as pd
import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="Phonepe Data Visualization webpage",layout="wide")
st.title(" :iphone: PhonePe Pulse:zap:")
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()
lottie_s=load_lottieurl(r"https://assets4.lottiefiles.com/packages/lf20_GXS1DssMnR.json")
lottie_t=load_lottieurl(r"https://assets4.lottiefiles.com/packages/lf20_kdcvbate.json")
with st.container():
    st.write("---")
    left_column,right_column=st.columns(2)
    with left_column:
        st_lottie(
                lottie_t,
                speed=3,
                reverse=False,
                loop=True,
                quality="low",
                height=100),
        st.subheader(
                 """
                 :large_orange_diamond: Here you can explore the trends of transaction happening in India!!!
                 """
            )
        x1=st.selectbox('Select Your Option :white_check_mark:', ("Transaction Data","User Data"))
        s1=st.button("Submit")
        if "s1_state" not in st.session_state:
            st.session_state.s1_state=False
            
        if (s1 or st.session_state.s1_state) and x1=="Transaction Data":
            st.session_state.s1_state=True
            x2=st.selectbox('Select Your Option :white_check_mark:',("Year Wise Transaction Data","State Wise Transaction Data"))
            s2=st.button("submit")
            if "s2_state" not in st.session_state:
                st.session_state.s2_state=False
            if (s2 or st.session_state.s2_state) and x2=="Year Wise Transaction Data":
                st.session_state.s2_state=True
                x3=st.selectbox('Select the Year :date: :white_check_mark:',(2018,2019,2020,2021,2022))
                x4=st.selectbox('Select the Quarter :date: :white_check_mark:',(1,2,3,4))
                s3=st.button("okay")
                if "s3_state" not in st.session_state:
                    st.session_state.s3_state=False
                    
                if s3 or st.session_state.s3_state:
                    st.session_state.s3_state=True
                    path=f'C:/Users/Aswini Praba/Desktop/python/git/pulse/data/aggregated/transaction/country/india/{x3}/{x4}.json'
                    with open(path,'r') as f:
                        info=json.load(f)
                        tran_data=info['data']['transactionData']
                        rows=[]
                        for data in tran_data:
                            data_row=data['paymentInstruments']
                            n=data['name']
                            for row in data_row:
                                row['name']=n
                                rows.append(row)
                        df=pd.DataFrame(rows)
                        df=df.pivot_table(index='name').reset_index()
                        st.write(df)
            
            elif (s2 or st.session_state.s2_state) and x2=="State Wise Transaction Data":
                st.session_state.s2_state=True
                s_n=st.selectbox("Select the State :round_pushpin: :white_check_mark:",('andaman-&-nicobar-islands','andhra-pradesh','arunachal-pradesh','assam','bihar','chandigarh','chhattisgarh','dadra-&-nagar-haveli-&-daman-&-diu','delhi','goa','gujarat','haryana','himachal-pradesh','jammu-&-kashmir','jharkhand','karnataka','kerala','ladakh','lakshadweep','madhya-pradesh','maharashtra','manipur','meghalaya','mizoram','nagaland','odisha','puducherry','punjab','rajasthan','sikkim','tamil-nadu','telangana','tripura','uttar-pradesh','uttarakhand','west-bengal'))
                y=st.selectbox("Select the Year :date: :white_check_mark:",(2018,2019,2020,2021,2022))
                Q=st.selectbox("Select the Quarter :date: :white_check_mark:",(1,2,3,4))
                s4=st.button("Okay")
                if "s4_state" not in st.session_state:
                    st.session_state.s4_state=False
                if s4 or st.session_state.s4_state:
                    st.session_state.s4_state=True
                    path1=f'C:/Users/Aswini Praba/Desktop/python/git/pulse/data/aggregated/transaction/country/india/state/{s_n}/{y}/{Q}.json'
                    with open(path1,'r') as f:
                        info=json.load(f)
                        tran_data=info['data']['transactionData']
                        rows=[]
                        for data in tran_data:
                            data_row=data['paymentInstruments']
                            n=data['name']
                            for row in data_row:
                                row['name']=n
                                rows.append(row)
                        df=pd.DataFrame(rows)
                        df=df.pivot_table(index='name').reset_index()
                        st.write(df)                    
                    
        if "s1_state" not in st.session_state:
            st.session_state.s1_state=False
        elif (s1 or st.session_state.s1_state) and x1=="User Data":
            st.session_state.s1_state=True
            x2=st.selectbox('Select Your Option :white_check_mark:',("Year Wise User Data","State Wise User Data"))
            s2=st.button("ssubmit")
            if "s2_state" not in st.session_state:
                st.session_state.s2_state=False
                
            if (s2 or st.session_state.s2_state) and x2=='Year Wise User Data':
                st.session_state.s2_state=True
                x3=st.selectbox("Select the Year :date: :white_check_mark:",(2018,2019,2020,2021,2022))
                x4=st.selectbox("Select the Quarter :date: :white_check_mark:",(1,2,3,4))
                s3=st.button("Done")
                if "s3_state" not in st.session_state:
                    st.session_state.s3_state=False
                    
                if s3 or st.session_state.s3_state:
                    st.session_state.s3_state=True
                    path2=f'C:/Users/Aswini Praba/Desktop/python/git/pulse/data/aggregated/user/country/india/{x3}/{x4}.json'
                    with open(path2,'r') as f:
                        info=json.load(f)
                        t=info['data']['aggregated']['registeredUsers']
                        st.write('Registration Users :',t)
                        tran_data =info['data']['usersByDevice']
                        dd=pd.DataFrame(tran_data)
                        st.write(dd)
            if "s2_state" not in st.session_state:
                st.session_state.s2_state=False
            elif (s2 or st.session_state.s2_state) and x2=='State Wise User Data':
                st.session_state.s2_state=True
                s_n=st.selectbox("Select the State :round_pushpin: :white_check_mark:",('andaman-&-nicobar-islands','andhra-pradesh','arunachal-pradesh','assam','bihar','chandigarh','chhattisgarh','dadra-&-nagar-haveli-&-daman-&-diu','delhi','goa','gujarat','haryana','himachal-pradesh','jammu-&-kashmir','jharkhand','karnataka','kerala','ladakh','lakshadweep','madhya-pradesh','maharashtra','manipur','meghalaya','mizoram','nagaland','odisha','puducherry','punjab','rajasthan','sikkim','tamil-nadu','telangana','tripura','uttar-pradesh','uttarakhand','west-bengal'))
                y=st.selectbox("Select the Year :date: :white_check_mark:",(2018,2019,2020,2021,2022))
                Q=st.selectbox("Select the Quarter :date: :white_check_mark:",(1,2,3,4))
                s4=st.button("done")
                if "s4_state" not in st.session_state:
                    st.session_state.s4_state=False
                if s4 or st.session_state.s4_state:
                    st.session_state.s4_state=True
                    path3=f'C:/Users/Aswini Praba/Desktop/python/git/pulse/data/aggregated/user/country/india/state/{s_n}/{y}/{Q}.json'
                    with open(path3,'r') as f:
                        info = json.load(f)
                        t=info['data']['aggregated']['registeredUsers']
                        st.write('Registration Users :',t)
                        tran_data =info['data']['usersByDevice']
                        dd=pd.DataFrame(tran_data)
                        st.write(dd)
    

    with right_column:
        st.empty()
        st_lottie(
            lottie_s,
            speed=0.2,
            reverse=False,
            loop=True,
            quality="low",
            height=500,
            width=None,
            key=None
            )

