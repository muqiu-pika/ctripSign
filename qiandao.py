# -*- coding: utf8 -*-
import requests
import json
def start():
    headers={
        "Content-Type": "application/json; charset=UTF-8"
    }
    url = "https://m.ctrip.com/restapi/soa2/16575/signin"
    pyload = {"openId":"96c1079b-fe61-4e97-82ea-37541ba889c1","activityId":"wechat_signin_activity","aid":"","sid":"","clickId":"","head":{"cid":"09031044311841901045","ctok":"","cver":"1.1.69","lang":"01","sid":"","syscode":"30","auth":"5DA45F4627AEC6C7190EF57E149C9B58A19BCD67763C29780B71DBC45FD9ECDC","sauth":"","extension":[{"name":"appId","value":"wx0e6ed4f51db9d078"},{"name":"scene","value":"1007"},{"name":"appId","value":"wx0e6ed4f51db9d078"},{"name":"scene","value":"1007"}]}}
    response = requests.post(url, data=json.dumps(pyload), headers=headers).text
    print(response)
    return response;
def main_handler(event, context):
    return start()
if __name__=='__main__':
    start();
