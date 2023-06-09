import streamlit as st

import numpy as np
import pandas as pd
import random

st.markdown("""
            # This is a header
            ## this is a sub header
            this is a text
            - a list
            *italic*
            """)

@st.cache
def return_df():
    df = pd.DataFrame({
        'random column': random.sample(range(10, 50), 10),
        'normal column': np.arange(10, 101, 10)
    })
    return df

line_count = st.slider('Select number of lines', 1, 10, 3)

st.write(return_df().head(line_count))
