
import random
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageOps, ImageFilter
from matplotlib import cm


saved_convergence = {}

def check_convergence(z, c, max_iterations, boundary):
    if z in saved_convergence:
        return saved_convergence[z]
        
    iterations = 0
    while iterations < max_iterations and abs(z) < boundary:
        z = (z**2) + c
        iterations += 1
        
    ret = iterations if iterations < max_iterations else None
    saved_convergence[z] = ret
    return ret
    
all_color_maps = [cm.flag,cm.prism,cm.ocean,cm.gist_earth,cm.terrain,cm.gist_stern,cm.gnuplot,cm.gnuplot2,cm.CMRmap,cm.cubehelix,cm.brg,cm.gist_rainbow,cm.rainbow,cm.jet,cm.turbo,cm.nipy_spectral,cm.gist_ncar]
random.shuffle(all_color_maps)
def paint_julia(image_height, image_width, time_ratio, max_iterations, boundary, number_of_transition_windows):

    transition_window_index = int(time_ratio*number_of_transition_windows)
    color_map = all_color_maps[transition_window_index % len(all_color_maps)]
    
    pil_image = Image.new('RGBA', (image_width, image_height), (0,0,0,255))
    draw = ImageDraw.Draw(pil_image)
    
    color = color_map(0)
    color = tuple([int(255*c) for c in color])
    draw.rectangle(
        [(0,0), (pil_image.width, pil_image.height)],
        fill = color
    )
    
    
    
    open_cv_image = np.array(pil_image) 
    # Convert RGB to BGR 
    open_cv_image = open_cv_image[:, :, ::-1].copy() 
    return open_cv_image
    
    
    
    

    """#https://www.learnpythonwithrune.org/numpy-calculate-the-julia-set-with-vectorization/
    #c = -0.4 + 0.6j
    
    c = -0.1 + (0.9 + np.sin(2*np.pi*time_ratio))*(1j)
    
    x, y, zoom = 0, 0, 1
    
    x_width = 1.5
    y_height = 1.5*image_height/image_width
    
    x_from = x - x_width/zoom
    x_to = x + x_width/zoom
    
    y_from = y - y_height/zoom
    y_to = y + y_height/zoom
    
    # Here the actual algorithm starts
    x = np.linspace(x_from, x_to, image_width).reshape((1, image_width))
    y = np.linspace(y_from, y_to, image_height).reshape((image_height, 1))
    
    z = x + 1j * y
    
    # Initialize z to all zero
    c = np.full(z.shape, c)
    
    # To keep track in which iteration the point diverged
    div_time = np.zeros(z.shape, dtype=int)
    
    # To keep track on which points did not converge so far
    m = np.full(c.shape, True, dtype=bool)
    
    for i in range(max_iterations):
        z[m] = z[m]**2 + c[m]
        m[np.abs(z) > 2] = False
        div_time[m] = i
    
    
    #plt.imshow(div_time, cmap='magma')
    #plt.show()
    
    #color map and conversions
    
    
    #here
    #pil_image = Image.fromarray(np.uint8(cm.gist_earth(div_time)*255))
    pil_image = Image.fromarray(np.uint8(color_map(div_time)*255))
    
    open_cv_image = np.array(pil_image) 
    # Convert RGB to BGR 
    open_cv_image = open_cv_image[:, :, ::-1].copy() 
    return open_cv_image"""
    
    
    # image = np.zeros((image_height,image_width,4), np.uint8)
    # c = -0.8 + 0.34j
    
    # for x in range(image_width):
        # xx = (x/image_width) - 0.5
        # for y in range(image_height):
            # yy = (y/image_height) - 0.5
        
            # z = xx + yy*1j
            
            # iterations = int(255*random.random()) #check_convergence(z, max_iterations, boundary)
            # # print(z, iterations)
            
            # """if iterations == None:
                # image[y][x][0] = 255
                # image[y][x][1] = 255
                # image[y][x][2] = 255
                # image[y][x][3] = 255
                
            # else:
                # iterations_ratio = iterations/max_iterations
                
                # image[y][x][0] = int(255*iterations_ratio)
                # image[y][x][1] = 0
                # image[y][x][2] = 0
                # image[y][x][3] = 255"""
    
    # # for idx in range(500):
       # # image[idx][idx][0] = 255
        
    # return image