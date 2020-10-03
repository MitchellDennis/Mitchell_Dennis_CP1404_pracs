
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
# from kivy.properties import StringProperty

NAMES = ["Meliodas", "Ban", "King", "Diane", "Elizabeth"]

class dynamic_labels(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = NAMES

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_lables.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_label = Label(text=name, id=name)
            self.root.ids.entries_box.add_widget(temp_label)

dynamic_labels().run()