
database = {
    1:"erfan",
    2:"ali",
    3:"mahdiar"
}

def get_user_from_db(user_id):
    return database.get(user_id)