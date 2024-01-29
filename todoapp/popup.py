from modules import *

class PopupWidget(Popup):
    def __init__(self, text, current_status, id, tasksbox, **kwargs):
        super().__init__(**kwargs)
        self.current_status = current_status
        self.id = id
        self.tasksbox = tasksbox

        self.title = "Edit Panel"
        self.background = "./white.jpg"
        self.title_color = (0, 0, 0, .78)
        self.size_hint = (1, None)
        self.height = dp(350)
        self.pos_hint = {"center_x": .5, "center_y": .5}
        self.auto_dismiss = False

        grid_box = GridLayout(cols=1, size_hint=(1, 1), spacing=dp(5))
        box_lay1 = BoxLayout(orientation="horizontal", size_hint=(1, .3))
        box_lay2 = BoxLayout(orientation="horizontal", size_hint=(1, .3))
        box_lay3 = BoxLayout(orientation="horizontal", size_hint=(1, .3))
        self.box_lay4 = BoxLayout(orientation="horizontal", size_hint=(1, .3))
        self.text_field = TextInput(text=text, size_hint=(1, None), height=dp(100), font_size=dp(20), cursor_color=(235/255, 235/255, 235/255, 1), foreground_color=(135/255, 135/255, 135/255, 1))
        box_lay2.spacing = dp(15)

        delete_button = Button(text="Delete", background_normal="", background_color=(245/255, 44/255, 56/255, 1), color=(1, 1, 1, 1), on_press=self.delete_task)
        save_button = Button(text="Save", background_normal="", background_color=(27/255, 207/255, 96/255), color=(1, 1, 1), on_press=self.save_changes)
        exit_button = Button(text="Exit", background_normal="", background_color=(199/255, 199/255, 199/255), color=(0, 0, 0, 1), on_press=self.close_popup)

        # list style
        self.seleted_op = current_status
        status = ["Todo", "Doing", "Done"]
        self.box_lay4.spacing = dp(20)
        for s in status:
            btn = Button(text=s, background_normal="", background_color=(219/255, 241/255, 255/255, 1), color=(35/255, 68/255, 89/255, 1), on_press=self.select_options)
            if s.lower() == current_status.lower():
                btn.background_color = (35/255, 68/255, 89/255, 1)
                btn.color = (1, 1, 1, 1)
            self.box_lay4.add_widget(btn)

        box_lay1.add_widget(self.text_field)
        box_lay2.add_widget(delete_button)
        box_lay2.add_widget(save_button)
        box_lay3.add_widget(exit_button)

        grid_box.add_widget(box_lay1)
        grid_box.add_widget(self.box_lay4)
        grid_box.add_widget(box_lay2)
        grid_box.add_widget(box_lay3)
        self.add_widget(grid_box)
    def close_popup(self, *args):
        self.dismiss()
    def select_options(self, instance):
        for child in self.box_lay4.children:
            child.background_color = (219/255, 241/255, 255/255, 1)
            child.color = (35/255, 68/255, 89/255, 1)
        instance.background_color = (35/255, 68/255, 89/255, 1)
        instance.color = (1, 1, 1, 1)
        self.seleted_op = instance.text
    def save_changes(self, *args):
        is_saved = False
        for task in self.tasksbox.children:
            if task.children[1].id == self.id:
                task.children[1].text = self.text_field.text.replace("\n", " ")
                task.children[2].text = self.seleted_op
                is_saved = True
                break
        if is_saved:
            Todo().edit_task_name(self.id, self.text_field.text.replace("\n", " "))
            Todo().edit_tasks_status(self.id, self.seleted_op)
            self.dismiss()
    def delete_task(self, *args):
        is_deleted = False
        for task in self.tasksbox.children:
            if task.children[1].id == self.id:
                self.tasksbox.remove_widget(task)
                is_deleted = True
                break
        if is_deleted:
            Todo().delete_task(self.id)
            self.dismiss()

