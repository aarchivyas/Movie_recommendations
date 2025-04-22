🎬 Movie Recommendation System
This is a simple AI-powered movie recommendation system built using Python and pandas. It allows users to get movie suggestions based on their preferred genre or a minimum rating. The interaction is entirely through the command-line, making it easy to run and use for beginners.

This project includes features like filtering movies by genre, recommending movies above a specific rating, and suggesting similar genre movies automatically after the main recommendation.

It was built using Python 3.13.1 and pandas for data handling. The program runs from a single script (app.py) which handles all the logic and user interaction.

To run this project:

Clone the repository using git clone https://github.com/yourusername/movie-recommendation-system.git and navigate into the folder.

Install the required package using pip install pandas.

Run the project with the command python app.py.

Once launched, it will display three options:

Get recommendations by Genre

Get recommendations based on Rating

Exit

Based on the user’s choice, it will ask for genre or rating and display matching movies with their ratings. If no matches are found, it politely informs the user.

Sample Output:
Welcome to the Movie Recommender!

Get recommendations by Genre

Get recommendations based on Rating

Exit
Enter your choice (1/2/3): 1
Enter your preferred genre (e.g., Sci-Fi, Action): Sci-Fi

Recommended Movies:
Inception – 8.8
Interstellar – 8.6
The Matrix – 8.7

Here are more movies from the same genre:
Inception – 8.8
Interstellar – 8.6
The Matrix – 8.7

In the future, this system can be enhanced by integrating APIs like TMDB to fetch real-time movie data, allowing user feedback for better recommendations, adding a GUI or web interface, and even implementing AI models like collaborative filtering.

From this project, I learned how to build a basic recommender system using pandas, how to interact with users via the terminal, and how to think about user experience in CLI-based applications.

