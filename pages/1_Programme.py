import streamlit as st
import pandas as pd

from eac_utils import load_json, inject_global_css, top_nav, section_title, pill


links = load_json("links.json")
schedule = load_json("schedule.json")

inject_global_css()
top_nav(links)

section_title(
    "Programme & locations",
    "Built for mobile: day tabs + searchable list. Locations marked TBC should be finalised before publication.",
)

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

view_mode = st.radio("View", ["Cards (mobile-first)", "Table"], horizontal=True)

if not day_filter:
    st.info("Select at least one day to view the programme.")
    st.stop()

if view_mode == "Table":
    st.dataframe(fdf, use_container_width=True, hide_index=True)
else:
    # Day tabs are easier to scan on mobile
    tabs = st.tabs(day_filter)
    for tab_day, tab in zip(day_filter, tabs):
        with tab:
            day_items = fdf[fdf["Date"] == tab_day].copy()
            if day_items.empty:
                st.info("No sessions match the selected filters.")
                continue
            for _, r in day_items.iterrows():
                with st.container(border=True):
                    st.markdown(
                        f"{pill(r['Time'])} {pill(r['Type'])} {pill(r['Audience'])}",
                        unsafe_allow_html=True,
                    )
                    st.markdown(f"**{r['Session']}**")
                    st.write(f"📍 {r['Location']}")
                    if str(r.get("Note", "")).strip():
                        st.caption(str(r.get("Note", "")))

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
