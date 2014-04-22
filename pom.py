import rumps


@rumps.timer(5)
def pom(sender):
    print "pom callback"
    """
    if app.working and app.intervals_done == app.worklength:
        app.working = False
        app.resting = True
        app.intervals_done = 0
        print "Work cycle done, beginning rest cycle"
    elif app.resting and app.intervals_done == app.restlength:
        app.working = False
        app.resting = False
        app.intervals_done = 0
        app.pomodoros_done += 1
        print "Rest cycle done"
    elif app.working or app.resting:
        app.intervals_done += 1
        print "working = " + app.working
        print "resting = " + app.resting
        print "intervals_done = " + app.intervals_done
    else:
        print "Idling"
    """


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
        app.working = True

if __name__ == "__main__":
    rumps.debug_mode(True)
    app = Pompy()
    app.run()
