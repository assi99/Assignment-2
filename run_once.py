import os
from study_reminders.students_manager import StudentsManager
from study_reminders.reminder_generator import generate_reminder
from study_reminders.reminder_sender import send_reminder
from study_reminders.logger import log_reminder
base=os.path.dirname(__file__)
sm=StudentsManager(os.path.join(base,'students.json'))
for s in sm.get_students():
    r=generate_reminder(s['name'], s['course'])
    send_reminder(s['email'], r)
    log_reminder(s, r, logfile=os.path.join(base,'reminder_log.txt'))
print('Sample run completed.')
