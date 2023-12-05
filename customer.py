class Customer:
    # Class variable to keep track of all customers
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []  # List to store customer reviews
        Customer.all_customers.append(self)  # Add the customer to the list of all customers

    # Method to get the given name of the customer
    def get_given_name(self):
        return self.given_name

    # Method to get the family name of the customer
    def get_family_name(self):
        return self.family_name

    # Method to get the full name of the customer
    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    # Method to get the list of restaurants the customer has reviewed
    def restaurants(self):
        return list({review.restaurant for review in self.reviews})

    # Method to add a review for a restaurant by the customer
    def add_review(self, restaurant, rating):
        new_review = Review(self, restaurant, rating)
        self.reviews.append(new_review)

    #  list of all customers
    @classmethod
    def get_all(cls):
        return cls.all_customers

    # number of reviews by the customer
    def num_reviews(self):
        return len(self.reviews)

    # find a customer by full name
    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name().lower() == name.lower():
                return customer
        return None

    # find all customers by given name
    @classmethod
    def find_all_by_given_name(cls, name):
        return [customer for customer in cls.all_customers if customer.given_name.lower() == name.lower()]
