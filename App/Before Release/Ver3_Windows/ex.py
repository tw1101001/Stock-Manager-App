# import wx
# import wx.lib.scrolledpanel as scrolled
# import pandas as pd
#
# data = pd.read_csv("物資名.csv")
# names = data["名前"]
# checkbox = []
#
# class Top(wx.Frame):
#     def __init__(self):
#         super().__init__(None,wx.ID_ANY,"在庫管理システム")
#
# # class MyFrame(wx.Frame):
# #     def __init__(self):
# #        wx.Frame.__init__(self, None, -1, "Title")
#
#         # フレーム
#         self.SetSize((1000,700))
#         self.SetBackgroundColour((207,207,207))
#         self.Center()
#
#
#         # Notebook設定
#         # self.notebook = wx.Notebook(self,wx.ID_ANY,style=wx.NB_TOP)
#
#
#         # 現在の在庫状況
#         self.panel_home = wx.Panel(self,wx.ID_ANY)
#         self.panel_home_left = wx.Panel(self.panel_home,-1,pos=(0,0),size=(300,600))
#         self.panel_home_right = wx.Panel(self.panel_home,-1,pos=(300,0),size=(700,600))
#         # self.panel_home_left.SetupScrolling()
#         # self.panel_home_right.SetupScrolling()
#         self.layout_left = wx.BoxSizer(wx.VERTICAL)
#         self.layout_right = wx.BoxSizer(wx.VERTICAL)
#
#         for name in names:
#             tmp = wx.CheckBox(self.panel_home_left,wx.ID_ANY,str(name))
#             checkbox.append(tmp)
#             self.layout_left.Add(tmp)
#
#         self.panel_home_right.SetSizer(self.layout_right)
#         self.panel_home_left.SetSizer(self.layout_left)
#
#         self.Bind(wx.EVT_CHECKBOX,self.checked)
#
#         # self.notebook.InsertPage(0,self.panel_home, "現在の在庫状況")
#
#
#         # 発注
#         # self.panel_hacchu = wx.Panel(self.notebook,wx.ID_ANY)
#         # self.notebook.InsertPage(1,self.panel_hacchu, "本日の発注")
#
#
#         # 過去のデータ
#         # self.panel_kakonodata = wx.Panel(self.notebook,wx.ID_ANY)
#         # self.notebook.InsertPage(2,self.panel_kakonodata, "過去のデータ")
#         #
#
#         # 今後の発注数
#         # self.panel_syouhidouko = wx.Panel(self.notebook,wx.ID_ANY)
#         # self.notebook.InsertPage(3,self.panel_syouhidouko, "今後の発注数")
#
#
#         # 表示
#         self.Show()
#
#
#     def checked(self,event):
#         self.layout_right.Clear(False)
#         counts = 0
#         for checked in checkbox:
#             torf = checked.GetValue()
#             if torf == True:
#                 tmp2 = wx.StaticText(self.panel_home_right,wx.ID_ANY,str(names[counts]),size=(100,20))
#                 self.layout_right.Add(tmp2)
#             counts += 1
#
# app = wx.App()
# Top()
# app.MainLoop()




# -----------------------------------------------------------------------------------------




# import wx
#
# application = wx.App()
# frame = wx.Frame(None, wx.ID_ANY, 'テストフレーム', size=(300, 200))
#
# panel = wx.Panel(frame, wx.ID_ANY)
# panel.SetBackgroundColour('#AFAFAF')
#
# s_text_1 = wx.StaticText(panel, wx.ID_ANY, 'テキスト１')
# s_text_2 = wx.StaticText(panel, wx.ID_ANY, 'テキスト２')
# s_text_3 = wx.StaticText(panel, wx.ID_ANY, 'テキスト３')
# s_text_4 = wx.StaticText(panel, wx.ID_ANY, 'テキスト４')
# s_text_5 = wx.StaticText(panel, wx.ID_ANY, 'テキスト５')
#
# layout = wx.BoxSizer(wx.VERTICAL)
# layout.Add(s_text_1)
# layout.Add(s_text_2)
# layout.Add(s_text_3)
# layout.Add(s_text_4)
# layout.Add(s_text_5)
#
# panel.SetSizer(layout)
#
# frame.Show()
# application.MainLoop()




