import re
from datetime import datetime,timedelta,timezone

def to_timestamp(dt_str,tz_str):
    dt = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    tz = re.match(r'UTC([\+\-])(\d+):00',tz_str)
    if tz.group(1) == '+':
        dt_tz = dt.replace(tzinfo=timezone(timedelta(hours=int(tz.group(2)))))
        return dt_tz.timestamp()
    elif tz.group(1) == '-':
        dt_tz = dt.replace(tzinfo=timezone(timedelta(hours=-int(tz.group(2)))))
        return dt_tz.timestamp()
    
