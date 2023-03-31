import json
import pandas as pd
import streamlit as st
from streamlit_lottie import st_lottie
import requests
from streamlit_option_menu import option_menu
from PIL import Image
import os
import plotly.express as px
import geopandas as gpd
import sqlite3


st.set_page_config(page_title="Phonepe Data Visualization webpage",layout="wide")
st.title(" :iphone: PhonePe Pulse:zap:")
with st.sidebar:
    select=option_menu(None, ["Home", "Quarter wise Data", "Transaction Data","Users Data",  "Map", 'Contact','Feedback'], 
        icons=['house', 'book','search','search','globe', 'person-lines-fill','chat-dots'], 
        menu_icon="cast", default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "25px"}, 
            "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "green"},})
image1=Image.open(r"C:\Users\Aswini Praba\Desktop\completedproject\spotlight_1.jpg")
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()
lottie_s=load_lottieurl(r"https://assets4.lottiefiles.com/packages/lf20_GXS1DssMnR.json")
lottie_t=load_lottieurl(r"https://assets4.lottiefiles.com/packages/lf20_kdcvbate.json")
lottie_m=load_lottieurl(r"https://assets4.lottiefiles.com/datafiles/5FGDT1tGd6PRFWjrlnK36tsX4dv7kt1ihUMebNma/india.json")
#creating dataframes
#path=os.getcwd()+"/pulse/data/aggregated/transaction/country/india/state/"
path=f'C:/Users/Aswini Praba/Desktop/python/git/pulse/data/aggregated/transaction/country/india/state/'
Agg_state_list=os.listdir(path)
clm={'State':[], 'Year':[],'Quater':[],'Transacion_type':[], 'Transacion_count':[], 'Transacion_amount':[]}
for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)    
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)        
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['transactionData']:

              Name=z['name']
              count=z['paymentInstruments'][0]['count']
              amount=z['paymentInstruments'][0]['amount']
              clm['Transacion_type'].append(Name)
              clm['Transacion_count'].append(count)
              clm['Transacion_amount'].append(amount)
              clm['State'].append(i)
              clm['Year'].append(j)
              clm['Quater'].append(int(k.strip('.json')))
Agg_Trans=pd.DataFrame(clm)
#2
#path_tran_user=os.getcwd()+"/pulse/data/aggregated/user/country/india/state/"
path_tran_user=f'C:/Users/Aswini Praba/Desktop/python/git/pulse/data/aggregated/user/country/india/state/'
user_state_list=os.listdir(path_tran_user)
#Agg_state_list
user_table={'State':[], 'Year':[],'Quarter':[],'user_device_brand':[], 'user_count':[], 'user_percentage':[]}
for i in user_state_list:
    p_i=path_tran_user+i+"/"
    user_yr=os.listdir(p_i)    
    for j in user_yr:
        p_j=p_i+j+"/"
        user_yr_list=os.listdir(p_j)        
        for k in user_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            if D['data']['usersByDevice'] is not None:

              for z in D['data']['usersByDevice']:

                brand=z['brand']
                count=z['count']
                percentage=z['percentage']
                user_table['user_device_brand'].append(brand)
                user_table['user_count'].append(count)
                user_table['user_percentage'].append(percentage)
                user_table['State'].append(i)
                user_table['Year'].append(j)
                user_table['Quarter'].append(int(k.strip('.json')))

Agg_User=pd.DataFrame(user_table)
#3
#path_map_tran=os.getcwd()+"/pulse/data/map/transaction/hover/country/india/state/"
path_map_tran=f'C:/Users/Aswini Praba/Desktop/python/git/pulse/data/map/transaction/hover/country/india/state/'
map_tran_state_list=os.listdir(path_map_tran)
map_tran_list={'State':[], 'Year':[],'Quarter':[],'District':[], 'Transacion_count':[], 'Transacion_amount':[]}
for i in map_tran_state_list:
    p_i=path_map_tran+i+"/"
    map_tran_yr=os.listdir(p_i)    
    for j in map_tran_yr:
        p_j=p_i+j+"/"
        map_tran_yr_list=os.listdir(p_j)        
        for k in map_tran_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['hoverDataList']:

              Name=z['name']
              count=z['metric'][0]['count']
              amount=z['metric'][0]['amount']
              map_tran_list['District'].append(Name)
              map_tran_list['Transacion_count'].append(count)
              map_tran_list['Transacion_amount'].append(amount)
              map_tran_list['State'].append(i)
              map_tran_list['Year'].append(j)
              map_tran_list['Quarter'].append(int(k.strip('.json')))
