import pygame
from sklearn.cluster import KMeans
import numpy as np
import math

def distance(p1,p2):
    return math.sqrt((p1[0] - p2[0])** 2 + (p1[1] - p2[1])**2)

class ox_oy:
    def __init__(self,ox1,ox2,ox3,ox4,oy1,oy2,oy3,oy4,BLACK,up,ngang):
        self.ox1 = ox1
        self.ox2 = ox2
        self.ox3 = ox3
        self.ox4 = ox4
        self.oy1 = oy1
        self.oy2 = oy2
        self.oy3 = oy3
        self.oy4 = oy4
        self.BLACK = BLACK
        self.up = up
        self.ngang = ngang

    def draw_ox(self):
        return pygame.draw.line(screen,self.BLACK,(self.ox1,self.ox2),(self.ox3,self.ox4),3)

    def draw_oy(self):
        return pygame.draw.line(screen,self.BLACK,(self.oy1,self.oy2),(self.oy3,self.oy4),3)
    
    def draw_up(self):
        return screen.blit(self.up,(44,32))
    
    def draw_ngang(self):
        return screen.blit(self.ngang,(1100,588))

class show_cluster:
    def __init__(self,BLACK,
                      WHITE,
                        x,
                        y,
                        O,
                        Run_kmeans_button,
                        labels,
                        K_Kmeans_button,
                        k_button, dau_cong, dau_tru, run_button, algorithm_button,reset_button,
                        using_kmeans):
        self.BLACK = BLACK
        self.WHITE = WHITE
        self.x = x
        self.y = y
        self.O  = O 
        self.Run_kmeans_button = Run_kmeans_button
        self.labels = labels
        self.K_Kmeans_button = K_Kmeans_button
        self.k_button = k_button
        self.dau_cong = dau_cong
        self.dau_tru = dau_tru
        self.run_button = run_button
        self.algorithm_button = algorithm_button
        self.reset_button = reset_button
        self.using_kmeans = using_kmeans

    def show_rect(self):
        pygame.draw.rect(screen,self.BLACK,(50,605,1050,100))
        
        pygame.draw.rect(screen,self.WHITE,(55,610,535,40))
        pygame.draw.rect(screen,self.WHITE,(55,655,130,40))
        pygame.draw.rect(screen,self.WHITE,(190,655,50,40))
        pygame.draw.rect(screen,self.WHITE,(260,655,50,40))
        pygame.draw.rect(screen,self.WHITE,(325,655,130,40))
        pygame.draw.rect(screen,self.WHITE,(460,655,130,40))
        
        #K_knn button
        pygame.draw.rect(screen,self.WHITE,(595,610,110,40))
        pygame.draw.rect(screen,self.WHITE,(595,655,50,40))
        pygame.draw.rect(screen,self.WHITE,(655,655,50,40))

        #Run button    
        pygame.draw.rect(screen,self.WHITE,(710,610,190,40))
        
        #Alogithm
        pygame.draw.rect(screen,self.WHITE,(905,610,190,40))
        
        #Reset
        pygame.draw.rect(screen,self.WHITE,(710,655,385,40))

    def show_text(self):
        

        #K kmenas
        screen.blit(self.dau_cong,(200,650))
        screen.blit(self.dau_tru,(280,650))
        screen.blit(self.labels,(80,660))
    
        #K knn
        screen.blit(self.k_button,(605,605))
        screen.blit(self.dau_cong,(605,650))
        screen.blit(self.dau_tru,(675,650))
    
        screen.blit(self.run_button,(730,605))
        screen.blit(self.algorithm_button,(915,610))
        screen.blit(self.reset_button,(850,650))
        
        screen.blit(self.x, (1105, 605))
        screen.blit(self.y, (30, 35))
        screen.blit(self.O, (35, 590))

        screen.blit(self.K_Kmeans_button, (340,650))
        screen.blit(self.using_kmeans, (60,610))

def lower_bound(arr,x,l,r):
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if (arr[mid] == x):
            ans = mid
            r = mid - 1
        elif (arr[mid] < x):
            l = mid + 1
        else:
            r = mid - 1
    return ans
    
def upper_bound(arr,x,l,r):
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if (arr[mid] == x):
            ans = mid
            l = mid + 1
        elif (arr[mid] < x):
            l = mid + 1
        else:
            r = mid - 1
    return ans

