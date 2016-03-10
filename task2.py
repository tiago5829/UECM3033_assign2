import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import scipy.linalg as sp

#create a function
def svd(n):
    img=mpimg.imread('tree.jpg')
    [r,g,b] = [img[:,:,i] for i in range(3)]
    r1,r2,r3 = sp.svd(r)
    g1,g2,g3 = sp.svd(g)
    b1,b2,b3 = sp.svd(b)
    r_nonzero=(r2!=0).sum() #count how many non zero matrix
    g_nonzero=(g2!=0).sum()
    b_nonzero=(b2!=0).sum()
    print("The number of non zero elements in decompose sigma of red, green, blue matrices are", r_nonzero,"," ,g_nonzero,"and" ,b_nonzero, "respectively.")
    
    #create a matrix for dot multiplication
    r2[n:800]=np.zeros_like(r2[n:800])
    g2[n:800]=np.zeros_like(g2[n:800])
    b2[n:800]=np.zeros_like(b2[n:800])
    r2=sp.diagsvd(r2,800,1000)
    g2=sp.diagsvd(g2,800,1000)
    b2=sp.diagsvd(b2,800,1000)
    r_new=np.dot(r1, np.dot(r2,r3))
    g_new=np.dot(g1, np.dot(g2,g3))
    b_new=np.dot(b1, np.dot(b2,b3))
    
    #Create and display new resolution image
    img[:,:,0]=r_new
    img[:,:,1]=g_new
    img[:,:,2]=b_new
    
    display the modified picture
    fig = plt.figure(2)
    ax1 = fig.add_subplot(2,2,1)
    ax2 = fig.add_subplot(2,2,2)
    ax3 = fig.add_subplot(2,2,3)
    ax4 = fig.add_subplot(2,2,4)
    ax1.imshow(img)
    ax2.imshow(r, cmap = 'Reds')
    ax3.imshow(g, cmap = 'Greens')
    ax4.imshow(b, cmap = 'Blues')
    plt.show()
    
    #display original picture
    img=mpimg.imread('tree.jpg')
    [r,g,b]=[img[:,:,i] for i in range(3)]
    fig=plt.figure(1)
    ax1=fig.add_subplot(2,2,1)
    ax2 = fig.add_subplot(2,2,2)
    ax3 = fig.add_subplot(2,2,3)
    ax4 = fig.add_subplot(2,2,4)
    ax1.imshow(img)
    ax2.imshow(r, cmap = 'Reds')
    ax3.imshow(g, cmap = 'Greens')
    ax4.imshow(b, cmap = 'Blues')
    plt.show()

#low resolution    
svd(30)

#high resolution
svd(200)
