'''
This app helps user to add a movie to their collection, so that they can keep track of all their favorite movies. User can see a list off all the movies in their collection. User can search for a specific movie title.
'''
MENU_PROMPT= "Welcome to movies app\n Enter 'a' to add a movie to your collection \n Enter 'l' to see list of movies in your collection \n Enter 'f' to find a movie by title \n Enter 'q' to quit \n Enter your choice: "
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
    print("Movie successfully added to the collection")
def show_movies():
    if len(movies)==0:
            print("No movies added to the list yet")
    else:
        for movie in movies:
            print_movie(movie)
def print_movie(movie):
    print("--------------------------------------------------------")
    print(f"Title: {movie['title']}")
    print(f"Director : {movie['director']}")
    print(f"Year: {movie['year']}")
    print("--------------------------------------------------------")
def find_movies():
    search_title=input("Enter movie title you are looking for:")
    movie_exists=False
    for movie in movies:
        if movie["title"]==search_title:
            print_movie(movie)
            movie_exists=True
    if not (movie_exists):
            print("This movie does not exist in your collection")

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