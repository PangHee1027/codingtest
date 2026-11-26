def solution(emergency):
    emergency_dict = {x : i + 1 for i, x in enumerate(sorted(emergency, reverse = True))}
    return [emergency_dict[x] for x in emergency]