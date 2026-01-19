from openai import OpenAI

# Create client (put your NEW key here)
client = OpenAI(api_key="your-new-api-key")

class ChatBot:
    def get_response(self, user_input):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "assistant", "content": user_input}
            ],
            temperature=0.5,
            max_tokens=500
        )
        return response.choices[0].message.content


if __name__ == "__main__":
    bot = ChatBot()
    reply = bot.get_response("Hello, how are you?")
    print(reply)
