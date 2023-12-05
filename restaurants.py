class Restaurant:
    # Class variable to keep track of all restaurants
    all_restaurants = []

    # Constructor to initialize a restaurant with a name
    def __init__(self, name):
        self.name = name
        self.reviews = []  # List to store restaurant reviews
        Restaurant.all_restaurants.append(self)  # Add the restaurant to the list of all restaurants

    # Method to get the name of the restaurant
    def get_name(self):
        return self.name

    # Method to get the reviews of the restaurant
    def get_reviews(self):
        return self.reviews

    # Method to get the list of customers who reviewed the restaurant
    def get_customers(self):
        return list({review.customer for review in self.reviews})

    # Class method to get the list of all restaurants
    @classmethod
    def get_all(cls):
        return cls.all_restaurants

    # Method to calculate the average star rating of the restaurant
    def average_star_rating(self):
        total_ratings = sum(review.rating for review in self.reviews)
        num_reviews = len(self.reviews)
        if num_reviews > 0:
            return total_ratings / num_reviews
        else:
            return 0  # Return 0 if there are no reviews yet
