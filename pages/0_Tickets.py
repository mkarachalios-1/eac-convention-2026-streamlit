import streamlit as st
import pandas as pd

from eac_utils import load_json, inject_global_css, top_nav, section_title, card


links = load_json("links.json")
tickets = load_json("tickets.json")

inject_global_css()
top_nav(links)

section_title("Tickets & registration", "Use the official booking portal for live prices, availability and workshop rules.")

c1, c2, c3 = st.columns([1, 1, 1])
with c1:
    st.link_button("Book / register", links["register_page"])
with c2:
    st.link_button("Event details", links["event_details"])
with c3:
    st.link_button("Hotel booking (EAC 2026 rate)", links["hotel_booking_portal"])

st.write("")
section_title("Ticket types", "Tap a card, then use the portal to complete registration.")

df = pd.DataFrame(tickets)

headline = df[df["ticket_type"].isin(["Full Delegate", "Delegate Guest"])].copy()
c1, c2, c3 = st.columns([1, 1, 1])
if len(headline) >= 2:
    fd, dg = headline.iloc[0], headline.iloc[1]
    with c1:
        card("Full Delegate", f"€{int(fd['price_eur']):,} • {fd['includes']}", icon="🎟")
    with c2:
        card("Delegate Guest", f"€{int(dg['price_eur']):,} • {dg['includes']}", icon="🥂")
    with c3:
        st.markdown(
            "<div class='eac-card'><h3>🧭 How to book</h3>"
            "<p>Register and pay via the official portal. If anything here conflicts with the portal, trust the portal.</p>"
            "</div>",
            unsafe_allow_html=True,
        )
else:
    st.info("Ticket data not found. Update data/tickets.json.")

st.write("")
section_title("Full list (reference)", "This table is convenient for review; the cards above are optimised for mobile.")
df_disp = df[["ticket_type", "includes", "price_eur", "notes"]].copy()
df_disp.rename(
    columns={
        "ticket_type": "Ticket type",
        "includes": "Includes",
        "price_eur": "Price (EUR)",
        "notes": "Notes",
    },
    inplace=True,
)

df_disp["Price (EUR)"] = df_disp["Price (EUR)"].apply(lambda x: "" if x in (None, "") else f"€{int(x):,}")

st.dataframe(df_disp, use_container_width=True, hide_index=True)

st.warning(
    "Prices and availability can change. Exhibition space and some workshops may be add-ons and/or limited. "
    "Always confirm on the official portal before publishing pricing externally."
)
