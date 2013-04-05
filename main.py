# -*- coding: utf-8 -*-
'''
Created on 08/03/2013

@author: boni
'''
# coding=UTF-8
import numpy as np 
from PIL import Image
import time



class myImage():
    
    _img = None
    
    ## metodo responsavel por carregar a imagem num array
    #    @param image caminho da imagem 
    #    @return array de pixels da imagem
    def adread(self, image):
        self._img = Image.open( image )
        var = np.array( self._img.getdata() )
        var.resize( 256,256 )
        return var
    #adread()
    
    ## método responsável por mostrar a imagem armezanada num array
    #  @brief array imageArray array de pixels da  imagem    
    def adshow(self, imageArray ):        
        self._img.putdata( imageArray )
        self._img.show()
    #adshow()
        
    def adrot( self, imageArray ):        
        newImage = np.array([])
        newImage.resize( 256, 256 )
        
        for i in range(256):
            for j in range( 256 ):                
                newImage[i][j] = imageArray[j][255-i]
                
        self.adshow( np.ravel( newImage ) )
    #adrot()
    
    def adrot_transp( self, imageArray ):        
        imageArray = np.fliplr( imageArray )
        imageArray = imageArray.transpose()
        self.adshow( imageArray )
        
    def absHistogram(self, imageArray):
        histogram = np.zeros(256)
        ( maxr, maxc ) = imageArray.shape
        for i in range(maxr):
            for j in range(maxc):
                k = imageArray[i][j]
                histogram[k] = histogram[k] + 1
        
        return histogram
        
    def relHistogram( self, imageArray ):
        relHist = np.zeros( 256 )        
        absHist = self.absHistogram( imageArray ) 
        relHist = absHist/imageArray.size
        return relHist
            
    
#myImage
        
    
def main():
    imgObj = myImage()
    img    = imgObj.adread('emilia.jpg')
    imgObj.adshow( img )
    print img.shape
    
   
    print imgObj.relHistogram(img)
    
    
    t1 = time.time()
    imgObj.adrot( img )
    t2 = time.time()
    
    print "Tempo total = ", t2-t1
    
    t1 = time.time()
    imgObj.adrot_transp( img )
    t2 = time.time()
    
    print "Tempo total 2 = ", t2-t1
    

if __name__ == '__main__':
    main()