class TV:
    #constructor
    def __init__(self):
        self.channel = 1
        self.volume_level = 1
        self.power = False
    #method to turn on tv
    def turn_on(self):
        self.power = True
    #method to turn off tv
    def turn_off(self):
        self.power = False
    #method to get channel of tv
    def get_channel(self):
        return self.channel
    #method to set channel of tv
    def set_channel(self, channel):
        if self.power and 1 <= channel <= 120:
            self.channel = channel
    #method to get volume of tv
    def get_volume(self):
        return self.volume_level
    #method to set volume of tv
    def set_volume(self, volume_level):
        if self.power and 1 <= volume_level <= 7:
            self.volume_level = volume_level
    #method to channel up tv
    def channel_up(self):
        if self.channel > 120:
            self.channel += 1
    #method to channel down tv
    def channel_down(self):
        if self.channel > 120:
            self.channel -= 1
    #method to volume up tv
    def volume_up(self):
        if self.volume_level > 7:
            self.volume_level += 1
    #method to volume down tv
    def volume_down(self):
        if self.volume_level > 7:
            self.volume_level -= 1