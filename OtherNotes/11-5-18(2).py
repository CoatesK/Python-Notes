class Time:
    """
    Represents the time of day.

    Attributes:
    hours - integer; the hours
    minutes - integer; the minutes
    seconds - integer; the seconds

    Methods:
    We implement the magic methods.
    """

    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        mins, self.seconds = divmod(seconds, 60)
        h, self.minutes = divmod(minutes + mins, 60)
        self.hours = hours + h

    def __str__(self):
        return "hours: %d, minutes: %d, seconds: %d" %(self.hours, self.seconds, self.minutes)

class NewTime(Time):
    def __init__(self, days=0, hours=0, minutes=0, seconds=0):
        super().__init__(hours, minutes, seconds)
        self.days = days



if __name__ == '__main__':
    time = NewTime(7,1,2,3)
    print(time)
