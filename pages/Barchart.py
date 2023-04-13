import streamlit as st
import plotly.express as px
import sys

sys.path.insert(1, "pages")

from utility2 import Combined

st.title("Letter Counts in Dictionary")
Combined = Combined().combined_words()
word = ''.join(sorted(Combined))

letter = {}

for char in word:
    if char in letter:
        letter[char] += 1
    else:
        if len(letter) <= 25 and not char.isspace():
            letter[char] = 1

data = {"Letter": list(letter.keys()), "Count": list(letter.values())}

fig = px.bar(data, x="Letter", y="Count",
             labels={"Count": "Letter Count"}, hover_data={"Count": True},
             hover_name="Letter", text="Count")

fig.update_traces(hovertemplate="Letter: %{x}<br>Count: %{text}")
st.plotly_chart(fig, use_container_width=True)
