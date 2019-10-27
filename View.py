#==============================================================================
#==============================IMPORTING LIBRARIES=============================
#==============================================================================
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image
import sys
#==============================================================================


#==============================================================================
#============================DEFINITION OF VARIABLES===========================
#==============================================================================
windowWidth = 600
windowHeight = 600

positionX=0
positionY=0

rotationX=0.0
rotationY=0.0
rotationZ=0.0

yellow=[1.0,1.0,0.0]
blue=[0.0,0.0,1.0]
red=[1.0,0.0,0.0]
green=[0.0,1.0,0.0]
cian=[0.0,1.0,1.0]
magenta=[1.0,0.0,1.0]

positionEyeX=0.1
positionEyeY=0.1
positionEyeZ=21.5
pointCenterX=0.5
pointCenterY=0.0
pointCenterZ=-5.5
VectorUpX=0.0
VectorUpY=0.1
VectorUpZ=0.0

maze=[1,1,1,1,1,1,1,1,
      1,0,0,0,0,0,0,1,
      1,0,1,1,0,1,0,1,
      1,0,1,0,0,1,1,1,
      0,0,1,1,0,0,0,0,
      1,0,0,1,0,1,1,1,
      1,0,0,0,0,0,0,1,
      1,0,1,1,1,1,0,1,
      1,0,0,0,0,0,0,1,
      1,1,1,1,1,1,1,1
     ]
#==============================================================================



#==============================================================================
#===================Function That Draws The Walls Of The Maze==================
#==============================================================================
def drawWall():
    loadTextures()
    glEnable(GL_TEXTURE_2D)
    glBegin(GL_QUADS)
    #==========================================================================
    glTexCoord2f(0.0,1.0);glVertex3f(-1.0,-1.0,1.0)
    glTexCoord2f(1.0,1.0);glVertex3f(1.0,-1.0,1.0)
    glTexCoord2f(1.0,0.0);glVertex3f(1.0,1.0,1.0)
    glTexCoord2f(0.0,0.0);glVertex3f(-1.0,1.0,1.0)
    #==========================================================================
    glTexCoord2f(0.0,0.0);glVertex3f(-1.0,-1.0,-1.0)
    glTexCoord2f(0.0,1.0);glVertex3f(-1.0,1.0,-1.0)
    glTexCoord2f(1.0,1.0);glVertex3f(1.0,1.0,-1.0)
    glTexCoord2f(1.0,0.0);glVertex3f(1.0,-1.0,-1.0)
    #==========================================================================
    glTexCoord2f(1.0,1.0);glVertex3f(-1.0,1.0,-1.0)
    glTexCoord2f(1.0,0.0);glVertex3f(-1.0,1.0,1.0)
    glTexCoord2f(0.0,0.0);glVertex3f(1.0,1.0,1.0)
    glTexCoord2f(0.0,1.0);glVertex3f(1.0,1.0,-1.0)
    #==========================================================================
    glTexCoord2f(0.0,1.0);glVertex3f(-1.0,-1.0,-1.0)
    glTexCoord2f(1.0,1.0);glVertex3f(1.0,-1.0,-1.0)
    glTexCoord2f(1.0,0.0);glVertex3f(1.0,-1.0,1.0)
    glTexCoord2f(0.0,0.0);glVertex3f(-1.0,-1.0,1.0)
    #==========================================================================
    glTexCoord2f(0.0,0.0);glVertex3f(1.0,-1.0,-1.0)
    glTexCoord2f(0.0,1.0);glVertex3f(1.0,1.0,-1.0)
    glTexCoord2f(1.0,1.0);glVertex3f(1.0,1.0,1.0)
    glTexCoord2f(1.0,0.0);glVertex3f(1.0,-1.0,1.0)
    #==========================================================================
    glTexCoord2f(1.0,0.0);glVertex3f(-1.0,-1.0,-1.0)
    glTexCoord2f(0.0,0.0);glVertex3f(-1.0,-1.0,1.0)
    glTexCoord2f(0.0,1.0);glVertex3f(-1.0,1.0,1.0)
    glTexCoord2f(1.0,1.0);glVertex3f(-1.0,1.0,-1.0)
    #==========================================================================
    glEnd()
#==============================================================================



#==============================================================================
#=======================Function That Draws The 3D Plane=======================
#==============================================================================
def drawPlane():
    glDisable(GL_TEXTURE_2D)
    #Axis of the plane X=======================================================
    glColor3f(red[0],red[1],red[2])
    glBegin(GL_LINES)
    glVertex3f(0.0,0.0,0.0)
    glVertex3f(20.0,0.0,0.0)
    glEnd()
    #Axis of the plane Y#======================================================
    glColor3f(green[0],green[1],green[2])
    glBegin(GL_LINES)
    glVertex3f(0.0,0.0,0.0)
    glVertex3f(0.0,20.0,0.0)
    glEnd()
    #Axis of the plane Z#======================================================
    glColor3f(cian[0],cian[1],cian[2])
    glBegin(GL_LINES)
    glVertex3f(0.0,0.0,0.0)
    glVertex3f(0.0,0.0,20.0)
    glEnd()
#==============================================================================



