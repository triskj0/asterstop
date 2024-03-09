import tkinter
from PIL import Image
import customtkinter as ctk
from Asterisk_Key import Asterisk_Key


WIN_WIDTH = 500
WIN_HEIGHT = 480
asterisk = Asterisk_Key()


class Root(ctk.CTk):

    def button_function(self):
        if asterisk.asterisk_is_blocked():
            asterisk.unblock_key()
            self.blocked_label.configure(text=self.unblocked_label_text)

        else:
            asterisk.block_key()
            self.blocked_label.configure(text=self.blocked_label_text)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.APP_FONT = ctk.CTkFont(family = '@BatangChe',
                                    size   = 70,
                                    weight = 'bold')

        self.geometry(f'{WIN_WIDTH}x{WIN_HEIGHT}')
        self.resizable(False, False)
        self.title("Něco pro pana Krále :)")
        ctk.set_default_color_theme("dark-blue")
        
        self.blocked_label_text = "BLOCKED"
        self.unblocked_label_text = "UNBLOCKED"
        self.blocked_label = ctk.CTkLabel(self, text=self.blocked_label_text, padx=15, pady=15)
        self.blocked_label.grid(row=1, column=1)
        self.blocked_label.configure(font = self.APP_FONT)

        self.button_function() # disable by default
        self.asterisk_image = ctk.CTkImage(light_image=Image.open('./../assets/asterisk_white.png'), size=(100, 100))
        self.asterisk_image_button = ctk.CTkButton(master=self, height=300, width=450,
                                                   text="", image=self.asterisk_image, command=self.button_function)
        self.asterisk_image_button.grid(row=2, column=1, padx=22, pady=20)


if __name__ == '__main__':
    root = Root()
    root.mainloop()

