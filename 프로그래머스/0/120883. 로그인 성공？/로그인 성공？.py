def solution(id_pw, db):
    if id_pw in db :
        return 'login'
    elif id_pw[0] in [x[0] for x in db] :
        return 'wrong pw'
    return 'fail'