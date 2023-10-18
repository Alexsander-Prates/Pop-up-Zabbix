import requests
import sys
import os

diretorio_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

sys.path.append(diretorio_projeto)

from popup_api.ext.login_user import get_token

def make_api_request():

    api_url = 'http://192.168.0.248/zabbix/api_jsonrpc.php'
    api_method = 'host.get'
    api_params = {
        "output": ["name"],
        "severities": 4
    }
    auth_token = get_token()

    headers = {'Content-Type': 'application/json-rpc'}
    data = {
        "jsonrpc": "2.0",
        "method": api_method,
        "params": api_params,
        "auth": auth_token,
        "id": 1
    }
    
    try:
        response = requests.post(api_url, headers=headers, json=data)
        
        response.raise_for_status()  # erros HTTP
        if response.status_code == 200:
            result = response.json()
            response = result
            if response:
                print(response)  
                host_info = []
                for host in response['result']:
                    host_name = host['name']
                    host_id = host['hostid']
                    host_info.append((host_id, host_name))
                return host_info
            
        else:
            print("Resposta inesperada da API:", response.status_code, response.text)
            return None
    except Exception as e:
        print("Ocorreu um erro durante a solicitação:", str(e))
        return None
    

