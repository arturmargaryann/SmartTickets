import streamlit as st

# Քո PNG-ի ամբողջական base64 string
icon_base64 = (
    "iVBORw0KGgoAAAANSUhEUgAAAWgAAAHCCAYAAADCYlNdAAABfWlDQ1BpY2MAACiRfZE9SMNA"
    "HMVfU6VFKg52EBHJUDuIBVERR6liESyUtkKrDiaXfghNGpIUF0fBteDgx2LVwcVZVwdXQRD8A"
    "HFxdVJ0kRL/lxRaxHhw3I939x537wChUWGq2TUOqJplpBNxMZdfEQOvCGAYQYwiKjFTT2YWsv"
    "AcX/fw8fUuxrO8z/05epWCyQCfSDzLdMMiXiee3rR0zvvEYVaWFOJz4jGDLkj8yHXZ5TfOJYcF"
    "nhk2suk54jCxWOpguYNZ2VCJp4gjiqpRvpBzWeG8xVmt1FjrnvyFoYK2nOE6zSEksIgkUhAho4"
    "YNVGAhRqtGiok07cc9/IOOP0UumVwbYOSYRxUqJMcP/ge/uzWLkxNuUigOdL/Y9scIENgFmnXb"
    "/j627eYJ4H8GrrS2v9oAZj5Jr7e1yBHQtw1cXLc1eQ+43AEGnnTJkBzJT1Mo"
    # Եթե base64-ը ամբողջությամբ օգտագործելուց հետո ավելորդ տեղ է, պարզապես փոխիր truncated հատվածը ամբողջ string-ով
)

icon_data = f"data:image/png;base64,{icon_base64}"

# Streamlit configuration
st.set_page_config(
    page_title="Okay Jeff App",
    page_icon=icon_data
)

st.title("Բարի գալուստ Okay Jeff հավելվածը!")
st.write("Այս հավելվածը ունի embed icon՝ base64-ով, չի կախված ֆայլի ուղուց։")
