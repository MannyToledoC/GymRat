import rumps
from rumps.rumps import MenuItem
import runner

def notfiy(message):
  title = '🐀 GymRat 🐀'
  subtitle  = 'Gym Notification For 4:00 PM'
  rumps.notification(title, subtitle, message)



def web_info(_):
  print('--------------------------------------')
  if runner.cheese() == False:
    print("False")
  else:
    notfiy('Spot Available!')
    timer.interval = 3600



def start_timer(_):
  stop.set_callback(stop_timer)
  start.set_callback(None)
  timer.start()
  print("Search has started")



def stop_timer(_):
  timer.stop()
  stop.set_callback(None)
  start.set_callback(start_timer)
  print("Search has been stopped")

@rumps.clicked("Debugger")
def check(_):
    print(rumps.timers())

if __name__ == '__main__':
  timer = rumps.Timer(web_info, 60)  
  GymRat = rumps.App('GymRat', '🐀')

  start = rumps.MenuItem(title='Start', callback=start_timer)
  stop = rumps.MenuItem(title='Stop', callback=None)
  GymRat.menu = [start, stop]
  GymRat.run()
