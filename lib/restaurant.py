class Customer:
    allCustomers = []

    def __init__(self, givenName, familyName):
        self.givenName = givenName
        self.familyName = familyName
        self.reviews = []
        Customer.allCustomers.append(self)

    def getGivenName(self):
        return self.givenName

    def getFamilyName(self):
        return self.familyName

    def fullName(self):
        return f"{self.givenName} {self.familyName}"

    @classmethod
    def all(cls):
        return cls.allCustomers

    def restaurants(self):
        return list({review.getRestaurant() for review in self.reviews})

    def addReview(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self.reviews.append(review)
        restaurant.addReview(review)

    def numReviews(self):
        return len(self.reviews)

    @classmethod
    def findByName(cls, name):
        return next((customer for customer in cls.allCustomers if customer.fullName() == name), None)

    @classmethod
    def findAllByGivenName(cls, givenName):
        return [customer for customer in cls.allCustomers if customer.getGivenName() == givenName]


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.reviews = []

    def getName(self):
        return self.name

    def getReviews(self):
        return self.reviews

    def averageStarRating(self):
        if not self.reviews:
            return 0.0
        totalRating = sum(review.getRating() for review in self.reviews)
        return totalRating / len(self.reviews)

    def customers(self):
        return list({review.getCustomer() for review in self.reviews})

    def addReview(self, review):
        self.reviews.append(review)


class Review:
    allReviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.allReviews.append(self)

    def getRating(self):
        return self.rating

    @classmethod
    def all(cls):
        return cls.allReviews

    def getCustomer(self):
        return self.customer

    def getRestaurant(self):
        return self.restaurant


