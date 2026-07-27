import requests

# 1. 替换成你自己的 API Key
API_KEY = "sk-5082c00e24c54974905d444a5c24dbd1"

# 2. DeepSeek 接口地址
url = "https://api.deepseek.com/v1/chat/completions"

# 3. 请求头（身份认证）
headers = {
    "Authorization": f"Bearer sk-5082c00e24c54974905d444a5c24dbd1",
    "Content-Type": "application/json"
}

# 4. 你要问的问题
data = {
    "model": "deepseek-chat",
    "messages": [
        {"role": "user", "content": "腾讯视频vip要多少钱"}

          ],
    "stream": False
}

# 5. 发送请求
response = requests.post(url, headers=headers, json=data)

# 6. 拿到返回结果
result = response.json()

# 7. 打印大模型的回答
print(result["choices"][0]["message"]["content"])