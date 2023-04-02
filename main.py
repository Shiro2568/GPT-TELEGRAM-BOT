from revChatGPT.ChatGPT import Chatbot
import json
import telebot
import datetime 
import os
import time
os.system('color')


def red(text):
    print('\033[31m', text, '\033[0m')

def green(text):
    print('\033[32m', text, '\033[0m')

def printed(text,arg):
    print('\033[33m', text, '\033[0m','\033[36m', arg, '\033[0m')



global chatbot
global config
global last_message
config = {
        "session_token": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..7SuZDOXzsNrGsoE5.BvK5Ev8ZXngVcOBC6Hb0EAaaBpOf9K5aZS81vOJzEd7-iE_Do_zZjUvbw3y78ewI16O1YCg2Qqe3EfeWcmAf2eSleXJGMGwZBzzWqwFC_5vJbnAv0gyuqvqLt9xE-rPEUKnvk_nWzmMZq1HI6gtLCHoSPPB0cm0ExCzGTgTr4hezn5imGOg42kf1Pi24KIKWqmwau5s_DrTYYQ03g4JB5IjheMs86SDAqK0xSnKLqyboZV0yN5ZHXHPnaUvYcTHU-J-DEoEv4SCO_XhI6jIvm2edOMscGSEQD2_6ACCL9VzNQ_UJ17o2TJ4-bGz2RAOjMbZ4s6oBg-2gq5Ja4lC_52wdnGVfmWThhWXCOOcojIwVUgM6ASQf4ETl1Ffh-D7IdwEWtqqZ6XvJPCXV9Lg_00P26m7oKBYDfHn_l_2GDErA9xMyx4XCr9_aRKsqFbKUxh6QDSK7-A_8vyOrAKQQL4GYwsqwRhgPDBg-BIdvI_r8kU6tL9g20nZ64j9SI1Ee1CyIsCmPI6wbH98OOJMknu7Uad1tWbW54M0CO9dDQ2Rt6vzlWJqcyU1u4_zj9ykj4-BgVv7tTU9vspiLlEeUd_qOKT1SQTaePkJ2qYsFdZoL39MpefrK83Z-Hag6QgGb77y_uzA1kHe_dF_wlISSrlNfxM1sIRCk4lmCHPoo0ODGiidhTkPs5IA7VKlj_iiL877vvcq-lStwg5muocaiTbvt3Bs-4Uq3doUg19MO5yjY4bv-QfHiBLvqbz-5SsyUKoMwR9kDFbFcMpWt2Olf7dM-Se_fpiE1laxNcbXJSZCWJr1nnMdJ8vp2_mNPGQmKBlXS61NiHAEbw48T7ug5hSmdt7SPR_yFRmG6caNI2O9WKqUZCVcMTPnGOW1K92P4pI7awx4kmcWl3AYNYTtqOXbMpukKPG65l1gIazchE7INoH0-wpBe6_tpkYemYH3i8N-5vMIWBzsBAzFUnWDm-uHkIEBGLdOcT_BJIMieUZlmgHnTBI2zMXClKp3qJwdXtIlZt5JYPKh-8LqFT-FJr8zn-P8p4_wlrk8IW1gmF6pqBvbW3FdmPoPZM2_F8Pcuft7wSTWR_XASAeq9TCmbPRtrOs64b7zUBHErmypbL5fQVC0jVyoCbBzLpj_npF21rAq-n62LtkctlykFbuyRxk-oMuw5PNu22jgoTolG6_46zYWJofVy1x7-Lo65PIYxhqvZb3x_4DRV1aWoKMTB5eNZku0ANWj9OBB9i9dSj-06C1bM4heRYJnhBBFasCRSNZaWlvvwB2Ntl_3IFas0yf7WqR1eIRh2FfnbJgA3oA44VsrebjqBlQhBTsXjKCVX9zpiD0_BMSQmx8Fg9924f2rjkXx2RZ7ZwHfMiB9Gw3_laTewYenF5o2PrfOMfm9R7-OUPxD8EGCQazK9H-ySEq52MzgOjbBtO8ncMpWe8BINZ19M53gZ9bF4huy-Y4UI5mp5cMPCM9c3XOnwDFdFsZLcH6l57-J9cdbzTD6Qy7PjDt0bAJ7SOhCPw_EKOWH3rIGSLDz0-N0Dti0UXmbRIadLPQ2voNo2zM-7Is8K_QPn6ruvd1bY_tf3pnv_nt-4Kj6sM_j1RP5qMvpTd_sTyj_wPWydyqn8YeFhJfc8f_9QSA8upsYbYLG9uQKTlJNHCqzCQOUy6SqW7OFApp7p-K17wluLhkjOq21ZuxwqRy7yCXlz9DZrmZ5twsl18EGCHevuMYlZpdByZODucFm6t8O4D7rbmIcKfIfQ6YD660Knwza234dw5h0h-LpYxId5wu8gHyXw0mDMfwVvNujEqb0ZOcM0v-UEPJHzxyQiJDS1O86MJk5ztpZwRtJ-MbI0RcCcEvWLzMUddwpYoPhyrq9RDx29QOKbV-TCdTRTWBGJVtgLt3P-dFqgGlSNcSsSDKEk8wmdsxN4Mg-CTlKsa5VA-G7gIZrrZqbeIQwlbV9xyz95cRovnKZS7sQ7iVjCT9lsuOEGLJbCk8J6bKGp0Vq5iG2WJSU4raNg-KR0P0-roAmSAcAJvcYlpW8MI7nTIt5tDBqcmbA1-GM9UDjb8_buMDyNHDNWoBzLotWG9xTM1gJoOc8F5RwMB1vUrJ3PXPjrS3Wa74j2ocnx6pGyMfyuahziT67f669Qgl9tcnjHLxgd9KRkgQDC4muTKWC9c5LSrK3aMYx6G-zGzqxp_Q-6DcJet4Y_JzJ1T9_oI9QcXtZ2EKtIQxi_Ey1bL4Rilj71U8_Xeq22EAex5lrnnC6p9XuQNw0ETK_o1Y-QAlGxcfRr6U7X9o9qRGPmTU1_rHBg3rGbF_dDg27OBxodM53Hu2p5LzH2xl-2g6NhaxTVf2PLTNIi2rt0ciRYamejWxvSRC-aD4ESiw.r8llyjGdxKPID_oEbq76pw",
        #"сf_clearance":"Blpqz6hSRo9xtu9FFmUEpLsvw4i2Dbr7kBokdZE_Hms-1670859858-0-160",
        #"user_agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
         }

