from random import randrange

import vk_api
from vk_api.longpoll import  VkLongPoll, VkEventType

token  = input ('Token:vk1.a.oyOMS9Mia8-1d9wzx4iaiL5ScyydRM4ZITb4n9tylutAyVSwQPj79P5mLUviOI6DGA8zKgl3LqaFeo58vWzIRnsaNl1pC8V3lqffNdnJGxqi2-v7TrQKtumdf6BqWN_PKXe6olRjna4KCrmjOv2XJnDoddi7tlZsutoRnusCE0holZYTGWbJ_BimKUOwEeGduNXwj9tzQRtwOskw3Meajw ')

vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)

session = vk_api.VkApi(token=token)
vk = session.get_api()

def user (user_id, message):
        vk.method('messages.send', {'user_id': user_id,
                                    'message': message,
                                    'random_id': randrange(10 ** 7)})

 for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:
            request = event.text

            if request == "привет":
                user(event.user_id, f"Хай, {event.user_id}")
            elif request == "пока":
                user(event.user_id, "Пока((")
            else:
                user(event.user_id, "Не поняла вашего ответа...");

def get_user_status(user_id):
    friends = session.method("friends.get", {"user_id":user_id})
    for friend in friends["items"]:
        user = session.method("users.get", {user_ids:friend})
        status = session.method("status.get", {user_id:friend})
        if status['text'] == "":
            continue
        else:
            print(f"{user[0]['first_name']} {user[0]['last_name']} / {status['text']}")
def _get_user_name_from_vk_id(self, user_id):
    request = requests.get("https://vk.com/id" + str(user_id))
    bs = bs4.BeautifulSoup(request.text, "html.parser")

    user_name = self._clean_all_tag_from_str(bs.findAll("title")[0])

    return user_name.split()[0]



 def get_photos_id(self, user_id):
                    url = 'https://api.vk.com/method/photos.getAll'
                    params = {'access_token': token,
                              'type': 'album',
                              'owner_id': user_id,
                              'extended': 1,
                              'count': 25,
                              'v': '5.131'}
                    resp = requests.get(url, params=params)
                    dict_photos = dict()
                    resp_json = resp.json()
                    try:
                        dict_1 = resp_json['response']
                        list_1 = dict_1['items']
                        for i in list_1:
                            photo_id = str(i.get('id'))
                            i_likes = i.get('likes')
                            if i_likes.get('count'):
                                likes = i_likes.get('count')
                                dict_photos[likes] = photo_id
                        list_of_ids = sorted(dict_photos.items(), reverse=True)
                        return list_of_ids
                    except KeyError:
                        self.write_msg(user_id, 'Ошибка получения токена');


def get_photo_1(self, user_id):
    list = self.get_photos_id(user_id)
    count = 0
    for i in list:
        count += 1
        if count == 1:
     return i[1]


def get_photo_2(self, user_id):
    list = self.get_photos_id(user_id)
    count = 0
    for i in list:
        count += 1
        if count == 2:
    return i[1]


def get_photo_3(self, user_id):
    list = self.get_photos_id(user_id)
    count = 0
    for i in list:
        count += 1
        if count == 3:
    return i[1]

def found_person_info(self, offset):
    tuple_person = select(offset)
    list_person = []
    for i in tuple_person:
        list_person.append(i)
    return f'{list_person[0]} {list_person[1]}, ссылка - {list_person[3]}'


def person_id (self, offset):
    tuple_person = select(offset)
    list_person = []
    for i in tuple_person:
        list_person.append(i)
    return str(list_person[2])

 bot = VKBot()