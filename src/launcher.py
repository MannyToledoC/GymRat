import rumps
import runner

class GymRat(object):
  def __init__(self):
    self.app = rumps.App("GymRat", "🐀")
    self.timer = rumps.Timer(self.web_info, 60)
    self.start_script = rumps.MenuItem(title="Start", callback=self.start_timer)
    self.stop_script = rumps.MenuItem(title="Stop", callback=self.stop_timer)
    self.app.menu = [self.start_script, self.stop_script]
    
    # self.start_script = rumps.MenuItem(title="Start", callback=self.web_info)
    # self.app.menu = [self.start_script]

  def run(self):
    self.app.run()

  def web_info(self, sender):
    if runner.cheese() == False:
      print("False")
    else:
      # rumps.notification(title="GymRat", subtitle="Sample", message='HEllo hows itgoing')
      print("Should be 2 seconds")
      self.timer.interval = 2

    
    # rumps.notification(title="GymRat", subtitle="Sample", message='HEllo hows itgoing')
    
  def start_timer(self, sender):
    self.timer.start()
    print("Search has started")
  def stop_timer(self, sender):
    self.timer.stop()
    print("Search has been stopped")

if __name__ == '__main__':
  app = GymRat()
  app.run()