def counts(arr,x,l,r):
    ans = -1
    while (l <= r):
        mid = (l + r) // 2
        if (arr[mid][0] == x):
            ans = mid
            l = mid + 1
        elif (arr[mid][0] < x):
            r = mid - 1
        else:
            l = mid + 1
    return ans

def binary_search(arr,x,l,r):
    while (l <= r):
        mid = (l + r) // 2
        if (arr[mid] == x):
            return True
        elif (arr[mid] < x):
            l = mid + 1
        else:
            r = mid - 1
    return False
pygame.init()
height = 1200
witd = 700
screen = pygame.display.set_mode((height,witd))

BLACKGROUP = (255,255,255)
BLACK = (0,0,0)

WHITE = (255,255,255)
GREY = (192,192,192)
RED = (255,0,0)

GREEN = (0,102,51)
BLUE = (0,0,153)
YELLOW = (255,255,0)
PURPLE = (255,0,255)
SKY = (0,255,255)
ORANGE = (255,125,25)
GRAPE = (100,25,125)
GRASS = (55,155,65)

COLORS_LABELS = {0 : GREEN,
                 1 : BLUE,
                 2 : YELLOW,
                 3 : PURPLE,
                 4 : SKY,
                 5 : ORANGE,
                 6 : GRAPE,
                 7 : GRASS}

test = 0
labels = []
clusters = []
list_labels_news = []
values = []
labels_index = []
K_knn = 0
K_Kmeans = 0
result = []
anssss = []
labels_points_news = []
runing = True
points = []

append_poinst = []


# test = 0
length = 0

