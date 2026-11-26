def solution(enroll, referral, seller, amount):
    n = len(enroll)
    enroll_idx = {x : i for i, x in enumerate(enroll)}
    enroll_parent = {x : y if y != '-' else '' for x, y in zip(enroll, referral)}
    enroll_income = [0] * n

    for s, a in zip(seller, amount) :
        child, parent = s, enroll_parent[s]
        cur_income = a * 100
        while child :
            parent_income = cur_income // 10
            enroll_income[enroll_idx[child]] += cur_income - parent_income
            if parent_income == 0 :
                break
            cur_income = parent_income
            if parent == '' :
                break
            child, parent = parent, enroll_parent[parent]

    return enroll_income