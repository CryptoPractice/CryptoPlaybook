#!/usr/bin/env python3

import time


def get_seed():
    SEED = 0x4a4147412074686520537461636b20435446204368616c6c656e6765
    return SEED + time.time_ns()


FLAG = b'''
     _______.___________. _______ ___    ___      _______    __    ____  ____  __   _______  __    __   _____         __         ____  __   _______  __    __   _____  ___
    /       |           ||   ____|__ \  |__ \    /  /\   \  /  \  /   / / __ \|  | |   ____||  |  |  | | ____|       |  |       / __ \/_ | |   ____||  |  |  | | ____| \  \
   |   (----`---|  |----`|  |__     ) |    ) |  |  |  \   \/    \/   / / / _` |  | |  |__   |  |  |  | | |__         |  |      / / _` || | |  |__   |  |  |  | | |__    |  |
    \   \       |  |     |   __|   / /    / /  /  /    \            / | | (_| |  | |   __|  |  |  |  | |___ \        |  |     | | (_| || | |   __|  |  |  |  | |___ \    \  \
.----)   |      |  |     |  |     / /_   / /_  \  \     \    /\    /   \ \__,_|  | |  |     |  `--'  |  ___) |       |  `----. \ \__,_|| | |  |     |  `--'  |  ___) |   /  /
|_______/       |__|     |__|    |____| |____|  |  |     \__/  \__/     \____/|__| |__|      \______/  |____/   _____|_______|  \____/ |_| |__|      \______/  |____/   |  |
                                                 \__\                                                          |______|                                                /__/
'''

ASCII_JAGA = b'''
................................................................................
................................................................................
................................................................................
................................................................................
..................................,,::~~~,......................................
........................................:~,...........:,........................
.......................,,..............:::I~,.........,~+=......................
...................,:~==:..............,,.=8D$I~........,=7=....................
.................,,,....=+==+I77$$ZZ$7I?~,..$NDDOI~.......,?:...................
.......................,~.=7$Z8DNNDDDDDDD8Z+,$D8DDD$~..,,=7,....................
........................:......,=78D888DDDNN8$88888DD$,.,.?~....................
..........................,::::,,.:I88DNNNDDDNDDDDDDDD8=.,$:....................
....................,~?7ZO88DDDDDDOZ8DDDND88888DDNNNDDNNI.ID:...................
.................,+$8DDDDDDDDNDDDDDDDDDDND88888888D888DDN?:NO,..................
...............:IODDD88888DNND88888888888888888888888888DN78D$..................
.............:7DNNDD8888D8DNND8888888888888888Z7IIIII$O88DD88D+.................
...........,7DDZ7?++7OD8888DDND8888888888888$?+=====+++?$8DDDDO.................
..........,+?~...:IODD88DDDDDNND8888888888Z?=:,,,,,,:~++=?OD88N+................
...............=ZDDD8DDDNNNNNNNNND8888888$+:,.........,~+++$88DZ................
.............:$DD88DDNNNNDDNNNDD888888887+:....,,,,,....~++=$D8Z,...............
............?DD888DNNNDDDDNDD88888D88887+~...............=++++:,,...............
..........,$DD8888DDDDNNNND88888888888Z++:.,...~I7I~...,.~++,...................
.........:OD888DDDDDDDDDDNDDDD8888888O?++:.,,.?DDN$::..,.~?:.IO7=...............
........:8DDDDD8Z$Z88DDDDDNNDD88DD8887+++=....OD88Z~?.,.,++,?NNI~=.,............
.......~DDZ7?=::+$8DDDNNNNDD888DD88ZI+++++~...INDDD$=..,=++:7NDO$=.,............
.......?+,....?ODNNNNNDNND88888888Z?+++++++=,..=7$I~..:=+++=:7OO+...............
...........,I8DDDNNDDDNND88DD8888OI?+++++++++=~,,,,,~=++++++=::,,::.............
...........7MDDDDDDNNNNN888888888ZI?+++++++++++++++++++++++++++++++.............
...........,+7Z8DDNDDDDDNNND888D88II?++++++++++++++++++++++++++++IOO+...........
...............,:~=$D8DDNDD88DD888OI??++++++++++++++?$+++++++++++8MNMZ,.........
.................~$8DDNND88888888888$I??++++++++++++7Z$I?+++++==:~7Z7+..........
...............~$DNNNNND8888888D88888O$7III?++++++++7$$7I?=~:...................
.............,7DD8NNNNNDDDDD88D888888888OI?++++++++++++=........................
............~8NDDDO8DDDDNNN888888DDD8888$?++++++++++++++=.......................
............:++=~~I88DDDND8888888888888Z?++++++++++++++++~...,:=~...............
................:$DDDNNNN88888D8888888OI+++++++++++++++++++??III7:..............
...............IDDDNNDDND88888888888887++++++II?????+++++++IIIIII,..............
.............,ZD88DNNNNND888888888888O?+++++++?????77++++++?IIII~...............
.............ZNDDDDDDDDDDDDDD88888888$++++++++++++=I7+++++++II+:................
.............:?77$8D888DDDNNNND8888887++++++++++++I7?+++++++=,..................
................~$8DDDDNNDNND88888D887++++++++??I7I?++++++++=...................
..............=ZDDD8DNNDDND888888DD88Z?+++++++???++++++++++++:..................
.............,OND888DDDNNND88888888888ZI+++++++++++++++++++++~..................
...............+$8DDD88DDDND888888DD888?+++++++++++++++++++++=..................
.................,+$ODD888DDNDDD8888887=+++++++++++++++++++++=..................
....................,+ZD8DDNNDDD88888O?++++++++++++++++++++++=..................
...................+D888DNND888888888O?++++++++++++++++++++++~..................
...................,+$8DMNN888888D888O?++++++++++++++++++++++:..................
.......................~$ODDDDD888D8DZ?++++++++++++++++++++++...................
...........................:=?ZOOOOOZ7?+++++++++++++++++++++~...................
..............................:+??II??++++++++++++++++++++++....................
...............................=+++++++++++++++++++++++++++:....................
................................+++++++++++=~~~~~=++++++++=.....................
................................,+++++++=,........,=++++++......................
.................................,+++++~...........:+++++,......................
..................................:++++............~++++:.......................
...................................=++=............=+++,........................
...............................,,,,:++~,,,,,,,,,,.,++=,.........................
......................:~~==========+???+=+++++=+?????===~:......................
.........................,,,,:::::::::::::::::::::::,,,,........................
................................................................................
................................................................................
................................................................................
................................................................................
................................................................................
'''

