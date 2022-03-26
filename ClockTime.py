class ClockTime:

    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    def set_hours(self, hour):
        self.hours = hour

    def set_minutes(self, mins):
        self.minutes = mins

    def set_seconds(self, sec):
        self.seconds = sec

    def set_time(self, hour, mins, sec):
        self.hours = hour
        self.minutes = mins
        self.seconds = sec

    def show_time(self):
        print(str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds))


hours = input("Set hour: ")
min = input("Set minutes: ")
sec = input("Set seconds: ")
time = ClockTime()
time.set_time(hours, min, sec)
print("The clock time is: ")
time.show_time()
