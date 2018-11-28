#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 16:01:34 2018

@author: bhavyababuta
"""

import numpy
from PIL import Image, ImageDraw

def loadImage(path):
    image = Image.open(path).convert("RGBA")
    image.show()

#Image is converted into numpy array
def convertImageIntoArray(image):
    image_array = numpy.asarray(image)
    return image_array

#Get Polygon from Dictionary
def get_polygon_from_dic(dic):
    polygon=[]
    for i in dic:
        x_i=i.get('x')
        y_i=i.get('y')
        polygon.append((x_i,y_i))
    return polygon

#Function to return only the Polygon Object
def returnCroppedImage(image_array,polygon):
    #Create a mask Image of L Mode and Black and White Colorscale
    mask = Image.new('L', (image_array.shape[1], image_array.shape[0]), 0)
    mask.show()
    
    ImageDraw.Draw(mask).polygon(polygon, outline=1, fill=1)
    mask_array = numpy.array(mask)
    
    #New Image
    cropped_image = numpy.empty(image_array.shape,dtype='uint8')
    
    #Add all the dimensions except for the Transparency Dimension
    cropped_image[:,:,:3] = image_array[:,:,:3]
    Image.fromarray(cropped_image,"RGBA").show()
    
    #Add Transparency. Only the polygon is unmasked.
    cropped_image[:,:,3] = mask_array*255
    cropped_image = Image.fromarray(cropped_image, "RGBA").show()
    
    return cropped_image