TOKEN = "<YOUR TOKEN>"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])

def start(message):
    bot.send_message(message.chat.id,"Привет, напиши мне все что угодно, спроси о чем угодно, я попробу ответить на твои вопросы.")
    bot.send_message(message.chat.id,"Мои команды - 1)/reset - сброс потока, вы сбрасываете весь контекст с ботом(он забывает о чем вы общались)\n 2)reask - переспросить текущий вопрос")
@bot.message_handler(commands=['reset'])
def reset(message):
    chatbot = Chatbot(config, conversation_id=None)
    bot.send_message(message.chat.id,"Поток был успешно сброшен.")


chatbot = Chatbot(config, conversation_id=None, parent_id=None)

@bot.message_handler()
def get_text(message):
    bot.send_message(message.chat.id,"Бот думает...")
    green("The message is received ✔")
    last_message = message.text
    response = chatbot.ask(message.text)
    bot.send_message(message.chat.id,response["message"])
    green('---------------------------------------------------------------------------------------')
    red(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    green("Logs: "), printed(f"Name:",message.from_user.username), printed("Message: ",message.text)
    printed("Bot message: ",response["message"])
    green('---------------------------------------------------------------------------------------')
@bot.message_handler(commands=['reask'])
def reask(message):
    
#bot.infinity_polling()
def telegram_polling():
    try:
        bot.polling(none_stop= False,timeout = 60)
    except:
        bot.stop_polling()
        time.sleep(5)
        telegram_polling()
   
telegram_polling()

