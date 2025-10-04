import sys, time, random, threading
from kolyre import Kolyre
win = '''
        00
       00 __   __   ___    _   _ __      __ ___    _  _   
    o O O \ \ / /  / _ \  | | | |\ \    / /|_ _|  | \| |  
   o       \ V /  | (_) | | |_| | \ \/\/ /  | |   | .` |  
  TS__[O]  _|_|_   \___/   \___/   \_/\_/  |___|  |_|\_|  
 {======|_| """ |_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| 
./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
'''
pool = list("ᚠᚢᚦᚨᚱᚲᚷᚹᚺᚾᛁᛃᛇᛈᛉᛋᛏᛒᛖᛗᛚᛜᛟᛞΑΒΓΔΘΛΞΠΣΦΨΩϞϘϠѦѨѪѬѮѰѲѴѶѺⲀⲂⲆⲈⲊⲎⲐⲘⲚⲞⲢⲤⲦⲨⲪⲬⲮ☉☽☿♀♂♃♄♅♆♇☥☧☩☯┼┤├┬┴╬║═")
esc = "\x1b"
sys.stdout.write(f'{esc}[?25l')
def azx(x,y,color):
    goto(x - 1, y)
    for i in cover1:
        sys.stdout.write(f"{Kolyre.foreground_256(color)}{i}{Kolyre.RESET}")
        sys.stdout.flush()
        time.sleep(0.02)
    draw_art(x-1,y+len(cover1)-1,f"{Kolyre.foreground_256(color)}{cover3}{Kolyre.RESET}",0.05)
    draw_art(x-1,y,f"{Kolyre.foreground_256(color)}{cover3}{Kolyre.RESET}",0.05)
    goto(x + 8, y)
    for i in cover2:
        sys.stdout.write(f"{Kolyre.foreground_256(color)}{i}{Kolyre.RESET}")
        sys.stdout.flush()
        time.sleep(0.02)


def goto(r, c):  # nhảy con trỏ tới (r, c)
    sys.stdout.write(f"{esc}[{r};{c}H")

def clear():     # xóa màn hình
    sys.stdout.write(f"{esc}[2J{esc}[H")
    sys.stdout.flush()

def glitch_then_reveal(r, c, text,text_color,noise_color, noise_cycles,delay):
    n = len(text)

    # Phase 1: nhiễu toàn dòng trong noise_cycles khung hình
    for _ in range(noise_cycles):
        goto(r, c)
        frame = "".join(random.choice(pool) for _ in range(n))
        sys.stdout.write(f"{Kolyre.foreground_256(noise_color)}{frame}{Kolyre.RESET}")
        sys.stdout.flush()
        time.sleep(delay)

    # Phase 2: hiện dần từng ký tự; phần chưa hiện vẫn là nhiễu
    for i in range(1, n):
        goto(r, c)
        # left = f"{Kolyre.foreground_256(color)}{text[:i]}{Kolyre.RESET}"
        left = text[:i]
        right = "".join(random.choice(pool) for _ in text[i:])
        final_left = f"{Kolyre.foreground_256(text_color)}{Kolyre.BOLD}{left}{Kolyre.RESET}"
        final_right = f"{Kolyre.foreground_256(noise_color)}{right}{Kolyre.RESET}"

        sys.stdout.write(final_left+final_right)
        sys.stdout.flush()
        time.sleep(delay)

    # Last frame print real text
    goto(r, c)
    sys.stdout.write(f"{Kolyre.foreground_256(text_color)}{Kolyre.BOLD}{text}{Kolyre.RESET}")
    sys.stdout.flush()
cover = """
    ╭━━━━━━━━━━━━━━━━━༺✦༻━━━━━━━━━━━━━━━━━╮






    ╰━━━━━━━━━━━━━━━━━༺✦༻━━━━━━━━━━━━━━━━━╯
    """
cover1 ="╭━━━━━━━━━━━━━━━━━━༺✦༻━━━━━━━━━━━━━━━━╮"
cover2 ="╰━━━━━━━━━━━━━━━━━━༺✦༻━━━━━━━━━━━━━━━━╯"
cover3 ="""
║
║
║
║
║
║
║
║
"""
def draw_art(r,c,text,delay,option=1):
    line = text.strip("\n").splitlines()
    control = option
    if control == 1:
        for k, l in enumerate(line):
            # clear()
            goto(r+k,c)
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(delay)

clear()
def blank_del(r,c,art):
    lines = art.splitlines()
    w = max((len(l)for l in lines))
    h = len(lines)
    blank = "\n".join(" "*w for _ in range(h+1))
    draw_art(r+1,c,blank,0)

def ani_train(r,c,art):
    ani_condi = False
    ani_row = r
    ani_col = 175
    ani_col2 = 190
    prev_col = None
    blankdel = ["  ","   "]
    while not ani_condi:
        ani_col -=3
        # ani_col2 -=1
        if prev_col is not None:
            blank_del(ani_row, prev_col, art)
        if ani_col < c:
            ani_col = c
            ani_condi = True
        draw_art(ani_row,ani_col,art,0)
        draw_art(ani_row, ani_col2,random.choice(blankdel),0)
        sys.stdout.flush()
        time.sleep(0.03)
        # time.sleep(0.000005)

        prev_col = ani_col
def ani_win(x,y,y2,str1):
    ani_condi =False
    ani_row = x
    ani_col1 = 0
    ani_col2 = 200
    # Up & Down Cover
    goto(x-1, y)
    for i in cover1:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.02)
    goto(x+8, y)

    for i in cover2:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.02)
    #Draw first time
    draw_art(x-1, y, cover1,0)
    draw_art(x+8, y, cover2,0)
    #Detect the width & height of the art.
    lines = str1.splitlines()
    w = max((len(l) for l in lines),default=0)
    l = len(lines)
    #Blank with w adn l = art
    blank = "\n".join(" "*w for _ in range(l-1))
    prev_col1 = None
    prev_col2 = None
    n = 4
    y2 = y+len(cover1)-1
    while not ani_condi:
        if prev_col1 is not None and prev_col2 is not None:
            draw_art(ani_row, prev_col1,blank,0)
            draw_art(ani_row, prev_col2,blank,0)

        ani_col1 +=1
        ani_col2 -=n
        if ani_col2 <= y2:
            ani_col2 = y2
            n = 0
        if ani_col1 >= y:
            ani_condi = True
            ani_col1 = y
            ani_col2 = y2
        draw_art(ani_row, ani_col1, str1,0)
        draw_art(ani_row, ani_col2, str1,0)
        while ani_condi:

            glitch_then_reveal(x+1, y+3, "All the villains are defeated", 2, 11, 24, 0.03)
            glitch_then_reveal(x+3, y+3, "All the airports are protected", 14, 11, 24, 0.03)
            glitch_then_reveal(x+5, y+3, "You are now pardoned of all crimes", 1, 11, 24, 0.03)
            t = threading.Thread(target=azx, args=(x, y, 11))
            t.start()
            t.join()
            ani_train(x-1,y-30,win)

            break

        sys.stdout.flush()
        time.sleep(0.002)
        prev_col1 = ani_col1
        prev_col2 = ani_col2
# ani_win(7,50,135,cover3)

def ani_win1(x,y,y2):
    ani_win(x,y,y2,cover3)
#Test here
