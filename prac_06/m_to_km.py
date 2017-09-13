from kivy.app import App
from kivy.lang import Builder

MILES_TO_KILOMETERS = 1.60934


class MilesToKilometers(App):
    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('m_to_km.kv')

    def handle_convert(self, value):
        miles = validate_input(value)
        kilometers = miles * MILES_TO_KILOMETERS
        self.root.ids.output_label.text = str(kilometers)

    def handle_increment(self, increment):
        miles = validate_input(self.root.ids.input_miles.text)
        self.root.ids.input_miles.text = str(miles + increment)


def validate_input(value):
    try:
        miles = int(value)
    except ValueError:
        miles = 0

    return miles


MilesToKilometers().run()
