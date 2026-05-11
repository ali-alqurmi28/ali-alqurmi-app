from kivy.app import App
from kivy.uix.label import Label

class AliApp(App):
    def build(self):
        return Label(text='أهلاً يا علي من الضالع 🇾🇪\nتطبيقك الأول شغال 100%')

AliApp().run()
