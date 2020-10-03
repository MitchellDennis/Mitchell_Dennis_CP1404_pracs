from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

CONVERSION_FACTOR = 1.609

class convert_miles_km(App):
    def build(self):
        Window.size = (600, 300)
        self.title = "Convert from Miles to Km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root
    def handle_up(self, value):
        try:
            value = int(value)
            value += 1
            self.root.ids.input_number.text = str(value)
        except ValueError:
            self.root.ids.input_number.text = str("1")

    def handle_down(self, value):
        try:
            value = int(value)
            value -= 1
            self.root.ids.input_number.text = str(value)
        except ValueError:
            self.root.ids.input_number.text = str("-1")

    def convert(self, value):
        try:
            value = int(value)
            result = value * CONVERSION_FACTOR
            self.root.ids.output_label.text = str(result)

        except ValueError:
            self.root.ids.output_label.text = str("0")





convert_miles_km().run()