import arcade
from grid_layer import GridLayer


class ClickPointWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.points = []

    def on_mouse_press(self, x, y, button, modifiers):
        self.points.append((x, y))

    def on_draw(self):
        arcade.start_render()
        for point in self.points:
            arcade.draw_circle_filled(point[0], point[1], 5, arcade.color.RED)
