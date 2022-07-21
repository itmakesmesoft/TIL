# Vending Machine
### 문제

주어진 코드를 활용하여 자판기 프로그램을 만들어봅니다. 자판기는 아래와 같은 동작을 수행합니다.

- 금액은 사용자가 그만 넣을 때까지 계속 넣을 수 있습니다. 금액은 누적됩니다.
- 누적된 금액을 통해 구매할 수 있는 메뉴만 화면에 출력합니다.
- 메뉴 구매 후 사용자에게 거스름돈을 반환합니다.

</br>

### 제공되는 변수 설명

`menus` : 메뉴 이름에 해당하는 리스트입니다. (내부 값 변경 금지)</br>
`costs` : 각 메뉴의 가격에 해당하는 리스트입니다. (내부 값 변경 금지)</br>
`budget` : 자판기에 넣은 총 누적 금액을 담는 변수입니다.</br>
`money` : 사용자가 한 번에 입력하는 금액을 담는 변수입니다</br>
</br>

### 제약사항

- **금액 넣기**
    - 주어진 코드에서 money 변수를 이용하여 사용자가 한 번에 넣는 금액을 입력받고 있습니다.
    (사용자는 정수만 입력한다고 가정합니다. 입력에서 소수나 문자에 대한 처리는 하지 않아도 됩니다.)
    - 사용자가 금액을 넣을 때마다 현재 누적 금액은 1200원입니다. 와 같은 문구를 통해 총 누적
    금액이 얼마인지 출력합니다. 이후 1-1로 돌아갑니다. (여기서 1200원은 예시이며, 실제로는 사용자가 넣은 총 누적 금액에 따라 달라져야 합니다.)
    - 사용자가 음수를 입력하는 경우, 금액은 1원 이상 넣어주세요. 라는 문구를 출력하고 [금액넣기]로 돌아갑니다.
    - 사용자가 숫자 0을 입력하는 경우, 더 이상 금액을 넣을 수 없으며 [메뉴 출력] 으로 넘어갑니다.
- **메뉴 출력**
    - 총 누적 금액이 가장 싼 메뉴의 가격보다 낮다면, 400원으로 구매 가능한 메뉴가 없습니다. 라는 문구를 출력하고 프로그램을 종료합니다. (여기서 400원은 예시이며, 실제로는 사용자가 넣은 총 누적 금액에 따라 달라져야 합니다.)
    - 총 누적 금액으로 구매 가능한 메뉴가 있다면, 3000원으로 구매 가능한 메뉴는 다음과 같습니다. 라는 문구를 출력하고, 바로 아래에 구매 가능한 메뉴 목록을 출력합니다. (여기서 3000원은 예시이며, 실제로는 사용자가 넣은 총 누적 금액에 따라 달라져야 합니다.)
    - 이후 [메뉴 선택]으로 넘어갑니다.
- **메뉴 선택**
    - 구매하실 메뉴의 번호를 입력하세요. 라는 문구와 함께 사용자가 구매할 메뉴의 번호를 입력
    받습니다. (사용자는 정수만 입력한다고 가정합니다. 입력에서 소수나 문자에 대한 처리는 하지 않아도 됩니다.)
    - 사용자가 구매 가능한 메뉴를 골랐다면 [거스름돈 반환] 으로 넘어갑니다.
    - 사용자가 구매 할 수 없는 메뉴를 골랐다면 구매할 수 없는 메뉴입니다. 라는 문구를 출력하고 [메뉴선택]으로 돌아갑니다.
- **거스름돈 반환**
    - 메뉴 선택 후, 사이다를 구매하셨습니다. 와 같은 문구와 함께 사용자가 어떤 메뉴를 선택했는지 보여줍니다. (여기서 사이다는 예시이며, 실제로는 사용자가 선택한 메뉴에 따라 달라져야 합니다.)
    - 이후 거스름돈은 2300원입니다. 감사합니다. 와 같은 문구와 함께 사용자에게 반환할 거스름
    돈을 출력하고 프로그램을 종료합니다. (여기서 2300원은 예시이며, 실제로는 거스름돈의 액수에 따라 달라져야 합니다.

</br>

### 풀이

```python
print('=================================')
print('         Vending Machine         ')
print('=================================')
print('[Menu]')
print('1. 콜라 500원')
print('2. 사이다 700원')
print('3. 레모네이드 4500원')
print('4. 오렌지주스 2000원')
print('5. 초코우유 1200원')
print('6. 아메리카노 3600원')
print('=================================')

menus = ['콜라', '사이다', '레모네이드', '오렌지주스', '초코우유', '아메리카노']  # 메뉴 이름
costs = [500, 700, 4500, 2000, 1200, 3600]  # 메뉴 가격
budget = 0  # 자판기에 넣은 총 누적 금액
possible_m=[]

while True:
    print()
    money = int(input('금액을 넣어주세요.(그만 넣으시려면 0을 입력하세요.) : '))
    if money==0:
        for ind, c in enumerate(costs):
            if c<=budget:
                possible_m.append((menus[ind], c))
        break
    elif money<0:
        print('금액은 1원 이상 넣어주세요.')
    else:
        budget+=money
        print(f'현재 누적 금액은 {budget}원입니다.')

if budget<min(costs):
    print(f'\n{budget}원으로 구매 가능한 메뉴가 없습니다.')
else:
    print(f'\n{budget}원으로 구매 가능한 메뉴는 다음과 같습니다.')
    cnt=1
    for menu, cost in possible_m:
        print(f'{cnt}. {menu} {cost}원')
        cnt+=1
    while True:
        choice=int(input('\n구매하실 메뉴의 번호를 입력하세요. : '))
        if choice<=0 or choice>len(possible_m):
            print('구매할 수 없는 메뉴입니다.')
        else:
            print(f'\n{possible_m[choice-1][0]}를 구매하셨습니다.')
            print(f'거스름돈은 {budget-possible_m[choice-1][1]}원입니다. 감사합니다.')
            break
```