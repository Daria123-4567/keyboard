import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from config import token
from diplom import VkWork



class VkBot:
    def __init__(self, token):
        self.bot = vk_api.VkApi(token=token)
        self.longpoll = VkLongPoll(self.vk)
        self.vk_work = VkWork(token)
        self.profiles = {}

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
                self.profiles = self.vk_work.users_get(event.user_id)
                self.write_msg(event.user_id, f'здравствуй {self.profiles["name"]}')
                if request == "ищи":
                    users = self.api.users_search(self.profiles)
                    user = users.pop()
                    photos = self.vk_work.photos_get(user['id'])
                    attachment = ''
                    for num, photo in enumerate(photos_user):
                        attachment += f'photo{photo["owner_id"]}_{photo["id"]}'
                        if num == 2:
                            break
                    self.write_msg(event.user_id, f'я нашел {user["name"]}', attachment=attachment)
                elif request == "далее":
                    self.write_msg(event.user_id, "далее")
                else:
                    self.write_msg(event.user_id, "куда уж дальше")
