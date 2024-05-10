movies=["Animal", "Ek tha tiger", "Titanic"]
class UserManager:
    #def __init__(self):
    registered_users = {}
    favorite_movies = []
    global movies

    def register_user(cls, email):
        #print("Logged in user:",email)
        if email in cls.registered_users:
            print("Logged in user:",email)
            print("Already registered you are logged in to your account")
            return False
        cls.registered_users[email]=[]
        print("Successfully registered :)")
        return True

    def search_movies(cls, query):
        #movies = ["Animal", "Ek tha tiger", "Titanic"]
        matching_movies = [movie for movie in movies if query.lower() in movie.lower()]
        if matching_movies:
            return matching_movies
        else:
            return False

    def view_movie_details(cls, movie_id):
        movie_details = {
        "Animal":{
            "title": "Animal",
            "cast": ["Ranbeer Kapoor", "Rashmika Mandana","Anil Kapoor"],
            "category": "Action",
            "release_date": "2023-12-01",
            "budget": "	₹100 crore"
            },
        "Ek tha tiger":{
            "title": "Ek tha tiger",
            "cast": ["Salman Khan", "Katrina Kaif","Ranvir Shore"],
            "category": "Action",
            "release_date": "2012-08-15",
            "budget": "	₹75 crore"
        },
        "Titanic":{
            "title": "Titanic",
            "cast": ["Leonardo DiCaprio", "Kate Winslet","Billy Zane"],
            "category": "Action/Romantic",
            "release_date": "1997-12-19",
            "budget": "	$200 million"
        }

        }
        if movie_id in movie_details:
            return movie_details
        else:
            return False

    def add_to_favorites(cls, email, movie_id):
        if movie_id not in cls.registered_users[email] and movie_id in movies:
            cls.registered_users[email].append(movie_id)
            print("Successfully added to favorite")
        elif movie_id not in movies:
            print("No such Movie found")    
        else:
            print("Movie is already in the list")
        print(cls.registered_users[email])

    def remove_from_favorites(cls, email, movie_id):
        # if not cls.registered_users[email]:
        #     print("Favorite list is empty")
        if movie_id in cls.registered_users[email]:
            cls.registered_users[email].remove(movie_id)
            print("{} Removed from favorites".format(movie_id))
        elif movie_id not in cls.registered_users[email] and len(cls.registered_users[email])>0:
            print("Movie not found in favourite :(")



    def view_favorite_movies(cls, email):
        if cls.registered_users[email]:
            return cls.registered_users[email]
        else:
            return []