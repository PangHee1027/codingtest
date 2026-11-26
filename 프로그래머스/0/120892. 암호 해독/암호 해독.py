def solution(cipher, code):
    return "".join(s for i, s in enumerate(cipher) if not (i + 1) % code)