import rumps


class Interval(rumps.Timer):

    interval_length = 1
    intervals_passed = 0

    def __init__(self, length, callback):
        super(self, callback, 5)
        self.interval_length = length
        self.intervals_passed = 0

    def increment_intervals(self):
        self.intervals_passed += 1

    def finished(self):
        return self.intervals_passed == self.interval_length


class Pomodoro(rumps.App):
    worklength = 10
    restlength = 5

    def __init__(self):
        super(Pomodoro, self).__init__('P', menu=['Start Work Cycle'])
        rumps.debug_mode(True)

    @rumps.clicked('Start Work Cycle')
    def start_work(self, sender):
        print "Hello world"
        Interval(self.worklength, self.work_timer_callback).start()

    def work_timer_callback(self, sender):
        print "work_timer_callback"
        sender.increment_intervals()
        if sender.finished():
            sender.stop()

    def rest_timer_callback(self, sender):
        return

if __name__ == "__main__":
    Pomodoro().run()
