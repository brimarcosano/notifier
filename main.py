from tkinter import *
from tkinter import ttk
from plyer import notification
import time
import datetime
import concurrent.futures

# self on callback functions and sringvars

class SetNotifications:
    def __init__(self, root):

        root.title('Notification Set Up')

        # creating frame widget which holds contents of UI
        mainframe = ttk.Frame(root, padding='3 3 12 12')
        mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
        # tells Tk that frame should expand when window resized
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.time = StringVar()
        self.time_entry = ttk.Entry(mainframe, width=7, textvariable=self.time)
        # placing entry in column 2, row 1
        # sticky is how widget should line up with grid cell
        self.time.set('00:00')
        self.time_entry.grid(column=1, row=1, sticky=W)

        self.notes = StringVar()
        self.notes_entry = ttk.Entry(mainframe, width=20, textvariable=self.notes)
        self.notes.set('Enter notes')
        self.notes_entry.grid(column=2, row=2, sticky=W)

        days = ['M', 'TU', 'W', 'TH', 'F', 'SA', 'SU']
        self.days_str = StringVar()
        # set default option
        self.days_str.set('M')
        days_menu = OptionMenu(mainframe, self.days_str, *days)
        days_menu.grid(column=2, row=2, sticky=E)

        ttk.Button(mainframe, 
                text="Set",
                command=lambda:[self.pushNotification(), self.clearEntry()]).grid(column=3, row=3, sticky=W)

        # adding padding to widgets contained within content frame
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        # put focus in entry field so cursor starts in this field
        self.time_entry.focus()
        # if user presses return key, it should enter info
        root.bind("<Return>", self.pushNotification)
    
    def clearEntry(self):
        self.time.set('00:00')
        # self.time_entry.delete(0, END)
        self.notes_entry.delete(0, END)

    def pushNotification(self, *args):
        time_input = self.time.get()
        time_list = []
        flag = True

        if time_input:
            time_list.append(time_input)

        print(time_list)

        msg = self.notes.get()
        while True:
            for t in time_list:
                now = datetime.datetime.now().strftime('%H:%M')
                # print(now)
                # print(t + ' t')
                if (t == now):
                    try:
                        notification.notify(
                            title=f'Reminder set for {t}',
                            message=msg,
                            app_name='notifications',
                            timeout=5
                            )
                        time_list.remove(t)
                        time.sleep(60)
                    except ValueError:
                        pass
                else:
                    continue


if __name__ == '__main__':
    root = Tk()
    SetNotifications(root)
    root.mainloop()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        f = executor.submit(pushNotification, 60)
        print(f.result())