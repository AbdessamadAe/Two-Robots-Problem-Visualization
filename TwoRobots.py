from manim import *


class TwoRobotsProblem(Scene):
    def construct(self):
        background = ImageMobject("./assets/Space").scale(.5).set_opacity(.5)
        self.add(background)
        line = Line(10 * LEFT, 10 * RIGHT)
        line.color = GREEN
        self.play(DrawBorderThenFill(line), run_time=3)
        
        robot1 = SVGMobject("./assets/robot").scale(.3).shift(0.32 * UP + 3 * LEFT)
        x1 = robot1.get_x()
        flag1 = ImageMobject("./assets/parachute.png").scale(.1).shift(0.21 * UP + 3 * LEFT)

        robot2 = SVGMobject("./assets/robot2").scale(.3).shift(0.32 * UP + 6 * LEFT)
        x2 = robot2.get_x()
        flag2 = ImageMobject("./assets/parachute.png").scale(.1).shift(0.21 * UP + 6 * LEFT)
        
        self.play(FadeIn(flag1, robot1), FadeIn(flag2, robot2), run_time=3)
        
        def roboMeet():
            count = 0
            Robot1ReachedParachute = False
            Robot2ReachedParachute = False

            while True: 
                if Robot1ReachedParachute:
                    self.play(
                        ApplyMethod(robot1.shift, .5*RIGHT, run_time=.5),
                    )
                elif Robot2ReachedParachute:
                    self.play(
                        ApplyMethod(robot2.shift, .5*RIGHT, run_time=.5),
                    )
                
                if abs(robot1.get_x() - robot2.get_x()) <= .3:
                    break

                self.play(
                        ApplyMethod(robot1.shift, .5*RIGHT, run_time=.5),
                        ApplyMethod(robot2.shift, .5*RIGHT, run_time=.5),
                    )
                
                count += 1

                if abs(robot1.get_x() - x2) <= .3:
                    Robot1ReachedParachute = True
                if abs(robot2.get_x()-x1) <= .3:
                    Robot2ReachedParachute = True
                
                self.wait(.5)



        roboMeet()
        
        self.wait(2)
