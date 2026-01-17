import streamlit as st
import pandas as pd

from eac_utils import load_json, inject_global_css, top_nav, section_title, card


info = load_json("info.json")
links = load_json("links.json")
sponsors = load_json("sponsors.json")

inject_global_css()
top_nav(links)

section_title("Partners & sponsors", "Official partner list is maintained on the EAC website; package summaries below are indicative.")

def fmt_eur(x):
    if x is None or x == "":
        return ""
    return f"€{int(x):,}"

st.link_button("View 2026 partners (official EAC site)", links["partners_page"])
st.markdown(
    "<div class='eac-card'><p>If your organisation is already a partner/sponsor, please confirm logo and preferred description so we can publish accurately.</p></div>",
    unsafe_allow_html=True,
)

st.markdown("---")

section_title("Partner packages", "Quick scan cards (mobile-first) + table for reference.")
df = pd.DataFrame(sponsors)

cols = st.columns(2)
for i, row in enumerate(df.to_dict(orient="records")):
    cost = fmt_eur(row.get("cost_eur"))
    cost_txt = f" • {cost}" if cost else ""
    with cols[i % 2]:
        card(
            row.get("tier", ""),
            f"Status: <strong>{row.get('status','')}</strong> • Availability: {row.get('quantity','')}{cost_txt}<br><small>{row.get('notes','')}</small>",
            icon="🤝",
        )
        st.write("")

with st.expander("Show as table (reference)", expanded=False):
    df_display = df.copy()
    df_display["Cost"] = df_display["cost_eur"].apply(fmt_eur)
    df_display = df_display[["tier", "status", "quantity", "Cost", "notes"]]
    df_display.rename(columns={"tier": "Tier", "status": "Status", "quantity": "Availability", "notes": "Notes"}, inplace=True)
    st.dataframe(df_display, use_container_width=True, hide_index=True)

section_title("Partnering enquiries")
st.write(f"For partnering enquiries: **{info['contact_email']}**")

st.info("To update packages or add sponsor profiles, edit data/sponsors.json.")
