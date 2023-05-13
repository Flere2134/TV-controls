from television import TV

#creates tv 1
television_1 = TV()
#turn on tv 1
television_1.turn_on()
#set channel of tv 1 to 30
television_1.set_channel(30)
#set volume of tv 1 to 3
television_1.set_volume(3)
#display tv 1 status
print('Television 1 is on channel', television_1.get_channel(), 'and volume is at', television_1.get_volume())
#increase volume up by 2
television_1.volume_up()
television_1.volume_up()
print('Television 1 volume at', television_1.get_volume())
#decrease volume by 1
television_1.volume_down()
print('Television 1 volume at', television_1.get_volume())

#create tv 2
television_2 = TV()
#turn on tv2
television_2.turn_on()
#set channel of tv 2 to 3
television_2.set_channel(3)
#set volume of tv to 2
television_2.set_volume(2)
#display tv 2 status
print('Television 2 is on channel', television_2.get_channel(), 'and volume is at', television_2.get_volume())