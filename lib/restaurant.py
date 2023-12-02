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



# Creates 4 different customers
customer1 = Customer("Don", "Draper")
customer2 = Customer("Peggy", "Olson")
customer3 = Customer("Pete", "Campbell")
customer4 = Customer("Betty", "Draper")

# Create 3 restaurants to review
restaurant1 = Restaurant("Restaurant A")
restaurant2 = Restaurant("Restaurant B")
restaurant3 = Restaurant("Restaurant C")

# Add reviews
customer1.addReview(restaurant1, 5)
customer1.addReview(restaurant2, 4)
customer1.addReview(restaurant3, 3)

customer2.addReview(restaurant1, 4)
customer2.addReview(restaurant2, 5)
customer2.addReview(restaurant3, 4)

customer3.addReview(restaurant1, 3)
customer3.addReview(restaurant2, 4)
customer3.addReview(restaurant3, 5)

customer4.addReview(restaurant1, 5)
customer4.addReview(restaurant2, 3)
customer4.addReview(restaurant3, 4)

# Print average ratings for each restaurant
print("Average rating for Restaurant A:", restaurant1.averageStarRating())
print("Average rating for Restaurant B:", restaurant2.averageStarRating())
print("Average rating for Restaurant C:", restaurant3.averageStarRating())

# Print full names of all customers
print("All customers:")
for customer in Customer.all():
    print(customer.fullName())

# Print customers who reviewed each restaurant
print("Customers who reviewed Restaurant A:")
for customer in restaurant1.customers():
    print(customer.fullName())

print("Customers who reviewed Restaurant B:")
for customer in restaurant2.customers():
    print(customer.fullName())

print("Customers who reviewed Restaurant C:")
for customer in restaurant3.customers():
    print(customer.fullName())

# Print customers with given name 'Don'
print("Customers with given name 'Don':")
for customer in Customer.findAllByGivenName("Don"):
    print(customer.fullName())
