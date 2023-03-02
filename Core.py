#哔哩哔哩视频信息
#感谢 https://github.com/SocialSisterYi/bilibili-API-collect 提供API文档!
#bilibili: https://space.bilibili.com/500328587
#github: https://github.com/AwAqwpAwA
#mail: cueavy@163.com/outlook.com
#哔哩哔哩干杯!

import requests , json , time

error_code = {-400:"请求错误",-403:"权限不足",-404:"无视频",62002:"稿件不可见",62004:"稿件审核中"}#错误代码

def T(Time):return time.strftime("%Y/%m/%d %H:%M:%S",time.localtime(Time))#秒级时间戳转字符串

def Video_info(av_or_bv):
    Get="?"
    if len(av_or_bv) <= 2 :Get+=f"aid={av_or_bv}"#AV
    elif av_or_bv[:2] in ["BV","bv","Bv","bV"]:Get+=f"bvid=BV{av_or_bv[2:]}"#BV
    elif av_or_bv[:2] in ["AV","av","Av","aV"]:Get+=f"aid={av_or_bv[2:]}"#AV
    else:Get+=f"aid={av_or_bv}"#AV
    response=requests.get(f"https://api.bilibili.com/x/web-interface/view{Get}")#调用API
    List=json.loads(response.content)
    return List

def Time(T):#把秒转换为Srt可识别的格式
    millisecond=int(T*1000)
    second=int(T%60)
    minute=int(T/60%60)
    hour=int(T/60/60%60)
    return str(hour)+":"+str(minute)+":"+str(second)+","+str(millisecond)[-3:]