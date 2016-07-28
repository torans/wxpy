#coding:utf-8

"""将用户输入的值通过MD5加密后显示在界面上。未完待续..."""
import wx
import hashlib
class TextFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Text Entry Example',
                size=(600, 400))
        panel = wx.Panel(self, -1)
        self.txt = wx.TextCtrl(panel, -1, u"123456")

        #result
        static2 = wx.StaticText(panel, wx.NewId(),u"32位：",
                pos=(10, 80))

        btn = wx.Button(panel,-1,u'加密')
        self.Bind(wx.EVT_BUTTON,self.Md5,btn)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.txt, 0, wx.ALL, 20)
        sizer.Add(btn, 0, wx.TOP|wx.RIGHT, 20)
        panel.SetSizer(sizer)

    def Md5(self,event):
        m = hashlib.md5()
        self.content = self.txt.GetValue().decode('gbk').encode('utf-8')
        m.update(self.content)
        result = m.hexdigest()
        print result

    print Md5
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = TextFrame()
    frame.Show()
    app.MainLoop()