from manim import *


class PerpendicularOscillationDetailedDerivation(Scene):
    def construct(self):
        # STEP 0: Show the original equations centered
        eqX = MathTex(r"x(t)=A_1", r"\sin\Big(\omega t+\phi_1\Big)")
        eqX.scale(0.9)

        eqX.move_to(ORIGIN + UP * 0.5)

        eqY = MathTex(r"y(t)=A_2", r"\sin\Big(\omega t+\phi_2\Big)")
        eqY.scale(0.9)
        eqY.move_to(ORIGIN + DOWN * 0.5)
        self.play(Write(eqX), Write(eqY))
        self.wait(2)

        expX = MathTex(
            r"x(t)=A_1", r"\Big[\sin(\omega t)\cos\phi_1+\cos(\omega t)\sin\phi_1\Big]"
        )
        expX.scale(0.9)
        expX.move_to(ORIGIN + UP * 0.5)
        expY = MathTex(
            r"y(t)=A_2", r"\Big[\sin(\omega t)\cos\phi_2+\cos(\omega t)\sin\phi_2\Big]"
        )
        expY.scale(0.9)
        expY.move_to(ORIGIN + DOWN * 0.5)
        self.play(
            ReplacementTransform(eqX, expX),
            ReplacementTransform(eqY, expY),
            run_time=1.5,
        )
        self.wait(2)

        expXA = MathTex(
            r"\frac{x(t)}{A_1}=", r"\sin(\omega t)\cos\phi_1+\cos(\omega t)\sin\phi_1"
        )
        expXA.scale(0.9)
        expXA.move_to(ORIGIN + UP * 0.6)
        expYA = MathTex(
            r"\frac{y(t)}{A_2}=", r"\sin(\omega t)\cos\phi_2+\cos(\omega t)\sin\phi_2"
        )
        expYA.scale(0.9)
        expYA.move_to(ORIGIN + DOWN * 0.6)
        self.play(
            ReplacementTransform(expX, expXA),
            ReplacementTransform(expY, expYA),
            run_time=1.5,
        )
        self.wait(2)

        copy1 = expXA.copy()
        copy2 = expYA.copy()

        #########FIRST REMOVEMENT##########
        num = ValueTracker(1)
        case = Circle(radius=0.3, color=WHITE)
        case.move_to(expXA.get_left() + LEFT * 1.5 + UP * 2.05)
        cnt = Text(text=str(int(num.get_value())), color=BLUE, font_size=40)
        cnt.move_to(case.get_center())
        self.play(FadeIn(case), Write(cnt))

        mult = Line(
            expXA.get_right() + DOWN + RIGHT * 0.5, expXA.get_right() + UP + RIGHT * 0.5
        )
        factor = MathTex(r"\cdot\cos\phi_2")
        factor.scale(0.7)
        factor.move_to(mult.get_center() + RIGHT * 0.7)
        self.play(FadeIn(mult), Write(factor), run_time=0.5)

        expXB = MathTex(
            r"\frac{x(t)\cos\phi_2}{A_1}",
            r"=\sin(\omega t)\cos\phi_1\cos\phi_2+\cos(\omega t)\sin\phi_1\cos\phi_2",
        )
        expXB.scale(0.7)
        expXB.move_to(ORIGIN + UP * 0.6 + LEFT * 0.5)
        self.play(ReplacementTransform(expXA, expXB), run_time=1)
        self.wait(1)

        mult2 = Line(
            expYA.get_right() + DOWN + RIGHT * 0.5, expYA.get_right() + UP + RIGHT * 0.5
        )
        factor2 = MathTex(r"\cdot\cos\phi_1")
        factor2.scale(0.7)
        factor2.move_to(mult2.get_center() + RIGHT * 0.7)

        self.play(
            ReplacementTransform(factor, factor2),
            ReplacementTransform(mult, mult2),
            run_time=1,
        )
        self.wait(1)

        expYB = MathTex(
            r"\frac{y(t)\cos\phi_1}{A_2}=",
            r"\sin(\omega t)\cos\phi_2\cos\phi_1+\cos(\omega t)\sin\phi_2\cos\phi_1",
        )
        expYB.scale(0.7)
        expYB.move_to(ORIGIN + DOWN * 0.6 + LEFT * 0.5)
        self.play(ReplacementTransform(expYA, expYB), run_time=1)
        self.wait(1)
        self.play(FadeOut(mult2), FadeOut(factor2), run_time=0.5)

        combined1 = MathTex(
            r"\frac{x(t)\cos\phi_2}{A_1}-\frac{y(t)\cos\phi_1}{A_2}=",
            r"\cos(\omega t)(\sin\phi_1\cos\phi_2-\sin\phi_2\cos\phi_1)",
        )

        combined1.scale(0.7)
        combined1.move_to(ORIGIN)
        self.play(ReplacementTransform(VGroup(expXB, expYB), combined1), run_time=1)
        self.wait(1)

        br1 = BraceBetweenPoints(
            combined1.get_center() + RIGHT * 0.4 + DOWN * 0.1,
            combined1.get_right() + DOWN * 0.1,
            color=BLUE,
            sharpness=0.5,
        )
        self.play(FadeIn(br1), run_time=1)
        self.wait(0.5)

        auxc1 = MathTex(r"\sin\Delta\phi")
        auxc1.move_to(br1.get_tip() + DOWN * 0.1)
        auxc1.scale(0.7)
        self.play(Write(auxc1), run_time=1)

        finalC1 = MathTex(
            r"\frac{x(t)\cos\phi_2}{A_1}-\frac{y(t)\cos\phi_1}{A_2}=",
            r"\cos(\omega t)(\sin\Delta\phi)",
        )

        finalC1.scale(0.7)
        finalC1.move_to(ORIGIN)
        self.play(
            ReplacementTransform(combined1, finalC1),
            FadeOut(auxc1),
            FadeOut(br1),
            run_time=1.5,
        )
        self.wait(1)

        self.play(FadeOut(finalC1), run_time=0.5)
        self.wait(1)

        #########SECOND REMOVEMENT

        num2 = ValueTracker(2)
        cnt2 = Text(text=str(int(num2.get_value())), color=BLUE, font_size=40)
        cnt2.move_to(case.get_center())
        self.play(ReplacementTransform(cnt, cnt2), run_time=0.5)
        self.wait(1)

        self.play(FadeIn(copy1), FadeIn(copy2), run_time=0.5)
        self.wait(1)

        mult3 = Line(
            expXA.get_right() + DOWN + RIGHT * 0.5, expXA.get_right() + UP + RIGHT * 0.5
        )
        factor3 = MathTex(r"\cdot\sin\phi_2")
        factor3.scale(0.7)
        factor3.move_to(mult3.get_center() + RIGHT * 0.7)
        self.play(FadeIn(mult3), Write(factor3), run_time=0.5)

        copyX = MathTex(
            r"\frac{x(t)\sin\phi_2}{A_1}",
            r"=\sin(\omega t)\cos\phi_1\sin\phi_2+\cos(\omega t)\sin\phi_1\sin\phi_2",
        )
        copyX.scale(0.7)
        copyX.move_to(ORIGIN + UP * 0.6 + LEFT * 0.5)
        self.play(ReplacementTransform(copy1, copyX), run_time=1)
        self.wait(1)

        mult4 = Line(
            expYA.get_right() + DOWN + RIGHT * 0.5, expYA.get_right() + UP + RIGHT * 0.5
        )
        factor4 = MathTex(r"\cdot\sin\phi_1")
        factor4.scale(0.7)
        factor4.move_to(mult4.get_center() + RIGHT * 0.7)

        self.play(
            ReplacementTransform(factor3, factor4),
            ReplacementTransform(mult3, mult4),
            run_time=1,
        )
        self.wait(1)

        copyY = MathTex(
            r"\frac{y(t)\sin\phi_1}{A_2}=",
            r"\sin(\omega t)\cos\phi_2\sin\phi_1+\cos(\omega t)\sin\phi_2\sin\phi_1",
        )
        copyY.scale(0.7)
        copyY.move_to(ORIGIN + DOWN * 0.6 + LEFT * 0.5)
        self.play(ReplacementTransform(copy2, copyY), run_time=1)
        self.wait(1)
        self.play(FadeOut(mult4), FadeOut(factor4), run_time=0.5)

        combined2 = MathTex(
            r"\frac{x(t)\sin\phi_2}{A_1}-\frac{y(t)\sin\phi_1}{A_2}=",
            r"\sin(\omega t)(\sin\phi_1\cos\phi_2-\sin\phi_2\cos\phi_1)",
        )

        combined2.scale(0.7)
        combined2.move_to(ORIGIN)
        self.play(ReplacementTransform(VGroup(copyX, copyY), combined2), run_time=1)
        self.wait(1)

        br2 = BraceBetweenPoints(
            combined2.get_center() + RIGHT * 0.4 + DOWN * 0.1,
            combined2.get_right() + DOWN * 0.1,
            color=BLUE,
            sharpness=0.5,
        )
        self.play(FadeIn(br2), run_time=1)
        self.wait(0.5)

        auxc2 = MathTex(r"-\sin\Delta\phi")
        auxc2.move_to(br2.get_tip() + DOWN * 0.1)
        auxc2.scale(0.7)
        self.play(Write(auxc2), run_time=1)

        finalC2 = MathTex(
            r"\frac{x(t)\sin\phi_2}{A_1}-\frac{y(t)\sin\phi_1}{A_2}=",
            r"-\sin(\omega t)(\sin\Delta\phi)",
        )

        finalC2.scale(0.7)
        finalC2.move_to(ORIGIN)
        self.play(
            ReplacementTransform(combined2, finalC2),
            FadeOut(auxc2),
            FadeOut(br2),
            run_time=1.5,
        )
        self.wait(1)

        self.play(FadeOut(finalC2), run_time=0.5)
        self.wait(1)

        g1 = VGroup(cnt2, case)
        self.play(FadeOut(g1))

        finalC1.move_to(ORIGIN + UP * 0.5)
        finalC2.move_to(ORIGIN + DOWN * 0.5)

        self.play(FadeIn(finalC1), FadeIn(finalC2), run_time=1)
        self.wait(1)

        c1br = MathTex(
            r"(\frac{x(t)\cos\phi_2}{A_1}-\frac{y(t)\cos\phi_1}{A_2})^{2}=",
            r"(\cos(\omega t)(\sin\Delta\phi))^{2}",
        )

        c2br = MathTex(
            r"(\frac{x(t)\sin\phi_2}{A_1}-\frac{y(t)\sin\phi_1}{A_2})^{2}=",
            r"(-\sin(\omega t)(\sin\Delta\phi))^{2}",
        )
        c1br.scale(0.7)
        c1br.move_to(ORIGIN + UP * 0.5)

        c2br.scale(0.7)
        c2br.move_to(ORIGIN + DOWN * 0.5)

        self.play(
            ReplacementTransform(finalC1, c1br),
            ReplacementTransform(finalC2, c2br),
            run_time=1,
        )
        self.wait(3)

        cc1 = MathTex(
            r"(\frac{x(t)\cos\phi_2}{A_1})^{2}+",
            r"(\frac{y(t)\cos\phi_1}{A_2})^{2}-",
            r"\frac{2x(t)y(t)\cos\phi_2\cos\phi_1}{A_1A_2}="
            r"(\cos(\omega t)(\sin\Delta\phi))^{2}",
        )

        cc2 = MathTex(
            r"(\frac{x(t)\sin\phi_2}{A_1})^{2}+",
            r"(\frac{y(t)\sin\phi_1}{A_2})^{2}-",
            r"\frac{2x(t)y(t)\sin\phi_2\sin\phi_1}{A_1A_2}="
            r"(\sin(\omega t)(\sin\Delta\phi))^{2}",
        )
        cc1.scale(0.7)
        cc1.move_to(ORIGIN + UP * 0.5)
        cc2.scale(0.7)
        cc2.move_to(ORIGIN + DOWN * 0.5)
        self.play(
            ReplacementTransform(c1br, cc1), ReplacementTransform(c2br, cc2), run_time=1
        )

        self.wait(2)

        final1 = MathTex(
            r"(\frac{x(t)}{A_1})^{2}+",
            r"(\frac{y(t)}{A_2})^{2}-",
            r"\frac{2x(t)y(t)}{A_1A_2}(\cos\phi_2\cos\phi_1+\sin\phi_2\sin\phi_1)="
            r"(\sin\Delta\phi)^{2}",
        )
        final1.scale(0.7)
        final1.move_to(ORIGIN)
        self.play(ReplacementTransform(VGroup(cc1, cc2), final1), run_time=1)
        self.wait(2)

        br3 = BraceBetweenPoints(
            final1.get_center() + LEFT * 0.3 + DOWN * 0.1,
            final1.get_center() + RIGHT * 3 + DOWN * 0.1,
            color=BLUE,
            sharpness=0.5,
        )
        self.play(FadeIn(br3), run_time=1)
        self.wait(0.5)

        auxc3 = MathTex(r"\cos\Delta\phi")
        auxc3.move_to(br3.get_tip() + DOWN * 0.2)
        auxc3.scale(0.7)
        self.play(Write(auxc3), run_time=1)
        self.wait(1)

        final = MathTex(
            r"(\frac{x(t)}{A_1})^{2}+",
            r"(\frac{y(t)}{A_2})^{2}-",
            r"\frac{2x(t)y(t)}{A_1A_2}\cos\Delta\phi=" r"(\sin\Delta\phi)^{2}",
        )
        final.scale(0.7)
        final.move_to(ORIGIN)
        self.play(
            ReplacementTransform(final1, final),
            FadeOut(auxc3),
            FadeOut(br3),
            run_time=1.5,
        )
        self.wait(1)
