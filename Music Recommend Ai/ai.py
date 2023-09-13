'''
알고리즘 구상을 위해 임시로 제작
나중에 js로 수정 가능성 있음
'''

musicList = [
    #['이름', '재생횟수', [['관련곡', '재생횟수']]]
    ['후라이의 꿈', 0, [], []],
    ['헤어지자 말해요', 0, [], []],
    ['사막에서 꽃을 피우듯', 0, [], []],
    ['모래 알갱이', 0, [], []],
    ['비오는 날', 0, [], []],
    ['비오는 오후', 0, [], []],
    ['서울밤거리', 0, [], []],
    ['푸르름', 0, [], []],
    ['벚꽃 엔딩', 0, [], []],
    ['벚꽃이 지면', 0, [], []],
    ['그날에 우리', 0, [], []],
    ['내가 너라면', 0, [], []],
    ['유서', 0, [], []],
    ['우리 함께', 0, [], []],
    ['기억을 걷는 시간', 0, [], []],
    ['비가 올 때면', 0, [], []],
    ['너무너무', 0, [], []],
    ['자격', 0, [], []],
    ['나만큼만', 0, [], []],
    ['자유', 0, [], []],
    ['우리는 여기 오래 남아', 0, [], []],
    ['님이여', 0, [], []],
]


def deyMusic(music):
    '''
    노래 리스트를 입력
    '''
    for Mu in range(len(music)):    #노래만큼 반복
        music[Mu][1] += 1

        for mu in music:            #관련성 추가
            if not mu[0] == music[Mu][0]:
                if not mu[0] in music[Mu][2]:
                    music[Mu][2].append(mu[0])
                    music[Mu][3].append(0)
                music[Mu][3][music[Mu][2].index(mu[0])] += 1
                
    return music

def foundName(*name):
    '''
    이름을 찾아 리스트에 값으로 변환
    '''
    music = []

    for n in name:
        for musicNumber in musicList:
            if n == musicNumber[0]: music.append(musicNumber)

    return music

def listAdd(li):
    '''
    수정한 값을 리스트에 추가
    '''

    musicList_ = musicList

    for l in li:
        for musicNumber in range(len(musicList_)):
            if l[0] == musicList_[musicNumber][0]: musicList_[musicNumber] = l

    return musicList_

def musicRecommend(music):
    '''
    노래 추천
    '''
    recommend_list = []

    name = foundName(music)[0]
    for i in range(len(name[2])):
        recommend_list.append([name[2][i], name[3][i] / foundName(name[2][i])[0][1] / name[1]])

    return recommend_list

musicList = listAdd(deyMusic(foundName('후라이의 꿈', '모래 알갱이', '푸르름', '기억을 걷는 시간', '너무너무')))
musicList = listAdd(deyMusic(foundName('비가 올 때면', '비오는 날', '자격', '서울밤거리', '너무너무')))
musicList = listAdd(deyMusic(foundName('비가 올 때면', '비오는 날', '비오는 오후', '유서', '너무너무')))

print(musicRecommend('비오는 날'))
