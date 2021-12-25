<p align="center">
  <a href="https://www.pixiv.net/artworks/93066887">
    <img src="https://raw.githubusercontent.com/BlingCc233/go-cqhttp-ccbot/main/OtoAi.png" width="200" height="200" alt="Cc-bot">
  </a>
</p>

<div align="center">
  
# go-cqhttp-ccbot
> 🤖一个基于<a href="https://github.com/Mrs4s/go-cqhttp/releases">go-cqhttp</a>和Python的开箱即用的机器人

  <p align="center">
  <a href="https://github.com/BlingCc233/go-cqhttp-ccbot/releases">
    <img src="https://img.shields.io/github/v/release/BlingCc233/go-cqhttp-ccbot?color=blueviolet&include_prereleases&style=for-the-badge" alt="release">
  </a>
</p>

## 声明
一切开发旨在学习，请勿用于非法用途
</div>

## 启动
- 使用时仅需修改`/go-cqhttp/config.yml`中的账号密码，以及`/bot/main.py`与`/bot/api.py`中的高级管理员账号(请自行参考注释)
- 也可按需修改`/bot/api.py`中的管理群，欢迎语，<a href="#涩图">涩图API</a>等。（不改也能直接使用）
- 违禁词可以添加至`/bot/mingan_words.txt`中
- 需要用到的库(pip(3) install)：flask 和 requests
- 先运行/go-cqhttp目录下的./go-cqhttp
- 再运行/bot目录下的main.py
## 功能
- 参考`/bot/api.py`的注释

| 功能        | 说明                       |
| ---------- | ------------------------- |
| 复读机      | 发送 复读 + XXX             |
| 防撤回      | 管理员私聊/anti_recall 1/0 开/关  |
| 关键词回复   | 无特殊                     |
| 涩图bot     | 发送/setu                  |
| 反馈        | 发送/feedback + XXX 提交bug |
| 自动回复     | 管理员私聊/status 1/0 开/关  |
| 指定发送     | /send +接受者账号 +内容     |

## 施工中的功能
- [ ] [狼人杀🐺](https://github.com/HUZHU-TEAM/Wolf-game "狼人杀")
- [ ] 打断+1复读
- [ ] QRcode二维码生成
- [ ] 识别群图片二维码，并撤回
- [X] 进群欢迎 ~~验证~~
- [ ] 群禁言
- [X] ~~超级管理员~~指定对象发送信息
## 涩图
- 使用`/setu ././?`自定义涩图类型，for instance:`/setu ?r18=1`
- <a href="https://api.lolicon.app/#/">参考涩图API调用方法</a>
