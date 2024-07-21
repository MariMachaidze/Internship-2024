I'm gonna start with having a 4x4 grid where one resistor breaks inside the square lattice how the current changes in the perimeter. I want to see how everything changes depending on which resistor broke and figure out some formula.


Prompt: We have a 4x4 grid with resistors. One of them breaks and we need to figure out which one broke.

input A - output G

Node g: -6.5 V
Node h: -3.8 V
Node i: -2.3 V
Node j: -1.5 V
Node f: -3.8 V
Node 4: -2.7 V
Node 3: -1.5 V
Node k: -0.7 V
Node e: -2.3 V
Node 2: -1.5 V
Node 1: -0.4 V
Node l:  0.8 V
Node d: -1.5 V
Node c: -0.7 V
Node b:  0.8 V
Node a:  3.5 V



---------------

RH00 N00 N01 1kOhm
RV00 N00 N10 1kOhm
RH01 N01 N02 1kOhm
RV01 N01 N11 1kOhm
RH02 N02 N03 1kOhm
RV02 N02 N12 1kOhm
RV03 N03 N13 1kOhm
RH10 N10 N11 1kOhm
RV10 N10 N20 1kOhm
RH11 N11 N12 1kOhm
RV11 N11 N21 1kOhm
RH12 N12 N13 1kOhm
RV12 N12 N22 1kOhm
RV13 N13 N23 1kOhm
RH20 N20 N21 1kOhm
RV20 N20 N30 1kOhm
RH21 N21 N22 1kOhm
RV21 N21 N31 1kOhm
RH22 N22 N23 1kOhm
RV22 N22 N32 1kOhm
RV23 N23 N33 1kOhm
RH30 N30 N31 1kOhm
RH31 N31 N32 1kOhm
RH32 N32 N33 1kOhm


--------------------------------


V1 N00 0 10V
RH00 N00 N01 1kOhm
RV00 N00 N10 1kOhm
RH01 N01 N02 1kOhm
RV01 N01 N11 1kOhm
RH02 N02 N03 1kOhm
RV02 N02 N12 1kOhm
RV03 N03 N13 1kOhm
RH10 N10 N11 1kOhm
RV10 N10 N20 1kOhm
RH11 N11 N12 1kOhm
RV11 N11 N21 1kOhm
RH12 N12 N13 1kOhm
RV12 N12 N22 1kOhm
RV13 N13 N23 1kOhm
RH20 N20 N21 1kOhm
RV20 N20 N30 1kOhm
RH21 N21 N22 1kOhm
RV21 N21 N31 1kOhm
RH22 N22 N23 1kOhm
RV22 N22 N32 1kOhm
RV23 N23 N33 1kOhm
RH30 N30 N31 1kOhm
RH31 N31 N32 1kOhm
RH32 N32 N33 1kOhm
RGRD N33 0 1uOhm

Node N00: 10.0 V
Node N01:  7.3 V
Node N02:  5.8 V
Node N03:  5.0 V
Node N10:  7.3 V
Node N11:  6.2 V
Node N12:  5.0 V
Node N13:  4.2 V
Node N20:  5.8 V
Node N21:  5.0 V
Node N22:  3.8 V
Node N23:  2.7 V
Node N30:  5.0 V
Node N31:  4.2 V
Node N32:  2.7 V
Node N33:  0.0 V
Node N01, N00:  2.7 V <--
Node N10, N00:  2.7 V <--
Node N02, N01:  1.5 V <--
Node N11, N01:  1.2 V
Node N03, N02:  0.8 V <--
Node N12, N02:  0.8 V
Node N13, N03:  0.8 V <--
Node N11, N10:  1.2 V
Node N20, N10:  1.5 V <--
Node N12, N11:  1.2 V
Node N21, N11:  1.2 V
Node N13, N12:  0.8 V
Node N22, N12:  1.2 V
Node N23, N13:  1.5 V <--
Node N21, N20:  0.8 V
Node N30, N20:  0.8 V <--
Node N22, N21:  1.2 V
Node N31, N21:  0.8 V
Node N23, N22:  1.2 V
Node N32, N22:  1.2 V
Node N33, N23:  2.7 V <-- 
Node N31, N30:  0.8 V <--
Node N32, N31:  1.5 V <--
Node N33, N32:  2.7 V <--




Node N01, N00:  2.7 V <--
Node N02, N01:  1.5 V <--
Node N03, N02:  0.8 V <--
Node N13, N03:  0.8 V <--
Node N23, N13:  1.5 V <--
Node N33, N23:  2.7 V <-- 
Node N33, N32:  2.7 V <--
Node N32, N31:  1.5 V <--
Node N31, N30:  0.8 V <--
Node N30, N20:  0.8 V <--
Node N20, N10:  1.5 V <--
Node N10, N00:  2.7 V <--