import sys
import os
from hosts_problems import make_api_request

diretorio_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

sys.path.append(diretorio_projeto)


from popup_api.ext.login_user import login_user_zabbix
from popup_api.ext.notification import show_notification
from popup_api.ext.timer_problem import calculate_duration
app_icon = "/home/alexsanderprates/Downloads/iconBravo.ico" #verificar
  
zapi = login_user_zabbix()
host_info = make_api_request()


def problems_from_severity(host_info):

    message_list = []  # Lista para armazenar mensagens de hosts com problemas

    index = 0
    while index < len(host_info):
        host_id, host_name = host_info[index]

        problems = zapi.problem.get({
            "acknowledged": False,
            "suppressed": False,
            "hostids": host_id,
            "severities": 4,
            
            
        })
   
        for problem in problems:
            problema_name = problem['name']
            problema_timer = problem['clock']
            formatted_duration = calculate_duration(problema_timer)
            
            print("-----------------------")
            host_message = f'Host: {host_name}\nProblema: {problema_name} ({formatted_duration})'
            message_list.append(host_message)
            print(message_list)
            
            
            show_notification(
                title="NOC Bravo",
                message=host_message,
                app_icon=app_icon
            )
                

        index += 1
    return message_list    