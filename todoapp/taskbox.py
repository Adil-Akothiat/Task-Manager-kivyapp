from modules import *
from popup import PopupWidget

class TaskBox:
    def __init__(self, id, name, date, status, height):
        self.id = id
        self.name = name
        self.date = date
        self.status = status
        self.height = height
    def create_box(self):
        task_box = BoxLayout(size_hint=(1, None), height=self.height)
        task_box.spacing = dp(5)

        # task_id = Button(text=f"{self.id}", size_hint=(.1, None), height=self.height, background_normal='', background_color=(0, .6, 1), color=(1, 1, 1))
        task_status = Button(text=f"{self.status}", size_hint=(.2, None), height=self.height, background_normal='', background_color=(.5, 1, .5), color=(0, 0, 0))
        task_name = Button(text=self.name, valign="middle", halign="left", size_hint=(.65, None), height=self.height, background_normal='', background_color=(230/255, 230/255, 230/255), color=(0, 0, 0), padding=dp(10))
        task_name.id = f"{self.id}"
        task_date = Button(text=f"{self.date}", size_hint=(.35, None), height=self.height, background_normal='', background_color=(0, 0, 0, .1), color=(0, 0, 0), font_size=dp(12), padding=dp(5), valign="middle", halign="center")

        task_name.bind(size=task_name.setter("text_size"))
        task_date.bind(size=task_date.setter("text_size"))

        # task_box.add_widget(task_id)
        task_box.add_widget(task_status)
        task_box.add_widget(task_name)
        task_box.add_widget(task_date)
        return task_box

    def on_touch(self, touch, instance):
        if instance.collide_point(*touch.pos):
            return True
