# note_generator.py
def generate_note(title, content):
    note = {
        "title": title,
        "content": content,
        "created_at": datetime.now()
    }
    return note