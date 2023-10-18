import sched
import time
from problems import problems_from_severity
from hosts_problems import make_api_request

scheduler = sched.scheduler(time.time, time.sleep)
host_info = None  
s = sched.scheduler(time.time, time.sleep)

def host_problemas(make_api_request):
    return lambda: make_api_request

def wrapper_function(host_info):
    return lambda: problems_from_severity(host_info)

def verification_timer(host_info, s):
    if host_info is None:
        host_info = make_api_request()  #apenas se host_info for None

    if host_info:
        print(f'Tempo: {time.ctime()}')
        action = wrapper_function(host_info)
        host_problemas_function = host_problemas(make_api_request)
        
        s.enter(5, 1, host_problemas_function, ())  # Agenda 1
        s.enter(5, 2, action, ())  # Agenda 2


while True:
    verification_timer(host_info, s)
    s.run()
    time.sleep(5)
