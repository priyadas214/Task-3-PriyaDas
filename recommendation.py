print("=" * 60)
print("🎬 AI MOVIE RECOMMENDATION SYSTEM")
print("=" * 60)

movies = {
    "Interstellar": ["Sci-Fi", "Adventure", "Drama"],
    "Avengers Endgame": ["Action", "Adventure", "Sci-Fi"],
    "John Wick": ["Action", "Thriller"],
    "The Notebook": ["Romance", "Drama"],
    "Inception": ["Sci-Fi", "Action", "Thriller"],
    "Titanic": ["Romance", "Drama"],
    "Avatar": ["Adventure", "Sci-Fi"],
    "Doctor Strange": ["Action", "Fantasy", "Sci-Fi"],
    "The Dark Knight": ["Action", "Crime"],
    "Spider-Man No Way Home": ["Action", "Adventure", "Sci-Fi"]
}


def get_recommendations():

    print("\nAvailable Genres:")
    print("Action, Sci-Fi, Adventure, Drama, Thriller, Romance, Fantasy, Crime")

    user_input = input(
        "\nEnter your favorite genres (comma separated): "
    )

    user_preferences = [
        genre.strip().title()
        for genre in user_input.split(",")
    ]

    recommendations = []

    for movie, genres in movies.items():

        common_genres = set(user_preferences) & set(genres)

        score = len(common_genres)

        if score > 0:

            percentage = (score / len(user_preferences)) * 100

            recommendations.append(
                (movie, score, percentage, common_genres)
            )

    recommendations.sort(
        key=lambda x: x[1],
        reverse=True
    )

    print("\n" + "=" * 60)
    print("🎯 TOP MOVIE RECOMMENDATIONS")
    print("=" * 60)

    if recommendations:

        for i, (movie, score, percentage, common_genres) in enumerate(
            recommendations[:5], start=1
        ):

            print(f"\n{i}. {movie}")
            print(f"   Matched Genres   : {', '.join(common_genres)}")
            print(f"   Similarity Score : {score}")
            print(f"   Match Percentage : {percentage:.0f}%")

        rating = input(
            "\nRate these recommendations (1-5): "
        )

        with open("history.txt", "a") as file:

            file.write("\n")
            file.write("=" * 50 + "\n")
            file.write(
                f"User Preferences: {', '.join(user_preferences)}\n"
            )

            for movie, score, percentage, common_genres in recommendations[:5]:

                file.write(
                    f"{movie} | Score: {score} | Match: {percentage:.0f}%\n"
                )

            file.write(f"User Rating: {rating}/5\n")

        print("\n✅ Recommendation history saved!")

    else:
        print("\n❌ No matching movies found.")


def view_history():

    try:
        with open("history.txt", "r") as file:

            content = file.read()

            if content.strip():
                print("\n📜 RECOMMENDATION HISTORY")
                print("=" * 60)
                print(content)
            else:
                print("\nNo history available.")

    except FileNotFoundError:
        print("\nNo history found.")


def clear_history():

    with open("history.txt", "w") as file:
        pass

    print("\n🗑️ History cleared successfully!")


while True:

    print("\n")
    print("=" * 60)
    print("MAIN MENU")
    print("=" * 60)

    print("1. Get Recommendations")
    print("2. View History")
    print("3. Clear History")
    print("4. Exit")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        get_recommendations()

    elif choice == "2":
        view_history()

    elif choice == "3":
        clear_history()

    elif choice == "4":
        print("\n👋 Thank you for using the Movie Recommendation System!")
        break

    else:
        print("\n❌ Invalid choice. Please enter 1-4.")