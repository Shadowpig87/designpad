import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

keyboard.modules.append(MediaKeys())

keyboard.col_pins = (board.D7, board.D3, board.D6)
keyboard.row_pins = (board.D10, board.D9, board.D8)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.pins = (
    (board.D0, board.D1, board.D2, False), 
)

keyboard.keymap = [
    [
        KC.NLCK, KC.PSLS, KC.PAST, 
        KC.P7,   KC.P8,   KC.P9,   
        KC.P4,   KC.P5,   KC.P6    
    ]
]
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.MUTE),)
]

if __name__ == '__main__':
    keyboard.go()