map_tran_table=pd.DataFrame(map_tran_list)
#4
#path_map_user=os.getcwd()+"/pulse/data/map/user/hover/country/india/state/"
path_map_user=f'C:/Users/Aswini Praba/Desktop/python/git/pulse/data/map/user/hover/country/india/state/'
map_user_state_list=os.listdir(path_map_user)
map_user_list={'State':[], 'Year':[],'Quarter':[],'District':[], 'Registered_Users':[]}
for i in map_user_state_list:
    p_i=path_map_user+i+"/"
    map_user_yr=os.listdir(p_i)    
    for j in map_user_yr:
        p_j=p_i+j+"/"
        map_user_yr_list=os.listdir(p_j)        
        for k in map_user_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z,Z in D['data']['hoverData'].items():
              Name=z
              reg_users=Z['registeredUsers']
              map_user_list['District'].append(Name)
              map_user_list['Registered_Users'].append(reg_users)
              map_user_list['State'].append(i)
              map_user_list['Year'].append(j)
              map_user_list['Quarter'].append(int(k.strip('.json')))
map_user_table=pd.DataFrame(map_user_list)
#5
#path_top_tran=os.getcwd()+"/pulse/data/top/transaction/country/india/state/"
path_top_tran=f'C:/Users/Aswini Praba/Desktop/python/git/pulse/data/top/transaction/country/india/state/'
top_tran_state_list=os.listdir(path_top_tran)
top_tran_list={'State':[], 'Year':[],'Quarter':[],'District':[], 'Transacion_count':[], 'Transacion_amount':[]}
for i in top_tran_state_list:
    p_i=path_top_tran+i+"/"
    top_tran_yr=os.listdir(p_i)    
    for j in top_tran_yr:
        p_j=p_i+j+"/"
        top_tran_yr_list=os.listdir(p_j)        
        for k in top_tran_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['districts']:

              Name=z['entityName']
              count=z['metric']['count']
              amount=z['metric']['amount']
              top_tran_list['District'].append(Name)
              top_tran_list['Transacion_count'].append(count)
              top_tran_list['Transacion_amount'].append(amount)
              top_tran_list['State'].append(i)
              top_tran_list['Year'].append(j)
              top_tran_list['Quarter'].append(int(k.strip('.json')))
top_tran_table=pd.DataFrame(top_tran_list)
#6
#path_top_user=os.getcwd()+"/pulse/data/top/user/country/india/state/"
path_top_user=f'C:/Users/Aswini Praba/Desktop/python/git/pulse/data/top/user/country/india/state/'
top_user_state_list=os.listdir(path_top_user)
top_user_list={'State':[], 'Year':[],'Quarter':[],'District':[], 'Registered_Users':[]}
for i in top_user_state_list:
    p_i=path_top_user+i+"/"
    top_user_yr=os.listdir(p_i)    
    for j in top_user_yr:
        p_j=p_i+j+"/"
        top_user_yr_list=os.listdir(p_j)        
        for k in top_user_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['districts']:
              Name=z['name']
              reg_users=z['registeredUsers']
              top_user_list['District'].append(Name)
              top_user_list['Registered_Users'].append(reg_users)
              top_user_list['State'].append(i)
              top_user_list['Year'].append(j)
              top_user_list['Quarter'].append(int(k.strip('.json')))
top_user_table=pd.DataFrame(top_user_list)
# uploading df table to database by connecting sqlite3
conn=sqlite3.connect('phonepaypulse.db')
create_sql_1="CREATE TABLE IF NOT EXISTS agg_tran(State text,Year text,Quater integer,Transaction_type text,Transaction_count integer,Transaction_amount float)"
cursor=conn.cursor()
cursor.execute(create_sql_1)
for row in Agg_Trans.itertuples():
  insert_sql_1=f"INSERT INTO agg_tran(State,Year,Quater,Transaction_type,Transaction_count,Transaction_amount) values ('{row[1]}','{row[2]}',{row[3]},'{row[4]}',{row[5]},{row[6]} )"
  cursor.execute(insert_sql_1)
