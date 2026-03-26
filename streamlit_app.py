import streamlit as st

# Ձեր icon ֆայլի ուղին
icon_path = "Okay_jeef.png"  # կամ "icon.ico"

# Page config, սա միշտ առաջինը պետք է լինի
st.set_page_config(
    page_title="Իմ հավելվածը",
    page_icon=icon_path
)

st.title("Բարի գալուստ իմ հավելվածը!")
