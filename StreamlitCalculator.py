# File: StreamlitCalculator.py  (or calculator.py)
import streamlit as st

# ───────────────────────────────────────────────
# Custom CSS for responsive calculator design
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

    /* Special button colors */
    .operator { background-color: #ff9500 !important; color: white !important; }
    .clear    { background-color: #ff3b30 !important; color: white !important; }
    .equals   { background-color: #34c759 !important; color: white !important; font-size: 1.6rem !important; }

    /* Responsive adjustments for smaller screens */
    @media (max-width: 640px) {
        .calculator-display {
            font-size: 2.2rem !important;
            padding: 0.8rem !important;
            min-height: 70px !important;
        }
        .stButton > button {
            height: 65px !important;
            font-size: 1.3rem !important;
        }
    }
    </style>
""", unsafe_allow_html=True)

# ───────────────────────────────────────────────
# App title and layout
# ───────────────────────────────────────────────
st.title("🧮 Calculator")

# Initialize session state for display
if 'display' not in st.session_state:
    st.session_state.display = "0"
if 'previous' not in st.session_state:
    st.session_state.previous = ""
if 'operator' not in st.session_state:
    st.session_state.operator = None
if 'new_input' not in st.session_state:
    st.session_state.new_input = True

# Display area
st.markdown(f'<div class="calculator-display">{st.session_state.display}</div>', unsafe_allow_html=True)

# ───────────────────────────────────────────────
# Button layout (4 columns)
# ───────────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)

def button_click(value, is_operator=False, is_clear=False, is_equals=False):
    if is_clear:
        st.session_state.display = "0"
        st.session_state.previous = ""
        st.session_state.operator = None
        st.session_state.new_input = True
        return

    if is_equals:
        if st.session_state.operator and st.session_state.previous:
            try:
                result = eval(f"{st.session_state.previous} {st.session_state.operator} {st.session_state.display}")
                st.session_state.display = str(result) if result % 1 != 0 else str(int(result))
            except:
                st.session_state.display = "Error"
            st.session_state.operator = None
            st.session_state.previous = ""
            st.session_state.new_input = True
        return

    if is_operator:
        if st.session_state.display != "Error":
            st.session_state.previous = st.session_state.display
            st.session_state.operator = value
            st.session_state.new_input = True
        return

    # Number or decimal input
    if st.session_state.new_input or st.session_state.display == "0" or st.session_state.display == "Error":
        st.session_state.display = value
        st.session_state.new_input = False
    else:
        if value == "." and "." in st.session_state.display:
            return  # prevent multiple dots
        st.session_state.display += value

# Row 1
with col1:
    if st.button("C", key="clear", on_click=button_click, args=("C", False, True)):
        pass
with col2:
    if st.button("(", key="("):
        button_click("(")
with col3:
    if st.button(")", key=")"):
        button_click(")")
with col4:
    if st.button("÷", key="/", on_click=button_click, args=("/", True)):
        pass

# Row 2
with col1:
    if st.button("7", key="7", on_click=button_click, args=("7",)):
        pass
with col2:
    if st.button("8", key="8", on_click=button_click, args=("8",)):
        pass
with col3:
    if st.button("9", key="9", on_click=button_click, args=("9",)):
        pass
with col4:
    if st.button("×", key="*", on_click=button_click, args=("*", True)):
        pass

# Row 3
with col1:
    if st.button("4", key="4", on_click=button_click, args=("4",)):
        pass
with col2:
    if st.button("5", key="5", on_click=button_click, args=("5",)):
        pass
with col3:
    if st.button("6", key="6", on_click=button_click, args=("6",)):
        pass
with col4:
    if st.button("−", key="-", on_click=button_click, args=("-", True)):
        pass

# Row 4
with col1:
    if st.button("1", key="1", on_click=button_click, args=("1",)):
        pass
with col2:
    if st.button("2", key="2", on_click=button_click, args=("2",)):
        pass
with col3:
    if st.button("3", key="3", on_click=button_click, args=("3",)):
        pass
with col4:
    if st.button("+", key="+", on_click=button_click, args=("+", True)):
        pass

# Row 5
with col1:
    if st.button("0", key="0", on_click=button_click, args=("0",)):
        pass
with col2:
    if st.button(".", key=".", on_click=button_click, args=(".",)):
        pass
with col3:
    if st.button("=", key="equals", on_click=button_click, args=("", False, False, True)):
        pass
with col4:
    pass  # empty for layout balance

# Optional: small footer
st.caption("Simple responsive calculator built with Streamlit")
