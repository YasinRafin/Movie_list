from userManager import UserManager


def main():
    user_manager = UserManager()
    while True:
        print("""\t1:Register User
        2:Search Movies
        3:View Movie details
        0:Exit""")
        try:
            choice=int(input("Enter your choice:"))
        except:
            print("Input must be number")
            break
        if choice==0:
            break
        elif choice==1:
            # User registration
            email = input("Enter your email address to register: ")
            User=user_manager.register_user(email)
            if not User:
                while True:
                    print("""\t\t    1:Add to your favorite list
                    2:Remove from your favorite list
                    3:View your favorite list
                    0:Log out""")
                    try:
                        choice1=int(input("Enter your choice:"))
                    except:
                        print("Input must be a number")
                        break
                    if choice1==0:
                        break
                    if choice1==1:
                        # Add to favorites
                        movie_id = input("Enter the movie title to add to favorites: ")
                        user_manager.add_to_favorites(email,movie_id)
                    elif choice1==2:
                        # Remove from favorites
                        if user_manager.registered_users[email]:
                            movie_id = input("Enter the movie title to remove from favorites: ")
                            user_manager.remove_from_favorites(email,movie_id)
                        else:
                            print("Favorite list is empty")
                    elif choice1==3:
                        # View favorite movies
                        listMovie=user_manager.view_favorite_movies(email)
                        if listMovie:
                            print("Your favourite list:")
                            for movie in listMovie:
                                print("-",movie)
                        else:
                            print("No movies in favourite list :(")
                         
                    else:
                        print("Invalid choice")



        elif choice==2:
            # Movie search
            query = input("Enter a movie title, cast, or category to search: ")
            matching_movies = user_manager.search_movies(query)
            if matching_movies:
                print("Searched Movies:")
                for movie in matching_movies:
                    print("-", movie)
            else:
                print("No such movie found :(")
        elif choice==3:
            # View movie details
            movie_id = input("Enter the movie title to view details: ")
            details=user_manager.view_movie_details(movie_id)
            if details:
                #details=user_manager.view_movie_details(movie_id)
                print("Movie Title:", details[movie_id]["title"])
                print("Cast:", ", ".join(details[movie_id]["cast"]))
                print("Category:", details[movie_id]["category"])
                print("Release Date:", details[movie_id]["release_date"])
                print("Budget:", details[movie_id]["budget"])
            else:
                print("No such movie found :(")
        else:
            print("Invalid choice")

        # # Add to favorites
        # movie_id = input("Enter the movie title to add to favorites: ")
        # user_manager.add_to_favorites(movie_id)

        # # Remove from favorites
        # movie_id = input("Enter the movie title to remove from favorites: ")
        # user_manager.remove_from_favorites(movie_id)

        # # View favorite movies
        # user_manager.view_favorite_movies()

if __name__ == "__main__":
    main()