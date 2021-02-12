import rumps
import runner

def notify(message):
  title = 'GymRat'
  subtitle  = message
  rumps.notification(title, subtitle, '')



def web_info(_):
  print('--------------------------------------')
  result = runner.cheese()
  if result[0] == False:
    print("False")
  else:
    notify(result[1] + ' 🧀')
    timer.interval = 3600



def start_timer(_):
  stop.set_callback(stop_timer)
  start.set_callback(None)
  timer.start()
  print("Search has been started...")
  notify('Search has been started... 🧀')



def stop_timer(_):
  timer.stop()
  stop.set_callback(None)
  start.set_callback(start_timer)
  print("Search has been stopped...")
  notify('Search has been stopped... 🧀')


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
