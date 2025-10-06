import schedule, time, datetime

def _norm(t):
    t=t.strip()
    try:
        hh,mm=t.split(':')[:2]
        if 'AM' in mm.upper() or 'PM' in mm.upper():
            raise ValueError
        return f"{int(hh):02d}:{int(mm):02d}"
    except:
        dt=datetime.datetime.strptime(t.upper().replace('.',''),'%I:%M %p')
        return dt.strftime('%H:%M')

def schedule_reminders(sm, gen, send, log, loop=True):
    for s in sm.get_students():
        r=gen(s['name'], s['course'])
        at=_norm(s.get('preferred_time','08:00'))
        def job(st=s, rr=r):
            send(st['email'], rr); log(st, rr)
        schedule.every().day.at(at).do(job)
    if not loop:
        schedule.run_all(delay_seconds=0); return
    while True:
        schedule.run_pending(); time.sleep(60)
