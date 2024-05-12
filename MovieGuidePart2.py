#Roseburrow_CIS261_MovieGuidePart2
def display_menu():
    print("MENU")
    print("1. Display all movie titles")
    print("2. Add a movie title")
    print("3. Delete a movie title")
    print("4. Exit")

def read_movies_file():
    try:
        with open("movies.txt", "r") as file:
            movies = file.readlines()
            return [movie.strip() for movie in movies]
    except FileNotFoundError:
        print("movies.txt not found. Creating a new file.")
        return []

def write_movies_file(movies):
    with open("movies.txt", "w") as file:
        for movie in movies:
            file.write(movie + "\n")

def display_all_titles(movies):
    print("All Movie Titles:")
    for movie in movies:
        print(movie)

def add_title(movies, new_title):
    movies.append(new_title)

def delete_title(movies, title_to_delete):
    if title_to_delete in movies:
        movies.remove(title_to_delete)
        print(f"{title_to_delete} removed from the list.")
    else:
        print(f"{title_to_delete} not found in the list.")

def main():
    movies = read_movies_file()
    print("Movies from file:", movies)  
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            display_all_titles(movies)
        elif choice == "2":
            new_title = input("Enter the new movie title: ")
            add_title(movies, new_title)
            write_movies_file(movies)
            display_all_titles(movies)
        elif choice == "3":
            title_to_delete = input("Enter the movie title to delete: ")
            delete_title(movies, title_to_delete)
            write_movies_file(movies)
            display_all_titles(movies)
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid command. Please enter a valid number.")

if __name__ == "__main__":
    main()
