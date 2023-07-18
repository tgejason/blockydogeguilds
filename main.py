
import arcade
from game_window import MyGameWindow
import time
from LayerEditButtons import ActionEditWindow




class MainMenuWindow(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Main Menu")
        
    def on_draw(self):
        arcade.start_render()
        # Draw the main menu options
        
    def on_key_press(self, key, modifiers):
        if key == arcade.key.E:
            edit_window = LayerEditButtons()
            self.close()
        elif key == arcade.key.G:
            game_window = MyGameWindow()
            self.close()



def main():
    try:
        window = MyGameWindow()
        assert isinstance(window, MyGameWindow), "Failed to create MyGameWindow instance"
        time.sleep(0.20)  # Add a small delay
        arcade.run()
    except AssertionError as e:
        print("AssertionError occurred:")
        traceback.print_exc()



if __name__ == "__main__":
    main()
