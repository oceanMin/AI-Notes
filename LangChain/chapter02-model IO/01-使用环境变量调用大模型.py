import os

from langchain_openai import ChatOpenAI

# 1、获取大模型
chat_model = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=os.environ["OPENAI_API_KEY"],
    base_url=os.environ["OPENAI_BASE_URL"],
)

# 2、调用大模型
response = chat_model.invoke('请介绍一下你自己?')

# 3、输出响应文本
print(response.content)