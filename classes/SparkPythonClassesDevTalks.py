class Business:
    def __init__(self, business_id, name, city, state, stars, review_count):
        self.business_id = business_id
        self.name = name
        self.city = city
        self.state = state
        self.stars = stars
        self.review_count = review_count

    def display(self):
        return `self.business_id` + ", " + `self.name` + ", " + self.city + ", " + self.state + ", " + `self.stars` + ", " + `self.review_count`

        
class Review:
    def __init__(self, business_id, user_id, stars, text, date, votes):
        self.business_id = business_id
        self.user_id = user_id
        self.stars = stars
        self.text = text
        self.date = date
        self.votes = votes

    def display(self):
        return `self.business_id` + ", " + `self.user_id` + ", " + `self.stars`  + ", " + `self.text` + ", " + self.date + ", " + `self.votes`

class User:
    def __init__(self, user_id, name, review_count, average_stars, votes, yelping_since):
        self.user_id = user_id
        self.name = name
        self.review_count = review_count
        self.average_stars = average_stars
        self.votes = votes
        self.yelping_since = yelping_since

    def display(self):
        return `self.user_id` + ", " + `self.name` + ", " + `self.review_count` + ", " + `self.average_stars` + ", " + `self.votes` + ", " + `self.yelping_since`

class Checkin:
    def __init__(self, business_id, checkin_info):
        self.business_id = business_id
        self.checkin_info = checkin_info
        
    def display(self):
        return `self.business_id` + ", " + `self.checkin_info`

class Tip:
    def __init__(self, business_id, user_id, text, date, likes):
        self.business_id = business_id
        self.user_id = user_id
        self.text = text
        self.date = date
        self.likes = likes

    def display(self):
        return `self.business_id` + ", " + `self.user_id` + ", " + `self.text` + ", " + `self.date` + ", " + `self.likes`

