import random

class lastword:

    def __init__(self):
        self.UserCount = 0
        self.UserList = []
        self.WordList = []

    def userCount(self):
        while(True):
            Count = input("참여 인원 수 입력 (최대 10명): ")
            if Count.isdigit() == False:
                print("숫자만 입력해주세요.")
            elif int(Count) > 10:
                print("최대 인원은 10명입니다.")
            else:
                break
        self.UserCount = int(Count)
        print("========================================")

    def userName(self):
        for i in range(self.UserCount):
            while(True):
                name = input("{}번 인원 닉네임을 입력해주세요. : ".format(i + 1))
                if name in self.UserList:
                    print("중복입니다.")
                elif name.isalpha() == False:
                    print("문자만 입력 가능합니다.")
                else:
                    self.UserList.append(name)
                    break
        print("========================================")

    def Draw(self):
        print("순서 정하기 1. 랜덤 2. 입력순서 거꾸로 3. 입력순서")
        while(True):
            draw = input("번호 입력 : ")
            if draw.isdigit() == False:
                print("숫자를 입력해주세요.")
            elif draw != "1" and draw != "2" and draw != "3":
                print("입력 범위를 벗어 났습니다.")
            else:
                draw = int(draw)
                break
        if draw == 1:
            print("랜덤을 선택했습니다.")
            random.shuffle(self.UserList)
            print("순서는 \n", self.UserList)
        elif draw == 2:
            print("인력순서 거꾸로 선택했습니다.")
            self.UserList.reverse()
            print("순서는 \n", self.UserList)
        else:
            print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
            print("입력순서를 선택했습니다.")
            print("순서는 \n", self.UserList)
        print("========================================")

    def Start(self):
        UserList = self.UserList
        LoserList = []
        print("게임을 시작합니다.")
        print("========================================")
        gameCount = 0
        while(True):
            for name in self.UserList:
                LoseCount = 0
                while(True):
                    if LoseCount == 3:
                        print("실패 3회 초과 탈락입니다.")
                        print("\"{}\"님은 탈락입니다.".format(name))
                        LoserList.append(name)
                        UserList.remove(name)
                        gameCount += 1
                        break
                    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
                    print("{}턴 ".format(gameCount + 1) + "\"" + name + "\"" + "님 차레입니다.")
                    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
                    word = input("단어를 입력하세요. : ")
                    if word.isalpha == False or len(word) <= 1:
                        LoseCount += 1
                        print("{}회 실패 단어를 정확하게 입력해주세요.".format(LoseCount))
                    else:
                        # 단어가 있다면 탈락
                        if word in self.WordList:
                            print("========================================")
                            print("\"{}\"는 중복 문자입니다.".format(word))
                            print("\"{}\"님은 탈락입니다.".format(name))
                            LoserList.append(name)
                            UserList.remove(name)
                            print("========================================")
                            gameCount += 1
                            break
                        # 첫번째 턴이 아니라면
                        elif gameCount != 0:
                            # 앞에 단어를 Test에 삽입
                            Test = self.WordList[gameCount - 1]
                            # 앞에 단어 맨뒤와 지금 입력단어 맨앞을 비교 
                            if Test[-1] != word[0]:
                                print("========================================")
                                print("\"{}\"는 연결되지 않습니다.".format(word))
                                print("\"{}\"님은 탈락입니다.".format(name))
                                LoserList.append(name)
                                UserList.remove(name)
                                print("========================================")
                                gameCount += 1
                                break
                            else:
                                print("통과")
                                self.WordList.append(word)
                                gameCount += 1
                                break
                        # 정확하면
                        else:  
                            print("통과")
                            self.WordList.append(word)
                            gameCount += 1
                            break
                
            if len(UserList) == 1:
                LoserList.append(UserList[0])
                print(" 게 임 종 료 ")
                break
            
               
        print("========================================")
        print(" 순 위 ")
        LoserList.reverse()
        for i in range(len(LoserList)):
            print("{}등 {}님,".format(i + 1, LoserList[i]),end=" ")

if __name__ == "__main__":
    Game = lastword()
    Game.userCount()
    Game.userName()
    Game.Draw()
    Game.Start()