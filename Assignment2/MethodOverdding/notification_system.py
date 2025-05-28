class Notification:
    def send(self, message):
        print(f"Sending generic notification: {message}")

class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending email: {message}")

# Usage
notif = Notification()
notif.send("Hello!")

email = EmailNotification()
email.send("Welcome!")
