from datetime import datetime, timedelta, timezone

print('The program is used to display realtime for Beijing/Tokyo/London.')
addr = input('Please select a place: ')
addr_list = ('Beijing', 'Tokyo', 'London')
if addr not in addr_list:
    print('Sorry,you can only chose from Beijing/Tokyo/London.')
else:
    if addr == 'Beijing':
        print('北京时间：%s' % datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(
            timezone(timedelta(hours=8))).strftime('%Y-%m-%d %H:%M:%S'))
    elif addr == 'Tokyo':
        print('东京时间：%s' % datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(
            timezone(timedelta(hours=9))).strftime('%Y-%m-%d %H:%M:%S'))
    elif addr == 'London':
        print('伦敦时间：%s' % datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(
            timezone(timedelta(hours=0))).strftime('%Y-%m-%d %H:%M:%S'))        