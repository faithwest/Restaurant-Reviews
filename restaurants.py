class Restaurant :
    def _init_ (self,name,rating)
        self.name = _name
        self.rating =_rating
        self.reviewers = []

    def add_review(self,review):
        self.reviews.append(reviews) 

    def get_all_reviews(self):
        return self.reviews


    def get_unique_customers(self):
        unique_customers=[]
        for review in self.reviews:
            customer=review.get_customer()
            if customer not in unique_customer:
                unique_customers.append(customer)
              return unique_customers  



