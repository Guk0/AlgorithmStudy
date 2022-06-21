# https://programmers.co.kr/learn/courses/30/lessons/17678
# [1차] 셔틀버스

# 9:00 부터 총 n회 t분 간격으로 셔틀옴. 셔틀에 탈 수 있는 최대 인원 m

# 셔틀 정거장에 제일 늦게 도착해도 되는 시간.
# 셔틀 540 부터
def solution(n, t, m, timetable):
    answer = ''
    shutles_dict = {}
    # int로 변환
    for i in range(len(timetable)):
        hour, minute = timetable[i].split(":")
        timetable[i] = 60 * int(hour) + int(minute)
    
    timetable.sort()
    # 배차 시간을 shutles_dict에 담는다. 이 dict의 value에는 위에서 변환한 timetable 시간이 들어간다.
    for i in range(n):
        shutles_dict[540+i*t] = []

    # 배차 시간에 맞게 timetable의 시간을 할당한다.
    i = 0
    for el in shutles_dict.keys():
        while i < len(timetable) and timetable[i] <= el and len(shutles_dict[el]) < m:
            shutles_dict[el].append(timetable[i])
            i += 1

    # 배차시간에 할당된 사람의 수를 비교한다. 마지막 배치시간에 사람이 꽉차있으면 마지막 사람의 시간에서 -1이 답이된다.
    # 사람이 없다면 그냥 해당 배차 시간이 답이 된다.
    last_key = list(shutles_dict.keys())[-1]
    last_value = shutles_dict[last_key]
    if len(last_value) < m:
        answer = last_key
    else:
        answer = last_value[-1] -1
    
    result_hour = answer // 60
    result_minute = answer % 60
    result_hour = str(result_hour) if result_hour > 9 else "0"+str(result_hour)
    result_minute = str(result_minute) if result_minute > 9 else "0"+str(result_minute)
    
    return result_hour + ":" + result_minute


