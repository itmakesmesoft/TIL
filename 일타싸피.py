def play(conn, gameData):
    angle = 0.0
    power = 0.0

    # 이 위는 일타싸피와 통신하여 데이터를 주고 받기 위해 작성된 부분이므로 수정하면 안됩니다.
    #
    # 모든 수신값은 gameData에 들어갑니다.
    #   - gameData.order: 1인 경우 선공, 2인 경우 후공을 의미
    #   - gameData.balls[][]: 일타싸피 정보를 수신해서 각 공의 좌표를 배열로 저장
    #     예) gameData.balls[0][0]: 흰 공의 X좌표
    #         gameData.balls[0][1]: 흰 공의 Y좌표
    #         gameData.balls[1][0]: 1번 공의 X좌표
    #         gameData.balls[4][0]: 4번 공의 X좌표
    #         gameData.balls[5][0]: 마지막 번호(8번) 공의 X좌표

    # 여기서부터 코드를 작성하세요.
    # 아래에 있는 것은 샘플로 작성된 코드이므로 자유롭게 변경할 수 있습니다.

    r = 5.73  # 공의 반지름
    hole_distance = 999999999  # 가까운 홀을 찾기 위해 큰 값을 임의로 지정
    whiteBall_x = gameData.balls[0][0]
    whiteBall_y = gameData.balls[0][1]

    player_one = [1, 3, 5]
    player_two = [2, 4, 5]
    if gameData.order == 1:
        for l in player_one:
            if gameData.balls[l][0] >= 1:
                targetBall_x = gameData.balls[l][0]
                targetBall_y = gameData.balls[l][1]
                break
    elif gameData.order == 2:
        for l in player_two:
            if gameData.balls[l][0] >= 1:
                targetBall_x = gameData.balls[l][0]
                targetBall_y = gameData.balls[l][1]
                break

    # 타격포인트와 비교
    distance = math.sqrt((targetBall_x - whiteBall_x) ** 2 + (targetBall_y - whiteBall_y) ** 2)
    target_x = targetBall_x
    target_y = targetBall_y



    for i in range(6):
        x = HOLES[i][0]
        y = HOLES[i][1]

        hit_width = abs(x - targetBall_x)
        hit_height = abs(y - targetBall_y)

        hole_radian = math.atan(hit_width / hit_height)

        hit_x = targetBall_x
        hit_y = targetBall_y

        if targetBall_x > x and targetBall_y > y:
            hit_x += (r * math.sin(hole_radian))
            hit_y += (r * math.cos(hole_radian))
        elif targetBall_x > x and targetBall_y < y:
            hit_x += (r * math.sin(hole_radian))
            hit_y -= (r * math.cos(hole_radian))
        elif targetBall_x < x and targetBall_y < y:
            hit_x -= (r * math.sin(hole_radian))
            hit_y -= (r * math.cos(hole_radian))
        elif targetBall_x < x and targetBall_y > y:
            hit_x -= (r * math.sin(hole_radian))
            hit_y += (r * math.cos(hole_radian))

        # 타격포인트와 흰공까지의 거리
        target_distance = math.sqrt((hit_x - whiteBall_x) ** 2 + (hit_y - whiteBall_y) ** 2)
        # 타격포인트가 타격볼보다 가까운 경우에만
        if distance > target_distance:
            # 홀까지 거리를 계산하고
            target_hole = math.sqrt((targetBall_x - HOLES[i][0]) ** 2 + (targetBall_y - HOLES[i][1]) ** 2)
            # 가장 가까운 홀 찾기
            if hole_distance > target_hole:
                hole_distance = target_hole
                target_x = hit_x
                target_y = hit_y

    width = abs(target_x - whiteBall_x)
    height = abs(target_y - whiteBall_y)

    radian = math.atan(width / height)
    angle = 180 / math.pi * radian

    if target_x > whiteBall_x and target_y > whiteBall_y:
        radian = math.atan(width / height)
        angle = 180 / math.pi * radian

    elif target_x > whiteBall_x and target_y < whiteBall_y:
        radian = math.atan(height / width)
        angle = 90 + (180 / math.pi * radian)

    elif target_x < whiteBall_x and target_y < whiteBall_y:
        radian = math.atan(height / width)
        angle = 180 + (90 - (180 / math.pi * radian))

    elif target_x < whiteBall_x and target_y > whiteBall_y:
        radian = math.atan(height / width)
        angle = (180 / math.pi * radian) + 270

    distance = math.sqrt(width ** 2 + height ** 2)
    power = (distance * 1.2 + hole_distance * 0.8) / 3.75

    conn.send(angle, power)


def main():
    conn = Conn()
    gameData = GameData()
    while True:
        gameData.read(conn)
        if gameData.balls[0][0] == SIGNAL_ORDER:
            gameData.arrange()
            continue
        elif gameData.balls[0][0] == SIGNAL_CLOSE:
            break
        gameData.show()
        play(conn, gameData)
    conn.close()


if __name__ == '__main__':
    main()