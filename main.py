import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title="Please Drink Water Now",
            message="It will help you to stay Hydrated.",
            app_icon="glassofwater.ico",
            timeout=10
        )
        time.sleep(20 * 60)