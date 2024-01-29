import datetime
from modules import *
from taskbox import TaskBox
from create_task import AddButton, TaskField, TasksBox
from popup import PopupWidget

class ScrollBox(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, 1)

class MainWidget(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.task_b = None
        # self.tasks = []
        self.cols = 1
        self.spacing = dp(10)
        self.padding = dp(20)
        self.size_hint = (1, 1)
        self.bind(size=lambda instance, value: self.update_size(instance, value, (1, 1, 1)))
        self.btn_height = dp(40)
        self.text_value = ""
        self.tasks_height = 100

        add_button = AddButton(self.btn_height).create()
        self.task_field = TaskField(self.btn_height).create()
        add_button.bind(on_press=self.create_task)
        # add_button.bind(on_press=self.create_task)
        self.task_field.bind(on_text_validate=self.create_task)

        self.task_field.bind(text=self.get_value)

        # text input + submit button
        box = BoxLayout(size_hint=(1, None), height=self.btn_height, orientation="horizontal")

        box.spacing = dp(20)
        box.add_widget(self.task_field)
        box.add_widget(add_button)
        self.add_widget(box)

        self.tasks_box = TasksBox()
        self.tasks_box.bind(size=self.focus_on_entry)
        scroll_box = ScrollBox()
        scroll_box.add_widget(self.tasks_box)

        self.add_widget(scroll_box)
        add_button.bind(on_press=self.entry_focus)

        tasks = Todo().tasks
        if tasks:
            for task in tasks:
                self.add_task([task])

    def entry_focus(self, *args):
        self.task_field.focused = True
    def focus_on_entry(self, *args):
        self.task_field.focused = True
    def get_value(self, instance, value):
        self.text_value = value
    def create_task(self, instance):
        todo = Todo()
        if len(self.text_value) > 2:
            todo.create_task(self.text_value, d.datetime.now().strftime("%Y-%m-%d %H:%M"), "Todo")
            self.add_task(todo.get_tasks())
            self.task_field.text = ""
        else:
            print("Please write a task! Contains more than 4 characters!")

    def add_task(self, tasks):
        task = tasks[len(tasks)-1]
        self.task_b = TaskBox(task["id"], task["name"], task["date"], task["status"], self.btn_height).create_box()
        self.tasks_box.add_widget(self.task_b)
        self.task_b.children[1].bind(on_press=self.show_pop)
    def update_size(self, instance, value, color):
        with instance.canvas.before:
            instance.canvas.before.clear()
            Color(*color)
            Rectangle(size=value, pos=instance.pos)
    def show_pop(self, instance, *args):
        id, status = instance.parent.children[1].id, instance.parent.children[2].text
        popup = PopupWidget(instance.text, status, id, self.tasks_box)
        popup.open()
class TodoApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def build(self):
        Window.size = (450, 720)
        return MainWidget()

TodoApp().run()
