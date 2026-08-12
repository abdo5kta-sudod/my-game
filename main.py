import time
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle

class GameMazeEngine(Widget):
    def __init__(self, **kwargs):
        super(GameMazeEngine, self).__init__(**kwargs)
        self.survivors_count = 4
        self.monster_active = True
        self.current_floor = 1
        self.timer_seconds = 600  # 10 Minutes
        self.monsters = ["Cartoon Cat", "Bendy", "Huggy Wuggy", "Warden (Minecraft)"]
        self.monster_index = 0
        
        Clock.schedule_interval(self.update_game_loop, 1.0)

    def update_game_loop(self, dt):
        if self.timer_seconds > 0:
            self.timer_seconds -= 1
        else:
            self.timer_seconds = 600
            self.monster_index = (self.monster_index + 1) % len(self.monsters)
            print(f"Monster evolved to: {self.monsters[self.monster_index]}")

class AsymmetricalHorrorGame(App):
    def build(self):
        root = BoxLayout(orientation='vertical')
        
        self.status_label = Label(
            text="Game Initializing...
4 Survivors vs 1 Monster",
            font_size='20sp',
            size_hint=(1, 0.2)
        )
        root.add_widget(self.status_label)
        
        self.game_widget = GameMazeEngine(size_hint=(1, 0.7))
        root.add_widget(self.game_widget)
        
        controls = BoxLayout(size_hint=(1, 0.1))
        btn_floor = Button(text="Switch Floor (Floor 1 / Floor 2)")
        btn_floor.bind(on_press=self.toggle_floor)
        controls.add_widget(btn_floor)
        
        root.add_widget(controls)
        
        Clock.schedule_interval(self.update_ui, 1.0)
        return root

    def toggle_floor(self, instance):
        if self.game_widget.current_floor == 1:
            self.game_widget.current_floor = 2
        else:
            self.game_widget.current_floor = 1

    def update_ui(self, dt):
        m_name = self.game_widget.monsters[self.game_widget.monster_index]
        mins = self.game_widget.timer_seconds // 60
        secs = self.game_widget.timer_seconds % 60
        floor = self.game_widget.current_floor
        
        self.status_label.text = (
            f"Current Floor: {floor} | Time Left: {mins:02d}:{secs:02d}\n"
            f"Active Monster: {m_name} | Survivors Alive: {self.game_widget.survivors_count}/4"
        )

if __name__ == '__main__':
    AsymmetricalHorrorGame().run()