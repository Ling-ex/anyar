try:
    from ling.helpers.SQL import BASE, SESSION
except ImportError:
    raise AttributeError
from sqlalchemy import Column, Numeric, String, UnicodeText


class Filters(BASE):
    __tablename__ = "filters"
    chat_id = Column(String(14), primary_key=True)
    keyword = Column(UnicodeText, primary_key=True, nullable=False)
    reply = Column(UnicodeText)
    f_mesg_id = Column(Numeric)

    def __init__(self, chat_id, keyword, reply, f_mesg_id):
        self.chat_id = str(chat_id)
        self.keyword = keyword
        self.reply = reply
        self.f_mesg_id = f_mesg_id

    def __eq__(self, other):
        return (
            isinstance(other, Filters)
            and self.chat_id == other.chat_id
            and self.keyword == other.keyword
        )


Filters.__table__.create(checkfirst=True)


def get_filter(chat_id, keyword):
    try:
        return SESSION.query(Filters).get((str(chat_id), keyword))
    finally:
        SESSION.close()


def get_filters(chat_id):
    try:
        return SESSION.query(Filters).filter(Filters.chat_id == str(chat_id)).all()
    finally:
        SESSION.close()


def add_filter(chat_id, keyword, reply, f_mesg_id):
    if to_check := get_filter(chat_id, keyword):
        rem = SESSION.query(Filters).get((str(chat_id), keyword))
        SESSION.delete(rem)
        SESSION.commit()
        adder = Filters(str(chat_id), keyword, reply, f_mesg_id)
        SESSION.add(adder)
        SESSION.commit()
        return False
    else:
        adder = Filters(str(chat_id), keyword, reply, f_mesg_id)
        SESSION.add(adder)
        SESSION.commit()
        return True


def remove_filter(chat_id, keyword):
    if to_check := get_filter(chat_id, keyword):
        SESSION.delete(to_check)
        SESSION.commit()
        return True
    else:
        return False
