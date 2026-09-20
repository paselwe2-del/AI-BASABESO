from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Rectangle
import requests

class BasabesoApp(App):
    def build(self):
        # الخلفية الرئيسية - لون برغندي غامق
        self.root = BoxLayout(orientation='vertical', padding=10, spacing=10)
        with self.root.canvas.before:
            Color(0.3, 0.05, 0.1, 1)
            self.rect = Rectangle(size=(1000, 2000), pos=self.root.pos)

        # عنوان التطبيق
        title = Label(
            text="[b]AI BASABESO 🤖[/b]",
            markup=True,
            font_size='22sp',
            size_hint_y=None,
            height=50,
            color=(1, 0.85, 0.4, 1)
        )
        self.root.add_widget(title)

        # منطقة عرض المحادثة
        self.chat_label = Label(
            text="يا مرحب بيك مع بسبيسو! اكتب أي حاجة..\n",
            size_hint_y=None,
            font_size='16sp',
            color=(1, 1, 1, 1),
            halign='right',
            valign='top'
        )
        self.chat_label.bind(texture_size=self.chat_label.setter('size'))

        scroll = ScrollView(size_hint=(1, 1))
        scroll.add_widget(self.chat_label)
        self.root.add_widget(scroll)

        # منطقة الإدخال والزرار
        input_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=5)
        
        self.user_input = TextInput(
            hint_text="اكتب رسالتك هنا...",
            multiline=False,
            font_size='16sp'
        )
        send_btn = Button(
            text="ابعت",
            size_hint_x=0.25,
            background_color=(0.6, 0.1, 0.2, 1),
            color=(1, 1, 1, 1)
        )
        send_btn.bind(on_press=self.send_message)

        input_layout.add_widget(self.user_input)
        input_layout.add_widget(send_btn)
        self.root.add_widget(input_layout)

        return self.root

    def send_message(self, instance):
        msg = self.user_input.text.strip()
        if msg:
            self.chat_label.text += f"\nأنت: {msg}"
            self.user_input.text = ""
            self.chat_label.text += f"\nبسبيسو: حبيبي يا باسل، جاري تجهيز الرد البلدي الأصلي.. 😎\n"

if __name__ == '__main__':
    BasabesoApp().run()