# ----------------------------------------------------------------------------




# import numpy as np
# import matplotlib.pyplot as plt
#
# plt.rcParams["ytick.direction"] = "in"
# fig = plt.figure(figsize = (8, 0.5))
# # fig = plt.figure()
# ax = fig.add_subplot(111)
# fig.subplots_adjust(bottom=0.5)
# ax.set_xlim(0,10)
# ax.set_xticks([0,1,2,3,4,5,6,7,8,9,10])
# ax.set_xticklabels(["0%","10%","20%","30%","40%","50%","60%","70%","80%","90%","100%"])
# ax.set_ylim(0,1)
# ax.set_yticks([0.5])
# ax.set_yticklabels([""])
#
#
# x = [0.5]
# y = [4]
#
# plt.barh(x, y, align="center")           # 中央寄せで棒グラフ作成
# plt.show()




# ---------------------------------------------------------------------------------------




# import wx
#
#
# class Main(wx.Frame):
#
#     def __init__(self, parent, id, title):
#         """ レイアウトの作成 """
#
#         wx.Frame.__init__(self, parent, id, title)
#         panel = wx.Panel(self, wx.ID_ANY)
#
#         # メニューバーの生成
#         menu_bar = wx.MenuBar()
#
#         # 「ファイル」メニュー生成
#         file = wx.Menu()
#         file.Append(1, "新規")
#         file.Append(2, "終了")
#
#         # 「編集」メニュー作成
#         edit = wx.Menu()
#         edit.Append(3, "コピー")
#         edit.Append(4, "貼り付け")
#
#         # メニューをメニューバーへ登録
#         menu_bar.Append(file, 'ファイル')
#         menu_bar.Append(edit, '編集')
#
#         # フレームにメニュバー登録
#         self.SetMenuBar(menu_bar)
#
#         # メニュークリック時のイベント登録
#         self.Bind(wx.EVT_MENU, self.click_menu)
#
#         self.text = wx.StaticText(panel, wx.ID_ANY, "押されたメニューが表示されます")
#
#         self.Show(True)
#
#     def click_menu(self, event):
#         event_id = event.GetId()
#         msg = ""
#         if event_id == 1:
#             msg = "新規が押された"
#         elif event_id == 2:
#             msg = "終了が押された"
#         elif event_id == 3:
#             msg = "コピー押された"
#         elif event_id == 4:
#             msg = "貼り付けが押された"
#
#         self.text.SetLabel(msg)
#
#
# def main():
#     app = wx.App()
#     Main(None, wx.ID_ANY, "タイトル")
#     app.MainLoop()
#
# if __name__ == "__main__":
#     main()




# ----------------------------------------------------------------------------------------




