__author__ = 'BlingCc'

import json
import requests
from flask import request
import re
import random

#状态 1为自动回复 0为关键词模式 默认为0
status = 0
#防撤回 1为开启
anti_status = 1
#超级管理员账号，请修改为自己的
superid = 2415364721


def keyword_pr(message, uid, msgid):
	if message[0:7] == '/status' or message[0:12] == '/anti_recall':
		set_status(message,uid)
	if 'type=flash' in message:
		flash(message, uid, None, msgid)
	if status == 0:
		if message[0:11] == '/opensource': 
			open_source(None,uid)
		if message[0:2] == '复读':
			fudu_pr(message,uid)
		if message[0:1] == '在':
			hello(uid)
		if message == '/help':
			help(uid,None)
		if message[0:9] == '/feedback':
			feedback(message,uid,None)
		if message[0:5] == '/setu':
			setu(message,None,uid)   
		if message[0:5] == '/send':
			send(message,uid)
	if status == 1:
		ignore(uid)
     
#违禁词
file = open("mingan_words.txt","r")
bans = []
line = file.readline()
while line :
	line=line.replace('\n','')
	b = str(line)
	bans.append(b)
	line = file.readline()
#管理群,请添加自己的
groups = [697904286,701436956,877201026]

def keyword_gr(message, msgid, uid, gid):
	flash(message, uid, gid, msgid)
	if message == '/help':
		help(uid,gid)
	if message[0:2] == '复读':
		fudu_gr(message,uid,gid)
	if message[0:9] == '/feedback':
		feedback(message,uid,gid)
	if message[0:5] == '/setu':
		setu(message,gid,uid)
	if message[0:11] == '/opensource': 
		open_source(gid,uid)
	if gid in groups:
		for ban in bans:
			if ban in message:
				drawback(msgid,uid,gid)


#上报地址
uurl = 'http://127.0.0.1:22333'

#功能
#源码
def open_source(gid,uid):
	if gid != None:
		requests.get(url=uurl+ '/send_group_msg?group_id={0}&message=https://gitee.com/blingcc/go-cqhttp-ccbot'.format(gid))
	else:
		requests.get(url=uurl+'/send_private_msg?user_id={0}&message=https://gitee.com/blingcc/go-cqhttp-ccbot'.format(uid))

#复读机
def fudu_gr(message,uid,gid):
	requests.get(url=uurl+'/send_group_msg?group_id={0}&message={1}'.format(gid,r'[CQ:at,' r'qq=' + str(uid) + r']' + message[2: ]))

#复读机，因为优化问题写了两个，不改了
def fudu_pr(message,uid):
	requests.get(url=uurl+'/send_private_msg?user_id={0}&message={1}'.format(uid,message[2: ]))

#去他妈的“在”
def hello(uid):
	for num in range(1,3) :
		requests.get(url=uurl+'/send_private_msg?user_id={0}&message={1}'.format(uid,r'[CQ:face,id=181]'))

#菜单？    
def help(uid,gid):
	msg = '我是Cc的开源机器人，暂时冇有任何功能：\n'
	msg += '1./setu \n'
	msg += '2./feedback \n'
	msg += '3.复读 XXX \n'
	msg += '4.防撤回 \n'
	msg += '5.防闪照 \n'
	msg += '6./opensource \n'
	msg += '7.定时发消息'
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
	if uid != superid:
		return
	if message[0:7] == '/status':
		statu = int(message[8:9])
		global status
		if statu == 1 or statu == 0 :
			status = statu
	if message[0:12] == '/anti_recall':
		global anti_status
		statu = int(message[13:14])
		if statu == 1 or statu == 0 :
			anti_status = statu
	requests.get(url=uurl+'/send_private_msg?user_id={0}&message={1}'.format(uid,'已设置为状态 ' + str(statu)))
    
#自动回复    
def ignore(uid):
	msg = ['老爹古董店，有事请留言',' Cc不在，他在为建设共产主义而努力学习','Cc不在，他又去摸鱼了']
	rand = random.randint(0,len(msg)-1)
	requests.get(url=uurl+'/send_private_msg?user_id={0}&message={1}'.format(uid, msg[rand]))
    
#自动反馈    
def feedback(message,uid,gid):
	f = open("feedback.txt","a")
	f.write(message[9: ] + '\n \n')
	f.close()
	if gid != None:
		requests.get(url=uurl+'/send_group_msg?group_id={0}&message={1}'.format(gid,r'[CQ:at,' r'qq=' + str(uid) + r']' + '已反馈。'))
	else:
		requests.get(url=uurl+'/send_private_msg?user_id={0}&message={1}'.format(uid,"已反馈。"))
        
