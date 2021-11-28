from win10toast import ToastNotifier
#notify functiion
def notify(title, content, duration):
    dataconfirm = ToastNotifier()
    icon_path="app.ico"
    dataconfirm.show_toast(title, content, duration, icon_path)

