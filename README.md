# Harus-Turtlepad 
Turtlepad is a 9 key macropad with a rotary encoder, and an OLED Display, using KMK firmware.

#Features:
- 2 seperate pieces to make the case
- 0.91" OLED
- EC11 Rotary Encoder for Volume
- 9 Keyboard keys for Audio and General Control

  # CAD Model:
  Everything fits using M3 Bolys, and inserts.
  It contains 2 3d printed surfaces for the bottom and Top of the case, with the pcb sitting at the bottom with a usb c port open for the XIAO board to plug into.
This photo is of how the top of the case will look!
<img width="738" height="560" alt="image" src="https://github.com/user-attachments/assets/041b44b2-1520-4027-b066-e80994e5874f" />
Top left has the oled (the rectangle hole), and the 3x3 matrix in the middle with a rotary encoder on the right side.

The items will also be apart, which will be updated with real life photos to make sure that everyone gets the best viewing experience!
This is the photo of the case from another angle
 <img width="955" height="567" alt="image" src="https://github.com/user-attachments/assets/c64d52a1-dc1a-4268-b4e0-d273cf701129" />

  # PCB:
  Here's my schematic for the PCB, made in KICAD.
<img width="1253" height="649" alt="image" src="https://github.com/user-attachments/assets/87f9fa2d-f953-4715-869a-d9bc86414d6a" />

  Now Here is the layout of the actual PCB that will get printed, made up of 2 layers. It has a matrix next to a rotary encoder and an OLED.
<img width="1196" height="902" alt="image" src="https://github.com/user-attachments/assets/d536f1f4-47ff-4359-b964-599e71698927" />

 # Firmware
This runs entirely on KMK Firmware
- Rotary Encoder Deals with volume
- 9 keys will run different keybinds/Macros
- Oled will display days until my next competition
- These can change from a simple python file!

  # BOM:
  List of items for the hackpad
- 9x Cherry MX Switches
- 9x DSA Keycaps
- 5x M3x5x4 Heatset inserts
- 3x M3x16mm SHCS Bolts
- 2X M3x12mm SHCS Bolts
- 9x 1N4148 DO-35 Diodes.
- 1x 0.91" 128x32 OLED Display
- 1x EC11 Rotary Encoder
- 1x Xiao RP2040
- 1x Case (2x 3d printed pieces put together)
- 
  # Extra-info:
  I had to redo the entire pcb around 6 times because first I put the mcu in the middle, and then had to keep rewiring because the wires were horrible, and have learned quite a bit about pcb design.
