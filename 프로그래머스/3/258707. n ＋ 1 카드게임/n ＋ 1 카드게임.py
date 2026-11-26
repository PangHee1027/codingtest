def solution(coin, cards) :
    n = len(cards)
    n_plus_one = n + 1
    initial = n // 3
    max_round = (n - initial) // 2 + 1
    my_deck = set(cards[:initial])
    candidate = set()

    idx = initial
    for iter in range(max_round) :
        candidate.update(set(cards[idx : idx + 2]))
        idx += 2
        finded_pair = set()
        for card in my_deck :
            pair = n_plus_one - card
            if pair in my_deck :
                finded_pair.add(card)
                finded_pair.add(pair)
                break
        if finded_pair :
            my_deck -= finded_pair
            continue

        for card in my_deck :
            pair = n_plus_one - card
            if pair in candidate :
                if not coin :
                    continue
                finded_pair.add(card)
                finded_pair.add(pair)
                coin -= 1
                break    
        if finded_pair :
            my_deck -= finded_pair
            candidate -= finded_pair
            continue

        for card in candidate :
            if not coin :
                break
            pair = n_plus_one - card
            if pair in my_deck :
                finded_pair.add(card)
                finded_pair.add(pair)
                coin -= 1
                break
        if finded_pair :
            my_deck -= finded_pair
            candidate -= finded_pair
            continue
        for card in candidate :
            if coin < 2 :
                return iter + 1
            pair = n_plus_one - card
            if pair in candidate :
                finded_pair.add(card)
                finded_pair.add(pair)
                coin -= 2
                break
        if finded_pair :
            candidate -= finded_pair
            continue
        return iter + 1

    return max_round 