from flask import Flask, request

'''注意，这里的import api是另一个py文件，下文会提及'''
import api

app = Flask(__name__)

'''监听端口获取QQ信息'''
@app.route('/', methods=["POST"])
def post_data():
	'下面的request.get_json().get......是用来获取关键字的值用的，关键字参考上面代码段的数据格式'
	if request.get_json().get('message_type')=='private': # 如果是私聊信息		
		uid = request.get_json().get('sender').get('user_id') # 获取信息发送者的QQ号码
		message = request.get_json().get('raw_message') # 获取原始信息
		api.keyword_pr(message, uid) # 将 Q号和原始信息传到我们的后台
	if request.get_json().get('message_type')=='group':# 如果是群聊信息
		gid = request.get_json().get('group_id') # 获取群号
		uid = request.get_json().get('sender').get('user_id') # 获取信息发送者的QQ号码
		message = request.get_json().get('raw_message') # 获取原始信息
		drawback_msg = request.get_json().get('message_id') #获取撤回消息id
		api.keyword_gr(message, drawback_msg, uid, gid) # 将Q号和原始信息传到我们的后台
    	
	return 'OK'


if __name__ == '__main__':
	app.run(debug=True, host='127.0.0.1', port=12334)# 此处的host和port对应上面 yml文件的设置

