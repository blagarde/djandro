from kivy.app import App
from kivy.uix.button import Button
from android import AndroidService


class DjandroApp(App):
    def build(self):
        self.btn = Button(text='Start Django')
        self.btn.bind(on_press=self.toggle)
        self.service = AndroidService('Django', 'Django is running')
        self.running = False
        return self.btn

    def toggle(self, value):
        action = self.stop_service if self.running else self.start_service
        action()
        self.running = not self.running
        state = 'ON' if self.running else 'OFF'
        self.btn.text = "Django is " + state

    def start_service(self):
        self.service.start('')

    def stop_service(self):
        self.service.stop()

if __name__ == '__main__':
    DjandroApp().run()
