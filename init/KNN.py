from sklearn.cluster import KMeans
from init_class import pygame,calc_distance,array_counts,Linear_Search,check_value,Draw_ox_oy,COLORS,colors_init,Font,Show_mouse,draw_rect_backgroud,Draw_ox_oy,screen

colors = COLORS()
COLORS_LABELS = colors_init(colors)
fonts = Font()

class Name_button:
    def __init__(self,
                 K_Kmeans_button,
                dau_cong,
                dau_tru,
                # button_random,
                button_run_kmeans,
                k_knn,
                run_knn,
                deleter_labels,
                reset_button):
        self.K_Kmeans_button = K_Kmeans_button
        self.dau_cong = dau_cong
        self.dau_tru = dau_tru
        # self.button_random = button_random
        self.button_run_kmeans = button_run_kmeans
        self.k_knn = k_knn
        self.run_knn = run_knn
        self.deleter_labels = deleter_labels
        self.reset_button = reset_button
            
    def show_name_button(self): 
        screen.blit(self.K_Kmeans_button,(1230,25))
        screen.blit(self.dau_cong,(1255,80))
        screen.blit(self.dau_tru,(1225 + 80 + 10 + 30 + 5,78)) 
        # screen.blit(self.button_random,)
        screen.blit(self.button_run_kmeans,(1230,145))
        screen.blit(self.k_knn,(1250,205))
        screen.blit(self.dau_cong,(1255,260))
        screen.blit(self.dau_tru,(1255 + 100 - 5, 267 - 10)) 

        screen.blit(self.run_knn,(1225 + 30,267 + 60))
        screen.blit(self.deleter_labels,(1225,385))
        screen.blit(self.reset_button,(1270,445))

pygame.init()
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
    
    x = font.render("X", True, colors.BLACK)
    y = font.render("Y", True, colors.BLACK)
    O = font.render("0", True, colors.BLACK)
    screen.blit(x, (1100, 605))
    screen.blit(y, (30, 35))
    screen.blit(O, (35, 590))

    up = font.render("▲", True, colors.BLACK)
    ngang = font.render("►", True, colors.BLACK)

    button_random = font1.render("RANDOM", True, colors.BLACK)
    button_run_kmeans = font1.render("RUN KMEANS", True, colors.BLACK)
        
    dau_cong = font2.render("+", True, colors.BLACK)
    dau_tru = font2.render("-", True, colors.BLACK)
    run_knn = font1.render("RUN KNN" , True, colors.BLACK)
    deleter_labels = font1.render("DELETE LABEL", True, colors.BLACK)
    reset_button = font1.render("RESET" , True, colors.BLACK)

    title = font3.render("Illustration of the k-nearest neighbors algorithm",True,colors.BLACK)
    screen.blit(title,(200,600))
    draw_ox_oy = Draw_ox_oy(50, 50, 50, 600, 50, 600, 1100, 600, colors.BLACK, up, ngang,screen)
    draw_ox_oy.show()

    #button n_clusters
    rect = draw_rect_backgroud(1225,20,170,50,colors)
    rect.show()

    # + -
    rect = draw_rect_backgroud(1225,80,80,50,colors)
    rect.show()
    rect = draw_rect_backgroud(1225 + 80 + 10,80,80,50,colors)
    rect.show()

    #button random
    rect = draw_rect_backgroud(1225,140,170,50,colors)
    rect.show()

    #button run kmeans
    # rect = draw_rect_backgroud(1225,140,170,50,colors)
    # rect.show()
    
    #button thuat toan
    rect = draw_rect_backgroud(1225,200,170,50,colors)
    rect.show()

    #- +
    rect = draw_rect_backgroud(1225,260,80,50,colors)
    rect.show()
    rect = draw_rect_backgroud(1225 + 50 + 40,260,80,50,colors)
    rect.show()

    #button RUN KNN
    rect = draw_rect_backgroud(1225,320,170,50,colors)
    rect.show()

    #button deleter label
    rect = draw_rect_backgroud(1225,380,170,50,colors)
    rect.show()

    #button reset
    rect = draw_rect_backgroud(1225,440,170,50,colors)
    rect.show()

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
            # 1225,140,170,50
            elif (1225 <= x_mouse <= 1225 + 170 and 140 <= y_mouse <= 140 + 50):
                print("run kmeans")
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

            if (1225 <= x_mouse <= 1225 + 80 and 80 <= y_mouse <= 80 + 50):
                if (K_Kmeans >= 0 and K_Kmeans < 8):
                    K_Kmeans += 1

            elif (1225 + 80 + 10 <= x_mouse <= 1225 + 80 + 10 + 80 and 80 <= y_mouse <= 80 + 50):
                if (0 < K_Kmeans <= 8):
                    K_Kmeans -= 1

            # 1225,260,80,50
            elif (1225 <= x_mouse <= 1225 + 80 and 260 < y_mouse <= 260 + 50):
                if (K_knn >= 0 and K_knn < len(points)):
                    K_knn += 1

            # 1225 + 50 + 40,260,80,50
            elif (1225 + 50 + 40 <= x_mouse <= 1225 + 50 + 40 + 80 and 260 <= y_mouse <= 260 + 50):
                if (0 < K_knn <= len(points)):
                    K_knn -= 1
            #1225,320,170,50
            elif (1225 <= x_mouse <= 1225 + 170 and 320 <= y_mouse <= 320 + 50):
                print("Run KNN")
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
            
            # 1225,380,170,50
            elif (1225 <= x_mouse <= 1225 + 170 and 380 <= y_mouse <= 380 + 50):
                print("deleter labels")
                try:
                    list_labels_news = []
                    results = []                    
                except:
                    print("Error")
                    break
                
            # 1225,440,170,50
            elif (1225 <= x_mouse <= 1225 + 170 and 440 <= y_mouse <= 440 + 50):
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
            else:
                ...                        
    k_knn = font1.render("K KNN = " + str(K_knn), True, colors.BLACK)
    K_Kmeans_button = font1.render("n_clusters = " + str(K_Kmeans), True, colors.BLACK)               
    name_button = Name_button(K_Kmeans_button,
                              dau_cong,
                              dau_tru,
                            #   button_random,
                              button_run_kmeans,
                              k_knn,
                              run_knn,
                              deleter_labels,
                              reset_button
                              )
    name_button.show_name_button()
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

# if (check):
#     import backgroup2
