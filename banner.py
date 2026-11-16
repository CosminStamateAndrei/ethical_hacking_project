# ASCI banner
BANNER = r'''
                       _.-**-._
                    _,(        ),_
                 .-"   '-^----'   "-.
              .-'                    '-.
            .'                          '.
          .'    __.--**'""""""'**--.__    '.
         /_.-*"'__.--**'""""""'**--.__'"*-._\
        /_..-*"'   .-*"*-.  .-*"*-.   '"*-.._\
       :          /       ;:       \          ;
       :         :     *  !!  *     :         ;
        \        '.     .'  '.     .'        /
         \         '-.-'      '-.-'         /
      .-*''.                              .'-.
   .-'      '.                          .'    '.
  :           '-.        _.._        .-'        '._
 ;"*-._          '-._  --___ `   _.-'        _.*'  '*.
:      '.            `"*-.__.-*"`           (        :
 ;      ;                 *|                 '-.     ;
  '---*'                   |                    ""--'
   :                      *|                      :
   '.                      |                     .'
     '.._                 *|        ____----.._-'
      \  """----_____------'-----"""         /
       \  __..-------.._        ___..---._  /
       :'"              '-..--''          "';
        '""""""""""""""""' '"""""""""""""""'
'''.strip("\n")

# Color mask: one letter per character of BANNER (same row/column).
MASK = r'''
                       YYYYYYYY
                    YYY        YYY
                 CCC   YYYYYYYY   CCC
              CCC                    CCC
            CC                          CC
          CC    YYYYYYYYYYYYYYYYYYYYYY    CC
         YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
        YYYYYYYY   WWWWWWW  WWWWWWW   YYYYYYYY
       S          W       WW       W          S
       S         W     K  WW  K     W         S
        S        WW     WW  WW     WW        S
         S         WWWWW      WWWWW         S
      RRRSSS                              SSRR
   RRR      SS                          SS    RR
  R           SSS        SSSS        SSS        RRR
 YYYYYY          SSSS  SSSSS S   SSSS        YYYY  YYY
Y      YY            SSSSSSSSSSSS           Y        Y
 Y      Y                 KK                 YYY     Y
  YYYYYY                   K                    YYYYY
   R                      KK                      R
   RR                      K                     RR
     RRRR                 KK        RRRRRRRRRRRRR
      B  RRRRRRRRRRRRRRRRRRRRRRRRRRR         B
       B  BBBBBBBBBBBBBB        BBBBBBBBBB  B
       DDD              DDDDDDDD          DDD
        DDDDDDDDDDDDDDDDDD DDDDDDDDDDDDDDDDD
'''.strip("\n")

RESET = "\033[0m"
GREEN = "\033[92m"

_COLORS = {
    "Y": "\033[38;5;220m",  # pom-pom, hat brim, mittens
    "C": "\033[38;5;37m",   # hat
    "W": "\033[38;5;255m",  # eyes
    "K": "\033[38;5;244m",  # pupils, zipper
    "S": "\033[38;5;223m",  # face
    "R": "\033[38;5;160m",  # jacket
    "B": "\033[38;5;94m",   # trousers
    "D": "\033[38;5;240m",  # shoes
}


def colored_banner():
    out = []
    for line, mask in zip(BANNER.split("\n"), MASK.split("\n")):
        parts, current = [], None
        for i, ch in enumerate(line):
            code = _COLORS.get(mask[i]) if i < len(mask) else None
            if code and code != current:
                parts.append(code)
                current = code
            parts.append(ch)
        out.append("".join(parts) + RESET)
    return "\n".join(out)
