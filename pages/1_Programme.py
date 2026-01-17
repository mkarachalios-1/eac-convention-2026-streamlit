import streamlit as st
import pandas as pd

from utils import load_json, page_header, pill


info = load_json("info.json")
schedule = load_json("schedule.json")

page_header("Programme & locations", "Times are per the information pack; locations marked TBC should be finalised before publication.")

# Build flat table
rows = []
for day in schedule:
    for it in day["items"]:
        rows.append({
            "Date": day["day_label"],
            "Time": it.get("time",""),
            "Session": it.get("title",""),
            "Type": it.get("type",""),
            "Audience": it.get("audience",""),
            "Location": it.get("location",""),
            "Note": it.get("note",""),
        })

df = pd.DataFrame(rows)

# Filters
c1, c2, c3 = st.columns([1,1,1])
with c1:
    day_filter = st.multiselect("Filter by day", options=sorted(df["Date"].unique().tolist()), default=sorted(df["Date"].unique().tolist()))
with c2:
    type_filter = st.multiselect("Filter by type", options=sorted([t for t in df["Type"].unique().tolist() if t]), default=sorted([t for t in df["Type"].unique().tolist() if t]))
with c3:
    show_tbc_only = st.checkbox("Show only items with TBC", value=False)

fdf = df[df["Date"].isin(day_filter)]
if type_filter:
    fdf = fdf[fdf["Type"].isin(type_filter)]
if show_tbc_only:
    fdf = fdf[fdf.apply(lambda r: "TBC" in (str(r["Location"]) + " " + str(r["Note"])), axis=1)]

st.dataframe(fdf, use_container_width=True, hide_index=True)

st.markdown("### Location sanity checks")
st.write("• Confirm room allocations (and capacity) for all parallel workshops.")
st.write("• Confirm the exact area for the Welcome Reception and Exhibition.")
st.write("• Gala Dinner is listed at the Roof Garden Restaurant & Bar (hotel).")

st.markdown("### Export")
st.download_button(
    "Download programme (CSV)",
    data=fdf.to_csv(index=False).encode("utf-8"),
    file_name="eac_convention_2026_programme.csv",
    mime="text/csv",
)
