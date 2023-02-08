from CSE8AImage import *
from pa6 import *

"""
RGB codes for common colors. You can add on to this
if you want to experiment with different colors.
"""
black   = (0,0,0)
white   = (255,255,255)
red     = (255,0,0)
green   = (0,255,0)
blue    = (0,0,255)
yellow  = (255,255,0)
magenta = (255,0,255)
gray    = (128,128,128)
purple  = (128,0,128)
    
def test_mirror():
    # TEST CASE:
    test_img1 = load_img("images/cat.jpg")
    # Call your mirror function here
    img= mirror(test_img1)
    # Visualize the result by saving the image
    save_img(img, "mirror_cat.jpg")

    


def test_add_stamp():
    # TEST CASE:
    test_img1 = load_img("images/classified.jpg")
    test_img2 = load_img("images/classified_doc.jpg")
    # Call your add_stamp function here
    img= add_stamp(test_img1, test_img2)
    # Visualize the result by saving the image
    save_img(img, "classy_docs.jpg")
    


"""
OPTIONAL:
You can similarly create test functions for the other functions in pa6.
"""

def test_blend():
    test_img1= load_img("images/cat.jpg")
    test_img2= load_img("images/texture.jpg")
    img= blend(test_img1, test_img2)
    save_img(img, "textured_cat.jpg")

def test_find_waldo():
    test_img= load_img("images/waldo.jpg")
    img= find_waldo(test_img, 486, 450, 70, 100)
    save_img(img, "its_waldo.jpg")

"""
Calling the Test functions one after the other.
You may want to uncomment one test at a time.
"""

test_blend()
test_mirror()
test_find_waldo()
test_add_stamp()




Class[0].append(90)
Class=[[91,92,93,94],
 [80,81,82,83],
 [71,72,73,74]]

for i in range(3):
    for j in range(4):
        print(Class[i][j])