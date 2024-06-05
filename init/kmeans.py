# import pygame
from random import randint
from sklearn.cluster import KMeans
from init_class import Draw_ox_oy,Show_mouse,pygame,COLORS,upper_bound,lower_bound,colors_init,points_black_rect,points_white_circle,search_and_distance,prefix_sum

colors = COLORS()
rect_black = points_black_rect()
rect_white = points_white_circle()
COLORS_LABELS = colors_init(colors)
const = int(1e4)

# def solve():
    

class Draw_point:
    def __init__(self,point,WHITE,BLACK,label,COlOR):
        self.point = point
        self.WHITE = WHITE
        self.BLACK = BLACK
        self.label = label
        self.COlOR = COlOR

    def draw_points_panel(self):
        points = self.point
        color = self.COlOR
        labels = self.label

        for i in range(len(points)):
            pygame.draw.circle(screen,self.BLACK,(points[i][0] + 50, 600 - points[i][1]),8)
            if (len(labels) == 0):
                pygame.draw.circle(screen,self.WHITE,(points[i][0] + 50,600 - points[i][1]),7)
            else:
                pygame.draw.circle(screen,color[labels[i]],(points[i][0] + 50,600 - points[i][1]),8)

class Rectengo:
    def __init__(self,BLACK,WHITE):     
        self.BLACK = BLACK
        self.WHITE = WHITE
    def Draw(self):
        for i in range(len(rect_black)):
            pygame.draw.rect(screen,self.BLACK,rect_black[i])
            pygame.draw.rect(screen,self.WHITE,rect_white[i])
        pygame.draw.rect(screen,self.WHITE,(105,660,40,30))     
        pygame.draw.rect(screen,self.BLACK,(1100,650,90,45))
        pygame.draw.rect(screen,self.WHITE,(1105,655,80,35))

class Name_button:
    def __init__(self,random,algorithm,error,reset,k_button,run_button,dau_cong,dau_tru,img_button):
        self.random = random
        self.algorithm = algorithm
        self.error = error
        self.reset = reset
        self.k_button = k_button
        self.run_button = run_button
        self.dau_cong = dau_cong
        self.dau_tru = dau_tru
        self.img_button = img_button
    
    def show_name_button(self): 
        screen.blit(self.k_button,(60, 605))
        screen.blit(self.dau_cong,(115, 650))
        screen.blit(self.dau_tru,(65, 650))
        
        screen.blit(self.random,(175, 610))
        screen.blit(self.algorithm,(385, 615))
        screen.blit(self.error,(595, 615))
        screen.blit(self.reset,(830, 610))
        screen.blit(self.run_button,(1010, 610))
        screen.blit(self.img_button,(1110,650))

class Draw_clusters:
    def __init__(self,cluster,COLOR):
        self.cluster = cluster
        self.COLOR = COLOR
    def draw_clusters(self):
        clusters = self.cluster
        COLORS = self.COLOR
        for i in range(len(clusters)):
            # pygame.draw.circle(screen,COLORS[i],(clusters[i][0] + 50, 600 - clusters[i][1]),8)
            pygame.draw.rect(screen,COLORS[i],(clusters[i][0] + 50, 600 - clusters[i][1],15,15))

def cacl_point_mid(x,y,cnt):
    value = [x / cnt, y / cnt]
    return value

pygame.init()

