
import vk_api
from vk_api.longpoll import  VkLongPoll, VkEventType


token  = input ('Token:vk1.a.oyOMS9Mia8-1d9wzx4iaiL5ScyydRM4ZITb4n9tylutAyVSwQPj79P5mLUviOI6DGA8zKgl3LqaFeo58vWzIRnsaNl1pC8V3lqffNdnJGxqi2-v7TrQKtumdf6BqWN_PKXe6olRjna4KCrmjOv2XJnDoddi7tlZsutoRnusCE0holZYTGWbJ_BimKUOwEeGduNXwj9tzQRtwOskw3Meajw ')

vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)

session = vk_api.VkApi(token=token)
vk = session.get_api()

def write_msg (user_id, message):
        vk.method('messages.send', {'user_id': id,
                                    'message': message,
                                    'random_id': 0})
def write_msg(id, some_text):
    vk_session.method("messages.send, {}")

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        write_msg(event.user_id, "Привет я бот для поиска...")
        request = event.text

        if request == "ищи":
            write_msg(event.user_id, "я нашел")
        else:
            write_msg(event.user_id, "ищу как могу")
        if request == "далее":
            write_msg(event.user_id, "далее")
        else:
            write_msg(event.user_id, "куда уж дальше")


class VkBot:

    def __init__(self, user_id):
        print("Создан объект бота!")
        self._USER_ID = user_id
        self._USERNAME = self._get_user_name_from_vk_id(user_id)


def _get_user_name_from_vk_id(self, user_id):
    request = requests.get("https://vk.com/id" + str(user_id))
    bs = bs4.BeautifulSoup(request.text, "html.parser")

    user_name = self._clean_all_tag_from_str(bs.findAll("title")[0])

    return user_name.split()[0]

