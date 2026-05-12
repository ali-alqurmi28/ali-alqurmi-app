from kivy.app import App
from kivy.uix.label import Label

class AlQurmiApp(App):
    def build(self):
        return Label(
             text='تطبيق علي القورمي\nجاهز للنشر'
            font_size='32sp',
            halign='center'
        )

if __name__ == '__main__':
    AlQurmiApp().run()
