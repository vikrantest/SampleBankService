import time
import datetime

def get_time(datetime_obj = None):
	if not datetime_obj:
		return int(time.time())
	else:
		return datetime_obj.strftime('%s')

def get_local_datetime(unixtime):
	return datetime.datetime.strptime(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(unixtime)),'%Y-%m-%d %H:%M:%S')

def get_local_day_start_end(unixtime):
	datetime_obj = get_local_datetime(unixtime)
	start_time = unixtime - ((datetime_obj.hour*60*60)+(datetime_obj.minute*60)+datetime_obj.second)
	end_time = start_time + (24*60*60)-1
	return start_time,end_time

