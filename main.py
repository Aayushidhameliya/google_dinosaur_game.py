import pyautogui as gui
import time
import keyboard
import math
from PIL import Image, ImageGrab


def get_pixel(image, x, y):
    px = image.load()
    return px[x, y]


def start():
    # set size of the image to be taken
    x, y, width, height = 0, 102, 1920, 872

    # calculating time
    jumping_time = 0
    last_jumping_time = 0
    current_jumping_time = 0
    last_interval_time = 0

    # interval for bot to find obstacles
    y_search1, y_search2, x_start, x_end = 557, 486, 400, 415
    y_search_for_bird = 460

    # allowing 3s to switch the interface to Google Chrome
    # after the program is executed
    time.sleep(3)
    try:
        while True:
            t1 = time.time()
            # press q to exit the robot
            if keyboard.is_pressed('q'):
                break

            sct_img = gui.screenshot(region=(x, y, width, height))

            # Convert the screenshot to grayscale for pixel color comparison
            sct_img_gray = sct_img.convert('L')
            #sct_img.save("dino.jpg")

            # Get the background color of the screenshot (top-left corner pixel)
            bg_color = sct_img_gray.getpixel((0, 0))

        # get the background color of the screenshot image
        #bg_color = get_pixel(sct_img, 100, 100)

            for i in reversed(range(x_start, x_end)):
                # color of the pixel does not match the
                # color of the background color
                if get_pixel(sct_img, i, y_search1) != bg_color \
                    or get_pixel(sct_img, i, y_search2) != bg_color:
                    keyboard.press('up')
                    jumping_time = time.time()
                    current_jumping_time = jumping_time
                    break
            if get_pixel(sct_img_gray, x_end, y_search_for_bird) != bg_color:
                keyboard.press("down")
                time.sleep(0.4)
                # press keyboard arrow down to duck
                keyboard.release("down")
                #break

            # Time between this jump and the last one
            interval_time = current_jumping_time - last_jumping_time

            # game is accelerating if the intervals not same
            if last_interval_time != 0 and math.floor(interval_time) != math.floor(last_interval_time):
                x_end += 4
                if x_end >= width:
                    x_end = width

            # get the last jump
            last_jumping_time = jumping_time
            # get the time between the last jump and the previous one
            last_interval_time = interval_time

            # Add a small delay to reduce the frequency of screenshots
            time.sleep(0.1)  # Adjust as needed for your game's speed

    except Exception as e:
        print(f"Error occured: {e}")

# Call the main function to start playing the game
if __name__ == "__main__":
    start()