conn.commit()

create_sql_2="CREATE TABLE IF NOT EXISTS agg_users(State text,Year text,Quarter integer,user_device_brand text,user_count integer,user_percentage float)"
cursor=conn.cursor()
cursor.execute(create_sql_2)
for row in Agg_User.itertuples():
  insert_sql_2=f"INSERT INTO agg_users(State,Year,Quarter,user_device_brand,user_count,user_percentage) values ('{row[1]}','{row[2]}',{row[3]},'{row[4]}',{row[5]},{row[6]} )"
  cursor.execute(insert_sql_2)
conn.commit()

create_sql_3="CREATE TABLE IF NOT EXISTS map_tran(State text,Year text,Quarter integer,District text,Transaction_count integer,Transaction_amount float)"
cursor=conn.cursor()
cursor.execute(create_sql_3)
for row in map_tran_table.itertuples():
  insert_sql_3=f"INSERT INTO map_tran(State,Year,Quarter,District,Transaction_count,Transaction_amount) values ('{row[1]}','{row[2]}',{row[3]},'{row[4]}',{row[5]},{row[6]} )"
  cursor.execute(insert_sql_3)
conn.commit()

create_sql_4="CREATE TABLE IF NOT EXISTS map_users(State text,Year text,Quarter integer,District text,Registered_Users integer)"
cursor=conn.cursor()
cursor.execute(create_sql_4)
for row in map_user_table.itertuples():
  insert_sql_4=f"INSERT INTO map_users(State,Year,Quarter,District,Registered_Users) values ('{row[1]}','{row[2]}',{row[3]},'{row[4]}',{row[5]} )"
  cursor.execute(insert_sql_4)
conn.commit()

create_sql_5="CREATE TABLE IF NOT EXISTS top_tran(State text,Year text,Quarter integer,District text,Transaction_count integer,Transaction_amount float)"
cursor=conn.cursor()
cursor.execute(create_sql_5)
for row in top_tran_table.itertuples():
  insert_sql_5=f"INSERT INTO top_tran(State,Year,Quarter,District,Transaction_count,Transaction_amount) values ('{row[1]}','{row[2]}',{row[3]},'{row[4]}',{row[5]},{row[6]} )"
  cursor.execute(insert_sql_5)
conn.commit()

create_sql_6="CREATE TABLE IF NOT EXISTS top_users(State text,Year text,Quarter integer,District text,Registered_Users integer)"
cursor=conn.cursor()
cursor.execute(create_sql_6)
for row in top_user_table.itertuples():
  insert_sql_6=f"INSERT INTO top_users(State,Year,Quarter,District,Registered_Users) values ('{row[1]}','{row[2]}',{row[3]},'{row[4]}',{row[5]} )"
  cursor.execute(insert_sql_6)
conn.commit()

cursor = conn.cursor()

if select=="Home":
    with st.container():
     image_column,text_column=st.columns((1,2))
     with image_column:
      st.image(image1)
     with text_column:
      st.write(
			"""
			The Indian digital payments story has truly captured
			the world's imagination. From the largest towns to the
			remotest villages, there is a payments
			revolution being driven by the penetration of
			mobile phones and data.!!!
			As of now, nearly 40% of all payments done in India are digital!
			PhonePe Pulse is window to the world of how India transacts with
			interesting trends, deep insights and in-depth analysis based on
 		        cumulative phonepe users and transaction data provided!""")
      st.write("""
			Overall, digital transactions in India have revolutionized
			the way people make payments and conduct transactions.
			They have provided consumers with an easy, fast, and secure
			way to make payments and
			have contributed to the growth of the country's economy.

			"""
		)

     st_lottie(
            lottie_m,
            speed=0.1,
            reverse=False,
            loop=True,
            quality="low",
            height=500,
            width=None,
            key=None
            )     