#防撤回
def anti_recall(msgid, uid ,gid ,stid):
	if anti_status == 1:
		msg = requests.get(url=uurl+ '/get_msg?message_id={0}'.format(msgid))
		msg1 = json.loads(msg.text)
		msg2 = msg1.get("data").get("message")
		if gid != None and gid in groups:
			requests.get(url=uurl +'/send_group_msg?group_id={0}&message={1}'.format(gid, r'[CQ:at,' r'qq=' + str(uid) + r']' + ' 撤回无效，原文为：\n' + str(msg2)))
		else:
			requests.get(url=uurl +'/send_private_msg?user_id={0}&message={1}'.format(stid ,str(uid) + '\n' + str(msg2)))
		
#色图
def setu(message,gid,uid):
	menu = requests.get('https://api.lolicon.app/setu/v2'+str(message[6:]))
	#menu2 = menu.json()['data'][0]['urls']['regular']
	menu1 = json.loads(menu.text)
	menu3 = list(str(menu1))
	menu4 = menu3[::-1]
	menu5 = []
	i = 5
	while menu4[i] != "'":
		menu5.append(menu4[i])
		i+=1
	menu6 = menu5[::-1]
	menu2 = ""
	for o in menu6:
		menu2 += str(o)
	if gid != None:
		requests.get(url=uurl + '/send_group_msg?group_id={0}&message={1}'.format(gid, r'[CQ:image,' + r'file=' + str(menu2)+ r']'))
	else:
		requests.get(url=uurl+ '/send_private_msg?user_id={0}&message={1}'.format(uid,  r'[CQ:image,' + r'file=' + str(menu2) + r']'))
		
#指定回复
def send(msg,uid):
	msgl = list(str(msg[6:]))
	count = 0
	s_rcv_uid = ""
	for i in msgl:
		if str(i) == " ":
			break
		s_rcv_uid += str(i)
		count += 1
	rcv_uid = int(s_rcv_uid)
	sends = msg[count+6:]
	requests.get(url=uurl+ '/send_private_msg?user_id={0}&message={1}'.format(uid, "已发送"))
	requests.get(url=uurl+ '/send_msg?user_id={0}&message={1}'.format(rcv_uid , sends ))
	
#加群欢迎(验证)
def gr_increase(gid,uid):
	if gid in groups:
		msg = "\n欢迎入群，不许爆粗口、不许打广告哦。"
		requests.get(url=uurl + '/send_msg?group_id={0}&message={1}'.format(gid, r'[CQ:at,' r'qq=' + str(uid) + r']' + msg))
		
#转发私聊消息给超级管理
def forward(msg,uid):
	if uid != superid:
		requests.get(url=uurl+ '/send_msg?user_id={0}&message={1}'.format(superid,msg+'\nfrom.'+str(uid)))
		
#防闪照
def flash(msg,uid,gid,msgid):
	msg1 = requests.get(url=uurl+ '/get_msg?message_id={0}'.format(msgid))
	msg2 = json.loads(msg1.text)
	msg3 = msg2.get("data").get("message")
	msg4 = str(msg3)
	if gid != None and gid in groups:
		msg5 = msg4[:-28]
		menu3 = list(str(msg5))
		menu4 = menu3[::-1]
		menu5 = []
		i = 0
		while menu4[i] != "=":
			menu5.append(menu4[i])
			i+=1
		menu6 = menu5[::-1]
		menu2 = ""
		for o in menu6:
			menu2 += str(o)
		menu2 += r"term=2"
		requests.get(url=uurl +'/send_group_msg?group_id={0}&message={1}'.format(gid, r'[CQ:at,'+ r'qq='+str(uid)+r']' + ' 让我康康:\n' + r'[CQ:image,file=' +str(menu2) + r']'))
	else:
		msg5 = msg4[:-12]
		menu3 = list(str(msg5))
		menu4 = menu3[::-1]
		menu5 = []
		i = 0
		while menu4[i] != "=":
			menu5.append(menu4[i])
			i+=1
		menu6 = menu5[::-1]
		menu2 = ""
		for o in menu6:
			menu2 += str(o)
		msg5 = msg4[:-12] + r']'
		requests.get(url=uurl +'/send_private_msg?user_id={0}&message={1}'.format(superid ,str(uid) + '\n' + str(menu2)))
		
