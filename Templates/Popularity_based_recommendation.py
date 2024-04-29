import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Book Recommendation",
    page_icon="📚",
    layout="wide"
)

st.title(" Popular Books based on User Ratings")

df = pd.read_csv("src/data/popular_df.csv")

def display_star_rating(rating):
    full_star = '⭐️'
    empty_star = '⭐'
    
    stars = int(rating)
    
    stars_display = f"{full_star * stars} ({stars})"
    
    return stars_display

select = st.selectbox(label="Select a book", options=df['Book-Title'], index=0)

if select:
    q = df.index[df['Book-Title'] == select][0]
    col1, col2 = st.columns(2)
    col1.image(df.loc[q, 'Image-URL-S'],width = 200)
    
    col2.markdown(
        f'''
        # {df.loc[q, 'Book-Title']}
        ## Author :- {df.loc[q, 'Book-Author']} 
        ###    Year:{df.loc[q, 'Year-Of-Publication']}
        '''
    )

# Display the images in a grid layout
num_rows = 5
num_cols = 10

df_subset = df.head(num_rows * num_cols)

for i in range(num_rows):
    cols = st.columns(num_cols)
    for j in range(num_cols):
        index = i * num_cols + j
        if index < len(df_subset):
            rating = df_subset.iloc[index]['avg_rating']  # Use 'avg_rating' instead of 'avg-rating'
            caption = f"{df_subset.iloc[index]['Book-Title']}\n{display_star_rating(rating)}"
            cols[j].image(df_subset.iloc[index]['Image-URL-S'], caption=caption, use_column_width=True)
