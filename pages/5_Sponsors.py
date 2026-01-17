import streamlit as st
import pandas as pd

from utils import load_json, page_header


page_header("Sponsors & partnering", "High-level overview for delegates and potential partners.")

info = load_json("info.json")
sponsors = load_json("sponsors.json")

df = pd.DataFrame(sponsors)
df_display = df.copy()
df_display["Cost (EUR)"] = df_display["cost_eur"].apply(lambda x: "" if x is None else f"{int(x):,}")
df_display = df_display[["tier", "status", "quantity", "Cost (EUR)", "notes"]]
df_display.rename(columns={"tier":"Tier", "status":"Status", "quantity":"Availability", "notes":"Notes"}, inplace=True)

st.subheader("Partner packages (summary)")
st.dataframe(df_display, use_container_width=True, hide_index=True)

st.subheader("Partner benefits (selected)")
st.write("The information pack lists benefits such as programme adverts, website presence, banners, and mentions during sessions. Final inclusions should be confirmed in writing for each sponsor.")
st.write(f"For partnering enquiries: **{info['contact_email']}**")

st.subheader("Sponsor logos")
st.info("Place logo files in assets/ and reference them here once confirmed. For now, this section is intentionally empty to avoid publishing outdated sponsor lists.")
