import time

def get_time(datetime_obj = None):
	if not datetime_obj:
		return int(time.time())
