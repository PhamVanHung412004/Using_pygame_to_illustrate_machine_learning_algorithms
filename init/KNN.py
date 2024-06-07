from sklearn.cluster import KMeans
from init_class import pygame,calc_distance,array_counts,Linear_Search,check_value,Draw_ox_oy,COLORS,colors_init,Font,Show_mouse

colors = COLORS()
COLORS_LABELS = colors_init(colors)
fonts = Font()

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

pygame.init()
height = 1400
witd = 750
screen = pygame.display.set_mode((height,witd))

test = 0
labels = []
clusters = []
list_labels_news = []
labels_index = []
K_knn = 0
K_Kmeans = 0
results = []
runing = True
points = []
clock = pygame.time.Clock()
font = pygame.font.SysFont('sans', 20)
font1 = pygame.font.SysFont('sans', 30)
font2 = pygame.font.SysFont('sans', 40)
font3 = pygame.font.SysFont('sans', 50) 
check = False
while runing:
    clock.tick(60)
    screen.fill(colors.BACKGROUND)
    x_mouse , y_mouse = pygame.mouse.get_pos()
    
    show_mouse = Show_mouse(x_mouse, y_mouse, font,colors.BLACK,screen)
    if (50 <= x_mouse <= 1100 and 50 <= y_mouse <= 600):
        show_mouse.show()
    
    up = font.render("▲", True, colors.BLACK)
    ngang = font.render("►", True, colors.BLACK)
    x = font1.render("X", True, colors.BLACK)
    y = font1.render("Y", True, colors.BLACK)
    O = font1.render("0", True, colors.BLACK)

    Run_kmeans_button = font.render("RUN_KMEANS", True, colors.BLACK)
    labelss = font.render("LABELS", True, colors.BLACK)
    using_kmeans = font2.render("IMG degis", True, colors.BLACK)
    k_button = font2.render("K = " + str(K_knn), True, colors.BLACK)
    K_Kmeans_button = font2.render("K = " + str(K_Kmeans), True, colors.BLACK)
    dau_cong = font2.render("+", True, colors.BLACK)
    dau_tru = font2.render("-", True, colors.BLACK)
    run_button = font2.render("RUN_KNN" , True, colors.BLACK)
    algorithm_button = font1.render("DELETE LABEL", True, colors.BLACK)
    reset_button = font2.render("RESET" , True, colors.BLACK)

    draw_ox_oy = Draw_ox_oy(50, 50, 50, 600, 50, 600, 1100, 600, colors.BLACK, up, ngang,screen)
    draw_ox_oy.show()

    rect_clusters = show_cluster(colors.BLACK,
                                 colors.WHITE,
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
            # import test
            check = True
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
                    print("Error")
                    break

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
                poins_news = []
                results = []
                list_point = []
                try:
                    for i in list_labels_news: # O(n)
                        list_distance_labels = []
                        for j in range(len(labels_index)): # O(n)
                            distance = calc_distance(i,labels_index[j][0])
                            list_distance_labels.append([distance,labels_index[j][1]])
                        list_distance_labels.sort() # O(nlog(n))
                        (begin,end,list_counts,labels_distance) = array_counts(list_distance_labels,K_knn) # O(3*n)

                        value_counts = -1
                        list_counts_update = []
                        for index in range(begin,end + 1): # O(m)
                            if (list_counts[index] != 0):
                                list_counts_update.append([list_counts[index],index])
                                value_counts = max(value_counts,list_counts[index])

                        list_index_value_max = Linear_Search(list_counts_update,value_counts) # O(m)
                        labels_distance.sort() # (O(nlog(n)))

                        label = check_value(list_index_value_max,labels_distance) # O(mlog(n))
                        results.append(label) 
                        labels_index.append([i,label])
                    K_knn = 0
                except:
                    print("Error")
                    break

            if (905 <= x_mouse <= 1095 and 610 <= y_mouse <= 650):
                try:
                    list_labels_news = []
                    results = []                    
                except:
                    print("Error")
                    break
            if (710 <= x_mouse <= 710 + 385 and 655 <= y_mouse <= 695):
                try: 
                    list_labels_news = []
                    results = []
                    points = []
                    labels_index = []
                    K_knn = 0
                    K_Kmeans = 0
                    test = 0
                    labels = []
                    print("Reset")
                except:
                    print("Error")
                    break                        
                   
    for i in range(len(points)):
        pygame.draw.circle(screen,colors.BLACK,(points[i][0] + 50,600 - points[i][1]),8)
        pygame.draw.circle(screen,colors.WHITE,(points[i][0] + 50,600 - points[i][1]),7)

    if (len(labels) != 0):
        for i in range(len(points)):
            pygame.draw.circle(screen,COLORS_LABELS[labels[i]],(points[i][0] + 50,600 - points[i][1]),7)

    if (len(list_labels_news) != 0):
        for i in range(len(list_labels_news)):
            pygame.draw.circle(screen,colors.BLACK,(list_labels_news[i][0] + 50,600 - list_labels_news[i][1]),8)
            pygame.draw.circle(screen,colors.WHITE,(list_labels_news[i][0] + 50,600 - list_labels_news[i][1]),7)
        
    if (len(results) != 0):
        for i in range(len(results)):
            pygame.draw.circle(screen,COLORS_LABELS[results[i]],(list_labels_news[i][0] + 50, 600 - list_labels_news[i][1]),7)
    
    pygame.display.flip()
pygame.quit()

if (check):
    import backgroup2
