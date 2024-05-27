from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        # Create a button widget
        button = Button(text='Click Me!')
        # Bind the button's on_press event to the callback method
        button.bind(on_press=self.on_button_click)
        return button

    def on_button_click(self, instance):
        # Callback method to be executed when the button is clicked
        print("Button clicked!")


MyApp().run()