#Quarter wise data of aggregate transaction and user
if select =="Quarter wise Data":
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
if select == "Contact":
    aboutme ="""I am interested in pursuing a career in data science
                  and eager to learn and grow in the field of data science
                  and working towards becoming a professional in
                  this exciting and rapidly evolving field.!"""
    links={
        "GITHUB": "https://github.com/Aswini-Prabha",
        "LINKEDIN": "https://www.linkedin.com/in/aswini-prabha-a32229268/"}
    column1, column2= st.columns(2)
    with column1:
        column1.image(Image.open(r"C:\Users\Aswini Praba\Documents\Me\photograph.jpg.jpg"),width=150)
    with column2:
        st.subheader("AswiniPrabha")
        st.subheader(f'{"Mail :"}  {"aswiniprabha22@gmail.com"}')
        st.write(aboutme)
        S=st.columns(len(links))
        for i, (x, y) in enumerate(links.items()):
             S[i].write(f"[{x}]({y})")


if select=="Transaction Data":
    op_1=st.selectbox("",["Aggregate Transaction","District wise transaction","Top Transaction"],0)
    if op_1=="Aggregate Transaction":
        cursor.execute("SELECT DISTINCT State FROM agg_tran")
        states = [""] + [row[0] for row in cursor.fetchall()]
        col1,col2,col3 = st.columns(3)
        with col1:
            st.write("SELECT THE TYPE OF TRANSACTION")
            transaction_type = st.selectbox("",["","Peer-to-peer payments",
                                        "Merchant payments", "Financial Services",
                                        "Recharge & bill payments", "Others"],0)
            if transaction_type:
                cursor.execute(f"SELECT DISTINCT State,Quater,Year,Transaction_type,Transaction_count,Transaction_amount FROM agg_tran WHERE Transaction_type = '{transaction_type}' ORDER BY State,Quater,Year")
                df = pd.DataFrame(cursor.fetchall(), columns=['State','Quater', 'Year', 'Transaction_type','Transaction_count', 'Transaction_amount'])
                st.write(df)
        with col2:
            st.write("SELECT THE YEAR")
            select_year = st.selectbox("",["","2018", "2019", "2020", "2021", "2022"],0)
            if transaction_type and select_year:
                cursor.execute(f"SELECT DISTINCT State,Year,Quater,Transaction_type,Transaction_count,Transaction_amount FROM agg_tran WHERE Year = '{select_year}' AND Transaction_type = '{transaction_type}' ORDER BY State,Quater,Year")
                df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'Transaction_type','Transaction_count', 'Transaction_amount'])
                st.write(df)
        with col3:
            st.write("SELECT THE STATE")
            select_state = st.selectbox("State", states, 0)
            if transaction_type and select_state and select_year:
                cursor.execute(f"SELECT DISTINCT State,Year,Quater,Transaction_type,Transaction_count,Transaction_amount FROM agg_tran WHERE State = '{select_state}' AND Transaction_type = '{transaction_type}' And Year = '{select_year}' ORDER BY State,Quater,Year")
                df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'Transaction_type','Transaction_count', 'Transaction_amount'])
                st.write(df)
#----------

    if op_1=="District wise transaction":
        
       cursor.execute("SELECT DISTINCT District FROM map_tran")
       map_trans = pd.DataFrame(cursor.fetchall(), columns=['District'])

       cursor.execute("SELECT DISTINCT State FROM map_tran")
       states = [""] + [row[0] for row in cursor.fetchall()]
       col1,col2,col3 = st.columns(3)
       with col1:
           st.subheader("SELECT THE STATE")
           select_state = st.selectbox("State", states, 0)
           if select_state:
               cursor.execute(f"SELECT DISTINCT State,Year,Quarter,District,Transaction_count,Transaction_amount FROM map_tran WHERE State = '{select_state}' ORDER BY State,Year,Quarter,District");
               df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quarter", 'District', 'Transaction_count','Transaction_amount'])
               st.write(df)
       with col2:
            st.subheader("SELECT THE YEAR")
            select_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
            if select_year and select_state:
                cursor.execute(f"SELECT DISTINCT State,Year,Quarter,District,Transaction_count,Transaction_amount FROM map_tran WHERE Year = '{select_year}' AND State = '{select_state}' ORDER BY State,Year,Quarter,District");
                df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quarter", 'District', 'Transaction_count','Transaction_amount'])
                st.write(df)
       with col3:
           st.subheader("SELECT THE DISTRICT")
           district = st.selectbox("search by", map_trans["District"].unique().tolist())
           if district and select_state and select_year:
               cursor.execute(f"SELECT DISTINCT State,Year,Quarter,District,Transaction_count,Transaction_amount FROM map_tran WHERE District = '{district}' AND State = '{select_state}' AND Year = '{select_year}' ORDER BY State,Year,Quarter,District");
               df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quarter", 'District', 'Transaction_count','Transaction_amount'])
               st.write(df)
