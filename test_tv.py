from television import TV
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

#creates tv 1
television_1 = TV()
#turn on tv 1
television_1.turn_on()
#set channel of tv 1 to 30
television_1.set_channel(30)
#set volume of tv 1 to 3
television_1.set_volume(3)
#display tv 1 status
time.sleep(1)
print(Fore.GREEN + Style.BRIGHT + '\nTelevision 1 is on channel ' + str(television_1.get_channel()) + ' and volume is at '+ str(television_1.get_volume()))
#increase volume up by 2
television_1.volume_up()
television_1.volume_up()
#increase channel by 1
television_1.channel_up()
#display tv status
time.sleep(1)
print(Fore.YELLOW + Style.BRIGHT + '\nTelevision 1 is on channel ' + str(television_1.get_channel()) + ' and volume is at '+ str(television_1.get_volume()))
#decrease volume by 1
television_1.volume_down()
#decrease channel by 2
television_1.channel_down()
television_1.channel_down()
#display tv status
time.sleep(1)
print(Fore.BLUE + Style.BRIGHT + '\nTelevision 1 is on channel ' + str(television_1.get_channel()) + ' and volume is at '+ str(television_1.get_volume()))

#create tv 2
television_2 = TV()
#turn on tv2
television_2.turn_on()
#set channel of tv 2 to 3
television_2.set_channel(3)
#set volume of tv to 2
television_2.set_volume(2)
#display tv 2 status
time.sleep(1)
print(Fore.GREEN + Style.BRIGHT + '\nTelevision 2 is on channel ' + str(television_2.get_channel()) + ' and volume is at '+ str(television_2.get_volume()))
#increase channel and volume by 1
television_2.channel_up()
television_2.volume_up()
#display tv status
time.sleep(1)
print(Fore.YELLOW + Style.BRIGHT + '\nTelevision 2 is on channel ' + str(television_2.get_channel()) + ' and volume is at '+ str(television_2.get_volume()))#decrease channel by 1
television_2.channel_down()
#display tv status
time.sleep(1)
print(Fore.BLUE + Style.BRIGHT + '\nTelevision 2 is on channel ' + str(television_2.get_channel()) + ' and volume is at '+ str(television_2.get_volume()))