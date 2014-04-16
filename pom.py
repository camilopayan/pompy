import rumps


class Pomodoro(rumps.App):
    pom_interval = 20  # Work time in minutes
    break_interval = 5  # Break time in minutes

    time_spent = 0
    working = False

    def __init__(self):
        super(Pomodoro, self).__init__("pom")
        self.menu = [
            'Start Work Cycle'
            ]
        rumps.debug_mode(True)

    @rumps.clicked('Start Work Cycle')
    def start_work(self):
        if self.working:
            print "There is already a work cycle going. Starting a new " + \
                "one anyway"
        self.working = True

    def update_pomodoro(self):
        self.time_spent += 1

    @rumps.timer(60)
    def a(sender):
        sender.update_pomodoro()

    @rumps.clicked('On')
    def button(self, sender):
        sender.title = 'Off' if sender.title == 'On' else 'On'
        rumps.Window("I can't think of a good example app...").run()

if __name__ == "__main__":
    Pomodoro().run()
