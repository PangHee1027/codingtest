def count_alarms(time):
  if time < 0:
    return 0

  # 0초를 포함하여 time초까지 초-분 알람이 울린 횟수 (0초 시점 +1 보정)
  minute_matches = (59 * time) // 3600 + 1
  # 0초를 포함하여 time초까지 초-시 알람이 울린 횟수 (0초 시점 +1 보정)
  hour_matches = (719 * time) // 43200 + 1

  # 0초일 때(그리고 12시 정각 43200초일 때) 시침/분침/초침이 동시에 겹치는 순간은 중복 카운트되므로 제거
  overlap = 1
  if time >= 43200:
    overlap = 2

  return minute_matches + hour_matches - overlap


def solution(h1, m1, s1, h2, m2, s2):
  start_time = h1 * 3600 + m1 * 60 + s1
  stop_time = h2 * 3600 + m2 * 60 + s2

  # 시작 시각(start_time) 자체에 알람이 울렸는지 확인
  start_is_alarm = 0
  if (59 * start_time) % 3600 == 0 or (719 * start_time) % 43200 == 0:
    start_is_alarm = 1

  # (0초~stop_time 누적 횟수) - (0초~start_time 누적 횟수) + (start_time 자체 알람 여부)
  return count_alarms(stop_time) - count_alarms(start_time) + start_is_alarm