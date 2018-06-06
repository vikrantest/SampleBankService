import time
import datetime

def get_time(datetime_obj = None):
	"""
	Get current epoch time or convert given datetime to epoch time
	"""
	if not datetime_obj:
		return int(time.time())
	else:
		return datetime_obj.strftime('%s')

def get_local_datetime(unixtime):
	"""
	Get Local adtetime object from epoch time
	"""
	return datetime.datetime.strptime(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(unixtime)),'%Y-%m-%d %H:%M:%S')

def get_local_day_start_end(unixtime):
	"""
	get local day start and end hours
	"""
	datetime_obj = get_local_datetime(unixtime)
	start_time = unixtime - ((datetime_obj.hour*60*60)+(datetime_obj.minute*60)+datetime_obj.second)
	end_time = start_time + (24*60*60)-1
	return start_time,end_time

