from sqlalchemy import Column, Numeric, String, UnicodeText

from ling.helpers.SQL import BASE, SESSION


class Note(BASE):
    __tablename__ = "note"
    user_id = Column(String(14), primary_key=True)
    keyword = Column(UnicodeText, primary_key=True, nullable=False)
    f_mesg_id = Column(Numeric)

    def __init__(self, user_id, keyword, f_mesg_id):
        self.user_id = str(user_id)
        self.keyword = keyword
        self.f_mesg_id = int(f_mesg_id)


Note.__table__.create(checkfirst=True)


def get_note(user_id, keyword):
    try:
        return SESSION.query(Note).get((str(user_id), keyword))
    finally:
        SESSION.close()


def get_notes(user_id):
    try:
        return SESSION.query(Note).filter(Note.user_id == str(user_id)).all()
    finally:
        SESSION.close()


def add_note(user_id, keyword, f_mesg_id):
    to_check = get_note(user_id, keyword)
    if not to_check:
        adder = Note(str(user_id), keyword, f_mesg_id)
        SESSION.add(adder)
        SESSION.commit()
        return True
    rem = SESSION.query(Note).get((str(user_id), keyword))
    SESSION.delete(rem)
    SESSION.commit()
    adder = Note(str(user_id), keyword, f_mesg_id)
    SESSION.add(adder)
    SESSION.commit()
    return False


def rm_note(user_id, keyword):
    to_check = get_note(user_id, keyword)
    if not to_check:
        return False
    rem = SESSION.query(Note).get((str(user_id), keyword))
    SESSION.delete(rem)
    SESSION.commit()
    return True

