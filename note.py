import json

class Note:
    def __init__(self, id):
        self.__set_id(id)

    def __set_id(self, id):
        self.note_id = id

    def set_head(self, head):
        self.note_head = head

    def set_body(self, body):
        self.note_body = body
    
    def set_date(self, date):
        self.note_date = date

    def generate_json(self, notes):
        if notes == "":
            notes = {}

        notes[self.note_id] = {'head': self.note_head, 'body': self.note_body, 'date': self.note_date}
        
        return json.dumps(notes)