#-----------
    if op_1=="Top Transaction":
        cursor.execute("SELECT DISTINCT Year FROM top_tran")
        years = [""] + [str(row[0]) for row in cursor.fetchall()]

        cursor.execute("SELECT DISTINCT State FROM top_tran")
        states = [""] + [row[0] for row in cursor.fetchall()]

        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("SELECT THE STATE")
            select_state = st.selectbox("State", states, 0)
            if select_state:
                cursor.execute(f"SELECT State, Year, Quarter, District, Transaction_count, Transaction_amount FROM top_tran WHERE State = '{select_state}' GROUP BY State, Year, Quarter")
                df = pd.DataFrame(cursor.fetchall(), columns=["State", "Year", "Quarter", "District", "Transaction_count", "Transaction_amount"])
                st.write(df)
        with col2:
            st.subheader("SELECT THE YEAR")
            select_year = st.selectbox("Year", years, 0)
            if select_state and select_year:
                cursor.execute(f"SELECT State, Year, Quarter, District, Transaction_count, Transaction_amount FROM top_tran WHERE State = '{select_state}' AND Year = '{select_year}' GROUP BY State, Year, Quarter")
                df = pd.DataFrame(cursor.fetchall(), columns=["State", "Year", "Quarter", "District", "Transaction_count", "Transaction_amount"])
                st.write(df)
            
        with col3:
            st.subheader("SELECT THE QUARTER")
            select_quarter = st.selectbox("Quarter", ["", "1", "2", "3", "4"], 0)
            if select_state and select_year and select_quarter:
                cursor.execute(f"SELECT State, Year, Quarter, District, Transaction_count, Transaction_amount FROM top_tran WHERE State = '{select_state}' AND Year = '{select_year}' AND Quarter = '{select_quarter}' GROUP BY State, Year, Quarter")
                df = pd.DataFrame(cursor.fetchall(), columns=["State", "Year", "Quarter", "District", "Transaction_count", "Transaction_amount"])
                st.write(df)


