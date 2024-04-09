from abc import ABC


class Review(ABC):
    def __init__(self, review_message, rating):
        self.review_message = review_message
        self.rating = rating


class Reviews(ABC):
    def __init__(self):
        self.reviews = []

    def add_review(self, review: Review):
        self.reviews.append(review)