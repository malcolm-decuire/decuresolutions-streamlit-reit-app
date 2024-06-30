
#s1- import dependencies
import streamlit as st
import pandas as pd
import plotly.express as px
import time
from session_state import SessionState

#s1a set up the page 
st.set_page_config(page_title="Real-Estate App", page_icon="🏡", layout="wide")
st.header("FINTECH REIT APP EXAMPLE")
st.markdown("##")

#s1b progress bar
loading_page = "Please Wait 🤲🏽"
progress_text =loading_page
my_bar = st.progress(0, text=progress_text)
for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(1)
my_bar.empty()


#s1c - info to user remember to leave double spaces after each line '''
st.title("💡 Reader Outcomes")
st.write("📌 Learn about REIT analysis")
st.write("📌 Learn how to deploy a python fintech app")
st.write("📌 Learn basic corporate finance")
st.write("📌 Learn how to deploy local repo to Streamlit Cloud")
st.subheader("❓Target Audience")
st.write("🏘️ Real Estate Enthusiasts  &  👨‍💻 Developers")

st.divider()

#s2 setup
st.header("🤔 How do I use this app?")
st.header("📝 Visit the Insights Pages")
st.subheader("✏️ Insights Page includes basic REIT analysis")
st.subheader("👉 Select a REITs Financial Statement (e.g. Income)")
st.caption("As of Dec-2023: limited functionality")
st.subheader("✓ Check Product Roadmap page for upcoming features")

st.divider()

st.subheader("⚠️ WARNING: EODHD.com's Format Only" )

#s2 Utilize the local excel file & link to the source of the data 
def main():
    uploaded_file = st.file_uploader("", type=["xlsx"])

    if uploaded_file is not None:
        eodhd_df = pd.read_excel(uploaded_file, sheet_name=None)
    else:
        # for cloud & local deployment use a default file path (update as needed)
        file_path = "EODHD-Annual-RE Fundamentals-Final-v2-clean.xlsx"
        eodhd_df = pd.read_excel(file_path, sheet_name=None)

    if eodhd_df:
        sheet_names = list(eodhd_df.keys())
        selected_sheet = st.selectbox("Select a sheet", sheet_names)

        # for cloud & local deployment display the selected sheet's data
        st.dataframe(eodhd_df[selected_sheet])

if __name__ == "__main__":
    main()

#s3b create next section on pg
st.divider()

#s4
#placeholder for media 

#s5a progress bar reload 
st.button("🔄 Reload")