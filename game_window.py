import arcade
from player import Player
from grid_layer import GridLayer
from CoordinateLayer import ClickPointWindow 



class MyGameWindow(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "My Game")
        
        # Grid properties
        self.grid_layer = GridLayer(grid_size=50, window_width=800, window_height=600)

        # Coordinate layer
        self.coordinate_layer = ClickPointWindow()
        
        # Create the player object and pass the coordinate_layer instance
        self.player = Player(self.coordinate_layer)
        self.player.start_at_coordinate(7, 7, 7)

        
        # Load the background texture
        self.background_texture = arcade.load_texture(r"C:\Users\Rookie\Google Drive\Menjivar Company\Crypto\Doge_Game\images\Market_View.jpg")
        self.nft_image_path = r"C:\Users\Rookie\Google Drive\Menjivar Company\Crypto\Doge_Game\668.png"
        self.nft_texture = arcade.load_texture(self.nft_image_path)
        assert self.nft_texture is not None, "Failed to load NFT texture"
        
        self.player.start_at_coordinate(7, 7, 7)
        
        self.action_window = None

    def on_draw(self):
        arcade.start_render()

        # Draw the background image
        arcade.draw_texture_rectangle(
            self.width // 2,
            self.height // 2,
            self.width,
            self.height,
            self.background_texture
        )
        
        
        self.grid_layer.draw()

        # Draw the player's NFT image
        self.player.draw(self.nft_texture)
        
        self.coordinate_layer.draw()


    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player.move(0, 5, -5)  # Move along y-axis and decrease z-coordinate
        elif key == arcade.key.DOWN:
            self.player.move(0, -5, 5)  # Move along y-axis and increase z-coordinate
        elif key == arcade.key.LEFT:
            self.player.move(-5, 0, 0)  # Move along x-axis
        elif key == arcade.key.RIGHT:
            self.player.move(5, 0, 0)  # Move along x-axis
        if key == arcade.key.SPACE:
            self.grid_layer.is_building = True
            
        if key == arcade.key.E and modifiers == arcade.key.MOD_CTRL:
            self.open_act

    def on_key_release(self, key, modifiers):
        if (
            key == arcade.key.UP
            or key == arcade.key.DOWN
            or key == arcade.key.LEFT
            or key == arcade.key.RIGHT
        ):
            self.player.move(0, 0, 0)  # Stop the movement when key is released
            

    def open_action_window(self):
        if self.action_window is None:
            self.action_window = ActionWindow(self)
            
    def close_action_window(self):
        if self.action_window is not None:
            self.action_window.close()
            self.action_window = None

    def on_mouse_press(self, x, y, button, modifiers):
        if self.grid_layer.is_building:
            grid_x = x // self.grid_layer.grid_size
            grid_y = y // self.grid_layer.grid_size
           # coordinate = (grid_x, grid_y)
            #self.grid_layer.coordinates.append(coordinate)
            #print("Traced Coordinates:", self.grid_layer.coordinates)
            #self.grid_layer.is_building = False

    def on_update(self, delta_time):
        self.player.update()


