from src.pdf_reader import extract_text_from_pdf
from src.preprocess import preprocess_text
from src.ranking import rank_resume

import plotly.express as px
import tempfile
import pandas as pd

import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.main{
    background-color:#f8f9fa;
}

h1{
    color:#1565C0;
    text-align:center;
}

.metric-card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 0px 8px rgba(0,0,0,0.1);
}

.stButton>button{
    width:100%;
    height:55px;
    font-size:18px;
    font-weight:bold;
    background:#1565C0;
    color:white;
    border-radius:10px;
}

.stButton>button:hover{
    background:#0D47A1;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.title("📄 AI Resume Screening System")

st.caption(
    "AI Powered Resume Screening using NLP & Machine Learning"
)

st.divider()

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.header("📌 About")

    st.write("""
This system ranks resumes using

✅ NLP

✅ Machine Learning

✅ TF-IDF

✅ Cosine Similarity

Upload resumes and compare them with the Job Description.
""")

    st.divider()

    st.success("Developed using Streamlit")

# -----------------------------
# Dashboard Cards
# -----------------------------
c1,c2,c3,c4=st.columns(4)

with c1:
    st.metric(
        "📂 Total Resumes",
        "0"
    )

with c2:
    st.metric(
        "📈 Average Match",
        "0%"
    )

with c3:
    st.metric(
        "🏆 Best Match",
        "0%"
    )

with c4:
    st.metric(
        "🧠 Skills Found",
        "0"
    )

st.divider()

# -----------------------------
# Input Section
# -----------------------------
left,right=st.columns([2,1])

with left:

    st.subheader("📋 Job Description")

    job_description=st.text_area(
        "",
        height=300,
        placeholder="Paste Job Description Here..."
    )

with right:

    st.subheader("📂 Upload Resume(s)")

    uploaded_resumes=st.file_uploader(
        "",
        type=["pdf"],
        accept_multiple_files=True
    )

    st.info("Upload one or more PDF resumes.")

st.divider()

# -----------------------------
# Analyze Button
# -----------------------------
analyze=st.button("🔍 Analyze Resume")

if analyze:

    if not job_description:

        st.warning("Please enter Job Description.")

    elif not uploaded_resumes:

        st.warning("Please upload at least one Resume.")

    else:

        from src.pdf_reader import extract_text_from_pdf
        from src.preprocess import preprocess_text
        from src.ranking import rank_resume

        import pandas as pd

        with st.spinner("Analyzing resumes..."):

            jd = preprocess_text(job_description)

            results = []

            progress = st.progress(0)

            total = len(uploaded_resumes)

            for i, resume in enumerate(uploaded_resumes):

                resume_text = extract_text_from_pdf(resume)

                resume_text = preprocess_text(resume_text)

                score = rank_resume(jd, resume_text)

                results.append({

                    "Resume Name": resume.name,
                    "Match Score (%)": score

                })

                progress.progress((i + 1) / total)

            df = pd.DataFrame(results)

            df = df.sort_values(
                by="Match Score (%)",
                ascending=False
            )

        st.success("Analysis Completed Successfully!")

        # -----------------------------
        # Dashboard Metrics
        # -----------------------------
        
        total_resumes = len(df)
        average_score = round(df["Match Score (%)"].mean(), 2)
        best_score = round(df["Match Score (%)"].max(), 2)
        best_resume = df.iloc[0]["Resume Name"]

        st.divider()

        st.subheader("📊 Dashboard")

        m1, m2, m3 = st.columns(3)

        with m1:
            st.metric(
                "📂 Total Resumes",
                total_resumes
            )

        with m2:
            st.metric(
                "📈 Average Match",
                f"{average_score}%"
            )

        with m3:
            st.metric(
                "🏆 Best Match",
                f"{best_score}%"
            )

        st.divider()

        # -----------------------------
        # Match Score Chart
        # -----------------------------

        st.subheader("📈 Resume Match Scores")

        fig = px.bar(
            df,
            x="Resume Name",
            y="Match Score (%)",
            text="Match Score (%)",
            title="Resume Ranking"
        )

        fig.update_traces(textposition="outside")

        fig.update_layout(
            xaxis_title="Resume",
            yaxis_title="Match Score (%)",
            height=500
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.divider()

        # -----------------------------
        # Top Candidate
        # -----------------------------

        st.subheader("🏆 Best Candidate")

        best = df.iloc[0]

        st.success(
            f"""
            Best Resume

        📄 {best['Resume Name']}

        🎯 Match Score : {best['Match Score (%)']}%
        """
        )

        st.divider()

        # -----------------------------
        # Ranking Table
        # -----------------------------

        st.subheader("📋 Resume Ranking")

        df.index = df.index + 1

        st.dataframe(
            df,
            use_container_width=True
        )

        st.divider()

        # -----------------------------
        # Download Report
        # -----------------------------

        csv = df.to_csv(index=False)

        st.download_button(
            label="📥 Download CSV Report",
            data=csv,
            file_name="resume_ranking.csv",
            mime="text/csv"
        )