#==============================================================================
#===================Function That Draws The Floor Of The Maze==================
#==============================================================================
def drawFloor():
    glBegin(GL_QUADS)
    glColor3f(blue[0],blue[1],blue[2])
    glVertex3f(40,-1,40)
    glVertex3f(-40,-1,40)
    glVertex3f(-40,-1,-40)
    glVertex3f(40,-1,-40)
    glEnd()
#==============================================================================



#==============================================================================
#==============Function That Draws The Structure Of The Labyrinth==============
#==============================================================================
def drawMaze():
    yc=0
    xc=0
    for yc in range(0,10):
        for xc  in range (0,8):
            if (maze[xc+yc*8]==1):
                glPushMatrix()
                glTranslatef(xc*2.0,0.0,yc*2.0)
                drawWall()
                glPopMatrix()
#==============================================================================



#==============================================================================
#=============Function That Is Responsible For Drawing The Window==============
#==============================================================================
def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(50,2,0.1,30)
    glMatrixMode(GL_MODELVIEW)
    glDepthFunc(GL_LEQUAL)
    glEnable(GL_DEPTH_TEST)
    glClearDepth(1.0)
    glTexEnvi(GL_TEXTURE_ENV,GL_TEXTURE_ENV_MODE,GL_DECAL)
    glLoadIdentity();
    #glRotatef(rotationX,1.0,0.0,0.0)
    glRotatef(rotationY,0.0,1.0,0.0)
    #glRotatef(rotationZ,0.0,0.0,1.0)
    gluLookAt(0.1+positionEyeX,0.1+positionEyeY,0.5+positionEyeZ,0.5+positionEyeX,0.0,-5.5+positionEyeZ,0.0,1.0,0.0)
    glPointSize(10)
    drawPlane()
    drawFloor()
    glPolygonMode(GL_FRONT_AND_BACK,GL_FILL)
    drawMaze()
    glutSwapBuffers()
#==============================================================================



#==============================================================================
#==========Function That Activates And Defines A Set Of States Of OGL==========
#==============================================================================
def init():
    glEnable(GL_TEXTURE_2D)
    glClearDepth(1.0)
#==============================================================================



#==============================================================================
#========================Function To Rescale The Window========================
#==============================================================================
def reshape(width,height):
    lightPos=(-50.0,50.0,100.0,1.0)
    nRange=2.0
    if(height==0):
        height=1
    glViewport(0,0,width,height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if(width<=height):
        glOrtho(-nRange,nRange,-nRange*height/width,nRange*height/width,-nRange,nRange)
    else:
        glOrtho(-nRange*width/height,nRange*width/height,-nRange,nRange,-nRange,nRange)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glLightfv(GL_LIGHT0,GL_POSITION,lightPos)
#==============================================================================



#==============================================================================
#==================Function To Capture Events Of Special Keys==================
#==============================================================================
def specialKeys(key,valueX,valueY):
    global positionEyeX
    global positionEyeZ
    if(key==GLUT_KEY_UP):
        positionEyeZ-=1
        print("La posicion de la camara en Z es: ",positionEyeZ)
    if(key==GLUT_KEY_DOWN):
        positionEyeZ+=1
        print("La posicion de la camara en Z es: ",positionEyeZ)
    if(key==GLUT_KEY_LEFT):
        positionEyeX-=0.5
        print("La posicion de la camara en X es: ",positionEyeX)
    if(key==GLUT_KEY_RIGHT):
        positionEyeX+=0.5
        print("La posicion de la camara en X es: ",positionEyeX)
    glutPostRedisplay()
#==============================================================================



#==============================================================================
#=======================Function That Loads The Texture========================
#==============================================================================
def loadTextures():
    image=Image.open("Cube.bmp")
    sizeX=image.size[0]
    sizeY=image.size[1]
    image=image.tostring("raw","RGBX",0,-1)
    glBindTexture(GL_TEXTURE_2D,glGenTextures(1))
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D,0,3,sizeX,sizeY,0,GL_RGBA,GL_UNSIGNED_BYTE,image)
    glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_WRAP_S,GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_WRAP_T,GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_WRAP_S,GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_WRAP_T,GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV,GL_TEXTURE_ENV_MODE,GL_DECAL)
#==============================================================================



#==============================================================================
#======================Function To Capture Keyboard Events=====================
#==============================================================================
def keyboard(key,valueX,valueY):
    global rotationY
    if(key==b"a"):
        rotationY-=10.0
        print("El valor en grados de la rotacion en Y es: ",rotationY)
    if(key==b"d"):
        rotationY+=10.0
        print("El valor en grados de la rotacion en Y es: ",rotationY)
    glutPostRedisplay()
#==============================================================================



#==============================================================================
#================================Function Main=================================
#==============================================================================
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB|GLUT_DOUBLE|GLUT_DEPTH)
    glutInitWindowSize(windowWidth,windowHeight)
    glutInitWindowPosition(positionX,positionY)
    glutCreateWindow(b"Maze In PyOpenGL")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(specialKeys)
    glutMainLoop()
#==============================================================================



#==============================================================================
#=============================The Application Runs=============================
#==============================================================================
if(__name__=="__main__"):
    main()
#==============================================================================