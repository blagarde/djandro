from kivy.app import App
from android import AndroidService
from tempfile import NamedTemporaryFile
from time import sleep
from threading import Thread


class DjandroApp(App):
    def build(self):
        self.service = AndroidService('Django', 'Django is running')
        self.running = False
        self.tmp = NamedTemporaryFile(mode='w+')
        self.console = Thread(target=self.logging)

    def toggle(self):
        action = self.stop if self.running else self.start
        action()
        self.running = not self.running
        state = 'ON' if self.running else 'OFF'
        self.root.ids['btn'].text = "Django is " + state

    def start(self):
        self.service.start(self.tmp.name)
        self.console.start()

    def stop(self):
        self.service.stop()
        self.console.stop()

    def logging(self):
        label = self.root.ids['console']
        while True:
            self.tmp.seek(self.tmp.tell())
            text = self.tmp.read()
            if text != '':
                label.text += text
            sleep(0.1)


if __name__ == '__main__':
    DjandroApp().run()
