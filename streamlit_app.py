import streamlit as st

# Inject custom CSS to make the slider blue
st.markdown(
    """
    <style>
    .stSlider > div[data-testid="stSlider"] > div {
        background: linear-gradient(90deg, #3498db 0%, #3498db 100%);
    }
    .stSlider .rc-slider-track {
        background-color: #3498db !important;
    }
    .stSlider .rc-slider-handle {
        border: 2px solid #3498db !important;
        background: #3498db !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("My First Streamlit App")

st.header("Slider Example")
x = st.slider("Select a value")
st.write(x, "squared is", x * x)
