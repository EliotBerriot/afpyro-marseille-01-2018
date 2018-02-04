from datetime import datetime


class Event(object):
    def __init__(self, name, location, date,
                 participants=[], non_participants=[]):
        self.name, self.location, self.date = name, location, date
        self.participants = participants
        self.non_participants = non_participants


if __name__ == "__main__":
    event = Event('afpyro1', 'La Boate', datetime.utcnow)
