import sys
import numpy as np
from PNM import *
# define pi for convenience
pi = np.pi

def CreateAndSavePFM(out_path):
    width = 512
    height = 512
    numComponents = 3

    img_out = np.empty(shape=(width, height, numComponents), dtype=np.float32)
    
    for y in range(height):
        for x in range(width):
            img_out[y,x,:] = 1.0

    write_pfm(out_path, img_out)

def LoadAndSavePPM(in_path, out_path):
    img_in = read_ppm(in_path)
    img_out = np.empty(shape=img_in.shape, dtype=img_in.dtype)
    height,width,_ = img_in.shape # Retrieve height and width
    for y in range(height):
        for x in range(width):
            img_out[y,x,:] = img_in[y,x,:] # Copy pixels

    write_ppm(out_path, img_out)

def LoadAndSavePFM(in_path, out_path):
    img_in = read_pfm(in_path)
    img_out = np.empty(shape=img_in.shape, dtype=img_in.dtype)
    height,width,_ = img_in.shape # Retrieve height and width
    for y in range(height):
        for x in range(width):
            img_out[y,x,:] = img_in[y,x,:] # Copy pixels

    write_pfm(out_path, img_out)

def LoadPPMAndSavePFM(in_path, out_path):
    img_in = read_ppm(in_path)
    img_out = np.empty(shape=img_in.shape, dtype=np.float32)
    height,width,_ = img_in.shape
    for y in range(height):
        for x in range(width):
            img_out[y,x,:] = img_in[y,x,:]/255.0

    write_pfm(out_path, img_out)
            
def LoadPFMAndSavePPM(in_path, out_path):
    img_in = read_pfm(in_path)
    img_out = np.empty(shape=img_in.shape, dtype=np.float32)
    height,width,_ = img_in.shape
    for y in range(height):
        for x in range(width):
            img_out[y,x,:] = img_in[y,x,:] * 255.0

    write_ppm(out_path, img_out.astype(np.uint8))

def create_sphere_image():
    width = 511
    height = 511
    numComponents = 3

    img_out = np.empty(shape=(width, height, numComponents), dtype=np.float32)
    # the sphere has diameter 511, the center point is the center of the image, the other part outside the sphere is black
    for y in range(height):
        for x in range(width):
            if (x - 255.5) ** 2 + (y - 255.5) ** 2 <= 255.5 ** 2:
                img_out[y, x, :] = 1.0
            else:
                img_out[y, x, :] = 0.0

    return img_out

    

if '__main__' == __name__:
    # # LoadAndSavePFM('Office/Office7.pfm', 'test7.pfm')
    # # LoadAndSavePPM('Office/Office6.ppm', 'test6.ppm')
    # LoadPFMAndSavePPM('Office/Office7.pfm', 'grace.ppm')
    # # LoadPPMAndSavePFM('test.ppm', '9.pfm')
    # pass
    environment_graph = read_pfm('Office/Office6.pfm')
    # print(environment_graph)
    sphere = create_sphere_image()
    # clip the environment graph to the sphere
    environment_graph = environment_graph[0:511, 0:511, :]
    # the position of the sphere is at (0,0,1)
    sphere_position = np.array([0, 0, 1])
    # record the normal of the sphere in each pixel
    sphere_normal = np.empty(shape=(511, 511, 3), dtype=np.float32)
    for y in range(511):
        for x in range(511):
            if sphere[y, x, 0] == 1.0:
                sphere_normal[y, x, :] = np.array([x - 255.5, y - 255.5, 255.5]) / 255.5
            else:
                sphere_normal[y, x, :] = np.array([0, 0, 0])
    write_pfm('sphere.pfm', sphere)




