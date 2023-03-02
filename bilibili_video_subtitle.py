#哔哩哔哩视频信息
#感谢 https://github.com/SocialSisterYi/bilibili-API-collect 提供API文档!
#bilibili: https://space.bilibili.com/500328587
#github: https://github.com/AwAqwpAwA
#mail: cueavy@163.com/outlook.com
#哔哩哔哩干杯!

import Core

requests = Core.requests
json = Core.json

while 1:
    List=Core.Video_info(input("请输入AV/BV号>>>"))
    if List['code'] != 0 :
        print(f"{List['code']} {Core.error_code[List['code']]}")
        continue
    s=List['data']["subtitle"]
    print('==='*60)
    if not len(s['list']):
        print("此视频不包含字幕!")
        continue
    for i in s['list']:
        print('---'*60)
        print(f"{i['lan_doc']}",end=" ")#字幕语言名称
        print(f"[{i['lan']}]",end=" ")#字幕语言
        print(f"[ID {i['id']}]",end=" ")#字幕id
        print(f"[字幕状态 {['未锁定','已锁定'][i['is_lock']]}]",end=" ")#是否被锁定
        print(f"[类型 {['人工字幕','','AI字幕'][i['ai_status']]}]",end=" ")#是否为AI字幕
        if i['ai_status'] == 0:#是人工字幕
            print("|",end=" ")
            print(f"{i['author']['name']}",end=" ")#字幕作者名称
            print(f"[MID {i['author']['mid']}]",end=" ")#字幕作者MID
            print(f"[性别 {i['author']['sex']}]",end=" ")#字幕作者性别
        print(f"\n{i['subtitle_url']}")
        response=requests.get(i['subtitle_url'])#获取Json字幕文件
        Srt_List=json.loads(response.content)
        Srt_body=Srt_List['body']#字幕主体
        with open(f"{i['id']}.srt","w",encoding="utf-8") as file:
            for i in range(len(Srt_body)):
                file.write(f"{str(i+1)}\n")
                file.write(f"{Core.Time(Srt_body[i]['from'])} --> {Core.Time(Srt_body[i]['to'])}\n")
                file.write(f"{Srt_body[i]['content']}\n\n")
    print('---'*60)
    print('==='*60)