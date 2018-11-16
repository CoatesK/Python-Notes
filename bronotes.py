class Time:
    '''
    *Represents the time of day

    *attributes: hour, minute, second
    '''
    #Methods
    def return_time(time):
        return '%d:%d:%d' % (time.hour, time.minute, time.second)

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def time_to_int(time):
        minutes = time.hour * 60 + time.minute
        seconds = minutes * 60 + time.second
        return seconds

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

    #Magic Methods
    def __init__(self, hour = 0, minute = 0, second = 0):
        minutes, self.second = divmod(second, 60)
        hours, self.minute = divmod((minutes + minute), 60)
        self.hour = hours + hour

    def __str__(self):
        return '%d:%d:%d' % (self.hour, self.minute, self.second)

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        seconds = self.time_to_int() - other.time_to_int()
        return int_to_time(seconds)

#Main
if __name__ == '__main__':

    def int_to_time(seconds):
        '''
        A good example of how, when you aren't dealing with parameters that don't deal with the class being used,
        it's best to keep it in the __main__
        '''
        time = Time()
        minutes, time.second = divmod(seconds, 60)
        time.hour, time.minute = divmod(minutes, 60)
        return time
