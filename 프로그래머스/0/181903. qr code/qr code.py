def solution(q, r, code):
    return "".join(x for i, x in enumerate(code) if i % q == r)