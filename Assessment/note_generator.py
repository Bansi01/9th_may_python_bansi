import datetime

def generate_note(title, content):
    note = {
        "title": title,
        "content": content,
        "created_at": datetime.datetime.now()
    }
    return note

