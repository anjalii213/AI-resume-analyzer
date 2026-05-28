from utils import pdf_reader
import streamlit as st

from utils.pdf_reader import extract_text
from agents.ats_agent import ats_analysis
from agents.interview_agent import interview_question

st.set_page_config(page_title = "AI RESUME ANALYZER")
st.title("AI resume Analyzer")

upload_file = st.file_uploader(
    "Upload Resume",
    type = ["pdf"]
)

job_description = st.text_area(
    "Paste Job Description here."
)

if st.button("Analyze Resume"):
    if upload_file and job_description:
        with st.spinner("Analyzing your resume...."):
            resume_text = extract_text(upload_file)

            ats_result = ats_analysis(
                resume_text,
                job_description
            )

            interview_result = interview_question(
                resume_text,
                job_description
            )

            st.subheader("ATS ANALYSIS")
            st.write(ats_result)

            st.subheader("Interview Question")
            st.write(interview_result)