from flask import url_for
from flask_login import current_user
from jinja2.utils import urlize


def make_message_format(user, messages):
    message_tag = ''
    for message in messages:
        message_tag += '<div class="col-md-6"></div>'
        
        message_tag += '<div class="speech-bubble-dest col-md-4">'
        message_tag += f'<p>{urlize(message.message, target=True)}</p>'
        message_tag += f'<p>{message.create_at.strftime("%H:%M")}</p></div>'
        
        message_tag += '<div class="col-md-2">'
        if user.picture_path:
            message_tag += f'<img class="image-mini" src="{url_for("static", filename=user.picture_path)}">'
        else:
            message_tag += f'<img class="image-mini" src="{url_for("static", filename="user_images/profile_icon.png")}">'
        message_tag += f'<p>{user.username}</p></div>'
    return message_tag
