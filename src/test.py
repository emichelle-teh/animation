from manim import *
import sys
# config.disable_caching = False
config.disable_caching = True
# config.avg_frame_rate = "15"

p = "../"

class Man( Scene ):
    def swap( o1, o2 ):
        o1.set_opacity(0.0)
        o2.set_opacity(1.0)

    def construct( self ):
        lemon = ImageMobject( "../asset/lemon.webp" )
        man = ImageMobject( "../asset/man.png" )
        # man.scale( 10.0 )
        # man = ImageMobject( "man" )
        man.to_edge( RIGHT, buff=1 )
        lemon.to_edge( LEFT, buff=1)

        self.add( man )
        self.add( lemon )
        print( lemon.get_center())
        # self.play( Transform(man,lemon))
        self.play(man.animate.shift(DOWN), lemon.animate.shift( UP ))
        self.play(FadeOut(lemon))
        lemon.move_to(man)
        # self.play(FadeOut(man),FadeOut(lemon))
        # lemon.move_to(man)
        self.play(FadeOut(man))
        self.play(FadeIn(lemon))
        # self.play(lemon.animate.move_to(man))
        # self.play( Write( man ) )
        # self.play(man)
        # self.play( Create( man ) )

class Bird( Scene ):
    def swap( self, o1, o2 ):
        # o1.set_opacity(0.0)
        # o2.set_opacity(1.0)
        self.play(o1.animate(run_time=0.1).set_opacity(0.0))
        self.play(o2.animate(run_time=0.1).set_opacity(1.0))
        

    def construct( self ):
        birdUp = ImageMobject( "../asset/bird_wing_up.png" )
        birdDown = ImageMobject( "../asset/bird_wing_down.png" )

        birdDown.set_opacity( 0.0 )
        self.add( birdUp )
        self.add( birdDown )
        group = Group( birdUp, birdDown ).arrange( DOWN)
        
        for i in range( 2 ):
            # pass    
            # self.play( group.animate.shift(DOWN) )
            self.swap( birdUp, birdDown )
            # self.play( group.animate.shift(UP))
            self.swap( birdDown, birdUp )
            
class Bill( Scene ):
    # def __init__( self ):
    #     # pass
    #     self.bill1 = ImageMobject( "../asset/Bill1.png" )
    #     self.bill2 = ImageMobject( "../asset/Bill2.png" )

    #     # self.add( bill1, bill2 )
    #     # self.add(bill1)
    #     # group = Group( house1, house2 )
    #     shiftConst = .1
    #     self.bill = ImageMobject( "../asset/Bill1.png" )
    #     # bill.become(bill1)
    #     self.g = Group( self.bill1, self.bill2, self.bill )
    #     self.t=0

    # def updateB( self, b, dt ):
    #     # print( dt )
    #     self.g.rotate(PI*dt)
    #     b.shift([0,5*dt,0])
    #     self.t+=1
    #     print(self.t)
    #     # bill.rotate(PI*dt)

    #     # bill.add_updater(update)

    def construct( self ):
        global p
        bill1 = ImageMobject( f'{p}/asset/Bill1.png' )
        bill2 = ImageMobject( f'{p}/asset/Bill2.png' )

        # bill1 = ImageMobject( "../asset/Bill1.png" )
        # bill2 = ImageMobject( "../asset/Bill2.png" )

        # bill = ImageMobject( "../asset/Bill1.png" )
        bill = ImageMobject( f'{p}/asset/Bill1.png' )
        g = Group( bill1, bill2, bill )
        self.t=0

        def update( b, dt ):
            # print( dt )
            # g.rotate(PI*dt)
            # b.shift([0,5*dt,0])
            self.t+=1
            # print(self.t)
            # bill.rotate(PI*dt)

        bill.add_updater(update)
        self.add(bill) #  add bill to the scene
        # self.wait(1)
        # self.wait(4)
        # self.bill.add_updater(self.updateB)
        for i in range(2):
            self.wait(.5)
            # self.bill.become(self.bill2)
            bill.become(bill2)
            # self.play(bill.animate.shift(UP))
            self.wait(.5)
            bill.become(bill1)
            # self.bill.become(self.bill1)

class B( Scene ):
    def construct( self ):
        b = ImageMobject( "../asset/Bill1.png" )
        # Rotate(b,angle=PI)
        b.rotate(angle=PI)
        self.wait(.5)
        self.add(b)
        self.wait()
# b = B()
# b.render()
# Bill.render()
        
def main():
    global p
    if len( sys.argv ) >= 2:
        p = sys.argv[ 1 ]
    b = Bill()
    b.render()

if __name__=="__main__":
    main()