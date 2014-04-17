import rumps


@rumps.timer(60)
def pomodoro_update(sender):
    sender.update_pomodoro()


@rumps.timer(1)
def tester(sender):
    print sender.time_spent


pom_interval = 20  # Work time in minutes
break_interval = 5  # Break time in minutes

time_spent = 0
working = False


@rumps.clicked('Start Work Cycle')
def start_work(self):
    if self.working:
        print "There is already a work cycle going. Starting a new " + \
            "one anyway"
    self.working = True


def update_pomodoro(self):
    self.time_spent += 1


if __name__ == "__main__":
    global_namespace_timer = rumps.Timer(tester, 4)
    rumps.App('fuuu', menu=('Start Work Cycle')).run()
