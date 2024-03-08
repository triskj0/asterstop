import keyboard


class Asterisk_Key:
    def __init__(self):
        self.toggled_count = 0
        
    def block_key(self):
        keyboard.block_key('*')
        self.toggled_count += 1

    def unblock_key(self):
        keyboard.unhook_key('*')
        self.toggled_count += 1

    def asterisk_is_blocked(self):
        if self.toggled_count % 2 == 0:
            return False;
        return True;

