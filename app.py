import pandas as pd

movies = {
    'Movie': ['Inception', 'Interstellar', 'The Matrix', 'The Dark Knight', 'Avengers'],
    'Genre': ['Sci-Fi', 'Sci-Fi', 'Sci-Fi', 'Action', 'Action'],
    'Rating': [8.8, 8.6, 8.7, 9.0, 8.0]
}

df = pd.DataFrame(movies)
genre = input("Enter your preferred genre (e.g., Sci-Fi, Action): ")

recommended = df[df['Genre'].str.lower() == genre.lower()]

if not recommended.empty:
    print("\nRecommended Movies:")
    print(recommended[['Movie', 'Rating']])
else:
    print("No movies found in that genre.")
