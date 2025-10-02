import streamlit as st
import pandas as pd
import plotly.express as px

users = {
    "carlos@bhland.com": {"password": "Lamassu1", "client": "BHLAND"},
    "victor@ball.com": {"password": "Lamassu1", "client": "BALL"},
    "santi@venturefour.com": {"password": "Lamassu1", "client": "VENTUREFOUR"},
    "carlos@gregginvestment.com": {"password": "Lamassu1", "client": "GREGGINVESTMENTS"}
}

st.title("📊 Call Center Dashboard")

# Login form

dfs = pd.read_csv("camp_sum.csv")
username = st.text_input("Username")
password = st.text_input("Password", type="password")
login_btn = st.button("Login")



if login_btn:
    if username in users and users[username]["password"] == password:
        st.success(f"Welcome {username}!")
        client = users[username]["client"]

        # -------------------------
        # Example Data (replace with your real data)
        # -------------------------

        # Filter by logged-in client
        df_client = dfs[dfs["client"] == client]

        # -------------------------
        # Tabs
        # -------------------------
        tab1, tab2 = st.tabs(["📞 Dials", "🎯 Leads"])

        with tab1:
            st.subheader(f"Total Dials for {client}")
            fig1 = px.bar(df_client, x='w_year', y='Calls', title='Calls Evolution')
            st.plotly_chart(fig1, use_container_width=True)

            st.subheader(f"Contacted Percentaje for {client}")
            fig2 = px.bar(df_client, x='w_year', y='Contacted Percentaje', title='Contacted Calls')
            st.plotly_chart(fig2, use_container_width=True)

        with tab2:
            st.subheader(f"Total Leads for {client}")
            fig3 = px.bar(df_client, x='w_year', y='Contacted Percentaje', title='Dials')
            st.plotly_chart(fig3, use_container_width=True)
            st.dataframe(df_client.head())
    else:
        st.error("Invalid username or password ❌")