ASCII_JAGAHACKER = b'''
........................................................................................................................
..........................:+=+=,.,,,,,,,,,,...........................~:::,,............................................
........................,.7DO88~,,,,,,,,,,,,,:.......................:~..............................,,......:..........
......................,::,78ZOO~,:,,,,,,,,,,,,............:~,......:?+,,............:~,...............:,....,,..........
...................,:.,::,78OO8~,:,.......,,,,,~~:::,...~?~.....:?ZD7..~=?I77$$7I+==:,::,..............,,,,,,...........
.................,,,,,,,,.?OZZZ:,,,,,,,,,,..,,:I??=:::.:I:....:78DDI:IO8DDDNDO7+~~,:,...,........:,..,:~~~~~~:,...,,....
...............,,,,,,,,....,::,,.,,.,.,,,,,,:::?$7~,::,.~I,,.?8D888$DNDD8887~..,,,,,................:~~~~~~~~~~:..,,....
..............,,,,,,,...,,,,,,...............,,,,,,.,,,,:?.:$DD88DDDD8DDD8OI$O88888OZ$?=,..........,~~~~~~~~~~~~:.......
.............,.,,,...,,,.........................,,,....IO=ZNDDDD88O888DD8DDDDDDDDDDDDDD8$=........:~~~:~~~~~~~~~.......
..........:~~:::,...,,.............................,,,,=DZ8D888888888888888OO8O8DD8OZZO88DD8I:.....:~~~,,:~~~~~~~.,,....
..........~=~~~~~:,,............,.,.,.,.,.,..........,,ZDO888O$777$Z88888888888DDD8OI=,.,:~+I?:....,~~~::,,,~~~~,.,,....
..........,~~~~~=:,.........,.,...........,.,.........~D8D8ZI+++++++?$O8888888DDDDDDD8Z?,...........:~::~:,~~~~,........
..........,:,,,,,.........,...................,,,.,,,.INDD7+++++++??++?Z88888DDDDDDDD8DD8I,.,.......,~:~~:~~~:,.........
..........:,,.,,,.,.....,,....................,,,,,,,.OO?=:~=+++++~::::~788888888DDDDDD88DO=........~+~~,~~,............
.........,,,..,.......,,......................,,,,,,.,+,.....~++=,.......+888888888DDDDDDDDDI.......78O$7=..............
....,~:,.,...,.:~~:::,,.......................,,,,,,,:..,~I=..==...,,..,,.?D88888DDDDDDDDDD8D$.....,8888O,..............
.....=:::::~:,.~=~=~~~:..........,+===============+=+7..=+8D~.=~.,,+8O=.,.,7888888DDDDDDDD8DDD$....,+I$O~...............
.....:=~~==~,,.,~~~~~~:..........,++++++++++++++++?+=7,.+8N8:,+~.:+IDD8,..:+?O888888DDDDD8O7$8NI.......,................
.....,,,,,,.,...,,.,,.............++++++++++++++++++~++:,=?~:+++:.INDD$..,=++?8888888DDDDDDO=,=$~.......................
.....,.,,...,......,..............=+++++++++++++++++~=?++==+?++++~,=+=.,:++++?88888DDDDDDDDNN7..,.......................
.....,.,,..,,......,..............~?++++++++++++++++==+++??++++++?+=~~=++++++Z888888DDDDDDDDDNO~........................
.....,,::,..,......,..............:?++++++,.,+++++++=+7++++I7I+++++?I+?++++?Z888888888DDDDDDDDD8=.......................
...,,:::::,,,......,..............,+++++++:..+++++++=+8Z7I7NNN7+++?ZO++++I$88888888888DDDD88DD8D$.......................
..::::~:~::::......,..............,++++++++++++++++++~ZOO8O$$7??I7$$$?++788888888888DDDDDDD8OO8Z,.......................
..,::~~~~::::...,,..,..............=+++++++++++++++++~?$$7?+++++++++++++?O88D88888888DDDDDDD8OZO?.......................
...,,,,,,,,,,~:::::+:..............=?+++++++++++++++?~=?+++++++++++++++++I8888888888888DDDDDD8OOO~......................
........,,..,:.,::,?~..............~+++++++++++++++++==?+?+++????++++++??I8888888888888DDDDDD88OO$......................
........,,,.,~:~==:?~.,.............+IIIIIIII????IIIII=~~:==~+IIIIIIIIIIIIO88888888DDDDD88888888O8~.....................
.........,,,.,:IO$=:,..,,...........~+======I$$$$I???I=~~~==~=?IIIIIIIIIIIO8888888DDDDDDD8OOOOOOO8?.....................
..........:,,..::,,......,..................$OOOO+++++++??++?++?IIIIIIIIIIO88DD8888DDDDDD88OOOOOO8I.....................
...........,...............,.,.............:OOOOZ++++++++++++++++???????+I888888888DDD888888OOOOO87.....................
..........++++?I?II:..........,,,,.,.,.,.,.~OOOOO?+++++++++++++++++++++++Z888888888DDD88OOO88OOOO8?.....................
.........,$7?IODDDD~,,...............,.....,ZOOOOI++++++++++++++++++++++$D888DDDDDDDDDD8OOOOOOOOO8~.....................
..........ZOZ7$DDDD:.,,,....................+8O$?++++++++++++++++++++++$888888DDDD8DDD888OOOOOOO87......................
..........?II??7777:...,,,...................II++++++++++++++++++++++IO88888888DDDD888888OOOOOOO$,......................
'''

