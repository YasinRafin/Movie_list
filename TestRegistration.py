import unittest

class UserManager:
    registered_users = {}
    favorite_movies = []

    @classmethod
    def register_user(cls, email):
        print("Registering user:", email)
        if email in cls.registered_users:
            print("User already registered. Existing users:", cls.registered_users)
            print("Already registered. You are logged in to your account.")
            return False
        cls.registered_users[email] = []
        print("Successfully registered. Updated registered users:", cls.registered_users)
        return True

    @classmethod
    def search_movies(cls, query):
        movies = ["Animal", "Ek tha tiger", "Titanic"]
        matching_movies = [movie for movie in movies if query.lower() in movie.lower()]
        return matching_movies

    @classmethod
    def view_movie_details(cls, movie_id):
        movie_details = {
            "Animal": {
                "title": "Animal",
                "cast": ["Ranbeer Kapoor", "Rashmika Mandana", "Anil Kapoor"],
                "category": "Action",
                "release_date": "2023-12-01",
                "budget": "₹100 crore"
            },
            "Ek tha tiger": {
                "title": "Ek tha tiger",
                "cast": ["Salman Khan", "Katrina Kaif", "Ranvir Shore"],
                "category": "Action",
                "release_date": "2012-08-15",
                "budget": "₹75 crore"
            },
            "Titanic": {
                "title": "Titanic",
                "cast": ["Leonardo DiCaprio", "Kate Winslet", "Billy Zane"],
                "category": "Action/Romantic",
                "release_date": "1997-12-19",
                "budget": "$200 million"
            }
        }
        return movie_details.get(movie_id, None)

    @classmethod
    def add_to_favorites(cls, email, movie_id):
        if email not in cls.registered_users:
            print("User not registered.")
            return False

        if movie_id not in cls.registered_users[email] and movie_id in cls.search_movies(movie_id):
            cls.registered_users[email].append(movie_id)
            print("Successfully added to favorites.")
            return True
        elif movie_id not in cls.search_movies(movie_id):
            print("No such movie found.")
        else:
            print("Movie is already in the list.")
        return False

    @classmethod
    def remove_from_favorites(cls, email, movie_id):
        if email not in cls.registered_users:
            print("User not registered.")
            return False

        if movie_id in cls.registered_users[email]:
            cls.registered_users[email].remove(movie_id)
            print(f"{movie_id} removed from favorites.")
            return True
        elif len(cls.registered_users[email]) > 0:
            print("Movie not found in favorites.")
        else:
            print("Favorite list is empty.")
        return False

    @classmethod
    def view_favorite_movies(cls, email):
        if email not in cls.registered_users:
            print("User not registered.")
            return []
        return cls.registered_users[email]

class TestUserManager(unittest.TestCase):

    def setUp(self):
        self.user_manager = UserManager()

    def test_register_user(self):
        self.assertTrue(self.user_manager.register_user('user@example.com'))  # Test registering a new user
        self.assertFalse(self.user_manager.register_user('user@example.com'))  # Test registering a user with an already registered email

    def test_search_movies(self):
        expected_movies = ["Animal", "Ek tha tiger", "Titanic"]
        self.assertEqual(self.user_manager.search_movies(''), expected_movies)  # Test searching for all movies
        self.assertEqual(self.user_manager.search_movies('Animal'), ['Animal'])  # Test searching for a movie that exists
        self.assertEqual(self.user_manager.search_movies('Avengers'), [])  # Test searching for a movie that does not exist

    def test_view_movie_details(self):
        expected_details = {
            "title": "Animal",
            "cast": ["Ranbeer Kapoor", "Rashmika Mandana", "Anil Kapoor"],
            "category": "Action",
            "release_date": "2023-12-01",
            "budget": "₹100 crore"
        }
        self.assertEqual(self.user_manager.view_movie_details('Animal'), expected_details)  # Test viewing details of a movie that exists
        self.assertIsNone(self.user_manager.view_movie_details('Avengers'))  # Test viewing details of a movie that does not exist

    def test_add_to_favorites(self):
        self.assertTrue(self.user_manager.register_user('user@example.com'))
        self.assertTrue(self.user_manager.add_to_favorites('user@example.com', 'Animal'))  # Test adding a movie to favorites for a registered user
        self.assertFalse(self.user_manager.add_to_favorites('user@example.com', 'Animal'))  # Test adding a movie that is already in favorites
        self.assertFalse(self.user_manager.add_to_favorites('invaliduser@example.com', 'Animal'))  # Test adding to favorites for an unregistered user

    def test_remove_from_favorites(self):
        self.assertTrue(self.user_manager.register_user('user@example.com'))
        self.assertTrue(self.user_manager.add_to_favorites('user@example.com', 'Animal'))
        self.assertTrue(self.user_manager.remove_from_favorites('user@example.com', 'Animal'))  # Test removing a movie from favorites for a registered user
        self.assertFalse(self.user_manager.remove_from_favorites('user@example.com', 'Animal'))  # Test removing a movie that is not in favorites
        self.assertFalse(self.user_manager.remove_from_favorites('invaliduser@example.com', 'Animal'))  # Test removing from favorites for an unregistered user

    def test_view_favorite_movies(self):
        self.assertTrue(self.user_manager.register_user('user@example.com'))
        self.assertEqual(self.user_manager.view_favorite_movies('user@example.com'), [])  # Test viewing favorite movies for a registered user with no favorites
        self.assertEqual(self.user_manager.view_favorite_movies('invaliduser@example.com'), [])  # Test viewing favorite movies for an unregistered user

if __name__ == '__main__':
    unittest.main()