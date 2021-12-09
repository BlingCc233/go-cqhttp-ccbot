import json

import requests
import re
import random

'下面这个函数用来判断信息开头的几个字是否为关键词'
'如果是关键词则触发对应功能，群号默认为空'
def keyword_pr(message, uid):
    if message[0:1] == '火': 
        xuhuo(uid)
    if message[0:2] == '复读':
        fudu(message,uid)
    if message[0:1] == '在':
        hello(uid)
    if message == '/help':
        help(uid,gid)
     
#违禁词
bans = ['科学上网', '傻逼' , '艹', '卧槽' ,'woc']
#管理群
groups = [697904286,701436956]

def keyword_gr(message, drawback_msg, uid, gid):
    if message == '/help':
        help(uid,gid)
    if message[0:2] == '复读':
        fudu(message,uid,gid)
    for group in groups:
        if gid == group:
            for ban in bans:
                if ban in message:
                    drawback(drawback_msg,uid,gid)





#功能
def xuhuo(uid):
	requests.get(url='http://127.0.0.1:12333/send_private_msg?user_id={0}&message=火'.format(uid))

def fudu(message,uid,gid):
    if gid != None:
        requests.get(url='http://127.0.0.1:12333/send_group_msg?group_id={0}&message={1}'.format(gid,r'[CQ:at,' r'qq=' + str(uid) + r']' + message[2: ]))
    else:
        requests.get(url='http://127.0.0.1:12333/send_private_msg?user_id={0}&message={1}'.format(uid,message[2: ]))

def hello(uid):
    msg = 'Cc不在，我是机器人'
    requests.get(url='http://127.0.0.1:12333/send_private_msg?user_id={0}&message={1}'.format(uid,r'[CQ:face,id=181]'))
    
def help(uid,gid):
    msg = '我是Cc的机器人，暂时冇有任何功能：\n 回复" 在 "可以续火，在特定群可以管理并撤回违禁词，回复" 复读XXX "可以复读'
    if gid != None:
        requests.get(url='http://127.0.0.1:12333/send_group_msg?group_id={0}&message={1}'.format(gid,msg))
    else:
        requests.get(url='http://127.0.0.1:12333/send_private_msg?user_id={0}&message={1}'.format(uid,msg))
    
def drawback(msg_id,uid,gid):
    msg = ' 请注意言行'
    requests.get(url='http://127.0.0.1:12333/delete_msg?message_id={0}'.format(msg_id))
    requests.get(url='http://127.0.0.1:12333/send_group_msg?group_id={0}&message={1}'.format(gid,r'[CQ:at,' r'qq=' + str(uid) + r']' + msg))