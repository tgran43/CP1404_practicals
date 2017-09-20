from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label


class DynamicWidgetsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre", "Dave", "Bill"]

    def build(self):
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_widgets.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.entriesBox.add_widget(temp_label)



DynamicWidgetsApp().run()
