import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
#from st_aggrid import AgGrid, JsCode
#from st_aggrid.grid_options_builder import GridOptionsBuilder

nav = st.sidebar.radio("Navigation",["Constituencies","Opinion Poll"])

tab_titles =["HACHHEK", "DAMPA", "MAMIT", "Tuirial", "Kolasib", "Serlui", "Tuivawl", "Chalfilh",
             "Ṭawi", "Aizawl N-I", "Aizawl N-II", "Aizawl N-III", "Aizawl E-I", "Aizawl E-II",
             "Aizawl W-I", "Aizawl W-II", "Aizawl W-III", "Aizawl S-I", "Aizawl S-II", "Aizawl S-III",
             "Lengteng", "Tuichang", "Champhai N", "Champhai S", "E Tuipui", "Serchhip", "Tuikum",
             "Hrangturzo", "S Tuipui", "Lunglei N", "Lunglei E", "Lunglei W", "Lunglei S", "Thorang",
             "W Tuipui", "Tuichawng", "Lawngtlai W", "Lawngtlai E", "Siaha", "Palak"
             ]

tabs = st.tabs(tab_titles)

for i in range(39):
    with tabs[i]:
        No = [i + 1]
        st.title(tab_titles[i]+" :red[_Constituency_]")
        df_candidates = pd.read_excel(io = '/workspaces/mizoram2023/data/candidates.xlsx',
                                      engine='openpyxl', sheet_name='Sheet2', usecols='A:F')

        df_waves = pd.read_excel(io='/workspaces/mizoram2023/data/candidates.xlsx',
                                      engine='openpyxl',sheet_name='Sheet3', usecols='A:D')

        hachhek=df_candidates["ID"].isin(No)
        waves = df_waves["ID"].isin(No)

        df_1 = df_candidates[hachhek]
        df_2 = df_waves[waves]


        col1, col2  = st.columns (2)
        with col1:
            st.subheader ("_Party & Their Candidates_", divider="rainbow")
            #khua_list = df_2["Khua"].tolist()
            candidate_list = df_1["CANDIDATES"].tolist()
            #st.write(candidate_list)

            cola, colb, colc = st.columns([1.1,0.8,3])
            with cola:
                st.write("Symbol")
                st.image("/workspaces/mizoram2023/data/MNF_flag_2.jpg", width = 60)
                st.image("/workspaces/mizoram2023/data/INC_flag.jpeg", width = 60)
                st.image("/workspaces/mizoram2023/data/ZPM_flag.jpeg", width = 60)
                st.image("/workspaces/mizoram2023/data/BJP_flag.png", width = 60)
            with colb:
                st.write("Party")
                st.write("")
                st.write("MNF")
                st.write("")
                st.write("INC")
                st.write("")
                st.write("ZPM")
                st.write("")
                st.write("BJP")

            with colc:
                st.write("Name of Candidate")
                st.write("")
                st.write(candidate_list[0])
                st.write("")
                st.write(candidate_list[1])
                st.write("")
                st.write(candidate_list[2])
                st.write("")
                st.write(candidate_list[3])

        with col2:
            st.subheader(":orange[Winning] :blue[Probability]", divider="rainbow")
            fig = px.pie(df_1,values="Winning Probability", names="Party - Candidate", hole=0.3,
                     hover_name="Party - Candidate", color="PARTY",
                     color_discrete_map={"MNF":"dodgerblue","INC":"green","ZPM":"yellow","BJP":"orange"})
            fig.update_layout(showlegend=False,
            width=250, height=250, margin=dict(l=1,r=2,b=1,t=1), font=dict(size=15)
            )
            col2.write(fig)

        #st.write(df_2)
        st.subheader(":red[Candidate Campaign Waves]",divider="rainbow")
        #st.line_chart(df_2,x="Month",y=["Wave_Score"],color="Party")
        st.area_chart(df_2,x="Month",y="Wave_Score",color= "Party", width = 700, height = 500, use_container_width=True)
                      #color_discrete_map={"MNF": "dodgerblue", "INC": "green", "ZPM": "yellow", "BJP": "orange"})
                      #color_discrete_map=["#1E90FF","#008000","#FFFF00","#FFA500"])






