

import arcade
from grid_layer import GridLayer
from CoordinateLayer import ClickPointWindow

class ActionEditWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, "Layer Edit Buttons")
        self.grid_layer = GridLayer(grid_size=50, window_width=width, window_height=height)
        self.coordinate_layer = CoordinateLayer()

    def on_draw(self):
        arcade.start_render()
        self.grid_layer.draw()
                # Load the background texture
        self.background_texture = arcade.load_texture(r"C:\Users\Rookie\Google Drive\Menjivar Company\Crypto\Doge_Game\images\Enter.jpg")
        self.enter_image_path = r"C:\Users\Rookie\Google Drive\Menjivar Company\Crypto\Doge_Game\668.png"
        self.enter_texture = arcade.load_texture(self.enter_image_path)
        assert self.enter_texture is not None, "Failed to load Enter texture"
        
        self.coordinate_layer.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if x > button_grid_layer_x and x < button_grid_layer_x + button_width and y > button_grid_layer_y and y < button_grid_layer_y + button_height:
            self.grid_layer.edit()
        elif x > button_coordinate_layer_x and x < button_coordinate_layer_x + button_width and y > button_coordinate_layer_y and y < button_coordinate_layer_y + button_height:
            self.coordinate_layer.edit()
