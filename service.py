from aiogram.types import Message

def makeresponse(message: Message) -> str:
    response = ""
    if message.forward_from:
        forward = message.forward_from
        response = \
            f"Сообщение от пользователя \n" + \
            f"Имя пользоватеяля: {forward.first_name}\n" + \
            f"ID пользователя: {forward.id}\n" + \
            f"Username пользователя: @{forward.username}\n"
        return response
    elif message.forward_from_chat:
        chat = message.forward_from_chat
        response = \
            f"Сообщение из чата\n" + \
            f"Название чата: {chat.title}\n" + \
            f"ID чата: {chat.id}\n" + \
            f"Username чата: @{chat.username}\n"
        return response
    elif not message.forward_from and not message.forward_from_chat:
        user = message.from_user
        response = \
            f"Сообщение от пользователя\n" + \
            f"Имя пользователя: {user.first_name}\n" + \
            f"ID пользователя: {user.id}\n" + \
            f"Username пользователя: @{user.username}\n"
        return response
            
    return "Unknown message type."