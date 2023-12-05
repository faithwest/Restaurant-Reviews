class Review:
    # Class variable to keep track of all reviews
    all_reviews = []

    # Constructor to initialize a review with a customer, restaurant, and rating
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        restaurant.reviews.append(self)  # Add the review to the restaurant's list of reviews
        customer.reviews.append(self)  # Add the review to the customer's list of reviews
        Review.all_reviews.append(self)  # Add the review to the list of all reviews

    # Method to get the customer associated with the review
    def get_customer(self):
        return self.customer

    # Method to get the restaurant associated with the review
    def get_restaurant(self):
        return self.restaurant

    # Method to get the rating of the review
    def get_rating(self):
        return self.rating

    # Class method to get the list of all reviews
    @classmethod
    def get_all(cls):
        return cls.all_reviews
