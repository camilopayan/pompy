import rumps


class Pompy(rumps.App):
    worklength = 10
    restlength = 5
    working = resting = False
    intervals_done = 0
    pomodoros_done = 0

    def __init__(self):
        super(Pompy, self).__init__("P")
        self.menu = ['Start Work Cycle', None]

    @rumps.clicked('Start Work Cycle')
    def start_work(self, sender):
        self.working = True

    @rumps.timer(5)
    def pom(self, sender):
        print "pom callback"
        if self.working and self.intervals_done == self.worklength:
            self.working = False
            self.resting = True
            self.intervals_done = 0
            print "Work cycle done, beginning rest cycle"
        elif self.resting and self.intervals_done == self.restlength:
            self.working = False
            self.resting = False
            self.intervals_done = 0
            self.pomodoros_done += 1
            print "Rest cycle done"
        elif self.working or self.resting:
            self.intervals_done += 1
            print "working = {}".format(self.working)
            print "resting = {}".format(self.resting)
            print "intervals_done = {}".format(self.intervals_done)
        else:
            print "Idling"

if __name__ == "__main__":
    rumps.debug_mode(True)
    app = Pompy()
    app.run()