ASCII_JAGASCHOLAR = b'''
................................................................................
................................................................................
..............................,:~=+++?????+++=~:,...............................
.........................,~=?IIIII???+++????IIIIII?=~,..........................
......................:=?III?+===~==++++=~~~~~==++?III?=:.......................
...................,=?II?+=~~~~~~~,,,:~++~~~~~~~~~~~=+?II?=,....................
.................:+II?==~~~~~~~~~~:....:?~~~~~~~~~~~~~~==?II?+~,................
...............:?II+==+~~=~~~~~~~~~~,.=,:I=~~~~~~~~~~~~=?7Z88DD8ZI=:............
.............,+II+===:.~+~?7$ZZZZZZ$$?+=~?OZ?~~~~~~~?7Z88D8888888DD8Z7+.........
............=II+=~~,...,~,?7Z8DDDDDDDND8OI?ODO7=~~~~ZND8888888888888DN8.........
..........,?I?=~~~:,,,..~+=++I$8888DDDDDDNDO8DD8I~~~:=IZ8DD88888DD8O7+:.........
.........:II?~~~~~=~~=?$O8DDDDDDDDDDD88888DDDDDDDO+~=:..,~I$8D8ZI=,...~.........
........:II+~~~~~~~+7ODDDDDDND88888888O$77777ZO88DN??I+++:...:,..,=7OD8.........
.......:II+~=~~~~+ZDNDDDD8DNND888888OI+++===+++?7ZI,...,=O8Z?~+$8DDOI=,:........
......,II+~?+~+=$8O$7I?I$8DDDND8888$++~:,,,,:~=++=,.~+:,.,?$8D8Z?~...,+I,.......
......?I+=+:.~=,?+~~~+IZ8DDD888888Z+=,....,....~++.=NO~?,....,...:?$8D8I?.......
.....+I?=~....~=~~=7ODNND888888888I=,.,.,....,,.:?:=DD8O~.7O7+IZDD8$+:,?I=......
....:II=~,.,,::~=78DDND8888888888O?:.,.,.,=~:..,.=+~+ZOI.:?$ZOZ7=:,:=7Z?II:.....
....+I?~~~~~=~~?8DDDNN88888888888Z+,..,.:ZN$,=,..=++=~~:=++?7I=~+$8D8Z?~?I+.....
...,II=~~~~~~~7DD88DDNND888888888Z+:.,,.?N88Z7+.,++++++++++8MMMN8$+:...~+II,....
...=I?~~~~~~~$D88D888DDDNNND88888Z?+,.,.:ONDN8:.=+++++++++++II=,...~IZ8==II=....
...?I+~~~~~~7D8D88888DDDDND88D888O?++:,..,+I?:,=++++++++++7?,.,=7ODDO$+~~?I?....
..,II+~~~~~?DDD$7888DNNNND88D888887++++~::,,:=++++++++++==$8D8DDOI=,..,~~?II....
..,II=~~~~~ONO?=8D8DNNDNN8888888887+++++++++++++++++++I7~...:+~...,+788=~+II,...
..:II=~~~~ID7~~OD8DNDDDND88DD8D88O?++++++++++++I7??II+78D8ZI~,:?$8D8ZI~~~+II:...
..:II=~~~~7?~~ID88DNNNNDDDDN88D88OI++++++++++++?ZZZ7+,..,+7ODDD8$?:...:~~+II:...
..,II=~~~~~~~~OD8DDDDDDDDNND8888887??+++++++++++?7?=$8ZI=,...~,...~?Z88=~+II,...
...II+~~~~~~~?D8888DD88DNNN8888888O7I??++???+++++++++7O8D8O7+:=IZ8D8ZI+~~?I?....
...?I?~~~~~~~$D88DDZZDDNDND88D888888OZ$$7I?+++++++++++?II7Z8DDDO$I+~~~~~~?I+....
...=I?~~~~~~~ZD8D8I?8DNDDND88DD8DD8888DZI?+++++++++++++?III?=+=~~~~~~~~~=II=....
...,II+~~~~~~ODDZ=~8DDNDDNNNDND8D88888$I?+++++++++++++++?+=~~~~~~~~~~~~~?II,....
....+I?~~~~~~ODI~~ZD8DNNNNDDDN88888D8$I?+++++++++++++++++~~~~~~~~~~~~~~=II+.....
....,II+~~~~~Z?~~?DDDDD8ZZDDND88888D$I?+++++++++++++++++++~~~~~~~~~~~~~?II,.....
.....=II=~~~~=~~~+Z$7I+=~ODNND88DD8ZII++++++++++++++++++++=~~~~~~~~~~~+II=......
......?I?~~~~~~~~~~~~~~~7DDNNNDDNDOII?+++++++++++++++++++++~~~~~~~~~~=II?.......
......,II?~~~~~~~~~~~~~=88DNDD8DN87II+++I++++++++++++++++++=~~~~~~~~=?II,.......
.......:II?~~~~~~~~~~~~IDD87ZDDNNO?I?+++?7?+++++++++++++++++~~~~~~~=?II,........
........:II?=~~~~~~~~~~$87=~8DDNN7II+++++?II??++++++++++++++=~~~~~=III:.........
.........,?I?=~~~~~~~~~=~~~IDDNNDIII++++++++?III+++++++++++++~~~~+II?,..........
...........+II+~~~~~~~~~~~~$D8DNOII?++++++++++I$I++++++++++++~~=?II+............
............~II?=~~~~~~~~~~OND8OZII?+????++??I77?++++++++++++=+II?~.............
.............,=II?=~~~~~~~~I7I=7Z?I?+++?III77I?++++++++++++++?II=,..............
...............,+II?+=~~~~~~~~=D$?I++++++++++++++++++++++++++I+,................
.................,=III?==~~~~~IN$?I++++++++++++++++++++++++++,..................
...................,~?III?+=~~~=+II+++++++++++++++++++++++++:...................
......................,~+IIII??+=II+++++++++++++++++++++++++....................
..........................:~+?IIIII++++++++++++++++++++++++:....................
...............................,:~=+++++++++++++++++++++++=.....................
...................................:++++++=:,,...,:=++++++......................
....................................:++++=..........+++++,......................
.....................................=+++,..........++++:.......................
.....................................,++=..........,+++:........................
......................................=+:..........~?=,.........................
...................................................,,...........................
'''

