from nicegui import ui
import pyautogui

#Griglia utile al funzionamento del gioco
theBoard = {"top-L": " ", "top-M": " ", "top-R": " ",
            "mid-L": " ", "mid-M": " ", "mid-R": " ",
            "low-L": " ", "low-M": " ", "low-R": " "}

controllo = 0 #Turno
game_over = False  # Aggiunta della variabile di stato

class coordinate: #Classe utile a tracciare posizionamento del mouse. Funzionante su uno schermo avente risoluzione 1920x1080
    image_x = 0
    image_y = 0

    def setImage_x(self): #Traccia la coordinata x del cursore e setta il punto (x) di inizio dei disegni
        x = pyautogui.position()[0]
        if x < 150 or (150 <= x < 320):
            self.image_x = 140
        elif 320 <= x < 535:
            self.image_x = 285
        else:
            self.image_x = 430

    def setImage_y(self): #Traccia la coordinata y del cursore e setta il punto (y) di inizio dei disegni
        y = pyautogui.position()[1]
        if y < 235 or (235 <= y < 401):
            self.image_y = 70
        elif 401 <= y < 618:
            self.image_y = 215
        else:
            self.image_y = 360

def onclick():#Cosa succede al click della mappa
    global game_over
    if game_over:
        return  # Ignora gli input se il gioco è finito
    e = coordinate()
    e.setImage_x()
    e.setImage_y()
    funzionamento(e) 

def funzionamento(e):#Riempie col segno corrispettivo al turno il dizionario
    global controllo
    segno = "x" if controllo == 0 else "o"

    posizione = None
    if e.image_x == 140 and e.image_y == 70: posizione = "top-L"
    elif e.image_x == 285 and e.image_y == 70: posizione = "top-M"
    elif e.image_x == 430 and e.image_y == 70: posizione = "top-R"
    elif e.image_x == 140 and e.image_y == 215: posizione = "mid-L"
    elif e.image_x == 285 and e.image_y == 215: posizione = "mid-M"
    elif e.image_x == 430 and e.image_y == 215: posizione = "mid-R"
    elif e.image_x == 140 and e.image_y == 360: posizione = "low-L"
    elif e.image_x == 285 and e.image_y == 360: posizione = "low-M"
    elif e.image_x == 430 and e.image_y == 360: posizione = "low-R"

    if posizione and pieno(posizione):#Procede a controllare il la casella, disegnare il segno e controllare la vittoria
        theBoard[posizione] = segno
        controllaVittoria(controllo)
        disegno(e)
        controllo = 1 - controllo

def disegno(e): 
    color = 'SkyBlue'
    if controllo == 0:#Disegna la X 
        ii.content += f'<line x1="{e.image_x - 50}" y1="{e.image_y + 50}" x2="{e.image_x + 50}" y2="{e.image_y - 50}" style="stroke:red;stroke-width:2" />'
        ii.content += f'<line x1="{e.image_x + 50}" y1="{e.image_y + 50}" x2="{e.image_x - 50}" y2="{e.image_y - 50}" style="stroke:red;stroke-width:2" />'
    else:#Disegna la O
        ii.content += f'<circle cx="{e.image_x}" cy="{e.image_y}" r="50" fill="none" stroke="{color}" stroke-width="4"/>'

def pieno(posizione):#Controllo se la casella è già piena
    if theBoard[posizione] != " ":
        ui.run_javascript("alert('Lo spazio è già occupato')")
        return False
    return True

def controllaVittoria(turn):
    if turn==0: turn="X"
    else: turn="O"
    global game_over
    win_combinations = [#Combinazioni vincenti
        ["top-L", "top-M", "top-R"],
        ["mid-L", "mid-M", "mid-R"],
        ["low-L", "low-M", "low-R"],
        ["low-L", "mid-L", "top-L"],
        ["low-M", "mid-M", "top-M"],
        ["low-R", "mid-R", "top-R"],
        ["top-L", "mid-M", "low-R"],
        ["top-R", "mid-M", "low-L"]
    ]

    for combo in win_combinations: #Se viene trovata un'uguaglianza tra le combinazioni vincenti e la griglia viene restituito il messaggio di vittoria 
        if theBoard[combo[0]] != " " and theBoard[combo[0]] == theBoard[combo[1]] == theBoard[combo[2]]:
            ui.run_javascript(f"alert('Giocatore {turn} ha vinto')")
            game_over = True  # Imposta game_over su True
            return

    if all(theBoard[key] != " " for key in theBoard): #Altrimenti viene restituito l'esito di pareggio
        ui.run_javascript("alert('Pareggio')")
        game_over = True  # Imposta game_over su True

