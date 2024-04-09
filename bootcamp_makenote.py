#파이썬 응용 1주차 과제
from tkinter import *
from tkinter.filedialog import *

def new_flie(): #새파일 누르면 새파일이 열리게 해주는 함수
    text_area.delete(1.0, END)
def save_file(): #저장누르면 이 파일이 저장되게 하는 함수
    file_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:  # 사용자가 파일을 선택하고 저장 버튼을 누른 경우에만 파일을 저장
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, END))  # 텍스트 영역의 내용을 파일에 저장
def maker(): #누르면 텍스트가 나오게
    root=Tk()
    root.title("만든이")

    lbl = Label(root, text = "파이썬으로 메모장 만들기")
    lbl.pack()


#윈도우 생성하기
window = Tk()
window.title("Notepad")
window.geometry("400x400+800+300")
window.resizable(0,0)

window.iconbitmap("C:/Users/User/Documents/haedal/2024_Python_bootcamp/notepad-icon_34386.ico")
# png 파일로 추가할 시
# photo = PhotoImage("C:\Users\User\Documents\haedal\2024_haedal_bootcamp\notepad-icon_34386.ico")
# window.iconphoto(False,photo)

#텍스트 창 만들기
text_area = Text(window) #Text() -> 텍스트창이 만들어짐
#공백 설정하기
window.grid_rowconfigure(0, weight = 1) #가로로도 세로로도 꽉차게 해줘야함
window.grid_columnconfigure(0, weight = 1)
#텍스트 화면을 윈도우에 동서남북으로 붙인다.
text_area.grid(sticky = N+E+S+W) #sticky를 써서 비어있는 공간을 한칸씩 각자 붙힌다

#메뉴 생성
menuMaker = Menu(window)
#첫번째 메뉴 만들기
first_menu = Menu(menuMaker, tearoff=0)
#첫번째 메뉴의 세부메뉴 추가 및 함수 연결
first_menu.add_command(label='새 파일', command = new_flie)
first_menu.add_command(label='저장', command= save_file)
#메뉴 바 추가
menuMaker.add_cascade(label='파일', menu=first_menu)

#메뉴 구성
window.config(menu = menuMaker)
#첫번째 메뉴에 구분선 추가
first_menu.add_separator()
#종료 옵션 추가하기
first_menu.add_command(label='종료', command=window.destroy)

#두번재 메뉴 추가
second_menu = Menu(menuMaker, tearoff=0)
#세부 메뉴 추가, 함수 연결
second_menu.add_cascade(label = '만든 이', command = maker)
#메뉴 바 추가
menuMaker.add_cascade(label='정보', menu = second_menu)
window.mainloop() #임마는 꼭 필요하다잉