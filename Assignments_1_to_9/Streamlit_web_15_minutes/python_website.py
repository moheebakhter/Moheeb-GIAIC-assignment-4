import streamlit as st
import pandas as pd

st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Strip any whitespace from column names early
    df.columns = df.columns.str.strip()

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]

    st.subheader("Filtered Data")
    st.write(filtered_df)

    st.subheader("Plot Data")
    
    # Use filtered_df columns for plotting, not the original df
    plot_columns = filtered_df.columns.tolist()
    x_column = st.selectbox("Select x-axis column", plot_columns, key="x_column")
    y_column = st.selectbox("Select y-axis column", plot_columns, key="y_column")

    if st.button("Generate Plot"):
        try:
            st.line_chart(filtered_df.set_index(x_column)[y_column])
        except KeyError as e:
            st.error(f"Column not found: {e}")

else:
    st.write("Waiting on file upload...")
