import streamlit as st
import pandas as pd

st.title("Data Aggregators")

sidebar = st.sidebar.selectbox( label="Navigation", options=("NEWS RSS", "TWITTER"))

if sidebar  == "NEWS RSS":
    st.markdown("---")
    st.subheader("Explore Data With Filters")

    df = pd.read_csv("./rss-index.csv")
    df.rename(columns={"description": "text"}, inplace=True)
    df = df[df['link'].str.contains("mckinsey")].reset_index(drop=True)


    rows : list[int] = st.multiselect('Row', (i for i in range(len(df))))
    cols : list[str] = st.multiselect('Columns', (col for col in df.columns))

    df.loc[rows][cols]



    st.markdown("---")
    st.subheader("Raw Data")
    df

else:
    st.markdown("---")
    st.subheader("Explore Data With Filters")

    df = pd.read_csv("./twitter-index.csv")

    rows : list[int] = st.multiselect('Row', (i for i in range(len(df))))
    cols : list[str] = st.multiselect('Columns', (col for col in df.columns))

    df.loc[rows][cols]



    st.markdown("---")
    st.subheader("Raw Data")
    df
