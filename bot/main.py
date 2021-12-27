__author__ = 'BlingCc'

from flask import Flask, request

import api

app = Flask(__name__)

'''监听端口获取QQ信息'''
@app.route('/', methods=["POST"])



def post_data():
	superid = 1342171891#超级管理员，请修改为自己的

	
	if _get('msg_tp')=='private': # 如果是私聊信息		
		uid = _get('uuid') # 获取信息发送者的QQ号码
		message = _get('msg')# 获取原始信息
		api.keyword_pr(message, uid) # 将 Q号和原始信息传到我们的后台
		api.forward(message, uid)
		
		
	if _get('msg_tp')=='group':# 如果是群聊信息
		gid = _get('gid') # 获取群号
		uuid = _get('uuid') # 获取信息发送者的QQ号码
		message = _get('msg') # 获取原始信息
		msgid = _get('msgid') #获取撤回消息id
		api.keyword_gr(message, msgid, uuid, gid) # 将Q号和原始信息传到我们的后台
		
	if _get('ntc_tp')=='group_recall':#群撤回
		gid = _get('gid')
		guid = _get('guid') # 获取信息发送者的QQ号码
		opid = _get('opid') #获取操作者ID
		if opid == guid:
			msgid = _get('msgid')
			api.anti_recall(msgid ,guid ,gid,None)
	
	if _get('ntc_tp')=='friend_recall':#好友撤回
		uid = request.get_json().get('user_id')
		stid = superid
		msgid = _get('msgid')
		api.anti_recall(msgid ,uid, None, stid)
		
	if _get('ntc_tp')=='group_increase':#加群欢迎
		uid = _get('guid')
		gid = _get('gid')
		api.gr_increase(gid,uid)
    	
	return 'OK'

def _get(type):
	if type == 'ntc_tp':
		return request.get_json().get('notice_type')
	if type == 'msg_tp':
		return request.get_json().get('message_type')
	if type == 'uuid':
		return request.get_json().get('sender').get('user_id')
	if type == 'guid':
		return request.get_json().get('user_id')
	if type == 'gid':
		return request.get_json().get('group_id')
	if type == 'opid':
		return request.get_json().get('operator_id')
	if type == 'msgid':
		return request.get_json().get('message_id')
	if type == 'msg':
		return request.get_json().get('raw_message')
		
	

if __name__ == '__main__':
	app.run(debug=True, host='127.0.0.1', port=22334)# 此处的host和port对应 yml文件的设置

