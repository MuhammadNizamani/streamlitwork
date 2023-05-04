import streamlit as st
import numpy as np
import pandas as pd

# import streamlit as st
x = st.slider("Select a value")
st.write(x, "squared is", x * x)

# import streamlit as st
# import numpy as np

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)


dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)