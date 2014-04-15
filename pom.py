import rumps


class Pomodoro(rumps.App):
    pom_interval = 20  # Work time in minutes
    break_interval = 5  # Break time in minutes

    time_spent = 0
    working = True

    def __init__(self):
        super(Pomodoro, self).__init__("pom")
        self.menu = [
            rumps.MenuItem('Start Work Cycle', callback=self.start_work)
            ]
        rumps.debug_mode(True)

    def start_work(self):
        if self.working:
            print "There is already a work cycle going. Starting a new " + \
                "one anyway"

    def update_pomodoro(self):
        self.time_spent += 1

    @rumps.timer(1)
    def a(sender):
        print sender

    @rumps.clicked('On')
    def button(self, sender):
        sender.title = 'Off' if sender.title == 'On' else 'On'
        rumps.Window("I can't think of a good example app...").run()

if __name__ == "__main__":
    Pomodoro().run()
