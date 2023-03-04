import fontforge
import sys

fontfile = sys.argv[1]

f = fontforge.open(fontfile)

for glyph in f.glyphs():
    if glyph.encoding not in [0x23, 0x2a, 0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39]:
        glyph.correctDirection()

f.generate(fontfile)