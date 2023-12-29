import pyautogui as pt
from time import sleep
import subprocess
import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt
from PIL import Image
import cv2

def nav_to_image(image, clicks, off_x=0, off_y=0):
  position = pt.locateCenterOnScreen(image, confidence=0.9)

  if position is None:
    print(f'{image} not found')
    return 0
  else:
    pt.moveTo(position, duration=.1)
    pt.moveRel(off_x, off_y, duration=.1)
    pt.click(clicks=clicks, interval=.3)

def move_character(key_press, duration, action='walking'):
  pt.keyDown(key_press)

  if action == 'walking':
    print('Walking')
  elif action == 'attack':
    pt.keyDown('x')

  sleep(duration)
  pt.keyUp('x')
  pt.keyUp(key_press)

def locate_lava():
  position = pt.locateCenterOnScreen('images/lava.png', confidence=.5)

  if position is None:
    return False
  else:
    move_character('s', 2)
    print('found lava')
    return True
  

def main():
  start_game()
  duration = 0
  while duration != 0:
    # if not locate_lava():
    #   move_character('w',2,'attack')
    # else:
    #   break
    move_character(',', 2, 'attack')

    duration -= 1
    print('loops remaning: ', duration)

def start_game():
  load_dotenv()
  minecraft_launcher_path = os.getenv('MINECRAFTLAUNCHERPATH')
  # subprocess.Popen(minecraft_launcher_path) #start minecraft
  #wait for launcher to finish loading
  # sleep(20)
  image_path = r'MineBot\images\play.png'
  img = Image.open(image_path)
  img2 = cv2.imread(image_path)
  img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
  # plt.imshow(img2)
  # plt.axis('off')  # Turn off axis numbers
  # plt.show()  # Display the image
  # plt.imshow(img)
  # plt.axis('off')  # Turn off axis numbers
  # plt.show()

  #start minecraft
  try:
    # Locate the center of the image on screen
    location = pt.locateCenterOnScreen(img2, confidence=0.7)
    print("location: ", location)

    if location is not None:
      print("image found")
      pt.moveTo(location, duration=0.1)
      pt.click()
    else:
      print("Image not found on the screen.")
  except Exception as e:
    print(f"An error occurred: {e}")

if __name__ == "__main__":
  main()