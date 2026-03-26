import streamlit as st

# Քո PNG ֆայլի base64 string
icon_base64 = "iVBORw0KGgoAAAANSUhEUgAAAWgAAAHCCAYAAADCYlNdAAABfWlDQ1BpY2MAACiRfZE9SMNAHMVfU6VFKg52EBHJUDuIBVERR6liESyUtkKrDiaXfghNGpIUF0fBteDgx2LVwcVZVwdXQRD8AHFxdVJ0kRL/lxRaxHhw3I939x537wChUWGq2TUOqJplpBNxMZdfEQOvCGAYQYwiKjFTT2YWsvAcX/fw8fUuxrO8z/05epWCyQCfSDzLdMMiXiee3rR0zvvEYVaWFOJz4jGDLkj8yHXZ5TfOJYcFnhk2suk54jCxWOpguYNZ2VCJp4gjiqpRvpBzWeG8xVmt1FjrnvyFoYK2nOE6zSEksIgkUhAho4YNVGAhRqtGiok07cc9/IOOP0UumVwbYOSYRxUqJMcP/ge/uzWLkxNuUigOdL/Y9scIENgFmnXb/j627eYJ4H8GrrS2v9oAZj5Jr7e1yBHQtw1cXLc1eQ+43AEGnnTJkBzJT1Mo"  # truncate, ամբողջությամբ օգտագործիր

# Data URI
icon_data = f"data:image/png;base64,{icon_base64}"

# Streamlit page config
st.set_page_config(
    page_title="Okay Jeff App",
    page_icon=icon_data
)

st.title("Բարի գալուստ Okay Jeff հավելվածը!")
st.write("Այս հավելվածը ունի embed icon՝ base64-ով, չի կախված ֆայլի ուղուց։")
