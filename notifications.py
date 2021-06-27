from plyer import notification
import time
import datetime

def pushNotification():
    notification.notify(
        title=f'Reminder set for {time}',
        message=msg,
        timeout=15,
    )