# from Crypto.PublicKey import RSA
# from Crypto.Cipher import PKCS1_OAEP
#
# # pemロード
# with open('private.pem', 'br') as f:
#     private_pem = f.read()
#     private_key = RSA.import_key(private_pem)
#
# with open('public.pem', 'br') as f:
#     public_pem = f.read()
#     public_key = RSA.import_key(public_pem)
# #
# #
# # message = "a"
# # public_cipher = PKCS1_OAEP.new(public_key)
# # ciphertext = public_cipher.encrypt(message.encode())
# # print(ciphertext)
#
# # メッセージを復号
# ciphertext = b'}\x8e\xac\x90]M\xe8\xeb|V!\xb8\x9b\xcb\xb2T\xad\x88\xd5\xeb\x18y\x16\x95`\x8f\xe8\xce\xa5\x7f\xe7\x90\xd6\xcb\x88\x98\x8c\xff\x9c\xf9\xd3\x95\x94\xf0\xfa\xc2\x8e\xc0\xa5(g<\\CY\xe1W\xe4\xa9\x9b\xfb\xa51\x1cA\xa6\xd9\xdc\xfd)\xf8\xce\x12;Xkt@\xa29\xf6\xd08"\xe4\x96\x1a%\xa8\xa2\tA\xd2\x19W\x97r\xbf\x1f\xaa\x08)\xea\xf3\x00\xb0N\t\xa5\x12\xff\xb1:\x11\xb57\x01\xd7\x13\x8a\xa2\x0e\x8a\xb5~\x1b\xbd+'
# private_cipher = PKCS1_OAEP.new(private_key)
# message2 = private_cipher.decrypt(ciphertext).decode("utf-8")
# print(message2)




# -----------------------------------------------------------------------------------------------




# import base64
# import random
# from Crypto.Cipher import AES
# from hashlib import sha256
#
# class AESCipher(object):
#     def __init__(self, key, block_size=32):
#         self.bs = block_size
#         if len(key) >= len(str(block_size)):
#             self.key = key[:block_size]
#         else:
#             self.key = self._pad(key)
#
#     def generate_salt(self,digit_num):
#         DIGITS_AND_ALPHABETS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#         return "".join(random.sample(DIGITS_AND_ALPHABETS, digit_num)).encode()
#
#     def encrypt(self, raw):
#         raw = self._pad(raw)
#         salt = self.generate_salt(AES.block_size)
#         salted = ''.encode()
#         dx = ''.encode()
#         while len(salted) < 48:
#             hash = dx + self.key.encode() + salt
#             dx = sha256(hash).digest()
#             salted = salted + dx
#
#         key = salted[0:32]
#         iv = salted[32:48]
#
#         cipher = AES.new(key, AES.MODE_CBC, iv)
#         return base64.b64encode(salt + cipher.encrypt(raw))
#
#     def decrypt(self, enc):
#         enc = base64.b64decode(enc)
#         salt = enc[0:16]
#         ct = enc[16:]
#         rounds = 3
#
#         data00 = self.key.encode() + salt
#         hash = {}
#         hash[0] = sha256(data00).digest()
#         result = hash[0]
#         for i in range(1, rounds):
#             hash[i] = sha256(hash[i - 1] + data00).digest()
#             result += hash[i]
#
#         key = result[0:32]
#         iv = result[32:48]
#         cipher = AES.new(key, AES.MODE_CBC, iv)
#         return cipher.decrypt(enc[16:]).decode()
#
#     def _pad(self, s):
#         return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)
#
#     def _unpad(self, s):
#         return s[:-ord(s[len(s)-1:])]



# --------------------------------------------------------------------------------------------------------



import pickle

password_setting_hash_value = b'}\x8e\xac\x90]M\xe8\xeb|V!\xb8\x9b\xcb\xb2T\xad\x88\xd5\xeb\x18y\x16\x95`\x8f\xe8\xce\xa5\x7f\xe7\x90\xd6\xcb\x88\x98\x8c\xff\x9c\xf9\xd3\x95\x94\xf0\xfa\xc2\x8e\xc0\xa5(g<\\CY\xe1W\xe4\xa9\x9b\xfb\xa51\x1cA\xa6\xd9\xdc\xfd)\xf8\xce\x12;Xkt@\xa29\xf6\xd08"\xe4\x96\x1a%\xa8\xa2\tA\xd2\x19W\x97r\xbf\x1f\xaa\x08)\xea\xf3\x00\xb0N\t\xa5\x12\xff\xb1:\x11\xb57\x01\xd7\x13\x8a\xa2\x0e\x8a\xb5~\x1b\xbd+'

with open("secret.binaryfile","wb") as password:
  pickle.dump(password_setting_hash_value,password)