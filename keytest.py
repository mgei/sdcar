import keyboard

count = 0

while True:
    if keyboard.is_pressed('s'):
        count += 1
        print(count)
