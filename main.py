
main.py
from kivy.app import App
from kivy.uix.label import Label

class BlueScanApp(App):
    def build(self):
        return Label(
            text="BlueScan\nBluetooth Scanner",
            font_size=30
        )

BlueScanApp().run()