from vk_api.longpoll import VkLongPoll, VkEventType
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
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



