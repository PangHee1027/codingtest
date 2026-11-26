from collections import deque

def solution(storage, requests):
    h = len(storage)
    w = len(storage[0])
    
    # 격자 바깥쪽에 빈 공간('.') 패딩을 추가하여 경계 처리 쉽게 하기
    padded_h = h + 2
    padded_w = w + 2
    padded = [['.'] * padded_w for _ in range(padded_h)]
    for i in range(h):
        for j in range(w):
            padded[i + 1][j + 1] = storage[i][j]
            
    # 현재 외부 공기와 연결된 빈 공간들을 탐색하는 함수 (BFS)
    def get_outside_air():
        outside = [[False] * padded_w for _ in range(padded_h)]
        q = deque()
        
        # 테두리의 모든 좌표를 시작점으로 설정
        for i in range(padded_h):
            for j in range(padded_w):
                if i == 0 or i == padded_h - 1 or j == 0 or j == padded_w - 1:
                    outside[i][j] = True
                    q.append((i, j))
        
        # BFS로 연결된 빈 공간('.') 확산
        while q:
            cx, cy = q.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < padded_h and 0 <= ny < padded_w:
                    if not outside[nx][ny] and padded[nx][ny] == '.':
                        outside[nx][ny] = True
                        q.append((nx, ny))
                        
        return outside

    # 각 요청 처리
    for req in requests:
        target = req[0]
        is_crane = (len(req) == 2)
        
        # 현재 시점에서 외부 공기 영역 파악
        outside = get_outside_air()
        to_remove = []
        
        for i in range(1, padded_h - 1):
            for j in range(1, padded_w - 1):
                if padded[i][j] == target:
                    if is_crane:
                        to_remove.append((i, j))
                    else:
                        # 지게차: 사방 중 하나라도 외부 공기와 닿아 있는지 확인
                        accessible = False
                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            if outside[i + dx][j + dy]:
                                accessible = True
                                break
                        if accessible:
                            to_remove.append((i, j))
                            
        # 선택된 컨테이너 제거 (빈 공간 '.'으로 변경)
        for x, y in to_remove:
            padded[x][y] = '.'
            
    # 남은 컨테이너 개수 세기
    remain = 0
    for i in range(1, padded_h - 1):
        for j in range(1, padded_w - 1):
            if padded[i][j] != '.':
                remain += 1
                
    return remain