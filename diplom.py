import vk_api
from config import token
from vk_api.exсeptions import ApiError


class VkWork:
    def __init__(self, token):
        self.vk = None
        self.ext_api = vk_api.VkApi(token=token)

    def users_get(self, user_id):

        try:
            info = self.ext_api.method('users.get',
                                       {'user_id': user_id,
                                        'fields': 'date,city,sex'
                                        })

        except ApiError as e:
            info = {}
            print(f'error = {e}')
        result = {'name': info['first_name'] + '' + info['last_name'],
                  'sex': info.get('sex'),
                  'city': info.get('city')['title'],
                  'bdate': info.get('bdate')
                  }

        return result



    def users_search(self, city_id, age_from, age_to, sex, offset=None):

        try:
            profiles = self.ext_api.method('users_search',
                                           {'city_id': city_id,
                                            'age_from': age_from,
                                            'age_to': age_to,
                                            'sex': 1 if params['sex'] == 2 else 2,
                                            'count': 30,
                                            'offset': offset,
                                            })

        except ApiError:
            return profiles

        profiles = profiles['items']

        result = []
        for profile in profiles:
            if not profile['is_closed']:
                result.append({'name': profile['first_name'] + '' + profile['last_name'],
                               'id': profile['id']
                               })
        return result

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

