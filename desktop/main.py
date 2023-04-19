import ttkbootstrap

from views.login import Login

window = ttkbootstrap.Window(themename="darkly")
window.title('Проверка трафика')
window.geometry('1200x600')

start_page = Login(window)
start_page.pack()
window.mainloop()