clock = pygame.time.Clock()
while runing:
    clock.tick(60)
    screen.fill(BLACKGROUP)
    x_mouse , y_mouse = pygame.mouse.get_pos()
    
    x_test = x_mouse
    y_test = y_mouse

    font = pygame.font.SysFont('sans', 20)
    font11 = pygame.font.SysFont('sans', 30)
    font_1 = pygame.font.SysFont('sans', 40)
    font_2 = pygame.font.SysFont('sans', 50)    
    up = font.render("▲", True, BLACK)
    ngang = font.render("►", True, BLACK)
    x = font11.render("X", True, BLACK)
    y = font11.render("Y", True, BLACK)
    O = font11.render("0", True, BLACK)

    Run_kmeans_button = font.render("RUN_KMEANS", True, BLACK)
    labelss = font.render("LABELS", True, BLACK)
    using_kmeans = font_1.render("USE KMEANS TO MAKE LABELS", True, BLACK)

    k_button = font_1.render("K = " + str(K_knn), True, BLACK)
    K_Kmeans_button = font_1.render("K = " + str(K_Kmeans), True, BLACK)
    dau_cong = font_1.render("+", True, BLACK)
    dau_tru = font_1.render("-", True, BLACK)
    run_button = font_1.render("RUN_KNN" , True, BLACK)
    algorithm_button = font11.render("DELETE LABEL", True, BLACK)
    reset_button = font_1.render("RESET" , True, BLACK)

    draw_ox_oy = ox_oy(50, 50, 50, 600, 50, 600, 1100, 600, BLACK, up, ngang)
    draw_ox_oy.draw_ox()
    draw_ox_oy.draw_oy()
    draw_ox_oy.draw_ngang()
    draw_ox_oy.draw_up()

    rect_clusters = show_cluster(BLACK,
                                 WHITE,
                                 x,
                                 y,
                                 O,
                                 Run_kmeans_button,
                                 labelss,
                                 K_Kmeans_button,
                                 k_button, dau_cong, dau_tru, run_button, algorithm_button, reset_button,
                                 using_kmeans)
    rect_clusters.show_rect()
    rect_clusters.show_text()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (50 <= x_mouse <= 1100 and 50 <= y_mouse <= 600):
                if (test != 0):
                    list_labels_news.append([x_mouse - 50,abs(y_mouse - 600)])
                else:
                    x = float(x_mouse - 50)
                    y = float(abs(y_mouse - 600))
                    point = [x,y]
                    points.append(point)
              
            if (55 <= x_mouse <= 185 and 655 <= y_mouse <= 695):
                try:
                    labels_index = []
                    test += 1
                    kmeans = KMeans(n_clusters=K_Kmeans).fit(points)
                    labels = kmeans.predict(points)
                    clusters = kmeans.cluster_centers_

                    for i in range(len(labels)):
                        labels_index.append([points[i],labels[i]])
                
                except:
                    pass

            if (190 <= x_mouse <= 240 and 655 <= y_mouse <= 695):
                if (K_Kmeans >= 0 and K_Kmeans < 8):
                    K_Kmeans += 1

            if (260 <= x_mouse <= 310 and 655 <= y_mouse <= 695):
                if (0 < K_Kmeans <= 8):
                    K_Kmeans -= 1

            if (595 <= x_mouse <= 645 and 655 < y_mouse <= 695):
                if (K_knn >= 0 and K_knn < len(points)):
                    K_knn += 1

            if (655 <= x_mouse <= 705 and 655 <= y_mouse <=  695):
                if (0 < K_knn <= len(points)):
                    K_knn -= 1

            if (710 <= x_mouse <= 900 and 610 <= y_mouse <= 650):
                anssss = []
                labels_points_news = []
                poins_news = []
                result = []
                values = []
                list_point = []
                length = 0
                append_points = []
                try:
                    index_labels = 0
                    for i in list_labels_news: # O(n)
                        list_distance = []
                        labels_news = []
                        for j in range(len(labels_index)): # O(n)         
                            dis = distance(i,labels_index[j][0])
                            if (dis == 0.0):
                                continue                                
                            else:
                                list_distance.append([dis,labels_index[j][1]])
                        list_distance.sort() # O(nlog(n))
                        
                        for index in range(K_knn): # O(n)
                            labels_news.append(list_distance[index][1])
                        labels_news.sort()

                        value = []
                        index_max = -1

                        for ii in range(K_Kmeans): # O(m)
                            first = lower_bound(labels_news,ii,0,len(labels_news) - 1) # O(log(n))
                            second = upper_bound(labels_news,ii,0,len(labels_news) - 1) # O(log(n))
                            if (first != -1 and second != -1):                                    
                                value.append([second - first + 1,ii])
                                index_max = max(index_max,second - first + 1)
                        
                        value.sort(reverse=True) # O(mlog(m))
                        count_index_max = counts(value,index_max,0,len(value)- 1)
                        
                        if (count_index_max != -1):
                            list_distane_value = []
                            for index in range(count_index_max + 1):
                                min_distance_labels = 1e9
                                for dd in range(len(list_distance)):
                                    if (value[index][1] == list_distance[dd][1] and min_distance_labels > list_distance[dd][0]):
                                        min_distance_labels = list_distance[dd][0]
                                        list_distane_value.append([min_distance_labels,value[index][1]])

                            update_labels = min(list_distane_value)
                            result.append(update_labels[1])
                            labels_index.append([i,update_labels[1]]) 
                    K_knn = 0
                except:
                    pass
            if (905 <= x_mouse <= 1095 and 610 <= y_mouse <= 650):
                try:
                    list_labels_news = []
                    result = []                    
                    print("ALGORITHM")
                except:
                    pass    
            if (710 <= x_mouse <= 710 + 385 and 655 <= y_mouse <= 695):
                try: 
                    list_labels_news = []
                    result = []
                    points = []
                    labels_index = []
                    K_knn = 0
                    K_Kmeans = 0
                    test = 0
                    labels = []
                    print("Reset")
                except:
                    pass                        
                   
    for i in range(len(points)):
        pygame.draw.circle(screen,BLACK,(points[i][0] + 50,600 - points[i][1]),8)
        pygame.draw.circle(screen,WHITE,(points[i][0] + 50,600 - points[i][1]),7)

    if (len(labels) != 0):
        for i in range(len(points)):
            pygame.draw.circle(screen,COLORS_LABELS[labels[i]],(points[i][0] + 50,600 - points[i][1]),7)
    if (len(list_labels_news) != 0):
        for i in range(len(list_labels_news)):
            pygame.draw.circle(screen,BLACK,(list_labels_news[i][0] + 50,600 - list_labels_news[i][1]),8)
            pygame.draw.circle(screen,WHITE,(list_labels_news[i][0] + 50,600 - list_labels_news[i][1]),7)
        
    if (len(result) != 0):
        for i in range(len(result)):
            pygame.draw.circle(screen,COLORS_LABELS[result[i]],(list_labels_news[i][0] + 50, 600 - list_labels_news[i][1]),7)
    
    pygame.display.flip()
pygame.quit()

