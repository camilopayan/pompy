import rumps


class Pompy(rumps.App):
    worklength = 4
    restlength = 2
    working = resting = False
    intervals_done = 0
    pomodoros_done = 0

    def __init__(self):
        super(Pompy, self).__init__("P")
        self.menu = ['Start Work Cycle',
                     None,
                     'Change Work Length',
                     'Change Rest Length'
                     ]

    @rumps.clicked('Start Work Cycle')
    def start_work(self, sender):
        self.working = True
        self.title = "P{}".format(self.worklength)

    @rumps.clicked('Change Work Length')
    def change_work_length(self, sender):
        window = rumps.Window("Work Length is currently " +
                              "{} minutes".format(self.worklength),
                              title="Pompy")
        response = window.run()
        if response.clicked and int(response.text):
            self.worklength = int(response.text)

    @rumps.clicked('Change Rest Length')
    def change_rest_length(self, sender):
        window = rumps.Window("Rest Length is currently " +
                              "{} minutes".format(self.restlength),
                              title="Pompy")
        response = window.run()
        if response.clicked and int(response.text):
            self.restlength = int(response.text)

    @rumps.timer(2)
    def pom(self, sender):
        print "pom callback"
        if self.working and self.intervals_done == self.worklength:
            self.working = False
            self.resting = True
            self.intervals_done = 0
            rumps.notification(
                "Pompy",
                "Work Cycle Done",
                "{} minutes have passed, beginning rest cycle".format(
                    self.worklength
                    )
                )
        elif self.resting and self.intervals_done == self.restlength:
            self.working = False
            self.resting = False
            self.intervals_done = 0
            self.pomodoros_done += 1
            self.title = "P"
            rumps.notification(
                "Pompy",
                "Rest Cycle Done",
                "Congratulations! You've done {} pomodoros.".format(
                    self.pomodoros_done
                    )
                )
        elif self.working or self.resting:
            self.intervals_done += 1
            if self.working:
                self.title = "P{}".format(self.worklength -
                                          self.intervals_done)
            elif self.resting:
                self.title = "P{}".format(self.restlength -
                                          self.intervals_done)
            print "working = {}".format(self.working)
            print "resting = {}".format(self.resting)
            print "intervals_done = {}".format(self.intervals_done)

if __name__ == "__main__":
    rumps.debug_mode(True)
    app = Pompy()
    app.run()
