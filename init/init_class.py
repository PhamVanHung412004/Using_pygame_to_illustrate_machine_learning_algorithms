import pygame
import numpy as np
from math import sqrt
class COLORS:
    def __init__(self):
        self.BACKGROUND = (255,255,255)
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.GREY = (192,192,192)
        self.RED = (255,0,0)
        self.GREEN = (0,102,51)
        self.BLUE = (0,0,153)
        self.YELLOW = (255,255,0)
        self.PURPLE = (255,0,255)
        self.SKY = (0,255,255)
        self.ORANGE = (255,125,25)
        self.GRAPE = (100,25,125)
        self.GRASS = (55,155,65)

class Draw_ox_oy:
    def __init__(self,ox1,ox2,ox3,ox4,oy1,oy2,oy3,oy4,BLACK,up,ngang,screen):
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
        self.screen = screen

    def show(self):
        pygame.draw.line(self.screen,self.BLACK,(self.ox1,self.ox2),(self.ox3,self.ox4),3)
        pygame.draw.line(self.screen,self.BLACK,(self.oy1,self.oy2),(self.oy3,self.oy4),3)    
        self.screen.blit(self.up,(44,32))    
        self.screen.blit(self.ngang,(1100,588))

class Show_mouse:
    def __init__(self,x_mouse,y_mouse,font_mouse,BLACK,screen):
        self.x_mouse = x_mouse
        self.y_mouse = y_mouse
        self.font_mouse = font_mouse
        self.BLACK = BLACK    
        self.screen = screen
    def show(self):
        text_mouse = self.font_mouse.render("(" + "x = " + str((self.x_mouse - 50)) + "," + "y = " + str(abs(self.y_mouse-600)) + ")",True,self.BLACK)
        self.screen.blit(text_mouse, (self.x_mouse + 10, self.y_mouse))

class input_circle:
    def __init__(self,x_center,y_center,r,color,kniess,screen):
        self.x_center = x_center
        self.y_center = y_center
        self.r = r
        self.color = color
        self.kniess = kniess
        self.screen = screen

class draw_circle(input_circle):
    def __init__(self):
        super().__init__(self,x_center,y_center,r,color,kniess,screen)
    def show_circle(self):
        pygame.draw.circle(self.screen,self.color,(x_center + 50, 600 - y_center),kniess)
        
class input_rect:
    def __init__(self,begin1,end1,w,h,color,kniess,screen):
        self.begin1 = begin1
        self.end1 = end1
        self.w = w
        self.h = h
        self.color = color
        self.kniess = kniess
        self.screen = screen

class draw_rect(input_rect):
    def __init__(self):
        super().__init__(self,begin1,end1,w,h,color,kniess,screen)
    def show_rect(self):
        pygame.draw.rect(self.screen,self.color,(self.begin1, self.end1, self.w, self.h),self.kniess)

def prefix_sum():
    ...

# color = COLORS()

def points_black_rect():
    rect_black = [(50,610,100,40),(50,655,100,40),(165,610,200,50),(375,610,200,50),(585,610,200,50),(790,610,200,50),(1000,610,90,50)]
    return rect_black

def points_white_circle():
    rect_white = [(55,615,90,30),(55,660,40,30),(170,615,190,40),(380,615,190,40),(590,615,190,40),(795,615,190,40),(1005,615,80,40)]
    return rect_white

def COLORS_LABELS():
    ...

def lower_bound(arr,x):
    ans = -1
    l = 0
    r = len(arr) - 1
    if (arr[0] == 1):
        while l <= r:
            mid = int((l + r)/2)
            if (arr[mid] == x):
                ans = mid
                r = mid - 1
            elif (arr[mid] > x):
                l = mid + 1
            else:
                r = mid - 1
    else:
        while l <= r:
            mid = int((l + r)/2)
            if (arr[mid][0] == x):
                ans = mid
                r = mid - 1
            elif (arr[mid][0] < x):
                l = mid + 1
            else:
                r = mid - 1
    return ans


colors = COLORS()

def colors_init(colors):
    colorss = {0 : colors.GREEN,
                1 : colors.BLUE,
                2 : colors.YELLOW,
                3 : colors.PURPLE,
                4 : colors.SKY,
                5 : colors.ORANGE,
                6 : colors.GRAPE,
                7 : colors.GRASS}
    return colorss
def upper_bound(arr,x):
    ans = -1
    l = 0
    r = len(arr) - 1
    if (arr[0] == 1):
        while l <= r:
            mid = (l + r)//2
            if (arr[mid] == x):
                ans = mid
                l = mid + 1
            elif (arr[mid] < x):
                l = mid + 1
            else:
                r = mid - 1
    else:
        while l <= r:
            mid = (l + r)//2
            if (arr[mid][0] == x):
                ans = mid
                l = mid + 1
            elif (arr[mid][0] < x):
                l = mid + 1
            else:
                r = mid - 1
    return ans

def calc_distance(p1,p2):
    # if (len(p1) != 0 and len(p2) != 0):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def search_and_distance(points,clusters):
    labels_values = []
    labels = []
    index_distance = []
    print(points)
    for i in points: #O(n)
        min_points = []
        for c in clusters: # O(n)
            dis = calc_distance(i, c)
            min_points.append(dis)

        min_ans = min(min_points)
        index_labels = min_points.index(min_ans)
        labels_values.append([index_labels,i])
        labels.append(index_labels)
        index_distance.append([index_labels,min_points[index_labels]])
    return (labels_values, labels, index_distance)