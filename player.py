import arcade

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.width = 69
        self.height = 69
        self.depth = 0  # Added depth attribute
        self.change_x = 0
        self.change_y = 0
        self.change_z = 0  # Added change_z attribute
        #self.grid_layer = grid_layer  # Store the grid_layer instance
       
        
    def start_at_coordinate(self, x, y, z):
        self.x = x
        self.y = y 
        self.z = z
        
    def move(self, delta_x, delta_y, delta_z):
        self.change_x = delta_x
        self.change_y = delta_y
        self.change_z = delta_z

    def stop(self):
        self.change_x = 0
        self.change_y = 0
        self.change_z = 0


    def update(self):
        self.x += self.change_x
        self.y += self.change_y
        self.z += self.change_z

        # Define the boundary region
        boundary_left = self.grid_layer.grid_size // 2
        #boundary_right = self.grid_layer.window_width - self.grid_layer.grid_size // 2
        #boundary_bottom = self.grid_layer.grid_size // 2
        #boundary_top = self.grid_layer.window_height - self.grid_layer.grid_size // 2
       # boundary_depth = -200

        # Check boundaries
        if self.x - self.width / 2 < boundary_left:
            self.x = boundary_left + self.width / 2
            self.change_x = 0
        elif self.x + self.width / 2 > boundary_right:
            self.x = boundary_right - self.width / 2
            self.change_x = 0
        if self.y - self.height / 2 < boundary_bottom:
            self.y = boundary_bottom + self.height / 2
            self.change_y = 0
        elif self.y + self.height / 2 > boundary_top:
            self.y = boundary_top - self.height / 2
            self.change_y = 0
        if self.z < boundary_depth:
            self.z = boundary_depth
            self.change_z = 0

    def draw(self, nft_texture):
        scale = 1  # Keep a constant scale value
        width = self.width * scale
        height = self.height * scale

        # Calculate perspective scale based on z-coordinate
        perspective_scale = 1 / (1 - self.z / 200)

        x = self.x
        y = self.y - self.z  # Adjust the y-coordinate based on depth

        arcade.draw_texture_rectangle(
            x,
            y,
            self.width * perspective_scale,
            self.height * perspective_scale,
            nft_texture,
            0            
        )




