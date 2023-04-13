import streamlit as st
import regex
from utility1 import Dict

st.set_page_config(
    page_title="Dictionary"
)

st.title("English - Chinese Dictionary")

userinput = st.text_input(" ", "")

if userinput and not userinput.isspace():

    Dict = Dict(userinput.lower())
    temp_dict = Dict.user_dict()

    if len(temp_dict) > 20:
        st.write(f"Found {len(temp_dict)} words, showing the first 20")
    else:
        st.write(f"Found {len(temp_dict)} word(s)")
    en = " "
    en_type = " "
    cn = " "

    with st.expander('', expanded=True):
        col1, col2, col3, col4 = st.columns(4)

        for i in temp_dict:
            with col1:
                if 0 < i <= 5:
                    if regex.search(r'\p{Han}', userinput):
                        click = st.button(temp_dict[i]["cn"], key=i)
                    else:
                        click = st.button(temp_dict[i]["en"], key=i)

                    if click:
                        en = temp_dict[i]["en"]
                        en_type = temp_dict[i]["type"],
                        cn = temp_dict[i]["cn"]

            with col2:
                if 5 < i <= 10:
                    if regex.search(r'\p{Han}', userinput):
                        click = st.button(temp_dict[i]["cn"], key=i)
                    else:
                        click = st.button(temp_dict[i]["en"], key=i)

                    if click:
                        en = temp_dict[i]["en"]
                        en_type = temp_dict[i]["type"],
                        cn = temp_dict[i]["cn"]

            with col3:
                if 10 < i <= 15:
                    if regex.search(r'\p{Han}', userinput):
                        click = st.button(temp_dict[i]["cn"], key=i)
                    else:
                        click = st.button(temp_dict[i]["en"], key=i)

                    if click:
                        en = temp_dict[i]["en"]
                        en_type = temp_dict[i]["type"],
                        cn = temp_dict[i]["cn"]

            with col4:
                if 15 < i <= 20:
                    if regex.search(r'\p{Han}', userinput):
                        click = st.button(temp_dict[i]["cn"], key=i)
                    else:
                        click = st.button(temp_dict[i]["en"], key=i)

                    if click:
                        en = temp_dict[i]["en"]
                        en_type = temp_dict[i]["type"],
                        cn = temp_dict[i]["cn"]

    if not en.isspace():
        if regex.search(r'\p{Han}', userinput):
            st.write(f"Word selected: {cn}")
        else:
            st.write(f"Word selected: {en}")

    col5, col6, col7 = st.columns(3)

    if regex.search(r'\p{Han}', userinput):
        with col5:
            st.write(f"Chinese: {cn}")
        with col6:
            joint = ",".join(en_type)
            st.write(f"Type: {joint}")
        with col7:
            st.write(f"English: {en}")
    else:
        with col5:
            st.write(f"English: {en}")
        with col6:
            joint = ",".join(en_type)
            st.write(f"Type: {joint}")
        with col7:
            st.write(f"Chinese: {cn}")
