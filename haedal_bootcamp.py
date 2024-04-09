import tkinter as tkt
# ~~.pack() 이 창 자체에 레이블이나 버튼을 꽉 채우는 것

root=tkt.Tk()
root.title("이름")

lbl = tkt.Label(root, text = "이름")
lbl.pack()

txt = tkt.Entry(root) #입력받는 창
txt.pack()        

btn = tkt.Button(root,text="OK")
btn.pack()

root.mainloop()