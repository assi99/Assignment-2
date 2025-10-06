import datetime

def log_reminder(student, reminder, logfile='reminder_log.txt'):
    with open(logfile,'a',encoding='utf-8') as f:
        f.write(f"{datetime.datetime.now().isoformat(timespec='seconds')} - Sent to {student['name']}: {reminder}\n")
