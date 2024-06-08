# from sklearn.cluster import KMeans
from init_class import pygame,COLORS,screen
colors = COLORS()
# import pygame

class draw_rect_backgroud:
    def __init__(self,x,y,w,h,colors):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.colors = colors

    def show(self):
        pygame.draw.rect(screen,self.colors.BLACK,(self.x,self.y, self.w, self.h))
        pygame.draw.rect(screen,self.colors.GREY,(self.x + 5, self.y + 5, self.w - 10, self.h - 10))
    def black_white(self):
        pygame.draw.rect(screen,self.colors.BLACK,(self.x,self.y, self.w, self.h))
        pygame.draw.rect(screen,self.colors.WHITE,(self.x + 5, self.y + 5, self.w - 10, self.h - 10))
        
class Text:
    def __init__(self,kmeans,knn,svm):
        self.kmeans = kmeans
        self.knn = knn
        self.svm = svm
    def show_(self):
        screen.blit(self.kmeans,(600,170))
        screen.blit(self.knn,(650,320))         
        screen.blit(self.svm,(650,470))

pygame.init()
clock = pygame.time.Clock()
runing = True
font = pygame.font.SysFont('sans', 20)
font1 = pygame.font.SysFont('sans', 30)
font2 = pygame.font.SysFont('sans', 40)
font3 = pygame.font.SysFont('sans', 50) 

check_kmeans = False
check_knn = False

while runing:
    clock.tick(60)
    screen.fill(colors.BACKGROUND)
    x_mouse , y_mouse = pygame.mouse.get_pos()

    #Backgroud
    rect = draw_rect_backgroud(150,70,1100,600,colors)
    rect.show()

    #Background button Kmeans
    rect1 = draw_rect_backgroud(450,150,500,100,colors)
    rect1.show()

    #Background button KNN
    rect1 = draw_rect_backgroud(450,300,500,100,colors)
    rect1.show()

    #Background button SVM
    rect1 = draw_rect_backgroud(450,450,500,100,colors)
    rect1.show()

    button_kmens = font3.render("KMEANS" , True, colors.BLACK)
    button_KNN = font3.render("KNN" , True, colors.BLACK)
    button_SVM = font3.render("SVM" , True, colors.BLACK)

    show_text = Text(button_kmens,button_KNN,button_SVM)
    show_text.show_()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            #450,150,450,100
            if (450 <= x_mouse <= 450 + 450 and 150 <= y_mouse <= 150 + 100):
                import kmeans
                # check_kmeans = True
                # check_knn = False
                print("Button kmeans")

            #450,300,500,100
            if (450 <= x_mouse <= 450 + 500 and 300 <= y_mouse <= 300 + 100):
                # check_knn = True
                # check_kmeans = False
                import KNN
                print("Button KNN")
            #450,450,500,100
            if (450 <= x_mouse <= 450 + 500 and 450 <= y_mouse <= 450 + 100):
                print("Button SVM")


    pygame.display.flip()
pygame.quit()

# if (check_kmeans):
#     import kmeans

# if (check_knn):
#     import KNN
