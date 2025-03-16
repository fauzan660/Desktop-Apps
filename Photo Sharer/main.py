from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
import time
import webbrowser

from file_sharer import FileSharer

Builder.load_file("frontend.kv")

class CameraScreen(Screen):
    def start(self):
        self.ids.camera.play = True
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        self.ids.camera.play = False
        self.ids.camera.texture = None

    def capture(self):
        current_time = time.strftime('%Y%m%d-%H%M%S')
        self.filename = f"Image Files/{current_time}.png"
        self.ids.camera.export_to_png(self.filename)
        self.manager.current = "image_screen"
        self.manager.current_screen.ids.img.source = self.filename

class ImageScreen(Screen):
    def create_link(self):
        """Accesses the photo filepath, uploads it to the web,
            and inserts the link in the label widget"""

        file_path = App.get_running_app().root.ids.camera_screen.filename
        filesharer = FileSharer(filepath = file_path)
        self.url = filesharer.share()
        self.ids.link.text = self.url
        self.ids.link.color = 1, 1, 1, 1
        self.ids.link.font_size = 24

    def copy_link(self):
        """   Copy the link   """
        try:
            Clipboard.copy(self.url)
        except:
            label = self.ids.link
            label.text = "Create a link first!"
            label.color = 1, 0, 0, 1
            label.font_size = 30

    def open_link(self):
        """   Open the link   """
        try:
            webbrowser.open(self.url)
        except:
            label = self.ids.link
            label.text = "Create a link first!"
            label.color = 1, 0, 0, 1
            label.font_size = 30



class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

MainApp().run()