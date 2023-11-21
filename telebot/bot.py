import logging
from dotenv import load_dotenv
import telebot
import openai



BOT_API_KEY = #for added security add API keys from OS ENV (I didn't find the need to.)
OPENAI_API_KEY = #for added security add API keys from OS ENV (I didn't find the need to.)
USER_KEY = #for added security add API keys from OS ENV (I didn't find the need to.)


logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

def set_context():
    
    context = '''....''' # this is for context injections (I found them necessary to avoid wrong answers put up to 300 words to avoid token abuse)
    return context

bot = telebot.TeleBot(BOT_API_KEY)
openai.api_key = OPENAI_API_KEY
user_id = int(USER_KEY)

@bot.message_handler(func=lambda message: True)
def get_response(message):
    #message handling logic
    chat_id = int(message.chat.id)
    context = set_context()
    user_message = message.text
    print(user_message)
    response = openai.ChatCompletion.create(
        
        model="....",# Your finetuned model
        messages=[
            {"role": "system", "content": "You are acting as the representative for Formulaw, legal technology company."},
            {"role": "assistant", "content": context},
            {"role": "user", "content": user_message},
        ],
        temperature=0.30,
        max_tokens=130,
        top_p=0.83,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    bot_message = response['choices'][0]['message']['content'].strip()
    bot.send_message(chat_id, bot_message)  # Send the generated message back to the user

# Main execution
if __name__ == '__main__':
    bot.infinity_polling()
