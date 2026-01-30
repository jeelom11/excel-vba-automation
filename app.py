"""Streamlit UI for N3 expected value calculations."""

from __future__ import annotations

import io

import pandas as pd
import streamlit as st

from n3.ev import Outcome, expected_value

st.set_page_config(page_title="N3 EV Calculator", page_icon="🎯", layout="centered")

st.title("N3 Expected Value Calculator")

st.markdown(
    """
Enter outcome data with three columns: `name`, `sales`, and `payout`.
Paste CSV data below, or keep the sample values to see the calculation.
"""
)

sample_csv = """name,sales,payout
777,100,10
700,50,5
701,25,2
"""

csv_text = st.text_area("Outcome data (CSV)", value=sample_csv, height=150)

try:
    data = pd.read_csv(io.StringIO(csv_text))
    outcomes = [
        Outcome(name=row["name"], sales=int(row["sales"]), payout=float(row["payout"]))
        for _, row in data.iterrows()
    ]
    ticket_cost = st.number_input("Ticket cost", min_value=0.0, value=1.0, step=0.1)
    ev = expected_value(outcomes, ticket_cost=ticket_cost)
    st.metric("Expected value", f"{ev:.4f}")
    st.dataframe(data, use_container_width=True)
except Exception as exc:  # noqa: BLE001 - surface parsing errors in UI
    st.error(f"Unable to parse the CSV data: {exc}")
