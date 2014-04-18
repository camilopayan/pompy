import rumps


class Interval(rumps.Timer):

    interval_length = 1

    def __init__(self, length, callback):
        super(self, callback, 5)
        self.interval_length = length


class Pomodoro(rumps.App):
    worklength = 10
    restlength = 5

    def __init__(self):
        super(Pomodoro, self).__init__('P', menu=['Start Work Cycle'])
        rumps.debug_mode(True)

    @rumps.clicked('Start Work Cycle')
    def start_work(self, sender):
        print "Hello world"


if __name__ == "__main__":
    Pomodoro().run()