height = 1200
witd = 700
screen = pygame.display.set_mode((height,witd))
clock = pygame.time.Clock()
runing = True
points = []
clusters = []
labels = []
labels_values = []
k = 0
error = 0
prefix_sum_x = []
prefix_sum_y = []
index_distance = []
arr1 = []
arr2 = []
arr3 = [] 
font = pygame.font.SysFont('sans', 20)
font11 = pygame.font.SysFont('sans', 30)
font_1 = pygame.font.SysFont('sans', 40)
font_2 = pygame.font.SysFont('sans', 50) 
# error_min = [int(1e9)] * const
# error_min[0] = 0
check = False
while runing:
    clock.tick(60)
    screen.fill(colors.BACKGROUND)
    x_mouse,y_mouse = pygame.mouse.get_pos()
    
    #Font
    up = font.render("▲", True, colors.BLACK)
    ngang = font.render("►", True, colors.BLACK)

    #draw ox,oy,up,ngang
    draw_ox_oy = Draw_ox_oy(50, 50, 50, 600, 50, 600, 1100, 600, colors.BLACK, up, ngang,screen)
    draw_ox_oy.show()

    # Show mouse
    show_mouse = Show_mouse(x_mouse, y_mouse, font,colors.BLACK,screen)
    if (50 <= x_mouse <= 1100 and 50 <= y_mouse <= 600):
        show_mouse.show()
        
    #Draw rect
    rectengo = Rectengo(colors.BLACK,colors.WHITE)
    rectengo.Draw()

    #Event mouse
    for event in pygame.event.get():
        #Button quit
        if (event.type == pygame.QUIT):
            # import backgroup
            check = True
            runing = False  

        #Mouse button down
        if (event.type == pygame.MOUSEBUTTONDOWN):
            if (50 <= x_mouse <= 1100 and 50 <= y_mouse <= 600):
                labels = []
                x = float(x_mouse - 50)
                y = float(abs(y_mouse - 600))
                point = [x,y]
                points.append(point)
            
            # -= 1 clusters
            elif (55 <= x_mouse <= 95 and 660 <= y_mouse <= 690):
                if (k > 0):
                    k -= 1

            # += 1 clusters
            elif (105 <= x_mouse <= 145 and 655 <= y_mouse <= 695):
                if (k >= 0 and k < 8):
                    k += 1

            #button random
            elif ( 165 <= x_mouse <= 385 and 610 <= y_mouse <= 660):
                T = k
                clusters = []
                test_mid = []
                while(T > 0):
                    cluster = [randint(50,1110) - 50, abs(randint(50,600) - 600)]
                    clusters.append(cluster)
                    test_mid.append(cluster)
                    T -= 1

            #button run    
            elif (1000 <= x_mouse <= 1090 and 610 <= y_mouse <= 660):
                try:
                    print("Run")
                    labels = []
                    labels_values = []
                    prefix_sum_x = []
                    prefix_sum_y = []
                    index_distance = []
                    error = 0                    

                    if (len(clusters) == 0):
                        continue
                    
                    (labels_values, labels, index_distance) = search_and_distance(points,clusters)
                    
                    #=> O(n^2)
                    labels_values.sort() # O(nlog(n))
                    index_distance.sort() # O(nlog(n))
                    value_init = labels_values[0][1]

                    prefix_sum_x = [0] * len(labels_values) # O(n)
                    prefix_sum_y = [0] * len(labels_values) # O(n)

                    prefix_sum_x[0] = value_init[0]
                    prefix_sum_y[0] = value_init[1] 

                    for i in range(1,len(labels_values)): # O(n)
                        value = labels_values[i][1]
                        prefix_sum_x[i] = prefix_sum_x[i - 1] + value[0] 
                        prefix_sum_y[i] = prefix_sum_y[i - 1] + value[1]
                        index_distance[i][1] += index_distance[i - 1][1]
                        
                    for i in range(0,7): # O(m)
                        first_value = lower_bound(labels_values,i) # O(log(n))
                        second_value = upper_bound(labels_values,i) # O(log(n))
                        
                        if (first_value != -1 and second_value != -1 and second_value - first_value + 1 > 0):
                            if (first_value == 0):
                                ans = cacl_point_mid(
                                    prefix_sum_x[second_value],
                                    prefix_sum_y[second_value],
                                    second_value - first_value + 1
                                )
                                error += index_distance[second_value][1]
                                clusters[i] = ans
                            else:
                                ans = cacl_point_mid(
                                    prefix_sum_x[second_value] - prefix_sum_x[first_value - 1],
                                    prefix_sum_y[second_value] - prefix_sum_y[first_value - 1],
                                    second_value - first_value + 1
                                )
                                error += index_distance[second_value][1] - index_distance[first_value - 1][1]
                                clusters[i] = ans
                except:
                    print("Error")
                    break

            #Button ALGORITHM
            elif ( 375 <= x_mouse <= 575 and 610 <= y_mouse <= 660):
                try:
                    error = 0
                    arr1 = []
                    arr2 = []
                    arr3 = [] 
                    print("\nAlgorithm")
                    kmeans = KMeans(n_clusters=k).fit(points)
                    labels = kmeans.predict(points)
                    clusters = kmeans.cluster_centers_
                    
                    (arr1, arr2, arr3) = search_and_distance(points,clusters)
                    arr3.sort()
                    arr2 = list(set(arr2))

                    total_error = prefix_sum(arr3)
                    for i in range(len(arr2)):
                        l = lower_bound(arr3,arr2[i])
                        r = upper_bound(arr3,arr2[i])
                        if (l != -1 and r != -1):
                            if (l == 0):
                                error += total_error[r]
                            else:
                                error += total_error[r] - total_error[l - 1]
                except:
                    print("Error")
                    break
                    
            elif (585 <= x_mouse <= 785 and 610 <= x_mouse <= 660):
                continue
            
            #Button reset
            elif (790 <= x_mouse <= 990 and 610 <= y_mouse <= 660):
                try: 
                    points = []
                    clusters = []
                    labels = []
                    index_distance = []
                    prefix_sum_x = []
                    prefix_sum_y = []
                    error = 0
                    k = 0
                    arr1 = []
                    arr2 = []
                    arr3 = []
                except:
                    print("Error")
                    break
            #button IMG
            # 1100,650,90,45
            elif (1100 <= x_mouse <= 1100 + 90 and 650 <= y_mouse <= 650 + 45):
                # import read_dir_img_kmeans
                import img_kmeans
                print("IMG")

            else:
                print("Error")
                continue
    k_button = font_1.render("K = " + str(k), True, colors.BLACK)          
    dau_cong = font_1.render("+", True, colors.BLACK)
    dau_tru = font_1.render("-", True, colors.BLACK)
    random_button = font_1.render("RANDOM", True, colors.BLACK)
    algorithm_button = font11.render("ALGORITHM", True, colors.BLACK)
    # if (error_min == []):

    error_button = font11.render("ERROR = "  + str(int(error)), True, colors.BLACK)
    reset_button = font_1.render("RESET" , True, colors.BLACK)
    run_button = font_1.render("RUN" , True, colors.BLACK)
    img_button = font_1.render("IMG" , True, colors.BLACK)
    x = font11.render("X", True, colors.BLACK)
    y = font11.render("Y", True, colors.BLACK)
    O = font11.render("0", True, colors.BLACK)
    screen.blit(x, (1100, 605))
    screen.blit(y, (30, 35))
    screen.blit(O, (35, 590))
    name_button = Name_button(random_button,
                              algorithm_button,
                              error_button,
                              reset_button,
                              k_button,
                              run_button,
                              dau_cong,
                              dau_tru,
                              img_button)
    name_button.show_name_button()

    draw_clusters = Draw_clusters(clusters, COLORS_LABELS)
    draw_clusters.draw_clusters()

    draw_points = Draw_point(points, colors.WHITE, colors.BLACK,labels,COLORS_LABELS)
    draw_points.draw_points_panel()
    
    pygame.display.flip()
pygame.quit()
if (check):
    import backgroup1
