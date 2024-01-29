from modules import *

class TaskField:
    def __init__(self, height):
        self.height = height
    def create(self):
        field = TextInput(multiline=False, size_hint=(.75, None), height=self.height, font_size=dp(22),text_validate_unfocus=False, cursor_color=(235/255, 235/255, 235/255, 1), foreground_color=(135/255, 135/255, 135/255, 1))
        field.bind(height=field.setter("height"))
        return field
class AddButton:
    def __init__(self, height):
        self.height = height
    def create(self):
        btn = Button(text="Add", size_hint=(.2, None), height=self.height, background_color=(0, 0, 1, 1), color=(1, 1, 1, 1))
        return btn

class TasksBox(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, None)
        self.cols = 1
        self.spacing = dp(20)
        self.bind(minimum_height=self.setter("height"))
