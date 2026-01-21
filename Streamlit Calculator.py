# File: calculator.py
import streamlit as st

# ───────────────────────────────────────────────
# Custom CSS for responsive design
# ───────────────────────────────────────────────
st.markdown("""
    <style>
    /* Main container adjustments */
    .stApp {
        max-width: 100%;
        padding: 1rem;
    }

    /* Display screen */
    .calculator-display {
        background-color: #2e2e2e;
        color: white;
        font-family: Arial, sans-serif;
        font-size: 2.8rem;
        padding: 1rem;
        text-align: right;
        border-radius: 12px;
        min-height: 80px;
        margin-bottom: 1rem;
        overflow-wrap: break-word;
        word-break: break-all;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }

    /* Buttons */
    .stButton > button {
        width: 100% !important;
        height: 70px !important;
        font-size: 1.4rem !important;
        font-weight: bold;
        border-radius: 12px !important;
        margin: 0.3rem 0 !important;
        padding: 0.5rem !important;
        transition: all 0.2s;
    }

    .stButton > button:hover {
        filter: brightness(1.15);
    }

    /* Special buttons styling */
    .operator { background-color: #ff9500 !important; color: white !important; }
    .clear { background-color: #ff3b30 !important; color: white !important; }
    .equals { background-color: #34c759 !important; color: white !important; font-size: 1.6rem !important; }

    /* Responsive adjustments */
    @media (max-width: 640px) {
        .calculator-display {
            font-size: 2.2rem !important;
            padding: 0.8rem !important;
            min-height: 70px !important;
        }
        .stButton > button {
            height: 65px !important;
            font-size: 1.