if select=="Users Data":
    op_2=st.selectbox("",["Aggregate brand users","District wise users","Top users"],0)
    
    if op_2=="District wise users":
        cursor.execute("SELECT DISTINCT State FROM map_users")
        states = [""] + [row[0] for row in cursor.fetchall()]

        cursor.execute("SELECT DISTINCT District FROM map_users")
        map_trans= pd.DataFrame(cursor.fetchall(), columns=['District'])
        col1,col2,col3 = st.columns(3)
        with col1:
            st.subheader("SELECT THE STATE")
            select_state = st.selectbox("State", states, 0)
            if select_state:
                cursor.execute(f"SELECT State,Year,Quarter,District,Registered_Users FROM map_users WHERE State = '{select_state}' ORDER BY State,Year,Quarter,District")
                df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quarter", 'District', 'Registered_Users'])
                st.write(df)
        with col2:
            st.subheader("SELECT THE YEAR")
            select_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
            if select_state and select_year:
                cursor.execute(f"SELECT State,Year,Quarter,District,Registered_Users FROM map_users WHERE Year = '{select_year}' AND State = '{select_state}' ORDER BY State,Year,Quarter,District")
                df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quarter", 'District', 'Registered_Users'])
                st.write(df)
        with col3:
            st.subheader("SELECT THE DISTRICT")
            district = st.selectbox("search by", map_trans["District"].unique().tolist())
            if select_state and select_year and district:
                cursor.execute(f"SELECT State,Year,Quarter,District,Registered_Users FROM map_users WHERE Year = '{select_year}' AND State = '{select_state}' AND District = '{district}' ORDER BY State,Year,Quarter,District")
                df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quarter", 'District', 'Registered_Users'])
                st.write(df)


    if op_2=="Aggregate brand users":
        cursor.execute(f"SELECT DISTINCT(user_device_brand) FROM agg_users ORDER BY user_device_brand");
        brands = [row[0] for row in cursor.fetchall()]
        
        cursor.execute("SELECT DISTINCT State FROM agg_users")
        states = [""] + [row[0] for row in cursor.fetchall()]
        
        col1,col2,col3 = st.columns(3)
        with col1:
            st.subheader("SELECT THE BRAND")
            brand_type = st.selectbox("search by", [""] + brands, 0)
        with col2:
            st.subheader("SELECT THE YEAR")
            select_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
        with col3:
            st.subheader("SELECT THE STATE")

            select_state = st.selectbox("State", states, 0)

        if brand_type:
            cursor.execute(f"SELECT State,Year,Quarter,user_device_brand,user_count,user_percentage FROM agg_users WHERE user_device_brand='{brand_type}' ORDER BY State,Year,Quarter,user_device_brand,user_count,user_percentage DESC")
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year', 'Quarter', 'user_device_brand', 'user_count', 'user_percentage'])
            with col1:
                st.write(df)
        if brand_type and select_year:
            cursor.execute(f"SELECT State,Year,Quarter,user_device_brand,user_count,user_percentage FROM agg_users WHERE Year='{select_year}' AND user_device_brand='{brand_type}' ORDER BY State,Year,Quarter,user_device_brand,user_count,user_percentage DESC")
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year', 'Quarter', 'user_device_brand', 'user_count', 'user_percentage'])
            with col2:
                st.write(df)
        if brand_type and select_year and select_state:
            cursor.execute(f"SELECT State,Year,Quarter,user_device_brand,user_count,user_percentage FROM agg_users WHERE State='{select_state}' AND Year='{select_year}' AND user_device_brand='{brand_type}' ORDER BY State,Year,Quarter,user_device_brand,user_count,user_percentage DESC")
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year', 'Quarter', 'user_device_brand', 'user_count', 'user_percentage'])
            with col3:
                st.write(df)



    if op_2=="Top users":
        cursor.execute("SELECT DISTINCT Year FROM top_users")
        years = [""] + [str(row[0]) for row in cursor.fetchall()]

        cursor.execute("SELECT DISTINCT State FROM top_users")
        states = [""] + [row[0] for row in cursor.fetchall()]

        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("SELECT THE STATE")
            select_state = st.selectbox("State", states, 0)
            if select_state:
                cursor.execute(f"SELECT State, Year, Quarter, District, Registered_Users FROM top_users WHERE State ='{select_state}' GROUP BY State, Year, Quarter")
                df = pd.DataFrame(cursor.fetchall(), columns=["State", "Year", "Quarter", "District", "Registered_Users"])
                st.write(df)
        with col2:
            st.subheader("SELECT THE YEAR")
            select_year = st.selectbox("Year", years, 0)
            if select_state and select_year:
                cursor.execute(f"SELECT State, Year, Quarter, District, Registered_Users FROM top_users WHERE State = '{select_state}' AND Year = '{select_year}' GROUP BY State, Year, Quarter")
                df = pd.DataFrame(cursor.fetchall(), columns=["State", "Year", "Quarter", "District", "Registered_Users"])
                st.write(df)
        with col3:
            st.subheader("SELECT THE QUARTER")
            select_quarter = st.selectbox("Quarter", ["", "1", "2", "3", "4"], 0)
            if select_state and select_year and select_quarter:
                cursor.execute(f"SELECT State, Year, Quarter, District, Registered_Users FROM top_users WHERE State = '{select_state}' AND Year = '{select_year}' AND Quarter = '{select_quarter}' GROUP BY State, Year, Quarter")
                df = pd.DataFrame(cursor.fetchall(), columns=["State", "Year", "Quarter", "District", "Registered_Users"])
                st.write(df)

