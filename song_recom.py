import streamlit as st
import pandas as pd
import random

# Load the dataset
data_path = 'ex.csv'  # Update with your file path
songs = pd.read_csv(data_path)

# Strip any leading/trailing whitespace from the column names
songs.columns = songs.columns.str.strip()

# Function to recommend songs based on genre
def recommend_songs(genre, num_recommendations=5):
    recommended_songs = songs[songs['Genre'].str.contains(genre, case=False, na=False)]
    return recommended_songs.sample(min(num_recommendations, len(recommended_songs)))

# Streamlit app
st.title("Song Recommendation System")

st.write("""
### Discover Your Next Favorite Song!
Select your favorite genre and get song recommendations.
""")

# Ensure the genre column exists
if 'Genre' in songs.columns:
    # Genre selection
    genre = st.selectbox("Choose a genre:", songs['Genre'].unique())

    # Number of recommendations
    num_recommendations = st.slider("Number of recommendations:", 1, 10, 5)

    # Recommend songs
    if st.button("Recommend"):
        recommendations = recommend_songs(genre, num_recommendations)
        st.write("### Recommended Songs:")
        for idx, row in recommendations.iterrows():
            st.write(f"**{row['Song-Name']}** by {row['Singer/Artists']}")
        
        # Feedback for recommendations
        st.write("\n\n### Feedback")
        feedback = st.slider("What do you think of the above recommendations? (1-10)", 1, 10)

        st.write(f"You rated the recommendations {feedback} out of 10.")

else:
    st.error(f"The column 'Genre' does not exist in the dataset.")

# Display the dataset
if st.checkbox("Show dataset"):
    st.write(songs)








