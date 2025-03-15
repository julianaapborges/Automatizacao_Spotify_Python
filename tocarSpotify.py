import pyautogui
import time

# aguardando um tempinho para começar
pyautogui.PAUSE = 0.5

# abrindo o aplicativo (Spotify)
pyautogui.press("win")
pyautogui.write("spotify")
pyautogui.press("enter")
time.sleep(10)

# pesquisando e clicando na playlist
pyautogui.hotkey("ctrl", "k")
pyautogui.write("top 50 brasil")
pyautogui.press("enter")
time.sleep(5)

# clicando para tocar a playlist
pyautogui.click(517, 432)
time.sleep(4)

# clicando para aumentar o volume
pyautogui.click(1694, 1043)
time.sleep(3)
pyautogui.click(1698, 990)
time.sleep(3)