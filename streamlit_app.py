import streamlit as st

# Հետաքրքիր բարի գալուստ
st.title("SmartTickets App")
st.header("Բարև, օգտվող 🌟")

# Input դաշտ
name = st.text_input("Գրի քո անունը՝")
if name:
    st.write(f"Բարև, {name}! Բարի գալուստ SmartTickets- ին 👋")

# Բազմընտրանքային ընտրություն
ticket_type = st.selectbox(
    "Ընտրիր տոմսի տեսակը", 
    ["Կոնցերտ", "Թատրոն", "Սպորտ"]
)
st.write(f"Դու ընտրեցիր {ticket_type} տոմսը 🎟️")

# Բազային կոճակ
if st.button("Գնել տոմս"):
    st.success(f"Շնորհավորում ենք, {name}! Գնել ես {ticket_type} տոմսը ✅")
