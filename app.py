import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# Load data
df = pd.read_csv("imdb_top_250.csv")
df['Decade'] = (df['Year'] // 10) * 10

st.title("🎬 IMDb Top 250 Movies Dashboard")

st.markdown("""
Explore the IMDb Top 250 dataset. Use the sidebar to filter by year and view different visualizations.
""")

# Sidebar filter
st.sidebar.header("Filter")
year_range = st.sidebar.slider("Choose Year Range", int(df['Year'].min()), int(df['Year'].max()), (1990, 2020))
filtered_df = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]

# Rating distribution
st.subheader("IMDb Rating Distribution")
fig1, ax1 = plt.subplots()
sns.histplot(filtered_df['Rating'], kde=True, color='orange', ax=ax1)
ax1.set_xlabel("Rating")
st.pyplot(fig1)

# Runtime distribution
st.subheader("Runtime Distribution")
fig2, ax2 = plt.subplots()
sns.histplot(filtered_df['Runtime'], kde=True, color='teal', ax=ax2)
ax2.set_xlabel("Runtime (Minutes)")
st.pyplot(fig2)

# Movies per year
st.subheader("Top Movies per Year")
fig3, ax3 = plt.subplots(figsize=(12, 4))
sns.countplot(data=filtered_df, x='Year', palette='viridis', order=sorted(filtered_df['Year'].unique()), ax=ax3)
ax3.set_xticklabels(ax3.get_xticklabels(), rotation=90)
st.pyplot(fig3)

# Runtime vs Rating
st.subheader("Runtime vs Rating")
fig4, ax4 = plt.subplots()
sns.scatterplot(data=filtered_df, x='Runtime', y='Rating', ax=ax4)
st.pyplot(fig4)

# Movies by decade
st.subheader("Top Movies by Decade")
fig5, ax5 = plt.subplots()
sns.countplot(data=filtered_df, x='Decade', palette='cool', ax=ax5)
st.pyplot(fig5)

# Show data
st.subheader("Filtered Data Table")
st.dataframe(filtered_df)
