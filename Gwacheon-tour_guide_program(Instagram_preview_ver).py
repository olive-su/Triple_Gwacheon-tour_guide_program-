from tkinter import*
import tkinter
import turtle

window = Tk()
window.title("과천 관광지 PREVIEW (인스타그램 ver)")
window.geometry("555x300")



###관광지 이미지 표시###

def process_1():
    window.destroy()
    t=turtle.Turtle()
    screen =turtle.Screen()
    image="./lets_run.gif"
    screen.addshape(image)
    t.shape(image)
    t.stamp()
    t.speed(0)
    
    Bio = Tk() #관광지 설명 텍스트 창

    Bio.geometry('450x300')
    Bio.title("렛츠런 파크 서울")
    Bio.resizable(True, True)

        

    label01 = Label(Bio, text="\n  렛츠런 파크 서울 \n 서울대공원과 서울랜드의 북쪽에 접한 국제규모의 경기장\n1986년 제10회 아시아경기대회,\n1988년 제24회 서울올림픽대회 개최 후 1989년 9월 개장\n경마에 관한 모든 업무를 이 곳에서 맡음\n주요 시설 : 지하 1층~6층의 관람대와 모래마장인 주경기장 , 마체 검사장\n관람대는 지하 1층·지상 6층의 규모로 길이 210m, 폭 50m\n각층마다 마권판매소와 식당·매점 등이 편의시설 있음\n이밖에 마장마술연습장·장애물비월연습장 등의 각종 부대시설 있음\n1994년 6월에는 경주로 안쪽 유휴부지에 \n일반시민을 위한 편의시설을 갖추고 서울승마공원 개장\n공원의 주요 시설 : 마사박물관·어린이승마장과 휴식공간 \n마사박물관은 1988년 개관하여 선사시대부터 근대에 이르기까지 \n말과 관련한 각종 유물 1300여 점을 전시\n")
    label01.grid(row=0,column=0)
    
    
def process_2():
    window.destroy()
    t=turtle.Turtle()
    screen =turtle.Screen()
    image="./science_center.gif"
    screen.addshape(image)
    t.shape(image)
    t.stamp()
    t.speed(0)
    
    Bio = Tk() #관광지 설명 텍스트 창

    Bio.geometry('450x300')
    Bio.title("국립 과천 과학관")
    Bio.resizable(True, True)

        

    label01 = Label(Bio, text="\n  국립과천과학관\n2008년 개관\n 기초과학,천문우주,생명과 자연에서 전통과학, 첨단기술에 이르기까지\n다양한 분야의 과학과 기술을 쉽게 보고 느끼고 체험할 수 있는 전시장이자,\n교육 프로그램과 문화행사를 펼치는 과학문화 확산의 공간\n최근 미래상상SF관, 자연사관, 첨단기술관을 새롭게 전시\n현대생활에서 어쩔 수 없이 수반되는 재해, 재난, 질병 등 국민적 관심사항에\n대해서도 과학관이 정확한 과학적 정보와 지식을 제공\n메이커, 소프트웨어 교육 등 시대에 맞는 \n교육프로그램을 개발하고 관람객이 체험하며\n호응하는 과학문화행사를 통해 과학과 문화가 어우러진 과천과학관으로 더욱 발전\n")
    label01.grid(row=0,column=0)
    
    
def process_3():
    window.destroy()
    t=turtle.Turtle()
    screen =turtle.Screen()
    image="./seoul_land.gif"
    screen.addshape(image)
    t.shape(image)
    t.stamp()
    t.speed(0)

    Bio = Tk() #관광지 설명 텍스트 창

    Bio.geometry('450x300')
    Bio.title("서울랜드")
    Bio.resizable(True, True)

        

    label01 = Label(Bio, text="\n  서울랜드\n1988년 5월 11일 88올림픽을 앞두고 개장한 국내 최초의 테마파크\n‘세계의 광장','삼천리동산’,‘미래의 나라’,‘모험의 나라’,‘환상의 나라’ 등 5개의\n테마구역으로 나누어 최첨단 대단위 주제공원으로 조성 다양한 놀이시설,\n전시 이벤트, 캐릭터 사업 등 시민들에게 즐거움을 주는 휴식공간으로서\n 문화, 공연, 축제 등이 함께 어우러진 공간\n")
    label01.grid(row=0,column=0)
    
        
