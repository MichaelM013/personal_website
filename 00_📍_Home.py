from pathlib import Path
import streamlit as st 
from PIL import Image
import base64
from io import BytesIO


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Michael.Moore.CV.pdf"
profile_pic = current_dir / "assets" / "mm_logo.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Profile | Michael Moore"
PAGE_ICON = "👋🏿"
NAME = "Hi! My name is Michael Moore 👋🏿"
EMAIL = "michaeloymoore@outlook.com"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD ASSETS ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# Convert profile_pic to base64
def image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

encoded_img = image_to_base64(profile_pic)

# --- HERO SECTION ---
st.markdown(f"""
    <div style='text-align: center; margin-top: -30px;'>
        <h1>{NAME}</h1>
        <img src='data:image/png;base64,{encoded_img}' width='250' style='margin-top: 10px; border-radius: 50%; object-fit: cover;'/>
    </div>
""", unsafe_allow_html=True)

# Subtitle
st.write('\n')
st.write(f"""<div class="subtitle" style="text-align: center;">👨🏿‍💻 Data Analyst with 2.5 years of experience</div>""", unsafe_allow_html=True)
st.write('\n')

# --- Social Icons Data ---
social_icons_data = {
    "LinkedIn": ["https://www.linkedin.com/in/michaelmoore123", "https://cdn-icons-png.flaticon.com/512/174/174857.png"],
    "GitHub": ["https://github.com/MichaelM013", "https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg"]
}

# --- EMAIL + DOWNLOAD + SOCIAL LINKS ALL IN ONE ROW ---
col1, col2, col3 = st.columns([1, 1, 1])
# Left: Email Link
with col1:
    st.markdown(
        f"""
        <div style='text-align: left;'>
            <a href="mailto:{EMAIL}" style="font-size: 16px; text-decoration: none; color: #1f77b4;">
                📫 Email
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

# Center: Download Button
with col2:
    st.download_button(
        label="📄 Download My Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )

# Right: Social Text + Icons
with col3:
    social_icons_html = "".join([
        f"<a href='{link}' target='_blank' style='margin-left: 10px;'>"
        f"<img src='{icon}' alt='{platform}' width='25' style='border-radius: 5px;'/>"
        f"</a>"
        for platform, (link, icon) in social_icons_data.items()
    ])

    st.markdown(f"""
        <div style="text-align: right;">
            <span style="font-size: 16px; color: white; margin-right: 10px;">Social:</span>
            {social_icons_html}
        </div>
    """, unsafe_allow_html=True)

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ Proven ability to extract actionable insights from complex data, informing decision-making across diverse projects.
- ✔️ Strong proficiency in Python, SQL, and Excel for data manipulation, modeling, and visualisation (Power BI).
- ✔️ Solid understanding of statistical methodologies and their practical applications.
- ✔️ Demonstrated initiative in leading projects and collaborating to deliver impactful analytical solutions.
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Skills")
st.write(
    """
- 👨🏿‍💻 Programming: Python (Matplotlib, Seaborn, Pandas, Numpy), SQL, VBA
- 📊 Data Visualisation: Power BI, Microsoft Excel
- 🗄️ Databases: Postgres, MySQL
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🔮", "**Future Risk Modelling Analyst | RSSB**")
st.write("SEP 2024 - MAR 2025")
st.write(
    """
- ► Developed an accident cost model in Microsoft Excel that directly contributed to the project securing Gate 2 approval.
- ► Analysed and modeled large datasets to develop an novel method for parameterising accident features into cost estimates.
- ► Authored a Phase 1 cost model report outlining key findings and recommendations, supporting the project's future development and continuity.
"""
)

# --- JOB 2
st.write('\n')
st.write("💻", "**Data Analyst | RSSB**")
st.write("SEP 2023 - SEP 2024")
st.write(
    """
- ► Migrated existing reporting solutions for 20+ Train Operating Companies to Power BI, improving data accessibility.
- ► Significantly enhanced stakeholder adoption and proficiency with Power BI, contributing to minimal disruption in reporting workflows and earning a Net Promoter Score (NPS) of 10 from end-users.
- ► Streamlined time-series analysis for railway industry groups by automating manual Excel workflows in Python, reducing prep time and improving accuracy.
"""
)

# --- JOB 3
st.write('\n')
st.write("👷", "**Risk and Safety Intelligence Analyst | RSSB**")
st.write("SEP 2022 - SEP 2023")
st.write(
    """
- ► Lead analyst in the annual production of Common Safety Indicators (CSIs) for all Train Operating Companies across the GB Mainline. 
- ► Independently managed the data collection in SQL, analysis in Microsoft Excel, and reporting in Microsoft Excel, proactively identifying and resolving potential roadblocks. 
- ► Successfully delivered the final CSI product 4 weeks ahead of schedule, achieving compliance with transport systems safety regulations.
"""
)



