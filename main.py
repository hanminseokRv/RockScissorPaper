import random as r



def start():
    print("컴퓨터와의 가위바위보 한 판 승부!")
    print("3번 이기면 나갈 수 있어요")
    print("묵=>1","가위=2", "보=>3")
    print(rock, scissor, paper)

rock='''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
       '''

scissor='''
   .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/
  '''

paper='''
     _.-._
    | | | |_
    | | | | |
    | | | | |
  _ |  '-._ |
  \`\`-.'-._;
   \    '   |
    \  .`  /
     |    |'''


def Game():
    start()
    win=0
    lose=0
    draw=0
    
    while True:
        print(f'현재{win}승 {draw}무 {lose}패')
        player=int(input("가위 바위 보!>>>"))
        computer=r.randint(1, 3)
        
        
        #1, 2, 3 이외에 다른 키 누름 방지    
        if str(player) not in ('123'):
          print("1, 2, 3 중에서만 고르세요!")
          continue
          
      #5번 이기면 종료  
        if win==4:
          print("축하합니다! 5번 승리하셨습니다")
          break 
        else:   
          #묵=1, 가위=2, 보=3
          if computer==1: #컴퓨터가 묵(1)일 때
            print(rock)
            if player==1:
              draw+=1
            elif player==2:
              lose+=1
            else:
              win+=1
              
          elif computer==2: #컴퓨터가 가위(2)일 때
            print(scissor)
            if player==1:
              win+=1
            elif player==2:
              draw+=1
            else:
              lose+=1
              
          elif computer==3: #컴퓨터가 보(3)일 때
            print(paper)
            if player==1:
              lose+=1
            elif player==2:
              win+=1
            else:
              draw+=1
              
          
          
      
        
          
Game()





# ***교훈****
# while 반복문을 다룰 때는 while 안에서 어떤 것이 반복되는지 인식해야 한다.
# 마구잡이로 코드를 작성하면..
# 반복되어야 하는 것이 반복되지 않을 수 있고,
# 반복되지 않아야 하는 것이 반복될 수 있다.
