from openai import OpenAI, APIStatusError

with open('DSapi.txt', 'r') as f:
    DS_api = f.read()
with open('GPTapi.txt', 'r') as f:
    GPT_api = f.read()

recommend_prompt = "你是一位专业的天气数据分析师，你正在向大众展示分析天气。稍后我会给你提供一些天气信息，总结这些天气数据的特点，给出大众准确且恰当的穿衣建议和出行建议。你总共需要回复两句话，第一句话包含穿衣建议，如衣服类型、颜色等；第二句话包含出行建议，如适合的户外活动、出行方式等。"

# platform: "DS" "GPT"
def fetch_from_AI(platform, sys_prompt, user_prompt):
    AI_model = ""
    if platform == "DS":
        base_url = "https://api.deepseek.com"
        AI_model = "deepseek-chat"
    elif platform == "GPT":
        # base_url = "https://api.openai.com"
        base_url = "https://api.f2gpt.com"
        AI_model = "gpt-3.5-turbo"
    else:
        return "Error: Invalid platform."

    response = None
    client = OpenAI(api_key=DS_api, base_url=base_url)
    try:
        response = client.chat.completions.create(
            model=AI_model,
            messages=[
                {"role": "system", "content": sys_prompt},
                {"role": "user", "content": user_prompt},
            ],
            stream=False
        )
    except APIStatusError as e: # handle APIStatusError
        if e.status_code == 402:
            print("Insufficient Balance")
        else:
            print(f"APIStatusError: {e}")

    except Exception as e:  # handle other exceptions
        print(f"Error: {e}")

    if response:
        print(response.choices[0].message.content)
        return response.choices[0].message.content

# if excepting model "remember context", user_prompt = last_user_prompt + this_user_prompt
