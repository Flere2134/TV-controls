class TV:
    #constructor
    def __init__(self, channel, volume_level, power):
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
    #method to channel down tv
    #method to volume up tv
    #method to volume down tv