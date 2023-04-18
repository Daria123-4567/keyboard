import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from config import token


class VkBot:
    def __init__(self, token):
        self.bot = vk_api.VkApi(token=token)

    def write_msg(self, user_id, message, photos=None):
        self.bot.method('messages.send', {'user_id': user_id,
                                          'message': message,
                                          'random_id': 0}
                        )

    def handler(self):
        longpoll = VkLongPoll(self.bot)
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                self.write_msg(event.user_id, "Привет я бот для поиска...")
                request = event.text

                if request == "ищи":
                    self.write_msg(event.user_id, "я нашел")
                elif request == "далее":
                    self.write_msg(event.user_id, "далее")
                else:
                    self.write_msg(event.user_id, "куда уж дальше")
