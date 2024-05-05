MENU_PROMPT= "\n Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies=[]
def add_movie():
    title=input("Enter the movie title: ")
    director=input("Enter the movie director: ")
    year=input("Enter the year in which movie was released: ")

    movies.append({
        'title':title,
        'director':director,
        'year':year
    })
def show_movies():
    if len(movies)==0:
            print("No movies added to the list yet")
    else:
        for movie in movies:
            print_movie(movie)
def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director : {movie['director']}")
    print(f"Year: {movie['year']}")
def find_movies():
    search_title=input("Enter movie title you are looking for:")
    for movie in movies:
        if movie["title"]==search_title:
            print_movie(movie)
        else:
            print("Details of this movie does not exist in this list")
def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'a':
            add_movie()
        elif selection =='l':
            show_movies()
        elif selection =='f':
            find_movies()
        else:
            print("Unknown command. please try again.")

        selection=input(MENU_PROMPT)

menu()