def reset_game():#Resetta tutti gli elementi per eseguire di nuovo il gioco
    global theBoard, controllo, game_over
    # Resetta il dizionario
    theBoard = {"top-L": " ", "top-M": " ", "top-R": " ",
                "mid-L": " ", "mid-M": " ", "mid-R": " ",
                "low-L": " ", "low-M": " ", "low-R": " "}
    controllo = 0
    game_over = False
    # REsetta l'immagine
    ii.content = """
        <rect class="top" id="TL" x="85" y="20" width="110" height="110" fill="none" stroke="none" pointer-events="all" cursor="pointer"/> 
        <rect class="top" id="TM" x="230" y="20" width="110" height="110" fill="none" stroke="none" pointer-events="all" cursor="pointer" /> 
        <rect class="top" id="TR" x="375" y="20" width="110" height="110" fill="none" stroke="none" pointer-events="all" cursor="pointer" />
        <rect class="mid" id="ML" x="85" y="165" width="110" height="110" fill="none" stroke="none" pointer-events="all" cursor="pointer" /> 
        <rect class="mid" id="MM" x="230" y="165" width="110" height="110" fill="none" stroke="none" pointer-events="all" cursor="pointer" /> 
        <rect class="mid" id="MR" x="375" y="165" width="110" height="110" fill="none" stroke="none" pointer-events="all" cursor="pointer" />
        <rect class="bottom" id="BL" x="85" y="310" width="110" height="110" fill="none" stroke="none" pointer-events="all" cursor="pointer" /> 
        <rect class="bottom" id="BM" x="230" y="310" width="110" height="110" fill="none" stroke="none" pointer-events="all" cursor="pointer" /> 
        <rect class="bottom" id="BR" x="375" y="310" width="110" height="110" fill="none" stroke="none" pointer-events="all" cursor="pointer" />
    """
    ui.run_javascript("alert('Il gioco è stato resettato!')")

#Griglia di gioco
src = 'Tris.png'
ii = ui.interactive_image(src,
                          content="""<rect class="top" id="TL" x="85" y="20" width="110" height="110" fill="none" stroke="none" pointer-events="all" cursor="pointer"/>
                          <rect class="top" id="TM" x="230" y="20" width="110" height="110" fill="none" stroke="none" pointer-events="all" cursor="pointer" />
                          <rect class="top" id="TR" x="375" y="20" width="110" height="110" fill="none" stroke="none" pointer-events="all" cursor="pointer" />
                          <rect class="mid" id="ML" x="85" y="165" width="110" height="110" fill="none" stroke="none" pointer-events="all" cursor="pointer" /> 
                          <rect class="mid" id="MM" x="230" y="165" width="110" height="110" fill="none" stroke="none" pointer-events="all" cursor="pointer" /> 
                          <rect class="mid" id="MR" x="375" y="165" width="110" height="110" fill="none" stroke="none" pointer-events="all" cursor="pointer" />
                          <rect class="bottom" id="BL" x="85" y="310" width="110" height="110" fill="none" stroke="none" pointer-events="all" cursor="pointer" /> 
                          <rect class="bottom" id="BM" x="230" y="310" width="110" height="110" fill="none" stroke="none" pointer-events="all" cursor="pointer" /> 
                          <rect class="bottom" id="BR" x="375" y="310" width="110" height="110" fill="none" stroke="none" pointer-events="all" cursor="pointer" />""").on('svg:pointerdown', onclick)

# Reset
ui.button('Resetta il Gioco', on_click=reset_game)

# Annuncio del giocatore iniziale
def startup():
    ui.run_javascript("alert('Inizia il giocatore x')")

ui.timer(0.1, startup, once=True)

ui.run()