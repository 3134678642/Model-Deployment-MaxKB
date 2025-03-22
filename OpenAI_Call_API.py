from openai import OpenAI

# 初始化客户端，指向 Ollama 的本地服务
client = OpenAI(
    base_url="http://127.0.0.1:8080/api/application/d9959a02-04bc-11f0-99ad-0242ac110002",
    api_key="application-ba607f71636f6cbc867db2ddeb1e0a1c"
)

# 反复调用，但是并不保存上次对话记录

# while True:
#     qun = input("请输入问题")
#     if qun != "退出":
#         response = client.chat.completions.create(
#             model="test",
#             messages=[
#                 {"role": "user", "content": f"{qun}"}
#             ],
#         )
#         print(response.choices[0].message.content)
#     else:
#         # 发送请求
#         break

# 单次调用

# qun = input("请输入问题")
# response = client.chat.completions.create(
#     model="test",
#     messages=[
#         {"role": "user", "content": f"{qun}"}
#     ],
# )
# print(response.choices[0].message.content)



# 指定模型名称
model_name = "test"

# 输入文本数据
input_text = input("")

# 调用 API 服务，获取推理结果
result = client.chat.completions.create(model=model_name,messages=[{"role":"system","content":"你是一个天才"},{"role":"user","content":f"{input_text}"}])
# 打印推理结果
print(result.choices[0].message.content)



