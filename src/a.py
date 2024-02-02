from manim import *
import sys
import os

# print( os.getcwd() )
p = "../"

class C( Scene ):
    def construct( self ):
        c = Circle()
        c.set_fill( PINK, opacity=0.5 )
        self.play( Create( c ) )

def main():
    c = C()
    c.render()

if __name__=="__main__":
    # print(len(sys.argv))
    main()
