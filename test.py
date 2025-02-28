import requests  # 导入requests库，用于发送HTTP请求

# 定义headers，包含Authorization字段，传递API密钥用于身份验证
headers = {
    'accept': 'application/json',  # 期望返回JSON格式的数据
    'AUTHORIZATION': 'application-5c47c527625c5c0df2cd2e0080b5cb8b'  # 替换为你自己的API密钥
}
chat_id = ""  # 初始化chat_id为空

# 获取profile id
def get_profile_id():
    profile_url = 'http://localhost:8080/api/application/profile'  # 替换为实际的API端点URL
    response = requests.get(profile_url, headers=headers)  # 发送GET请求获取profile信息
    if response.status_code == 200:  # 如果请求成功
        return response.json()['data']['id']  # 返回profile的id
    else:
        print("获取profile id失败")  # 请求失败时打印提示
        return None  # 返回None表示失败

# 获取chat id
def get_chat_id(profile_id):
    chat_open_url = f'http://localhost:8080/api/application/{profile_id}/chat/open'  # 使用profile_id构造聊天接口的URL
    response = requests.get(chat_open_url, headers=headers)  # 发送GET请求打开聊天
    if response.status_code == 200:  # 如果请求成功
        return response.json()['data']  # 返回chat id
    else:
        print("获取chat id失败")  # 请求失败时打印提示
        return None  # 返回None表示失败

# 发送聊天消息
def send_chat_message(chat_id, payload):
    chat_message_url = f'http://localhost:8080/api/application/chat_message/{chat_id}'  # 构造发送消息的URL
    response = requests.post(chat_message_url, headers=headers, json=payload)  # 发送POST请求发送消息
    if response.status_code == 200:  # 如果请求成功
        return response.json()  # 返回响应的JSON数据
    else:
        print(f"发送消息失败，状态码: {response.status_code}")  # 打印失败状态码
        return None  # 返回None表示失败

# 主函数
def main(message, re_chat=True, stream=False):
    if profile_id:  # 如果profile_id存在
        if chat_id:  # 如果chat_id存在
            # 构造消息的payload，包含消息内容和其他参数
            chat_message_payload = {
                "message": message,  # 消息内容
                "re_chat": re_chat,  # 是否继续聊天
                "stream": stream  # 是否启用流式传输
            }
            response = send_chat_message(chat_id, chat_message_payload)  # 调用send_chat_message函数发送消息
            if response:  # 如果返回响应
                print("消息发送成功")  # 打印成功消息
                content = response['data']['content']  # 获取响应中的聊天内容
                print(content)  # 打印聊天内容
                return content  # 返回聊天内容
        else:
            print("获取chat id失败")  # 如果chat_id不存在，打印错误信息
            return None  # 返回None表示失败
    else:
        print("获取profile id失败")  # 如果profile_id不存在，打印错误信息
        return None  # 返回None表示失败

# 程序入口
if __name__ == "__main__":
    profile_id = get_profile_id()  # 获取profile_id
    chat_id = get_chat_id(profile_id)  # 获取chat_id
    # 循环接收用户输入并发送消息
    while True:
        message = input("")  # 提示用户输入消息
        if message != "退出":  # 如果输入的不是"退出"
            real_chat_id = chat_id  # 设置真实的chat_id
            r = main(message, re_chat=True, stream=False)  # 调用main函数发送消息
        else:
            break  # 如果输入"退出"，则退出循环
