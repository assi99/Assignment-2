from .students_manager import StudentsManager
from .reminder_generator import generate_reminder
from .reminder_sender import send_reminder
from .logger import log_reminder
from . import scheduler as sched
import argparse

def main():
    p=argparse.ArgumentParser(); p.add_argument('--students-json',default='students.json');
    sub=p.add_subparsers(dest='cmd', required=False)
    sub.add_parser('list'); a=sub.add_parser('add'); a.add_argument('name'); a.add_argument('email'); a.add_argument('course'); a.add_argument('preferred_time', nargs='?', default='08:00');
    r=sub.add_parser('remove'); r.add_argument('name'); sub.add_parser('send-once'); sub.add_parser('schedule')
    args=p.parse_args(); sm=StudentsManager(args.students_json)
    if args.cmd=='list' or args.cmd is None:
        sm.list_students(); return
    if args.cmd=='add':
        sm.add_student(args.name,args.email,args.course,args.preferred_time); print(f"Added {args.name}"); return
    if args.cmd=='remove':
        sm.remove_student(args.name); print(f"Removed {args.name}"); return
    if args.cmd=='send-once':
        for s in sm.get_students():
            r=generate_reminder(s['name'], s['course']); send_reminder(s['email'], r); log_reminder(s, r, logfile=os.path.join(os.path.dirname(args.students_json),'reminder_log.txt'))
        print('Sent reminders once.'); return
    if args.cmd=='schedule':
        print('Starting scheduler...'); sched.schedule_reminders(sm, generate_reminder, send_reminder, log_reminder, loop=True)

if __name__=='__main__':
    main()
