# Module 3D models

## PocketBeagle2.stpZ

- Source: BeagleBoard.org PocketBeagle 2 hardware repository,
  https://openbeagle.org/pocketbeagle/pocketbeagle-2 , file `design/old/pocketbeagle2_v03_21_EVT.stp`
  (EVT revision; board outline and P1/P2 header positions match the revA dimension drawing).
- License: Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0),
  (c) BeagleBoard.org Foundation. This copy is unmodified, only gzip-compressed (KiCad `.stpZ`).
- Used by: `KL_Footprints:BeagleBoard_PocketBeagle`. The footprint is drawn from the PB2 SoC side,
  so the model is flipped (rotate 180/0/-90) and offset so P1 pin 1 is at the footprint origin.
  The Z offset assumes the PB2 SoC-side face sits 10.1 mm below the cape top
  (1.6 mm cape + 8.5 mm female header); adjust it for the real stack.
