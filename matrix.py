import math

def make_translate( x, y, z ):
    translate = new_matrix()
    ident(translate)
    translate[3][0] = x
    translate[3][1] = y
    translate[3][2] = z
    return translate

def make_scale( x, y, z ):
    scale = new_matrix()
    ident(scale)
    scale[0][0] = x
    scale[1][1] = y
    scale[2][2] = z
    return scale

def make_rotX( theta ):
    theta = math.radians(theta)
    rotX = new_matrix()
    ident(rotX)
    rotX[1][1] = math.cos(theta)
    rotX[2][1] = -1 * math.sin(theta)
    rotX[1][2] = math.sin(theta)
    rotX[2][2] = math.cos(theta)
    return rotX
    
def make_rotY( theta ):
    theta = math.radians(theta)
    rotY = new_matrix()
    ident(rotY)
    rotY[0][0] = math.cos(theta)
    rotY[0][2] = -1 * math.sin(theta)
    rotY[2][0] = math.sin(theta)
    rotY[2][2] = math.cos(theta)
    return rotY

def make_rotZ( theta ):
    theta = math.radians(theta)
    rotZ = new_matrix()
    ident(rotZ)
    rotZ[0][0] = math.cos(theta)
    rotZ[1][0] = -1 * math.sin(theta)
    rotZ[0][1] = math.sin(theta)
    rotZ[1][1] = math.cos(theta)
    return rotZ



def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print s

def ident( matrix ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            if r == c:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):

    point = 0
    for row in m2:
        #get a copy of the next point
        tmp = row[:]
        
        for r in range(4):
            m2[point][r] = (m1[0][r] * tmp[0] +
                            m1[1][r] * tmp[1] +
                            m1[2][r] * tmp[2] +
                            m1[3][r] * tmp[3])
        point+= 1


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