def process_4():
    window.destroy()
    t=turtle.Turtle()
    screen =turtle.Screen()
    image="./mmca_gwacheon.gif"
    screen.addshape(image)
    t.shape(image)
    t.stamp()
    t.speed(0)

    Bio = Tk() #관광지 설명 텍스트 창

    Bio.geometry('450x300')
    Bio.title("국립 현대미술관(과천)")
    Bio.resizable(True, True)

        

    label01 = Label(Bio, text="\n  국립 현대미술관(과천)\n1969년 개관 이래 대한민국을 대표하는 문화공간\n현대미술관은 1986년 과천, 1998년 덕수궁, 2013년 서울에 \n이어 2018년 청주 개관으로 4관 체계를 만들었으며,\n유기적이면서도 각각의 색깔을 지님\n건축, 디자인, 공예 등 다양한 시각예술 장르를 아우르며\n자연 속에서 휴식을 제공 복합예술, 과학, 인문학을 비롯한 다양한 학문이\n현대미술과 소통할 수 있는 문화의 산실로 거듭 남\n50년 축적된 국립현대미술관의 역사를 바탕으로 미술계의 의견을 두루 모아\n 전문가 눈높이에서는 미술계 담론을 생산하는 본거지 역할을 하는 동시에\n국민들에게는 미술사를 바탕으로 체계화된 전시와 교육의 역할을 하는 곳\n")
    label01.grid(row=0,column=0)
    
    
def process_5():
    window.destroy()
    t=turtle.Turtle()
    screen =turtle.Screen()
    image="./grandpark_seoul_camping.gif"
    screen.addshape(image)
    t.shape(image)
    t.stamp()
    t.speed(0)

    Bio = Tk() #관광지 설명 텍스트 창

    Bio.geometry('450x300')
    Bio.title("과천 서울대공원 자연 캠핑장")
    Bio.resizable(True, True)

        

    label01 = Label(Bio, text="\n  과천 서울대공원 자연 캠핑장\n캠핑장 정보\n캠핑장 규모 : 일반캠핑_일반텐트(148동)\n캠핑장 이용시간 : -개장 및 이용기간 : 매년 개장일(3월30일)~11월 10일 \n*3월에서 11월 운영기간 중 무휴\n서울대공원 캠핑장은 청계산 맑은 계곡물과 \n울창한 산림에서 나오는 상쾌한 공기가 피부에 전해지는 공간으로 \n야영 및 취사, 레크레이션, 피크닉을 즐기실 수 있습니다.")
    label01.grid(row=0,column=0)
   
    
def process_6():
    window.destroy()
    t=turtle.Turtle()
    screen =turtle.Screen()
    image="./grandpark_seoul.gif"
    screen.addshape(image)
    t.shape(image)
    t.stamp()
    t.speed(0)

    Bio = Tk() #관광지 설명 텍스트 창

    Bio.geometry('450x300')
    Bio.title("서울 동물원")
    Bio.resizable(True, True)

        

    label01 = Label(Bio, text="\n  서울 동물원\n동물에게 더 생태적이고 쾌적한 환경을 제공함으로써,\n동물들이 행복하고 행복한 동물을 보면서 관람객이 행복해지는 동물원을 만들고자 \n노력하고 있으며 동물원의 기능인 전시, 보전, 교육, 연구에 힘쓰고 있음\n귀중한 동물자원을 다음 세대에 건강하게 넘겨주어야 할 중요한 보존 및 연구 역할을\n가지고 있다고 생각하고 국제적 희귀종뿐만 아니라 국내 멸종위기 동물의\n보존과 번식을 위하여 체계적이고 과학적인 연구를 하고 있으며,\n이와 발맞추어 다양한 내용의 동물 보전 교육 프로그램도 함께 추진\n국제적으로는 야생동물보호를 위한 기능과 업적을 높이 평가 받아\n국내에서는 유일하게 ISIS(국제종보전시스템) 및 \nIUDZG-WZO(세계동물원기구)에 정회원으로서의 자격 부여\n")
    label01.grid(row=0,column=0)
   
    
    
def off(): #종료하기
    window.destroy()

close = Button(window, width=50, text="종료하기",command=off)
close.grid(row=10, column=0)



######################
### 초기 버튼 화면 ###
######################


L1 = Label(window, width=50, fg="yellow", bg="gray", font=("Gothitext"), text="<과천 관광지 PREVIEW (인스타그램 ver)>")
L2 = Label(window, width=50, fg="yellow", bg="gray", font=("Gothitext"), text=" ")
L3 = Label(window, width=50, fg="yellow", bg="gray", font=("Gothitext"), text="가상 인스타그램 피드를 보고싶은 장소를 선택하세요.")

L1.grid(row=1, column=0)
L2.grid(row=2, column=0)
L3.grid(row=3, column=0)



B1 = Button(window, width=50, text ="렛츠런 파크 서울",command=process_1)
B1.grid(row=4, column =0)
B2 = Button(window, width=50, text ="국립 과천 과학관", command=process_2)
B2.grid(row=5, column =0)
B3 = Button(window, width=50, text ="서울랜드", command=process_3)
B3.grid(row=6, column =0)
B4 = Button(window, width=50, text ="국립 현대미술관(과천)", command=process_4)
B4.grid(row=7, column =0)
B5 = Button(window, width=50, text ="과천 서울대공원 자연 캠핑장", command=process_5)
B5.grid(row=8, column =0)
B6 = Button(window, width=50, text ="서울 동물원", command=process_6)
B6.grid(row=9, column =0)



window.mainloop()
