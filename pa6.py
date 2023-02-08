from CSE8AImage import *

def blend(img1, img2):
    # TODO Write the body of the function here
    img=[]
    for a in range(len(img1)):
        abc=[]
        for b in range(len(img1[a])):
            img1[a][b]= ((img1[a][b][0]+ img2[a][b][0])/2 ,(img1[a][b][1] +img2[a][b][1])/2,(img1[a][b][2]+img2[a][b][2])/2)
            abc.append(img1[a][b])
        img.append(abc)
    return img



    # TODO Return the modified image


def mirror(img):
    # TODO Write the body of the function here
    
    for y in range(len(img)):
        for x in range(len(img[y])//2):
            temp = img[y][x]
            img[y][x] = img[y][len(img[y])-x-1]
            img[y][len(img[y])-x-1] = temp
    
    # TODO Return the modified image
    return img

def add_stamp(stamp_image, background_image):
    # TODO Write the body of the function here
    
    for x in range(len(stamp_image)):
        
        for y in range(len(stamp_image[x])):

            background_image[x][y]=stamp_image[x][y]
    
    # TODO Return the modified image
    return background_image


def find_waldo(img, topLeftrow, topLeftcol, width, height):
    # TODO Write the body of the function here
    image=[]
    for x in range(topLeftrow, topLeftrow + height):
        abc = []
        for y in range(topLeftcol, topLeftcol + width):
            abc.append(img[x][y])
        image.append(abc)
            
            



    # TODO Return the modified image
    return image




