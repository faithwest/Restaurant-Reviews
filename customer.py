class Customer:
    def __init__(self, name, family_name):
        self.given_name =given_name
        self.family_name=family_name
        self.full_name= given_name + "" + family_name
        Customer.instances.append(self)
        customer_reviews=[]

        @classmethod
        def get_instances(cls):
            return cls.instances

        def get_given_name(self):
            return self.given_name

        def get_family_name(self):
            return self.family_name

        def get_full_name(self):
            return self.full_name

    def write_review(self, restaurant, rating, comment):
        review = Review(restaurant, rating, comment)
        self.reviews.append(review)
        restaurant.add_review(review)

    def get_unique_restaurants(self):
        unique_restaurants = []
        for review in self.reviews:
            restaurant = review.get_restaurant()
            if restaurant not in unique_restaurants:
                unique_restaurants.append(restaurant)
        return unique_restaurants
        
    def calculate_average_rating(self):
            total_rating = 0
            num_ratings = len(self.reviews)
            for review in self.reviews:

            
    


