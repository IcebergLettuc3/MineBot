import pyautogui as pt
from time import sleep
import subprocess
import os
from dotenv import load_dotenv

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
  
# sleep(10)
# nav_to_image('images/start_game.png', 3)

#open minecraft launcher
load_dotenv()
minecraft_launcher_path = os.getenv('MINECRAFTLAUNCHERPATH')
print("path: ",minecraft_launcher_path)
subprocess.Popen(minecraft_launcher_path)
#wait for launcher to finish loading
sleep(2)
#start minecraft
try:
    # Locate the center of the image on screen
    location = pt.locateCenterOnScreen('MineBot\images\play.png', confidence=0.7)
    
    if location is not None:
        # Move to the location and click
        pt.moveTo(location, duration=0.1)
        pt.click()
    else:
        print("Image not found on the screen.")
except Exception as e:
    print(f"An error occurred: {e}")

# pt.moveTo(pt.locateCenterOnScreen('images/play.png', confidence=.7), duration=.1)
# pt.click()

duration =0
while duration != 0:
  # if not locate_lava():
  #   move_character('w',2,'attack')
  # else:
  #   break
  move_character(',', 2, 'attack')

  duration -= 1
  print('loops remaning: ', duration)