import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.peg_oled_display import Oled, OledData, OledDisplayMode, OledReactionType

keyboard = KMKKeyboard()

# I2C definitions
keyboard.SDA = board.D4
keyboard.SCL = board.D5

# Define your matrix pins (adjust to match your wiring)
keyboard.col_pins = (board.D3, board.D10, board.D9)
keyboard.row_pins = (board.D0, board.D1, board.D2)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

#OLED Code
oled_ext = Oled(
    OledData(
        corner_one={0: OledReactionType.STATIC, 1: ["XIAO Macropad"]},
        corner_two={0: OledReactionType.LAYER, 1: ["Layer 0"]},
        corner_three={0: OledReactionType.STATIC, 1: ["MODS"]},
        corner_four={0: OledReactionType.MODS, 1: ["S", "C", "A", "G"]},
    ),
    toDisplay=OledDisplayMode.TXT,
    flip=False,
)
keyboard.extensions.append(oled_ext)

# Define what each key does
keyboard.keymap = [
    [KC.COPY, KC.PASTE, KC.CUT],
    [KC.UNDO, KC.REDO, KC.SCREENSHOT],
    [KC.MPLY, KC.MNXT, KC.MUTE],    
]
encoder_handler = EncoderHandler()

encoder_handler.pins = (
    (board.D7, board.D6),  
)

encoder_handler.map = [((KC.VOLD, KC.VOLU),)]  # rotate CCW / CW

keyboard.modules.append(encoder_handler)


if __name__ == "__main__":
    keyboard.go()