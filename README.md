Movie Recommendation System

A content-based movie recommendation system that suggests the top 5 most similar movies based on a selected title. Built end-to-end — from raw data to a deployed, publicly accessible web application.

Problem: Users often struggle to discover movies similar to ones they already enjoy. This project solves that by analyzing movie metadata (genre, plot, cast, director) to find meaningful similarities.

Approach:

Cleaned and preprocessed the TMDB 5000 Movies dataset (~5,000 titles) using Pandas, handling missing values and parsing nested JSON-like fields (genres, cast, crew)
Engineered a unified "tags" feature by combining overview text, genres, keywords, cast, and director for each movie
Converted text data into numerical vectors using CountVectorizer (Bag-of-Words)
Computed pairwise Cosine Similarity to measure how closely movies relate to one another
Optimized storage using sparse matrix representation, reducing model size significantly for efficient deployment
Built an interactive UI with Streamlit where users select a movie and instantly get 5 recommendations
Deployed the application publicly via Streamlit Community Cloud, with version control on GitHub

Key Skills Demonstrated: Data cleaning, feature engineering, text vectorization, similarity-based ML, model optimization for deployment, and full-stack deployment of a data science project.
