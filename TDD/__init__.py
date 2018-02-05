from datetime import datetime


class Event(object):
    def __init__(self, name, location, date,
                 participants=[], non_participants=[]):
        self.name, self.location, self.date = name, location, date
        self.participants = participants
        self.non_participants = non_participants


class Events(object):
    def __init__(self, events=[]):
        self.events = events

    def set_going_or_not(self, event, user):
        pass


afpyro1 = Event('afpyro1', 'La Boate', datetime.utcnow)
afpyro2 = Event('afpyro2', 'La Boate', datetime.utcnow)
afpyro3 = Event('afpyro3', 'La Boate', datetime.utcnow)

if __name__ == "__main__":
    events = Events([afpyro1, afpyro2, afpyro3])

    print("Hello, World!")
