import os
from kivy.app import App
from android import AndroidService
from time import sleep
from threading import Thread


HERE = os.path.abspath(os.path.dirname(__file__))
LOGPATH = os.path.join(HERE, "djandro.log")


class DjandroApp(App):
    def build(self):
        self.service = AndroidService('Django', 'Django is running')
        open(LOGPATH, 'w').close()  # Touch the logfile
        self.running = False
        self.logging = False
        
    def toggle(self):
        action = self.stop if self.running else self.start
        self.running = not self.running
        action()
        self.root.ids['info'].text = "[color=#ff0000]Django is OFF[/color]"
        if self.running:
            self.root.ids['info'].text = "[color=#00ff00]Django is ON[/color]"

        btn_text = 'Stop' if self.running else 'Start'
        self.root.ids['btn'].text = btn_text + " Django"

    def start(self):
        self.service.start(LOGPATH)
        self.start_logging()

    def stop(self):
        self.service.stop()
        self.logging = False
        self.running = False

    def start_logging(self):
        self.console = Thread(target=self.logger)
        self.logging = True
        self.console.start()

    def logger(self):
        label = self.root.ids['console']
        log = open(LOGPATH, 'r')
        label.text = log.read()
        while self.logging:
            log.seek(log.tell())
            label.text += log.read()
            sleep(0.2)

    def on_pause(self):
        if self.logging:
            self.logging = False
            self.console.join()
        return True


    def on_resume(self):
        if self.running:
            self.start_logging()

if __name__ == '__main__':
    DjandroApp().run()