ASCII_JAGASUPER = b'''
................................................................................
.........................................................,,,,...................
..............................................,,............~,..................
...........................................,,::~:...........,+~.................
...............................................~:=?7O88Z$7+~..OO+,....:=,.......
.....................................................~$DDDDDO+:8N8?.....+=......
...........................................,~+I7$$$7I+~+O8DDNNOZDDDO~.,,=~......
........................................:IZDNNNNDNNNNNN88DDND8DDDDDDD=.:+.......
......................................~7OOOZZ$$O8DND8888D8DD8888DDDDDN:~I.......
......................................:,.....~?Z8DND88888888888888888DO~D:......
..........................................:IODDDNNNND88888888Z7I??I$O8DOD$......
........................................~$DDDDDDNNNDDD88888$?===+++++$8DD8,.....
.......................................IDDDDDNNND88888888OI~,,,,:++++=I88D~.....
.....................................:OD8DNNNNNND8888888Z?~......:++++=78D=.....
....................................~8NDDD8DNNNNDD88888Z++,..,?7?,:+++++ZD=.....
...................................~D8$?+?$8DND888888O7+++,..$NNI~.,:==,~=......
...................................+~..=$DNNND88D888Z?++++=,.$NNZ+...~:I8?:.....
.....................................I8NNNNNNDDD888OI+++++++:,+?=..,~+~DN7=.....
....................................?DDNNNDNNDD88D88I+++++++++~~~~=+++=+7+......
......................................:=?$DD88888888O?+++++++++++++++++=~~~.....
..::............................,,::~~~~=Z88OO8888888O7???++++++77=++++++7Z+....
..+Z?:................,:~=+?I7$$$ZZZZZZZZZ$$$$ZZZZZZZZOZ7?++++++ZZ7??+++=ZMN+...
..:ZZZ$?=~::::~~=+?I7$$ZZZZZZZZZZZZ$$$$$$ZZZZZZZZ$$ZZO8Z?+++++++??+,,.....:~,...
...$Z$ZZZZZZZZZZZZZZZZZZ$$$$$ZZZZZZZZZZZZZZZZZZZZZO888O?+++++++++++~~=+I:.......
...~Z$$$$$ZZZZ$$$$$$ZZZZZZZZZZZZZZZZZZZZZZZZZ$$ZO888887++++??????+++IIII,.......
....+ZZ$ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ$Z8888888O?++++++++II++++I?:........
.....=$ZZ$$$$$ZZ$$ZZZZZZZZZZZZZZZZZZZZZZZZ$Z8NNND8888Z++++++++?I?++++:..........
......,?$ZZZZZZZZZZ$$ZZZZZZZZZZZZZZZZZZZZ$ZDNND8888D8O?+++++???++++++:..........
.........~+??=:,~+$ZZZ$$$ZZZ$ZZZZZZZZZZZZZ8DDND8888888Z++++++++++++++=..........
...................=7ZZZZZ$ZZZZZZZZZZZZZZ$O8DDDDD88888$+++++++++=++++=..........
.....................,~==:,,IZ$ZZZZZZZZZ$,+Z88DDDD8888I??+++++?I77I?+=..........
.............................7Z$ZZZZZZZZI,$8DMN8888888ZZZZZ$$$7Z7~Z7Z7..........
.............................,7Z$$$$ZZZZI...~7ZO88888OIII77777I7II7I7=..........
...............................7ZZZZZZ$ZI.......:I777I++++++++++II++=...........
...............................:?III7ZZZ7........:++++++++++++++++++,...........
.....................................,=7Z,........~+++++~,,,,,~++++~............
........................................+~.........=?++........???+.............
.........................................,.........+Z$I.......,$Z$,.............
...................................................~ZZ~.......:ZZ?..............
...................................................=ZZ=.......:7IZ7~............
....................................................=+:..........,,.............
................................................................................
'''
