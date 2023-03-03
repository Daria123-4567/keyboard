
import vk_api
from vk_api.longpoll import  VkLongPoll, VkEventType
from token import token

vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)


def write_msg (user_id, message):
        vk.method('messages.send', {'user_id': id,
                                    'message': message,
                                    'random_id': 0})


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


 def ask_user(cls, attribute):
    path = os.path.join(resources, 'output', attribute)

    with open(f'{path}.txt', encoding='utf8') as f:
        question = f.read().strip()
    answer  = input (f'\n{question}\n\n')

    if answer.isdigit():
        answer = int(answer)

    print (answer)

