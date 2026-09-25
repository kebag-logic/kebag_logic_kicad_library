# Module 3D models

## PocketBeagle2.stpZ

- Source: BeagleBoard.org PocketBeagle 2 hardware repository,
  https://openbeagle.org/pocketbeagle/pocketbeagle-2 , file `design/old/pocketbeagle2_v03_21_EVT.stp`
  (EVT revision; board outline and P1/P2 header positions match the revA dimension drawing).
- License: Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0),
  (c) BeagleBoard.org Foundation. This copy is unmodified, only gzip-compressed (KiCad `.stpZ`).
- Used by: `KL_Footprints:BeagleBoard_PocketBeagle`. The PB2 P1/P2 female headers (8.5 mm,
  ST-FH-254-0182) are on the side opposite its components, so the PB2 sits on top of the cape,
  components up. The model is flipped (rotate 180/0/-90) and offset so P1 pin 1 is at the footprint
  origin. Z offset +11.0 mm puts the PB2 header face 11.0 mm above the cape top: 2.5 mm cape male
  header plastic + 8.5 mm PB2 female header. Adjust it if the cape header differs.