if select=='Feedback':
    with st.container():
        st.write('---')
        st.subheader("Hope you enjoyed using this webpage!!!:thumbsup:")
        st.write("Please provide your valuable Feedback!!!:speech_balloon:")
        st.write("##")
        contact_form="""
        <form action="https://formsubmit.co/aswiniprabha22@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">      
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_column,right_column=st.columns(2)
        with left_column:
            st.markdown(contact_form,unsafe_allow_html=True)
        with right_column:
            st.caption("Made with ❤️ by @aswinitheaspiringDS")

if select=='Map':
    conn = sqlite3.connect('phonepaypulse.db')
    cursor = conn.cursor()
    query = '''
            SELECT State, Year, transaction_type,
            SUM(transaction_count) as transaction_count_total,
            SUM(transaction_amount) as transaction_amount_total
            FROM agg_tran
            GROUP BY State, Year, transaction_type
            '''
    results = pd.read_sql_query(query, conn)
    df =results
    mapping = {
	'andaman-&-nicobar-islands': 'Andaman & Nicobar Island',
	'arunachal-pradesh': 'Arunanchal Pradesh',
	'andhra-pradesh':'Andhra Pradesh',
	'assam': 'Assam',
	'bihar': 'Bihar',
	'chandigarh': 'Chandigarh',
	'chhattisgarh': 'Chhattisgarh',
	'dadra-&-nagar-haveli-&-daman-&-diu': 'Dadara & Nagar Havelli',
	'delhi': 'NCT of Delhi',
	'goa': 'Goa',
	'gujarat': 'Gujarat',
	'haryana': 'Haryana',
	'himachal-pradesh': 'Himachal Pradesh',
	'jammu-&-kashmir': 'Jammu & Kashmir',
	'jharkhand': 'Jharkhand',
	'karnataka': 'Karnataka',
	'kerala': 'Kerala',
	'lakshadweep': 'Lakshadweep',
	'ladakh' : 'Ladakh',
	'madhya-pradesh': 'Madhya Pradesh',
	'maharashtra': 'Maharashtra',
	'manipur': 'Manipur',
	'meghalaya': 'Meghalaya',
	'mizoram': 'Mizoram',
	'nagaland': 'Nagaland',
	'odisha': 'Odisha',
	'puducherry': 'Puducherry',
	'punjab': 'Punjab',
	'rajasthan': 'Rajasthan',
	'sikkim': 'Sikkim',
	'tamil-nadu': 'Tamil Nadu',
	'telangana': 'Telengana',
	'tripura': 'Tripura',
	'uttar-pradesh': 'Uttar Pradesh',
	'uttarakhand': 'Uttarakhand',
	'west-bengal': 'West Bengal'
        }

    df['state_mapped'] = df['State'].map(mapping)
    shapefile_path =r"C:\Users\Aswini Praba\Desktop\python\git\India-State-and-Country-Shapefile-Updated-Jan-2020-master\India-State-and-Country-Shapefile-Updated-Jan-2020-master\India_State_Boundary.shp"
    gdf =gpd.read_file(shapefile_path)
    merged_data = gdf.merge(df, left_on='State_Name', right_on='state_mapped', how='right')
    df=merged_data
    df_grouped = df.groupby('state_mapped').agg({
                'geometry': 'first',
                'transaction_count_total': 'sum',
                'transaction_amount_total': 'sum',
    
                }).reset_index()
    df=df_grouped    
    op_3=st.selectbox("",["Statewise transaction count","Statewise transaction amount"],0)

    if op_3=="Statewise transaction amount":
        fig = px.choropleth(
                df,
                geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                featureidkey='properties.ST_NM',
                locations='state_mapped',
                color='transaction_amount_total',
                color_continuous_scale='Oranges'
        )

        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig)
    if op_3=="Statewise transaction count":
        fig = px.choropleth(
                df,
                geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                featureidkey='properties.ST_NM',
                locations='state_mapped',
                color='transaction_count_total',
                color_continuous_scale='Greens'
        )

        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig)
        

        
        



    
