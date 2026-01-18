import streamlit as st

from eac_utils import load_json, inject_global_css, top_nav, section_title


info = load_json("info.json")
links = load_json("links.json")
partners = load_json("sponsors.json")

inject_global_css()
top_nav(links)

section_title("Partners", "Confirmed partner list for EAC Convention 2026.")

st.link_button("Official partners page", links["partners_page"])

st.write("")
cols = st.columns(2)
for i, row in enumerate(partners):
    tier = row.get("tier", "")
    names = row.get("partners", [])
    items = "<br>".join([f"• {n}" for n in names]) if names else ""
    with cols[i % 2]:
        st.markdown(
            f"<div class='eac-card'><h3>🤝 {tier}</h3><p>{items}</p></div>",
            unsafe_allow_html=True,
        )
        st.write("")

section_title("Partnering enquiries")
st.write(f"For partnering enquiries: **{info['contact_email']}**")
