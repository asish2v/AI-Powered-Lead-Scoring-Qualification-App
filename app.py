import streamlit as st
import pandas as pd
from lead_scoring import score_lead, confidence_level, estimate_revenue, verify_email

st.set_page_config(page_title="Lead Scoring Tool", layout="wide")
st.title("🔍 Smart Lead Scoring & Filtering Tool")

uploaded_file = st.file_uploader("Upload Lead CSV File", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Score and enrich leads
    df['lead_score'] = df.apply(score_lead, axis=1)
    df['confidence'] = df['lead_score'].apply(confidence_level)
    df['estimated_revenue'] = df.apply(estimate_revenue, axis=1)
    df['email_validity'] = df['email'].apply(verify_email)

    # Sidebar filters
    st.sidebar.header("📊 Filters")
    job_filter = st.sidebar.multiselect("Filter by Job Title", options=df['job_title'].unique())
    location_filter = st.sidebar.multiselect("Filter by Location", options=df['location'].unique())
    search = st.sidebar.text_input("🔎 Search Job Title / Company")

    # Apply filters
    filtered_df = df.copy()
    if job_filter:
        filtered_df = filtered_df[filtered_df['job_title'].isin(job_filter)]
    if location_filter:
        filtered_df = filtered_df[filtered_df['location'].isin(location_filter)]
    if search:
        filtered_df = filtered_df[
            filtered_df['job_title'].str.contains(search, case=False, na=False) |
            filtered_df['company'].str.contains(search, case=False, na=False)
        ]

    # Display table
    st.write("### 🧠 Scored Leads with Confidence & Revenue Estimate")
    st.dataframe(filtered_df.sort_values(by='lead_score', ascending=False))

    # CSV download
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button("⬇️ Download Filtered Leads", csv, "filtered_leads.csv", "text/csv")

    # Mock Google Sheets export
    if st.button("📤 Send to Google Sheets (Mock)"):
        st.success("✔️ Leads sent to Google Sheets (simulated)")
else:
    st.info("Please upload a CSV file to begin.")
