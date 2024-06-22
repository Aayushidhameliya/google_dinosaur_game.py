# Google Dinosaur Game Automation

This Python script (`play_game.py`) automates playing the Google Dinosaur Game using `pyautogui` for simulating key presses and `Pillow` for capturing screenshots.

### Usage

1. Ensure you have Python installed.
2. Install required libraries:
3. Run `play_game.py`.
4. Switch focus to the Google Chrome window running the Dinosaur Game within 3 seconds after starting the script.

### Notes

- Adjust the coordinates in `is_obstacle_present` function based on your screen resolution and the actual location of obstacles on your screen.
- Fine-tune the delay (`time.sleep(0.1)`) to match your system's processing speed and ensure accurate gameplay.
- Ensure the game window is visible and not covered by any other windows for the script to work correctly.
