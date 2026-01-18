import streamlit as st
import pandas as pd

from eac_utils import load_json, inject_global_css, top_nav, section_title, pill


links = load_json("links.json")
schedule = load_json("schedule.json")

inject_global_css()
top_nav(links)

section_title(
    "Programme & locations",
    "Timetable overview. Locations may be updated; if marked TBC please confirm on-site.",
)

# Build flat table
rows = []
for day in schedule:
    for it in day["items"]:
        rows.append(
            {
                "Date": day.get("day_label", ""),
                "Time": it.get("time", ""),
                "Session": it.get("title", ""),
                "Type": it.get("type", ""),
                "Audience": it.get("audience", ""),
                "Location": it.get("location", ""),
                "Note": it.get("note", ""),
            }
        )

df = pd.DataFrame(rows)

# Filters
c1, c2, c3 = st.columns([1, 1, 1])
with c1:
    day_opts = sorted(df["Date"].unique().tolist()) if not df.empty else []
    day_filter = st.multiselect("Day", options=day_opts, default=day_opts)
with c2:
    type_opts = sorted([t for t in df["Type"].unique().tolist() if t]) if not df.empty else []
    type_filter = st.multiselect("Type", options=type_opts, default=type_opts)
with c3:
    show_tbc_only = st.checkbox("Only items with TBC", value=False)

fdf = df.copy()
if day_filter:
    fdf = fdf[fdf["Date"].isin(day_filter)]
if type_filter:
    fdf = fdf[fdf["Type"].isin(type_filter)]
if show_tbc_only and not fdf.empty:
    fdf = fdf[
        fdf.apply(lambda r: "TBC" in (str(r["Location"]) + " " + str(r["Note"])), axis=1)
    ]

view_mode = st.radio("View", ["Cards", "Table"], horizontal=True)

if not day_filter:
    st.info("Select at least one day to view the programme.")
    st.stop()

if view_mode == "Table":
    st.dataframe(fdf, use_container_width=True, hide_index=True)
else:
    # Tabs help scanning by day (including on phones)
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

st.markdown("### Export")
st.download_button(
    "Download programme (CSV)",
    data=fdf.to_csv(index=False).encode("utf-8"),
    file_name="eac_convention_2026_programme.csv",
    mime="text/csv",
)
