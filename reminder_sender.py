def send_reminder(email, reminder):
    if not email:
        raise ValueError('Email address is missing')
    print(f"Sending reminder to {email}: {reminder}")
