import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#data
df = pd.read_csv('data/netflix_cleaned.csv')

st.title("🎬 Netflix Movie & TV Show Analysis")
st.markdown("Explore trends in Netflix's catalog using interactive charts.")

# Sidebar Filters
st.sidebar.header("Filter")
content_type = st.sidebar.multiselect("Select Content Type", df['type'].unique(), default=df['type'].unique())

# Filtered Data
filtered_df = df[df['type'].isin(content_type)]

# Top Genres
st.subheader("Top 10 Genres on Netflix")
all_genres = filtered_df['listed_in'].str.split(', ').explode()
top_genres = all_genres.value_counts().head(10)

fig, ax = plt.subplots()
sns.barplot(x=top_genres.values, y=top_genres.index, ax=ax, palette="rocket")
ax.set_xlabel("Number of Titles")
ax.set_ylabel("Genre")
st.pyplot(fig)

if st.checkbox("Show Raw Data"):
    st.write(filtered_df.head(20))
