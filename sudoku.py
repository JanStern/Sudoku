import pygame, random
import data_sample

BLACK = (0, 0, 0)
GRAY = (200,200,200)
WHITE = (255, 255, 255)
YELLOW = (240,200,0)
RED = (255,0,0)
BLUE = (0,0,200)

segment_width = 42
segment_height = 42
segment_margin = 1

numbers_dict = {1:'1', 2:'2', 3:'3', 4:'4',5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
note_position_dict = {1:(2,0), 2:(segment_width//2-4,0), 3:(segment_width-6,0), 4:(2,segment_height//2-7),5:(segment_width//2-4,segment_height//2-7), 6:(segment_width-6,segment_height//2-7), 7:(2,segment_height-12), 8:(segment_width//2-4,segment_height-12), 9:(segment_width-6,segment_height-12)}



class Segment(pygame.sprite.Sprite):
    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
 

        # Numbers
        self.font = pygame.font.SysFont('notosans', 30)
        self.note_font = pygame.font.SysFont('notosans', 10)
        self.value = 0
        self.note_value = []
        self.all_note_value = []

        
        # Set height, width
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(WHITE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Mark selected segment
        self.selected = False
        self.finished = False
        self.error = False

        # Group 
        self.row = 0
        self.column = 0
        self.box = 0


    def set_color(self,COLOR):
        self.image.fill(COLOR)
        if COLOR == YELLOW: 
            self.selected=True
        else: self.selected=False

    def draw_number(self):
        global numbers_dict
        if self.selected: self.image.fill(YELLOW)
        else: self.image.fill(WHITE)
        if self.value:
            if self.error: self.textSurf = self.font.render(numbers_dict[self.value], 1, RED)
            elif self.finished: self.textSurf = self.font.render(numbers_dict[self.value],1,BLACK)
            else: self.textSurf = self.font.render(numbers_dict[self.value], 1, BLUE)
            self.image.blit(self.textSurf,(10,0))

        else:
            if show_options: array=self.all_note_value
            else: array = self.note_value

            for value in array:
                text = self.note_font.render(numbers_dict[value],1,BLUE)
                self.image.blit(text,note_position_dict[value])






class Graphics(object):

    def __init__(self):
        pygame.display.set_caption('Sudoku by Jan Sternagel')


    def main(self):
        draw_background()
        allspriteslist.draw(screen)
        draw_outline()
        draw_note_button()
        draw_solve_button()
        draw_option_button()
        in_case_of_victory()
        if pressed: mouse_collision(pygame.mouse.get_pos())
        for sprite in allspriteslist: sprite.draw_number()
        pygame.display.flip()




def check_for_error():
    d_rows,d_columns,d_box = create_array()
    for sprite in allspriteslist:
        sprite.error=False
    if check_for_double(d_rows) or check_for_double(d_columns) or check_for_double(d_box):
        for sprite in allspriteslist:
            sprite.error = True

def group_positions():
    row = 1
    for i,sprite in enumerate(allspriteslist,start=1):
        sprite.row = row
        column = i%9
        if column==0: 
            column =9
            row+=1
        sprite.column=column

        if sprite.row <=3 and sprite.column<=3: sprite.box=1
        elif sprite.row <=3 and sprite.column<=6: sprite.box=2
        elif sprite.row <=3 and sprite.column<=9: sprite.box=3
        elif sprite.row <=6 and sprite.column<=3: sprite.box=4
        elif sprite.row <=6 and sprite.column<=6: sprite.box=5
        elif sprite.row <=6 and sprite.column<=9: sprite.box=6
        elif sprite.row <=9 and sprite.column<=3: sprite.box=7
        elif sprite.row <=9 and sprite.column<=6: sprite.box=8
        elif sprite.row <=9 and sprite.column<=9: sprite.box=9







# Graphics
def draw_outline():
    delta_x = 3* (segment_margin + segment_width)
    delta_y = 3* (segment_height + segment_margin)

    for i in range(3):
        for k in range(3):
            x = 50 + (segment_width + segment_margin) *3*i
            y = 50 + (segment_height + segment_margin) *3*k
            pygame.draw.rect(screen, BLACK, (x, y, delta_x, delta_y), 2) 

def draw_background():
    screen.fill(WHITE)
    pygame.draw.rect(screen,BLACK,(50,50,9*(segment_width+segment_margin),9*(segment_height+segment_margin)))


def mouse_collision(pos):
    for sprite in allspriteslist:
        if sprite.rect.collidepoint(pos):
            sprite.set_color(YELLOW)

def set_value(num):
    global set_selected,note_modus
    for sprite in allspriteslist:
        if sprite.selected: 
            if not note_modus: sprite.value=num
            else: 
                if sprite.note_value.count(num)>0: sprite.note_value.remove(num)
                elif num>0: sprite.note_value.append(num)
            if set_selected:
                sprite.finished=True

def draw_note_button():
    global note_modus,font
    screen.blit(font.render(("Notes"), True, (0, 0, 0)), (600,200))
    pygame.draw.circle(screen,BLACK,(700,225),12)
    if note_modus: pygame.draw.circle(screen,BLUE,(700,225),10)
    else: pygame.draw.circle(screen,WHITE,(700,225),10)
       

def draw_solve_button():
    global solving,font
    screen.blit(font.render(("Solve"), True, (0, 0, 0)), (600,250))
    pygame.draw.circle(screen,BLACK,(700,275),12)
    if solving: pygame.draw.circle(screen,BLUE,(700,275),10)
    else: pygame.draw.circle(screen,WHITE,(700,275),10)

def draw_option_button():
    global show_options,font
    screen.blit(font.render(("Optio."), True, (0, 0, 0)), (600,300))
    pygame.draw.circle(screen,BLACK,(700,325),12)
    if show_options: pygame.draw.circle(screen,BLUE,(700,325),10)
    else: pygame.draw.circle(screen,WHITE,(700,325),10)


def in_case_of_victory():
    global victory
    if victory:
        font = pygame.font.SysFont("microsoftyibaiti", 60)
        screen.blit(font.render(("Congratulations you won"), True, (0, 0, 0)), (200,500))




# Logik
def create_array():
    array = []
    d_rows = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
    d_columns = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
    d_box = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}

    for sprite in allspriteslist:
        array.append(sprite.value)
    
    for i in range(9):
        for k in range(9):
            value = array[i*9+k]
            d_rows[i+1].append(value)
            d_columns[k+1].append(value)

    for k in d_rows:
        value = d_rows[k]
        for i in range(9):
            if k<=3: 
                if i<3: d_box[1].append(value[i])
                elif i<6: d_box[2].append(value[i])
                elif i<9: d_box[3].append(value[i])
            elif k<=6:
                if i<3: d_box[4].append(value[i])
                elif i<6: d_box[5].append(value[i])
                elif i<9: d_box[6].append(value[i])
            elif k<=9:
                if i<3: d_box[7].append(value[i])
                elif i<6: d_box[8].append(value[i])
                elif i<9: d_box[9].append(value[i])

    return d_rows, d_columns, d_box


def check_for_double(d):
    for k in d:
        for i in range(9):
            if d[k].count(i+1)>1: return k
    return False


def check_for_victory():
    global victory
    for sprite in allspriteslist:
        if sprite.error or sprite.value==0:
            break
    else:
        victory = True
    




def solve():
    get_all_options()

    for sprite in allspriteslist:
        if len(sprite.all_note_value)==1:
            sprite.value = sprite.all_note_value[0]

    for n,sprite in enumerate(allspriteslist):
        o_row = []
        o_column = []
        o_box = []
        for m,sprite_new in enumerate(allspriteslist):
            if n!=m:
                if sprite.row==sprite_new.row:
                    for element in sprite_new.all_note_value:
                        o_row.append(element)
                if sprite.column == sprite_new.column:
                    for element in sprite_new.all_note_value:
                        o_column.append(element)
                if sprite.box == sprite_new.box:
                    for element in sprite_new.all_note_value:
                        o_box.append(element)

        for i in sprite.all_note_value:
            if i not in o_row or i not in o_column or i not in o_box:
                sprite.value=i
                break


old_values = [0 for _ in range(81)]
def dead_end():
    global old_values
    new_values = []
    for i,sprite in enumerate(allspriteslist):
        new_values.append(sprite.value)
    
    if old_values==new_values:
        # print("Dead end reached")
        return True

    else:
        old_values=new_values
        return False


def try_one_option():
    for sprite in allspriteslist:
        if sprite.value == 0:
            if len(sprite.all_note_value)>1:
                sprite.value = sprite.all_note_value[random.randint(0,len(sprite.all_note_value)-1)]
                break
            
            else:
                for sprite in allspriteslist:
                    if not sprite.finished:
                        sprite.value=0


# d_tried = {i:[] for i in range(81)}
# def try_one_option():
#     global d_tried
#     for i,sprite in enumerate(allspriteslist):
#         if sprite.value==0:
#             if len(sprite.all_note_value)>1:
#                 for v in sprite.all_note_value: 
#                     if v not in d_tried[i]:
#                         sprite.value=v
#                         d_tried[i].append(v)
#                         break

#             else:
#                 for sprite in allspriteslist:
#                     sprite.note_value=[]
#                     if not sprite.finished:
#                         sprite.value=0  
#             break



def solve_completle():
    global solving
    if solving and not victory: 
        solve()
        if dead_end():
            try_one_option()


                     





def get_all_options():   
    for sprite in allspriteslist:
        if sprite.value==0:
            sprite.all_note_value=[]
            for i in range(9):
                sprite.value=i+1
                d_rows,d_columns,d_box = create_array()
                sprite.all_note_value.append(i+1)
                if check_for_double(d_rows) or check_for_double(d_columns) or check_for_double(d_box):
                    sprite.all_note_value.remove(i+1)            
                sprite.value=0
        # print(sprite.hiden_note_value)


def start_game():
    start_values = data_sample.d_sample[random.randint(1,len(data_sample.d_sample))]
    for i,sprite in enumerate(allspriteslist):
        sprite.value = start_values[i]
        if start_values[i]:
            sprite.finished=True




pygame.init()
clock = pygame.time.Clock()
font = pygame.font.SysFont("microsoftyibaiti", 40)

screen = pygame.display.set_mode([800, 600])

 


allspriteslist = pygame.sprite.Group()
graphic = Graphics()
 
# Create initial sudoku
sudoku_segments = []
for k in range(9):
    for i in range(9):
        x = 50 + (segment_width + segment_margin) * i
        y = 50 + (segment_height + segment_margin) * k
        segment = Segment(x, y)
        sudoku_segments.append(segment)
        allspriteslist.add(segment)
 
group_positions()
start_game()

done = False
pressed = False
set_selected = False
note_modus = False
solving = False
show_options=False
victory = False
solveing = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                done = True
            if event.key == pygame.K_n:
                note_modus = not note_modus
            if event.key == pygame.K_s:
                solving = not solving
            if event.key == pygame.K_SPACE:
                print("[",end="")
                for sprite in allspriteslist:
                    print(sprite.value,end=",")
                print("]")
            if event.key == pygame.K_c:
                for sprite in allspriteslist:
                    sprite.value=0
                    sprite.finished=False

            if event.key == pygame.K_o:
                show_options = not show_options
                if show_options: get_all_options()
            if event.key == pygame.K_r:
                for sprite in allspriteslist:
                    sprite.note_value=[]
                    if not sprite.finished:
                        sprite.value=0
            if event.key == pygame.K_b:
                set_selected = not set_selected

            # if event.key == pygame.K_LEFT:
                

            if event.key == pygame.K_0: set_value(0)
            if event.key == pygame.K_1: set_value(1)
            if event.key == pygame.K_2: set_value(2)
            if event.key == pygame.K_3: set_value(3)
            if event.key == pygame.K_4: set_value(4)
            if event.key == pygame.K_5: set_value(5)
            if event.key == pygame.K_6: set_value(6)
            if event.key == pygame.K_7: set_value(7)
            if event.key == pygame.K_8: set_value(8)
            if event.key == pygame.K_9: set_value(9)

        # Selection with mouse
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pressed = True
            for sprite in allspriteslist:
                sprite.set_color(WHITE)
        if event.type == pygame.MOUSEBUTTONUP:
            pressed = False
    

    check_for_error()
    solve_completle()
    
    graphic.main()
    
    # wait to let pc cool down
    clock.tick(40)
    check_for_victory()




pygame.quit()

