from display import *
from matrix import *
from draw import *
import sys

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 move: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""

def round(m):
    for r in range(len(m)):
        toInt(m[r])

def toInt(L):
        for c in range(len(L)):
            try:
                L[c] = int(L[c])
            except(ValueError):
                pass   
	

def parse_file( fname, points, transform, screen, color ):
	
	#new functions to make script interaction easier
    def line(x0, y0, z0, x1, y1, z1):
        add_edge(points, x0, y0, z0, x1, y1, z1)
		
    def scale(x, y, z):
        m = make_scale(x,y,z)
        matrix_mult(m, transform)

    def move(x, y, z):
        m = make_translate(x,y,z)
        matrix_mult(m, transform)
		

    def rotate(axis, theta):
        if axis == 'x':
            m = make_rotX(theta)
        elif axis == 'y':
            m = make_rotY(theta)
        elif axis == 'z':
            m = make_rotZ(theta)
            matrix_mult(m, transform)

    def save(fname):
        display2()
        save_extension(screen, fname)
		
    def ident2(): #terrible naming
        ident(transform)

    def appl():
        matrix_mult(transform, points)

    def display2(): #terrible naming
        clear_screen(screen)
        #print points
        round(points)
        draw_lines(points, screen, color)
        display(screen)

	#---------------------------------------------------------------------
    needsArgs = {"line":line, "scale":scale, "move":move, "rotate":rotate, "save":save}

    noArgs = {"ident":ident2, "apply":appl, "display":display2, "quit": sys.exit}

	#---------------------------------------------------------------------             
    with open(fname, 'r') as f:
        command = "foo" #placeholder
        while command:
            command = f.readline().strip()
            if command in needsArgs:
                args = f.readline().split()
                print args
                toInt(args)
                print args
                needsArgs[command](*args)
            elif command in noArgs:
                noArgs[command]()
		






