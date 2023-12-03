from tkinter import *
from tkinter.ttk import *

class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_label_id_label = self.__tk_label_id_label(self)
        self.tk_input_id_input = self.__tk_input_id_input(self)
        self.tk_button_id_button = self.__tk_button_id_button(self)
        self.tk_table_info_table = self.__tk_table_info_table(self)
        self.tk_check_button_func_check_1 = self.__tk_check_button_func_check_1(self)
        self.tk_check_button_func_check_2 = self.__tk_check_button_func_check_2(self)
        self.tk_check_button_func_check_3 = self.__tk_check_button_func_check_3(self)
        self.tk_check_button_func_check_4 = self.__tk_check_button_func_check_4(self)
        self.tk_button_start_button = self.__tk_button_start_button(self)
        self.tk_progressbar_download_progress = self.__tk_progressbar_download_progress(self)
        self.tk_label_download_label = self.__tk_label_download_label(self)
        self.tk_label_app_info_label = self.__tk_label_app_info_label(self)
    def __win(self):
        self.title("Tkinter布局助手")
        # 设置窗口大小、居中
        width = 340
        height = 440
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.minsize(width=width, height=height)
        
    def scrollbar_autohide(self,vbar, hbar, widget):
        """自动隐藏滚动条"""
        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)
        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)
        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())
    
    def v_scrollbar(self,vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')
    def h_scrollbar(self,hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')
    def create_bar(self,master, widget,is_vbar,is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)
    def __tk_label_id_label(self,parent):
        label = Label(parent,text="输入ID：",anchor="center", )
        label.place(relx=0.029411764705882353, rely=0.022727272727272728, relwidth=0.17647058823529413, relheight=0.06818181818181818)
        return label
    def __tk_input_id_input(self,parent):
        ipt = Entry(parent, )
        ipt.place(relx=0.23529411764705882, rely=0.022727272727272728, relwidth=0.5294117647058824, relheight=0.06818181818181818)
        return ipt
    def __tk_button_id_button(self,parent):
        btn = Button(parent, text="检索", takefocus=False,)
        btn.place(relx=0.8235294117647058, rely=0.022727272727272728, relwidth=0.14705882352941177, relheight=0.06818181818181818)
        return btn
    def __tk_table_info_table(self,parent):
        # 表头字段 表头宽度
        columns = {"ID":63,"歌曲":95,"歌手":79,"专辑":79}
        tk_table = Treeview(parent, show="headings", columns=list(columns),)
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=True)  # stretch 不自动拉伸
        
        tk_table.place(relx=0.029411764705882353, rely=0.11363636363636363, relwidth=0.9411764705882353, relheight=0.5454545454545454)
        self.create_bar(parent, tk_table,True, False,10, 50, 320,240,340,440)
        return tk_table
    def __tk_check_button_func_check_1(self,parent):
        cb = Checkbutton(parent,text="歌曲下载",)
        cb.place(relx=0.029411764705882353, rely=0.6818181818181818, relwidth=0.23529411764705882, relheight=0.06818181818181818)
        return cb
    def __tk_check_button_func_check_2(self,parent):
        cb = Checkbutton(parent,text="歌词下载",)
        cb.place(relx=0.2647058823529412, rely=0.6818181818181818, relwidth=0.23529411764705882, relheight=0.06818181818181818)
        return cb
    def __tk_check_button_func_check_3(self,parent):
        cb = Checkbutton(parent,text="封面下载",)
        cb.place(relx=0.5, rely=0.6818181818181818, relwidth=0.23529411764705882, relheight=0.06818181818181818)
        return cb
    def __tk_check_button_func_check_4(self,parent):
        cb = Checkbutton(parent,text="属性编辑",)
        cb.place(relx=0.7352941176470589, rely=0.6818181818181818, relwidth=0.23529411764705882, relheight=0.06818181818181818)
        return cb
    def __tk_button_start_button(self,parent):
        btn = Button(parent, text="开始下载！", takefocus=False,)
        btn.place(relx=0.029411764705882353, rely=0.7727272727272727, relwidth=0.9411764705882353, relheight=0.06818181818181818)
        return btn
    def __tk_progressbar_download_progress(self,parent):
        progressbar = Progressbar(parent, orient=HORIZONTAL,)
        progressbar.place(relx=0.23529411764705882, rely=0.8636363636363636, relwidth=0.7382352941176471, relheight=0.045454545454545456)
        return progressbar
    def __tk_label_download_label(self,parent):
        label = Label(parent,text="下载进度：",anchor="center", )
        label.place(relx=0.029411764705882353, rely=0.8636363636363636, relwidth=0.17647058823529413, relheight=0.045454545454545456)
        return label
    def __tk_label_app_info_label(self,parent):
        label = Label(parent,text="163ListDownloader by CooooldWind_ | Ver xx.yy.zz",anchor="center", )
        label.place(relx=0.029411764705882353, rely=0.9318181818181818, relwidth=0.9411764705882353, relheight=0.045454545454545456)
        return label
class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()
    def SearchPlaylist(self,evt):
        print("<Return>事件未处理:",evt)
    def SearchPlaylist(self,evt):
        print("<Button>事件未处理:",evt)
    def StartDownload(self,evt):
        print("<Button>事件未处理:",evt)
    def __event_bind(self):
        self.tk_input_id_input.bind('<Return>',self.SearchPlaylist)
        self.tk_button_id_button.bind('<Button>',self.SearchPlaylist)
        self.tk_button_start_button.bind('<Button>',self.StartDownload)
        pass
if __name__ == "__main__":
    
    win = Win()
    win.mainloop()
