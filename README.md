<div align=center>

# IQIYI-CheckIn

----
##### Cookie变量设置 Secrets:**

| 名称                                                    | 内容                                                                           | 说明                                                                                                                 |
|-------------------------------------------------------|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `AUTH_PAT` | 使用Github Actions清理workflows日志 | [PAT获取教程](https://docs.github.com/cn/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) |
| [IQIYI_COOKIE](https://www.iqiyi.com) | 爱奇艺Cookie | F12控制台执行`console.log(document.cookie)`电脑版有效期三个月                                                                 |
| [GLADOS_COOKIE](https://glados.one/console/education) | [Clash for Windows](https://github.com/Fndroid/clash_for_windows_pkg/releases) | [Clash for Windows 汉化补丁](https://github.com/BoyceLig/Clash_Chinese_Patch/releases) |

##### IQIYI-CheckIn推送通知环境变量(目前提供`微信server酱`、`pushplus(推送加)`、`iOS Bark APP`、`telegram机器人`、`钉钉机器人`、`企业微信机器人`、`iGot`等通知方式)
|       Name        |                                        归属                                         | 属性  | 说明                                                                                                                                                                         |
|:-----------------:|:---------------------------------------------------------------------------------:|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|    `SEND_KEY`     |                                       推送开关                                        | 非必须 | 推送开关设置如设置该参数 仅在Cookie失效时推送,不设置则默认全部推送无论是否失败 |  
|    `BARK_PUSH`    |                                      BARK推送                                       | 非必须 | IOS用户下载BARK这个APP,填写内容是app提供的`设备码`，例如：https://api.day.app/123 ，那么此处的设备码就是`123` |
|   `BARK_SOUND`    |                                      BARK推送                                       | 非必须 | bark推送声音 |
|  `TG_BOT_TOKEN`   |                                    telegram推送                                     | 非必须 | tg推送(需设备可连接外网),`TG_BOT_TOKEN`和`TG_USER_ID`两者必需,填写自己申请[@BotFather](https://t.me/BotFather)的Token,如`10xxx4:AAFcqxxxxgER5uw` |
|   `TG_USER_ID`    |                                    telegram推送                                     | 非必须 | tg推送(需设备可连接外网),`TG_BOT_TOKEN`和`TG_USER_ID`两者必需,填写[@getuseridbot](https://t.me/getuseridbot)中获取到的纯数字ID |
|  `DD_BOT_TOKEN`   |                                       钉钉推送                                       | 非必须 | 钉钉推送(`DD_BOT_TOKEN`和`DD_BOT_SECRET`两者必需)[官方文档](https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq) ,只需`https://oapi.dingtalk.com/robot/send?access_token=XXX` 等于`=`符号后面的XXX即可 |
|  `DD_BOT_SECRET`  |                                       钉钉推送                                       | 非必须 | (`DD_BOT_TOKEN`和`DD_BOT_SECRET`两者必需) ,密钥，机器人安全设置页面，加签一栏下面显示的SEC开头的`SECXXXXXXXXXX`等字符 , 注:钉钉机器人安全设置只需勾选`加签`即可，其他选项不要勾选 |
|    `QYWX_KEY`     |                                   企业微信机器人推送                                 | 非必须 | 密钥，企业微信推送 webhook 后面的 key [详见官方说明文档](https://work.weixin.qq.com/api/doc/90000/90136/91770) |
|     `QYWX_AM`     |                                   企业微信应用推送                                  | 非必须 | 依次填入 企业id,secret,@all(或者成员id),AgentID,图片id |
|  `IGOT_PUSH_KEY`  |                                      iGot推送                                       | 非必须 | iGot聚合推送，支持多方式推送，确保消息可达 |
| `PUSH_PLUS_TOKEN` |                                    pushplus推送                                     | 非必须 | 微信扫码登录后一对一推送或一对多推送下面的token(您的Token) [官方网站](https://www.pushplus.plus/) |
| `PUSH_PLUS_USER`  |                                    pushplus推送                                    | 非必须 | 一对多推送的“群组编码”（一对多推送下面->您的群组(如无则新建)->群组编码）注:(1、需订阅者扫描二维码 2、如果您是创建群组所属人，也需点击“查看二维码”扫描绑定，否则不能接受群组消息推送)，只填`PUSH_PLUS_TOKEN`默认为一对一推送 |
|  `TG_PROXY_HOST`  |                                  Telegram 代理的 IP                                | 非必须 | 代理类型为 http。例子：http代理 http://127.0.0.1:1080 则填写 127.0.0.1 |
|  `TG_PROXY_PORT`  |                                  Telegram 代理的端口                                | 非必须 | 例子：http代理 http://127.0.0.1:1080 则填写 1080 |
|    `GOBOT_URL`    |                                   go-cqhttp URL                                   | 非必须 | 推送到个人 QQ: http://127.0.0.1/send_private_msg 群：http://127.0.0.1/send_group_msg |
|    `GOBOT_QQ`     |                                   go-cqhttp QQ                                    | 非必须 | 如果 GOBOT_URL 设置 /send_private_msg 则需要填入 user_id=个人 QQ 相反如果是 /send_group_msg 则需要填入 group_id=QQ 群 |
|   `GOBOT_TOKEN`   |                                  go-cqhttp Token                                  | 非必须 | 填写在 go-cqhttp 文件设置的访问密钥 |

##### GLaDOS-CheckIn推送通知环境变量(`微信Server酱`、`PushPlus(推送加)`、`Qmsg`)
|       Name        |                                        归属                                        | 属性  | 说明 |
|:-----------------:|:--------------------------------------------------------------------------------:|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SENDKEY` | [微信Server酱](https://sct.ftqq.com/) | 非必须 | 去你创建的那个`.yml`文件里面修改`is_ServerChan_push`的值为`1` |
| `TOKEN` | [PushPlus](https://www.pushplus.plus/) | 非必须 | 去你创建的那个`.yml`文件里面修改`is_PushPlus_push`的值为`1` |
| `Key` | [Qmsg](https://qmsg.zendee.cn/) | 非必须 | 去你创建的那个`.yml`文件里面修改`is_Qmsg_push`的值为`1` |
----
#### 参考项目：
- @feixuei: [feixuei/GLaDOS-CheckIn](https://github.com/feixuei/GLaDOS-CheckIn)
- @MayoBlueSky: [MayoBlueSky/My-Actions](https://github.com/MayoBlueSky/My-Actions/tree/master)