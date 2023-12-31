import pyautogui as pt
from time import sleep
import subprocess
import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt
from PIL import Image
import cv2
# import tkinter as tk

def nav_to_image(image, clicks, off_x=0, off_y=0, max_wait=20):
  while max_wait > 0 and position is not None:
    print("searching count down", max_wait)
    position = pt.locateCenterOnScreen(image, confidence=0.9)
    max_wait -= 1
    sleep(1)

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

def click_on_head(head_img = "", con = 0.7, wait = 0, attempts = 20):
  print("locating image")
  location = None
  while attempts > 0:
    print("search count down", attempts)
    try:
      # image_path = r'MineBot\images\play.png'
      # img = Image.open(image_path)
      img2 = cv2.imread(head_img)
      img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
      # Locate the center of the image on screen
      location = pt.locateCenterOnScreen(img2, confidence=con)
      print("location: ", location)

      if location is not None:
        print("image found")
        pt.moveTo(location, duration=0.1)
        pt.click()
        break
      else:
        print("Image not found on the screen.")
    except Exception as e:
      print(f"An error occurred: {e}")
    attempts -= 1
  sleep(wait)

def start_game():
  load_dotenv()
  print("start launcher")
  minecraft_launcher_path = os.getenv('MINECRAFTLAUNCHERPATH')
  subprocess.Popen(minecraft_launcher_path) #start minecraft
  #wait for launcher to finish loading
  sleep(20)
  print("click play button")
  click_on_head(r'MineBot\images\play.png')
  #start minecraft
  
  
  sleep(20)
  pt.hotkey('win', 'up') #maximize screen
  sleep(1)

  click_on_head(r'MineBot\images\multiplayer.png', 0.8, 1)
  # sleep(1)
  click_on_head(r'MineBot\images\direct_connection.png', 0.8, 1)
  click_on_head(r'MineBot\images\server_address.png', 0.7, 1)
  server_address = os.getenv('SERVER_ADDRESS')
  for i in range(50):
    pt.keyDown('backspace')
  # sleep(5)
  pt.keyUp('backspace')
  pt.write(server_address)
  click_on_head(r'MineBot\images\join_server.png', 0.8)

def main():
  start_game()
  duration = 10
  while duration != 0:
    print("Operating, durration:", duration)
    if not locate_lava():
      move_character('.',2,'attack')
    else:
      break
    move_character('e', 2, 'attack')

    duration -= 1
    print('loops remaning: ', duration)
  print("Automation Complete")

if __name__ == "__main__":
  main()