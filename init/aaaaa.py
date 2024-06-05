# from sklearn.cluster import KMeans
from init_class import pygame,COLORS
# from read_dir_img_kmeans import list_img
# import pygame
import os
path = "D:/init/img"
list_img = os.listdir(path)     
print(list_img)
class draw_rect_backgroud:
    def __init__(self,x,y,w,h,colors):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.colors = colors

    def show(self):
        pygame.draw.rect(screen,self.colors.BLACK,(self.x,self.y, self.w, self.h))
        pygame.draw.rect(screen,self.colors.WHITE,(self.x + 5, self.y + 5, self.w - 10, self.h - 10))
    # def black_white(self):
    #     pygame.draw.rect(screen,self.colors.BLACK,(self.x,self.y, self.w, self.h))
    #     pygame.draw.rect(screen,self.colors.WHITE,(self.x + 5, self.y + 5, self.w - 10, self.h - 10))
        
class Text:
    def __init__(self,
                 button_n_clusters,
                button_plus,
                button_tru,
                button_run,
                button_show,
                button_selection,
                ngang
                ):
        self.button_n_clusters = button_n_clusters
        self.button_plus = button_plus
        self.button_tru = button_tru
        self.button_run = button_run
        self.button_show = button_show
        self.button_selection = button_selection
        self.ngang = ngang

    def show_(self):
        # screen.blit(self.kmeans,(450,170))
        # screen.blit(self.knn,(500,320))
        # screen.blit(self.svm,(500,470))
        screen.blit(self.button_n_clusters,(1230,25))
        screen.blit(self.button_plus,(1255,80))
        screen.blit(self.button_tru,(1225 + 80 + 10 + 30,70))
        screen.blit(self.button_run,(1280,145))
        screen.blit(self.button_show,(1235,205))
        screen.blit(self.button_selection,(1235,265))
        screen.blit(self.button_plus,(1225 + 60 + 15,260))
        screen.blit(self.button_tru,(1225 + 60 + 50 + 20,250))
        screen.blit(self.ngang,(650,338))

pygame.init()

colors = COLORS()
height = 1400
witd = 750
screen = pygame.display.set_mode((height,witd))
clock = pygame.time.Clock()
runing = True
font = pygame.font.SysFont('sans', 20)
font1 = pygame.font.SysFont('sans', 30)
font2 = pygame.font.SysFont('sans', 40)
font3 = pygame.font.SysFont('sans', 50) 
k = 0
cnt = 0

list_ = []

path = "D:/init/img"

# print(list_img)
# print(list_img[0])
# print(path + "/" + list_img[0])
index = 0
cnt = -1
run_img = False

file_path_img_kmeas = "D:/init/list_img"

file_img = os.listdir(file_path_img_kmeas)
print(file_img)
while runing:
    clock.tick(60)
    screen.fill(colors.BACKGROUND)
    x_mouse , y_mouse = pygame.mouse.get_pos()

    #Backgroud
    rect = draw_rect_backgroud(20,20,1200,700,colors)
    rect.show()

   
    #n_clusters
    rect = draw_rect_backgroud(1225,20,170,50,colors)
    rect.show()

    # + -
    rect = draw_rect_backgroud(1225,80,80,50,colors)
    rect.show()
    rect = draw_rect_backgroud(1225 + 80 + 10,80,80,50,colors)
    rect.show()

   
    #button run
    rect = draw_rect_backgroud(1225,140,170,50,colors)
    rect.show()

    #button show
    rect = draw_rect_backgroud(1225,200,170,50,colors)
    rect.show()
    
    #button selection
    rect = draw_rect_backgroud(1225,260,50,50,colors)
    rect.show()
    #+
    rect = draw_rect_backgroud(1225 + 60,260,50,50,colors)
    rect.show()
    #-
    rect = draw_rect_backgroud(1225 + 60 + 50,260,50,50,colors)
    rect.show()

    #Menu
    rect = draw_rect_backgroud(1225,320,170,400,colors)
    rect.show()
    
    button_plus = font2.render("+" , True, colors.BLACK)
    button_tru = font3.render("-" , True, colors.BLACK)
    button_run = font1.render("Run" , True, colors.BLACK)
    button_show = font1.render("Image Show" , True, colors.BLACK)
    pygame.draw.line(screen,colors.BLACK,(560,350),(650,350),3)
    ngang = font.render("►", True, colors.BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            if (1225 <= x_mouse <= 1225 + 80 and 80 <= y_mouse <= 80 + 50):
                if (k >= 0):
                    k += 1
                # run_img = False
                print("+")

            if (1225 + 80 + 10 <= x_mouse <= 1225 + 80 + 10 + 80 and 80 <= y_mouse <= 80 + 50):
                if (k > 0):
                    k -= 1  
                # run_img = False
                print("-")

            if (1225 <= x_mouse <= 1225 + 170 and 140 <= y_mouse <= 140 + 50):
                
                cnt += 1
                # pygame.display.flip()
                print("Run")

            if (1225 <= x_mouse <= 1225 + 170 and 200 <= y_mouse <= 200 + 50):
                run_img = True
                print("Show")

            if (1225 + 60 <= x_mouse <= 1225 + 60 + 50 and 260 <= y_mouse <= 260 + 50):
                if (index >= 0 and index < len(list_img)):
                    index += 1
                run_img = False
                print("+ menu")

            if (1225 + 60 + 50 <= x_mouse <= 1225 + 60 + 50 + 50 and 260 <= y_mouse <= 260 + 50):
                if (index > 0):
                    index -= 1
                run_img = False
                print("- menu")
    # if (index !=; 0):
    # print(image
    if (run_img):
        if (index != 0 and index <= len(list_img)):
            image = pygame.image.load(path + "/" + list_img[index - 1])
            image1 = pygame.image.load(path + "/" + list_img[index])
            shape = (500,500)
            image = pygame.transform.scale(image, shape)
            image1 = pygame.transform.scale(image1, shape)
            screen.blit(image, (60, 80))
            #draw line
            
            screen.blit(image1, (665, 80))
        else:
            ...

    #     print(run_img)

    button_selection = font1.render(str(index) , True, colors.BLACK)
    button_n_clusters = font1.render("n_clusters = " + str(k) , True, colors.BLACK)
    show_text = Text(button_n_clusters,
                     button_plus,
                     button_tru,
                     button_run,
                     button_show,
                     button_selection,
                     ngang
                     )
    show_text.show_()

    pygame.display.flip()
pygame.quit()

# if (check_kmeans):
#     import kmeans

# if (check_knn):
#     import KNN
