
import fontforge
F = fontforge.open("../../Fonts/khorshid")
for name in F:
    filename = name + ".png"
    # print name
    # F[name].export(filename)
    F[name].export(filename, 600)     # set height to 600 pixels
    