from manim import *


# class CreateCircle(Scene):
#     def construct(self):
#         # circle = Circle()  # create a circle
#         # circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
#         # self.play(Create(circle))  # show the circle on screen

class Man( Scene ):
    def construct( self ):
        lemon = ImageMobject( "../asset/lemon.webp" )
        man = ImageMobject( "../asset/walkingRed.png" )
        # man.scale( 10.0 )
        # man = ImageMobject( "man" )
        # man.to_edge( RIGHT, buff=1 )

        self.add( man )
        # self.play( Transform(man,lemon))
        self.play(FadeOut(man))
        # self.play( Write( man ) )
        # self.play(man)
        # self.play( Create( man ) )