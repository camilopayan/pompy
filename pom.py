import rumps

worklength = 10
restlength = 5
working = resting = False
intervals_done = 0
pomodoros_done = 0

@rumps.timer(5)
def work_timer_callback(sender):
    print "work_timer_callback"
    if working or resting:
        intervals_done += 1
    if working and intervals_done==worklength:
        working = False
        resting = True
        intervals_done = 0
    elif resting and intervals_done==restlength:
        working = False
        resting = False
        intervals_done = 0


@rumps.clicked('Start Work Cycle')
def start_work(self, sender):
    print "Hello world"
    
    

if __name__ == "__main__":
    rumps.debug_mode(True)
    rumps.App('P',  menu=['Start Work Cycle']).run()
