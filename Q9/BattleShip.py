"""
BattleShip 게임을 만들어보자. 2인용 턴제 게임으로, 좌표를 통해 서로의 배를 격추시킨다. 모든 배를 먼저 격추시킨 플레이어가 승리한다.

특정 사이즈의 격자가 두 플레이어에게 동일하게 주어지고, 다양한 크기의 배를 두 플레이어가 각자 격자에 배치한다.
배는 세로, 또는 가로로 배치할 수 있다.
공격자가 특정좌표를 말하면, 수비자는 그 위치에 배가 있는지 없는지 말해준다.
공격자가 배가 차지하고있는 모든 좌표를 다 이야기했다면, 그 배는 격추된다.
모든 배를 격추시킨 플레이어가 승리한다.

각 문제는 모두 독립적인 문제.

각 플레이어에게 7X7 격자와, 길이가 2, 3, 4, 5이고 폭은 전부 1인 4척의 배가 주어진다.
플레이어1이 먼저 격자에 배를 배치한다. 배치를 입력받는 방법은 길이가 짧은 배 순으로, 배의 머리와 꼬리의 좌표를 입력한다.
(머리 행좌표, 머리 열좌표, 꼬리 행좌표, 꼬리 열좌표)
그 후 플레이어 2가 격자에 배를 배치한다.


a)
배치된 각 플레이어의 격자를 출력한다. 출력포맷 또한 자유롭게 구현해보자.


b)
플레이어1이 먼저 공격을 시작한다. 좌표(행, 열)를 입력하면, 프로그램은 자동으로 상대방 격자의 그 좌표에 배가 있는지 없는지 말해준다.
그 후, 플레이어 2가 공격을 진행한다.

각 공격이 진행된 후, 프로그램은 각 플레이어의 현재 격자상황을 출력해준다.
단, 배의 위치는 전부 숨긴채, 상대방이 공격한 격자의 위치와 그 위치에 배가 있었는지 없었는지만 보여준다.
출력 포맷은 자유롭게 구현해보자.

한 플레이어가 모든 배를 잃으면, 특정 플레이어가 승리했음을 출력하고 프로그램을 종료한다.


c)
GUI 로 구현해보자. pyGame 이나 tKinter 등을 사용해보자.



d)
플레이어 AI를 구현해보자.
자동으로 배를 배치하고, 공격한다.
깊게, 많이 고민해보자. 실제 구현은 하지 못하더라도, 아이디어를 여러개 생각해보자.


"""