# Module used to show notification
from plyer import notification

# Setting the Timer on notifications
import time

# Looping over the messages
while True:
    notification.notify(
        title='Hydration Reminder!', #Title of the notification
        message='Time to drink water and stay hydrated!',  #Message provided in the note
        app_name='Health Notifier', #App name
        app_icon = 'D:/Courses/Python/Course Files/Projects/DesktopNotifier/icon.ico',
        timeout=10  # Duration in seconds
    )
    time.sleep(60 * 60)  # Wait for 1 hour before showing again


# If you want to make the code always running in background then type this command in the terminal:
# pythonw notification.py

# Close this automation from the task manager