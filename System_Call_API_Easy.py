import requests

# 定义请求头，包含认证信息（API Key）
headers = {
    'AUTHORIZATION': 'application-ba607f71636f6cbc867db2ddeb1e0a1c'  # 替换为实际的API Key
}

# 获取应用配置信息的URL
profile_url = 'http://127.0.0.1:8080/api/application/profile'

# 发送GET请求，获取应用配置信息
response = requests.get(profile_url, headers=headers)

# 从响应中提取应用ID（profile_id）
profile_id = response.json()['data']['id']

# 构建聊天会话的URL，使用上一步获取的profile_id
chat_url = f"http://127.0.0.1:8080/api/application/{profile_id}/chat/open"

# 发送GET请求，创建或打开一个聊天会话，并获取会话ID（chat_id）
chat_id = requests.get(chat_url, headers=headers).json()["data"]

# 打印欢迎信息
print("您好,请问您有什么问题?")

# 进入聊天循环
while True:
    # 获取用户输入的问题
    message = input("")

    # 构建发送消息的请求体
    chat_message_payload = {
        "message": message,  # 用户输入的消息
        "re_chat": "True",   # 是否重新聊天（根据API文档调整）
        "stream": "False"    # 是否启用流式响应（根据API文档调整）
    }

    # 构建发送消息的URL，使用之前获取的chat_id
    chat_message_url = f'http://localhost:8080/api/application/chat_message/{chat_id}'

    # 发送POST请求，将用户消息发送到服务器
    send_chat_message = requests.post(chat_message_url, headers=headers, json=chat_message_payload).json()

    # 从响应中提取聊天内容
    content = send_chat_message['data']['content']

    # 打印服务器的回复
    print(content)