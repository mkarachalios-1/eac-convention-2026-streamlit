import streamlit as st
from pathlib import Path

from utils import load_json, inject_global_css, top_nav, section_title


links = load_json("links.json")

inject_global_css()
top_nav(links)

section_title("Safety (Barker) & downloads", "Confirm distribution permissions before wide sharing.")

DOWNLOADS = Path(__file__).resolve().parents[1] / "downloads"

def download_button(label: str, filename: str, mime: str):
    path = DOWNLOADS / filename
    if not path.exists():
        st.warning(f"Missing file: {filename}")
        return
    with open(path, "rb") as f:
        st.download_button(label, data=f, file_name=filename, mime=mime)

st.subheader("Barker database")
download_button(
    "Download: Airshow Accident Database (Excel)",
    "Airshow Accident Database_11-8-2025.xlsx",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
)

st.subheader("Barker reports (PDF)")
download_button("Download: Des Barker Report 2024 (PDF)", "Des Barker Report 2024.pdf", "application/pdf")
download_button("Download: Des Barker Report 2023 (PDF)", "Des Barker Report 2023.pdf", "application/pdf")
download_button("Download: Des Barker Report 2022 (PDF)", "Des Barker Report 2022.pdf", "application/pdf")

st.subheader("Safety indicators (Excel)")
download_button(
    "Download: 2024 Safety Indicators and Rates (Excel)",
    "2024 Barker report- Safety Indicators and Rates_v1.xlsx",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
)

st.info("If you prefer not to store files in GitHub, host them on an official EAC location and replace these buttons with links.")
