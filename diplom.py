import vk_api
from config import token
from vk_api.exсeptions import ApiError


class VkWork:
    pass

    def __init__(self, token):
        self.vk = None
        self.ext_api = vk_api.VkApi(token=token)

    def users_get(self, user_id):

        try:
            info = self.ext_api.method('users.get',
                                       {'user_id': user_id,
                                        'fields': 'date,city,sex'
                                        })

        except ApiError:
            return

        return info

    if __name__ == '__main__':
        work = VkWork(token)

        info = work.users_get()
        if info:
            print(work.users_get())
        else:
            pass

    def users_search(self, city_id, age_from, age_to, sex, offset=None):

        try:
            profiles = self.ext_api.method('users_search',
                                           {'city_id': city_id,
                                            'age_from': age_from,
                                            'age_to': age_to,
                                            'sex': sex,
                                            'count': 30,
                                            'offset': offset,
                                            })

        except ApiError:
            return

        profiles = profiles['items']

        result = []
        for profile in profiles:
            if not profile['is_closed']:
                result.append({'name': profile['first_name'] + '' + profile['last_name'],
                               'id': profile['id']
                               })
        return result

    if __name__ == '__main__':
        work = VkWork(token)
        profiles = work.users_search(city_id, age_from, age_to, sex, offset=None)

    def photos_get(self, user_id):
        photos = self.ext_api.method('photos.get',
                                     {'album_id': 'profile',
                                      'owner_id': user_id

                                      }
                                     )
        try:
            photos = photos['items']
            dict_photos = dict()
            for i in photos:
                photo_id = str(i.get('id'))
                i_likes = i.get('likes')
                if i_likes.get('count'):
                    likes = i_likes.get('count')
                    dict_photos[likes] = photo_id
            list_of_ids = sorted(dict_photos.items(), reverse=True)
        except KeyError:
            return list_of_ids

    def person_id(self, offset):
        pass


