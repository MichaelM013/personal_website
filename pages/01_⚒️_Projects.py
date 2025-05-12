from pathlib import Path
import streamlit as st 


# Define the current directory
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

# Use relative paths to the files
css_file = current_dir.parent / 'styles' / 'main.css'
depot_analysis_file = current_dir.parent / 'assets' / 'depot_incident_analysis.pdf'
excel_analysis_file = current_dir.parent / 'assets' / 'excel_sales_analysis.pdf'
powerbi_dashboard_file = current_dir.parent / 'assets' / 'sales_performance_dashboard.pdf'
# --- GENERAL SETTINGS ---
PAGE_TITLE = "Projects | Michael Moore"
PAGE_ICON = "📚"


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD ASSETS ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(powerbi_dashboard_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# --- Projects & Accomplishments ---
st.header("Projects 🛠️")
st.write("---")

# --- Power BI Dashboard ---
st.subheader("1. 🛒 Sales Performance Dashboard (Power BI)")
st.download_button(
        label="Report: Sales Performance Dashboard",
        data=PDFbyte,
        file_name=powerbi_dashboard_file.name,
        mime="application/octet-stream",
    )
#st.write("This project involved analysing depot safety incident data from RSSB’s Safety Management Intelligence System (SMIS) using Python (pandas, numpy, matplotlib, scipy). The analysis applied the Fatalities and Weighted Injuries (FWI) Index to assess incident severity and identify patterns in workforce harm. By leveraging statistical methods and data visualisation, actionable insights were presented, contributing to the development of a new industry Standard aimed at improving safety protocols.")

# --------------- Applying justified text to improve readability
justified_text1 = """
<p style="text-align: justify;">
This project involved developing an interactive dashboard in Power BI to analyse order and delivery performance using a synthetic dataset. The dashboard tracks KPIs such as total sales, average order value, units sold, and delivery obligation compliance. It features dynamic filters for year, shipping mode, and product category, with visualisations including maps, bar charts, and ribbon plots. DAX measures were created to evaluate shipping performance by mode and customer segment. The project demonstrates skills in data modelling, DAX, and visual storytelling to support operational decision-making.
</p>
"""

st.markdown(justified_text1, unsafe_allow_html=True)
#####
st.markdown(f"<u><a href='https://github.com/MichaelM013/performance_sales_dashboard'>View Project Repository</a></u>", unsafe_allow_html=True)


st.write('\n')
st.write('\n')

with open(depot_analysis_file, "rb") as pdf_file:
    PythonPDFbyte = pdf_file.read()

# --- Depot Incident Analysis ---
st.subheader("2. 🛤️ Depot Incident Analysis (Python)")
st.download_button(
        label="Report: Depot Incident Analysis",
        data=PythonPDFbyte,
        file_name=depot_analysis_file.name,
        mime="application/octet-stream",
    )
#st.write("This project involved analysing depot safety incident data from RSSB’s Safety Management Intelligence System (SMIS) using Python (pandas, numpy, matplotlib, scipy). The analysis applied the Fatalities and Weighted Injuries (FWI) Index to assess incident severity and identify patterns in workforce harm. By leveraging statistical methods and data visualisation, actionable insights were presented, contributing to the development of a new industry Standard aimed at improving safety protocols.")

# --------------- Applying justified text to improve readability
justified_text1 = """
<p style="text-align: justify;">
This project involved analysing depot safety incident data from RSSB’s Safety Management Intelligence System (SMIS) using Python (pandas, numpy, matplotlib, scipy). 
The analysis applied the Fatalities and Weighted Injuries (FWI) Index to assess incident severity and identify patterns in workforce harm. 
By leveraging statistical methods and data visualisation, actionable insights were presented, contributing to the development of a new industry Standard aimed at improving safety protocols.
</p>
"""

st.markdown(justified_text1, unsafe_allow_html=True)
#####
st.markdown(f"<u><a href='https://github.com/MichaelM013/Depot-Exploratory-Analysis'>View Project Repository</a></u>", unsafe_allow_html=True)


st.write('\n')
st.write('\n')

# Open the Excel analysis PDF file
with open(excel_analysis_file, "rb") as pdf_file:
    ExcelPDFbyte = pdf_file.read()

st.subheader("3. 📊 Sales Exploratory Analysis (Excel)")
st.download_button(
        label="Report: Sales Exploratory Analysis",
        data=ExcelPDFbyte,
        file_name=excel_analysis_file.name,
        mime="application/octet-stream",
    )
#st.write("This project analyses a synthetic sales dataset spanning 2022 to 2024, focusing on transactions from 2023 to 2024. Using Microsoft Excel, including Pivot Tables, Charts, and formulas, the analysis identifies key patterns and insights. The main objectives were to evaluate sales rep performance, regional revenue differences, product category performance, the impact of discounts, and the profitability of online vs retail channels. The project showcases data cleaning, exploratory analysis, and the generation of actionable business insights.")

# --------------- Applying justified text to improve readability
justified_text2 = """
<p style="text-align: justify;">
This project analyses a synthetic sales dataset spanning 2022 to 2024, focusing on transactions from 2023 to 2024. 
Using Microsoft Excel, including Pivot Tables, Charts, and formulas, the analysis identifies key patterns and insights. 
The main objectives were to evaluate sales rep performance, regional revenue differences, product category performance, the impact of discounts, and the profitability of online vs retail channels. 
The project showcases data cleaning, exploratory analysis, and the generation of actionable business insights.
</p>
"""

st.markdown(justified_text2, unsafe_allow_html=True)
#
st.markdown(f"<u><a href='https://github.com/MichaelM013/excel_analysis_synthetic_sales'>View Project Repository</a></u>", unsafe_allow_html=True)  