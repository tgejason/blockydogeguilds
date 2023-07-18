import arcade

class GridLayer:
    def __init__(self, grid_size, window_width, window_height):
        self.grid_size = grid_size
        self.window_width = window_width
        self.window_height = window_height
        self.coordinates = []
        self.is_building = False

    def draw(self):
        # Draw the grid lines and coordinate annotations
        for x in range(0, self.window_width, self.grid_size):
            for y in range(0, self.window_height, self.grid_size):
                if (x // self.grid_size + y // self.grid_size) % 2 == 0:
                    arcade.draw_rectangle_outline(x, y, self.grid_size, self.grid_size, arcade.color.WHITE)
                    arcade.draw_text(f"({x // self.grid_size}, {y // self.grid_size})", x + self.grid_size // 2, y + self.grid_size // 2,
                                     arcade.color.WHITE, 12, anchor_x="center", anchor_y="center")
