import json

import requests
import re
import random

#状态 1为自动回复 0为关键词模式 默认为0
status = 0

def keyword_pr(message, uid):
    if status == 0:
        if message[0:1] == '火': 
            xuhuo(uid)
        if message[0:2] == '复读':
            fudu_pr(message,uid)
        if message[0:1] == '在':
            hello(uid)
        if message == '/help':
            help(uid,None)
        if message[0:9] == '/feedback':
            feedback(message,uid,None)
        if message[0:7] == '/status':
            set_status(message,uid)
    if status == 1:
        if message[0:7] == '/status':
            set_status(message,uid)
        ignore(uid)
     
#违禁词
bans = ['妈卖批','科学上网', '傻逼' , '艹', '卧槽' ,'woc']
#管理群
groups = [697904286,701436956,877201026]

def keyword_gr(message, drawback_msg, uid, gid):
    if message == '/help':
        help(uid,gid)
    if message[0:2] == '复读':
        fudu_gr(message,uid,gid)
    if message[0:9] == '/feedback':
        feedback(message,uid,None)
    if gid in groups:
        for ban in bans:
            if ban in message:
                drawback(drawback_msg,uid,gid)


#上报地址
uurl = 'http://127.0.0.1:22333'

#功能
#自动续火
def xuhuo(uid):
	requests.get(url=uurl+'/send_private_msg?user_id={0}&message=火'.format(uid))

#复读机
def fudu_gr(message,uid,gid):
    requests.get(url=uurl+'/send_group_msg?group_id={0}&message={1}'.format(gid,r'[CQ:at,' r'qq=' + str(uid) + r']' + message[2: ]))

#复读机，因为优化问题写了两个，不改了
def fudu_pr(message,uid):
    requests.get(url=uurl+'/send_private_msg?user_id={0}&message={1}'.format(uid,message[2: ]))

#去他妈的“在”
def hello(uid):
    for 1 in 10 :
        requests.get(url=uurl+'/send_private_msg?user_id={0}&message={1}'.format(uid,r'[CQ:face,id=181]'))

#菜单？    
def help(uid,gid):
    msg = '我是Cc的机器人，暂时冇有任何功能：\n1.私聊回复" 在 "可以续火\n2.在特定群可以当管理并撤回违禁词。\n3.回复" 复读XXX "可以复读'
    if gid != None:
        requests.get(url=uurl+'/send_group_msg?group_id={0}&message={1}'.format(gid,msg))
    else:
        requests.get(url=uurl+'/send_private_msg?user_id={0}&message={1}'.format(uid,msg))
    
#群聊撤回    
def drawback(msg_id,uid,gid):
    msg = ['富强','民主','文明','和谐','自由','平等','公正','法治','爱国','敬业','诚信','友善']
    rand = random.randint(0,11)
    requests.get(url=uurl+'/delete_msg?message_id={0}'.format(msg_id))
    requests.get(url=uurl+'/send_group_msg?group_id={0}&message={1}'.format(gid,r'[CQ:at,' r'qq=' + str(uid) + r']' + '已撤回违禁词。\n学习社会主义核心价值观：' + msg[rand]))
 
#状态设置       
def set_status(message,uid):
    getnum = message[8:9]
    statu = int(getnum)
    global status
    if statu == 1 or statu == 0 :
        status = statu
        requests.get(url=uurl+'/send_private_msg?user_id={0}&message={1}'.format(uid,'已设置为状态 ' + str(statu)))
    
#自动回复    
def ignore(uid):
    msg = 'Cc不在，我是机器人，你可以更改status码来调教我'
    requests.get(url=uurl+'/send_private_msg?user_id={0}&message={1}'.format(uid, msg))
    
#自动反馈    
def feedback(message,uid,gid):
    f = open("feedback.txt","a")
    f.write(message[9: ] + '\n \n')
    f.close()
    if gid != None:
        requests.get(url=uurl+'/send_group_msg?group_id={0}&message={1}'.format(gid,r'[CQ:at,' r'qq=' + str(uid) + r']' + '已反馈。'))
    else:
        requests.get(url=uurl+'/send_private_msg?user_id={0}&message={1}'.format(uid,"已反馈。"))