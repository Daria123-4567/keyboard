import vk_api
from token import token
from vk_api.exсeptions import ApiError

class VkWork():
    def __init__(self, token):
        self.ext_api = vk_api.VkApi(token=token)

    def get_profile_info(self, user_id):

        try:
            info = self.ext_api.method('users.get',
                                      {'user_id': user_id
                                       'fields': 'bdate,city,sex'
                                      }

                                      )
        except ApiError:
            return

        return info



    def users_search(self, city_id, age_from, age_to, sex, offset = None):

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
        for profile in profiles
            if profile['is_closed'] == False:
                result.append({'name':profile['first_name'] + '' + profile['last_name'],
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
        except KeyError:
            return

        result = []
        for num, photo in enumerate(photos):
            result.append({'owner_id': photo['owner_id'],
                           'id':photo['id']
                           })
            if num == 2:




if__name__ == '__main__':
    work = VkWork(token)

    info = work.get_profile_info()
    if info:
        print(work.get_profile_info())
    else:
        pass



if__name__ == '__main__':
    work = VkWork(token)

    profiles = work.users_search(city_id, age_from, age_to, sex, offset = None)



