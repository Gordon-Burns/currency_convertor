import streamlit as st
from functions import get_available_currencies, query

st.set_page_config(layout="wide")
st.title("Currency Convertor")
col1, col2 = st.columns(2)

Currency_list = get_available_currencies()
with col1:
    selected_option_base = st.selectbox('Choose your base currency:', Currency_list)
    amount_to_convert = st.text_area("Enter amount to change")
with col2:
    selected_option_target = st.selectbox('Choose your target currency:', Currency_list)


button = st.button("Submit")
if button:
    rate = query(selected_option_base,selected_option_target)
    result = float(amount_to_convert) * float(rate)
    st.write(f"Currently 1 {selected_option_base} is worth {rate} {selected_option_target}")
    st.write(f"{amount_to_convert} {selected_option_base} = {result} {selected_option_target}")
