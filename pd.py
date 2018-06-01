from knots import *
d = {}
d[3_1] = Diagram(((1,5,2,4),(5,3,6,2),(3,1,4,6)))
d[4_1] = Diagram(((6,2,7,1),(2,6,3,5),(8,3,1,4),(4,7,5,8)))
d[5_1] = Diagram(((1,6,2,7),(7,2,8,3),(3,8,4,9),(9,4,10,5),(5,10,6,1)))
d[5_2] = Diagram(((1,4,2,5),(7,2,8,3),(3,8,4,9),(5,10,6,1),(9,6,10,7)))
d[6_1] = Diagram(((1,4,2,5),(9,3,10,2),(3,9,4,8),(5,12,6,1),(11,6,12,7),(7,10,8,11)))
d[6_2] = Diagram(((1,4,2,5),(9,3,10,2),(3,9,4,8),(5,10,6,11),(11,6,12,7),(7,12,8,1)))
d[6_3] = Diagram(((4,2,5,1),(2,8,3,7),(8,4,9,3),(10,5,11,6),(6,11,7,12),(12,9,1,10)))
d[7_1] = Diagram(((1,8,2,9),(9,2,10,3),(3,10,4,11),(11,4,12,5),(5,12,6,13),(13,6,14,7),(7,14,8,1)))
d[7_2] = Diagram(((1,4,2,5),(9,2,10,3),(3,10,4,11),(5,14,6,1),(13,6,14,7),(7,12,8,13),(11,8,12,9)))
d[7_3] = Diagram(((6,2,7,1),(2,10,3,9),(10,4,11,3),(4,12,5,11),(12,6,13,5),(14,8,1,7),(8,14,9,13)))
d[7_4] = Diagram(((6,2,7,1),(2,12,3,11),(10,4,11,3),(4,10,5,9),(12,6,13,5),(14,8,1,7),(8,14,9,13)))
d[7_5] = Diagram(((1,4,2,5),(9,2,10,3),(3,10,4,11),(5,12,6,13),(13,6,14,7),(7,14,8,1),(11,8,12,9)))
d[7_6] = Diagram(((1,4,2,5),(7,2,8,3),(3,8,4,9),(5,12,6,13),(11,6,12,7),(9,1,10,14),(13,11,14,10)))
d[7_7] = Diagram(((1,4,2,5),(9,3,10,2),(3,9,4,8),(5,10,6,11),(13,7,14,6),(7,13,8,12),(11,14,12,1)))
d[8_1] = Diagram(((1,4,2,5),(11,3,12,2),(3,11,4,10),(5,16,6,1),(15,6,16,7),(7,14,8,15),(13,8,14,9),(9,12,10,13)))
d[8_2] = Diagram(((1,4,2,5),(11,3,12,2),(3,11,4,10),(5,12,6,13),(13,6,14,7),(7,14,8,15),(15,8,16,9),(9,16,10,1)))
d[8_3] = Diagram(((6,2,7,1),(2,13,3,14),(12,3,13,4),(4,11,5,12),(10,5,11,6),(16,8,1,7),(8,16,9,15),(14,10,15,9)))
d[8_4] = Diagram(((6,2,7,1),(2,13,3,14),(10,3,11,4),(4,11,5,12),(12,5,13,6),(16,8,1,7),(8,16,9,15),(14,10,15,9)))
d[8_5] = Diagram(((6,2,7,1),(2,8,3,7),(8,4,9,3),(4,13,5,14),(12,5,13,6),(14,10,15,9),(10,16,11,15),(16,12,1,11)))
d[8_6] = Diagram(((1,4,2,5),(11,3,12,2),(3,11,4,10),(5,14,6,15),(15,6,16,7),(7,16,8,1),(13,8,14,9),(9,12,10,13)))
d[8_7] = Diagram(((1,4,2,5),(9,2,10,3),(3,10,4,11),(5,13,6,12),(13,7,14,6),(7,15,8,14),(15,9,16,8),(11,1,12,16)))
d[8_8] = Diagram(((1,4,2,5),(7,2,8,3),(3,8,4,9),(5,13,6,12),(13,7,14,6),(9,1,10,16),(15,11,16,10),(11,15,12,14)))
d[8_9] = Diagram(((6,2,7,1),(2,13,3,14),(10,3,11,4),(4,11,5,12),(12,5,13,6),(14,8,15,7),(8,16,9,15),(16,10,1,9)))
d[8_10] = Diagram(((1,4,2,5),(7,2,8,3),(3,8,4,9),(5,13,6,12),(13,7,14,6),(9,15,10,14),(15,11,16,10),(11,1,12,16)))
d[8_11] = Diagram(((1,4,2,5),(11,3,12,2),(3,11,4,10),(5,12,6,13),(15,6,16,7),(7,14,8,15),(13,8,14,9),(9,16,10,1)))
d[8_12] = Diagram(((4,2,5,1),(2,9,3,10),(8,3,9,4),(14,6,15,5),(6,14,7,13),(10,8,11,7),(16,11,1,12),(12,15,13,16)))
d[8_13] = Diagram(((1,4,2,5),(9,2,10,3),(3,10,4,11),(5,13,6,12),(15,7,16,6),(7,15,8,14),(13,9,14,8),(11,1,12,16)))
d[8_14] = Diagram(((1,4,2,5),(9,3,10,2),(3,9,4,8),(5,10,6,11),(13,6,14,7),(7,14,8,15),(11,16,12,1),(15,12,16,13)))
d[8_15] = Diagram(((1,4,2,5),(7,2,8,3),(3,8,4,9),(5,12,6,13),(11,6,12,7),(9,14,10,15),(15,10,16,11),(13,16,14,1)))
d[8_16] = Diagram(((6,2,7,1),(2,14,3,13),(8,3,9,4),(4,9,5,10),(14,6,15,5),(12,7,13,8),(10,15,11,16),(16,11,1,12)))
d[8_17] = Diagram(((6,2,7,1),(2,13,3,14),(8,3,9,4),(4,9,5,10),(12,5,13,6),(14,8,15,7),(10,16,11,15),(16,12,1,11)))
d[8_18] = Diagram(((6,2,7,1),(2,14,3,13),(8,3,9,4),(4,15,5,16),(10,6,11,5),(12,7,13,8),(14,10,15,9),(16,11,1,12)))
d[8_19] = Diagram(((4,2,5,1),(2,8,3,7),(8,4,9,3),(5,13,6,12),(13,7,14,6),(9,15,10,14),(15,11,16,10),(11,1,12,16)))
d[8_20] = Diagram(((4,2,5,1),(2,8,3,7),(8,4,9,3),(5,12,6,13),(11,6,12,7),(9,14,10,15),(15,10,16,11),(13,16,14,1)))
d[8_21] = Diagram(((1,4,2,5),(7,2,8,3),(3,8,4,9),(12,6,13,5),(6,12,7,11),(9,14,10,15),(15,10,16,11),(13,16,14,1)))
d[9_1] = Diagram(((1,10,2,11),(11,2,12,3),(3,12,4,13),(13,4,14,5),(5,14,6,15),(15,6,16,7),(7,16,8,17),(17,8,18,9),(9,18,10,1)))
d[9_2] = Diagram(((1,4,2,5),(11,2,12,3),(3,12,4,13),(5,18,6,1),(17,6,18,7),(7,16,8,17),(15,8,16,9),(9,14,10,15),(13,10,14,11)))
d[9_3] = Diagram(((8,2,9,1),(2,12,3,11),(12,4,13,3),(4,14,5,13),(14,6,15,5),(6,16,7,15),(16,8,17,7),(18,10,1,9),(10,18,11,17)))
d[9_4] = Diagram(((1,6,2,7),(11,2,12,3),(3,12,4,13),(13,4,14,5),(5,14,6,15),(7,18,8,1),(17,8,18,9),(9,16,10,17),(15,10,16,11)))
d[9_5] = Diagram(((6,2,7,1),(2,14,3,13),(12,4,13,3),(4,12,5,11),(14,6,15,5),(18,8,1,7),(8,18,9,17),(16,10,17,9),(10,16,11,15)))
d[9_6] = Diagram(((1,4,2,5),(11,2,12,3),(3,12,4,13),(5,14,6,15),(15,6,16,7),(7,16,8,17),(17,8,18,9),(9,18,10,1),(13,10,14,11)))
d[9_7] = Diagram(((1,4,2,5),(11,2,12,3),(3,12,4,13),(5,16,6,17),(17,6,18,7),(7,18,8,1),(15,8,16,9),(9,14,10,15),(13,10,14,11)))
d[9_8] = Diagram(((1,4,2,5),(7,2,8,3),(3,8,4,9),(5,14,6,15),(13,6,14,7),(9,1,10,18),(17,11,18,10),(11,17,12,16),(15,13,16,12)))
d[9_9] = Diagram(((1,6,2,7),(11,2,12,3),(3,12,4,13),(13,4,14,5),(5,14,6,15),(7,16,8,17),(17,8,18,9),(9,18,10,1),(15,10,16,11)))
d[9_10] = Diagram(((8,2,9,1),(2,12,3,11),(12,4,13,3),(4,16,5,15),(14,6,15,5),(6,14,7,13),(16,8,17,7),(18,10,1,9),(10,18,11,17)))
d[9_11] = Diagram(((1,4,2,5),(11,3,12,2),(3,11,4,10),(5,15,6,14),(15,7,16,6),(7,17,8,16),(17,9,18,8),(9,12,10,13),(13,1,14,18)))
d[9_12] = Diagram(((1,4,2,5),(9,2,10,3),(3,10,4,11),(5,16,6,17),(15,6,16,7),(7,14,8,15),(13,8,14,9),(11,1,12,18),(17,13,18,12)))
d[9_13] = Diagram(((14,2,15,1),(2,12,3,11),(12,4,13,3),(4,14,5,13),(10,6,11,5),(6,16,7,15),(18,8,1,7),(8,18,9,17),(16,10,17,9)))
d[9_14] = Diagram(((1,4,2,5),(11,3,12,2),(3,11,4,10),(5,12,6,13),(17,7,18,6),(7,17,8,16),(15,9,16,8),(9,15,10,14),(13,18,14,1)))
d[9_15] = Diagram(((16,2,17,1),(2,9,3,10),(8,3,9,4),(4,7,5,8),(14,5,15,6),(6,15,7,16),(18,11,1,12),(10,14,11,13),(12,17,13,18)))
d[9_16] = Diagram(((4,2,5,1),(2,12,3,11),(12,4,13,3),(16,6,17,5),(6,18,7,17),(18,8,1,7),(8,14,9,13),(14,10,15,9),(10,16,11,15)))
d[9_17] = Diagram(((1,4,2,5),(11,3,12,2),(3,11,4,10),(5,12,6,13),(13,6,14,7),(7,14,8,15),(17,9,18,8),(9,17,10,16),(15,18,16,1)))
d[9_18] = Diagram(((1,4,2,5),(11,2,12,3),(3,12,4,13),(5,14,6,15),(17,6,18,7),(7,16,8,17),(15,8,16,9),(9,18,10,1),(13,10,14,11)))
d[9_19] = Diagram(((1,4,2,5),(9,3,10,2),(3,9,4,8),(5,10,6,11),(15,7,16,6),(7,15,8,14),(11,18,12,1),(17,12,18,13),(13,16,14,17)))
d[9_20] = Diagram(((1,4,2,5),(9,2,10,3),(3,10,4,11),(5,14,6,15),(15,6,16,7),(7,16,8,17),(13,8,14,9),(11,1,12,18),(17,13,18,12)))
d[9_21] = Diagram(((1,4,2,5),(11,3,12,2),(3,11,4,10),(5,15,6,14),(17,7,18,6),(7,17,8,16),(15,9,16,8),(9,12,10,13),(13,1,14,18)))
d[9_22] = Diagram(((4,2,5,1),(2,9,3,10),(8,3,9,4),(10,6,11,5),(6,15,7,16),(14,7,15,8),(16,12,17,11),(12,18,13,17),(18,14,1,13)))
d[9_23] = Diagram(((1,4,2,5),(9,2,10,3),(3,10,4,11),(5,12,6,13),(15,6,16,7),(7,16,8,17),(11,8,12,9),(13,18,14,1),(17,14,18,15)))
d[9_24] = Diagram(((1,4,2,5),(7,2,8,3),(3,8,4,9),(5,14,6,15),(13,6,14,7),(9,17,10,16),(17,11,18,10),(11,1,12,18),(15,13,16,12)))
d[9_25] = Diagram(((1,4,2,5),(7,2,8,3),(3,8,4,9),(5,12,6,13),(11,6,12,7),(9,17,10,16),(15,11,16,10),(13,18,14,1),(17,14,18,15)))
d[9_26] = Diagram(((1,4,2,5),(11,3,12,2),(3,11,4,10),(5,12,6,13),(17,7,18,6),(7,15,8,14),(15,9,16,8),(9,17,10,16),(13,18,14,1)))
d[9_27] = Diagram(((1,4,2,5),(9,2,10,3),(3,10,4,11),(5,13,6,12),(15,6,16,7),(7,14,8,15),(17,9,18,8),(11,1,12,18),(13,17,14,16)))
d[9_28] = Diagram(((1,4,2,5),(7,2,8,3),(3,8,4,9),(5,13,6,12),(13,7,14,6),(9,16,10,17),(17,10,18,11),(11,15,12,14),(15,18,16,1)))
d[9_29] = Diagram(((6,2,7,1),(2,15,3,16),(10,4,11,3),(4,10,5,9),(14,5,15,6),(18,8,1,7),(8,13,9,14),(16,11,17,12),(12,17,13,18)))
d[9_30] = Diagram(((4,2,5,1),(2,9,3,10),(8,3,9,4),(10,6,11,5),(6,14,7,13),(14,8,15,7),(16,11,17,12),(12,17,13,18),(18,15,1,16)))
d[9_31] = Diagram(((1,4,2,5),(9,2,10,3),(3,10,4,11),(5,13,6,12),(17,7,18,6),(7,14,8,15),(15,8,16,9),(11,1,12,18),(13,16,14,17)))
d[9_32] = Diagram(((1,4,2,5),(9,3,10,2),(3,9,4,8),(5,12,6,13),(17,7,18,6),(7,15,8,14),(15,11,16,10),(11,17,12,16),(13,18,14,1)))
d[9_33] = Diagram(((4,2,5,1),(2,9,3,10),(8,3,9,4),(14,5,15,6),(6,17,7,18),(12,8,13,7),(10,16,11,15),(16,12,17,11),(18,13,1,14)))
d[9_34] = Diagram(((6,2,7,1),(2,15,3,16),(8,3,9,4),(4,14,5,13),(10,6,11,5),(16,8,17,7),(14,9,15,10),(18,11,1,12),(12,17,13,18)))
d[9_35] = Diagram(((1,8,2,9),(13,2,14,3),(3,12,4,13),(11,4,12,5),(5,16,6,17),(15,6,16,7),(7,14,8,15),(9,18,10,1),(17,10,18,11)))
d[9_36] = Diagram(((14,1,15,2),(2,15,3,16),(6,4,7,3),(4,11,5,12),(10,5,11,6),(16,7,17,8),(8,17,9,18),(12,10,13,9),(18,13,1,14)))
d[9_37] = Diagram(((1,4,2,5),(11,3,12,2),(3,11,4,10),(5,14,6,15),(13,6,14,7),(7,12,8,13),(17,9,18,8),(9,17,10,16),(15,18,16,1)))
d[9_38] = Diagram(((1,6,2,7),(13,2,14,3),(3,10,4,11),(9,4,10,5),(5,14,6,15),(7,18,8,1),(15,8,16,9),(11,16,12,17),(17,12,18,13)))
d[9_39] = Diagram(((1,6,2,7),(11,3,12,2),(3,11,4,10),(15,5,16,4),(5,15,6,14),(7,18,8,1),(13,9,14,8),(9,17,10,16),(17,13,18,12)))
d[9_40] = Diagram(((1,6,2,7),(11,3,12,2),(3,16,4,17),(9,4,10,5),(5,15,6,14),(7,12,8,13),(17,9,18,8),(15,10,16,11),(13,18,14,1)))
d[9_41] = Diagram(((6,2,7,1),(2,11,3,12),(10,3,11,4),(4,15,5,16),(14,5,15,6),(12,8,13,7),(8,17,9,18),(16,9,17,10),(18,14,1,13)))
d[9_42] = Diagram(((1,4,2,5),(9,3,10,2),(3,9,4,8),(5,10,6,11),(6,15,7,16),(14,7,15,8),(16,12,17,11),(12,18,13,17),(18,14,1,13)))
d[9_43] = Diagram(((4,2,5,1),(2,9,3,10),(8,3,9,4),(10,6,11,5),(6,14,7,13),(14,8,15,7),(11,17,12,16),(17,13,18,12),(15,1,16,18)))
d[9_44] = Diagram(((1,4,2,5),(9,3,10,2),(3,9,4,8),(5,10,6,11),(6,14,7,13),(14,8,15,7),(16,11,17,12),(12,17,13,18),(18,15,1,16)))
d[9_45] = Diagram(((4,2,5,1),(2,9,3,10),(8,3,9,4),(10,6,11,5),(13,6,14,7),(7,14,8,15),(16,11,17,12),(12,17,13,18),(18,15,1,16)))
d[9_46] = Diagram(((4,2,5,1),(2,11,3,12),(10,3,11,4),(5,14,6,15),(13,6,14,7),(7,12,8,13),(17,9,18,8),(9,17,10,16),(15,18,16,1)))
d[9_47] = Diagram(((6,2,7,1),(2,15,3,16),(8,3,9,4),(4,14,5,13),(10,6,11,5),(16,8,17,7),(14,9,15,10),(11,1,12,18),(17,13,18,12)))
d[9_48] = Diagram(((1,4,2,5),(11,3,12,2),(3,11,4,10),(14,6,15,5),(6,14,7,13),(12,8,13,7),(17,9,18,8),(9,17,10,16),(15,18,16,1)))
d[9_49] = Diagram(((6,2,7,1),(11,3,12,2),(3,11,4,10),(15,5,16,4),(5,15,6,14),(12,8,13,7),(17,9,18,8),(9,17,10,16),(18,14,1,13)))
d[10_1] = Diagram(((12,1,13,2),(2,11,3,12),(20,4,1,3),(4,20,5,19),(18,6,19,5),(6,18,7,17),(16,8,17,7),(8,16,9,15),(14,10,15,9),(10,14,11,13)))
d[10_2] = Diagram(((1,13,2,12),(5,3,6,2),(3,14,4,15),(13,4,14,5),(15,7,16,6),(7,17,8,16),(17,9,18,8),(9,19,10,18),(19,11,20,10),(11,1,12,20)))
d[10_3] = Diagram(((10,2,11,1),(2,10,3,9),(8,4,9,3),(4,17,5,18),(16,5,17,6),(6,15,7,16),(14,7,15,8),(20,12,1,11),(12,20,13,19),(18,14,19,13)))
d[10_4] = Diagram(((12,1,13,2),(2,13,3,14),(14,3,15,4),(4,11,5,12),(20,6,1,5),(6,20,7,19),(18,8,19,7),(8,18,9,17),(16,10,17,9),(10,16,11,15)))
d[10_5] = Diagram(((12,1,13,2),(2,13,3,14),(14,3,15,4),(4,17,5,18),(8,6,9,5),(6,16,7,15),(16,8,17,7),(18,9,19,10),(10,19,11,20),(20,11,1,12)))
d[10_6] = Diagram(((12,1,13,2),(2,11,3,12),(20,4,1,3),(4,16,5,15),(16,6,17,5),(6,18,7,17),(18,8,19,7),(8,20,9,19),(14,10,15,9),(10,14,11,13)))
d[10_7] = Diagram(((1,12,2,13),(11,2,12,3),(3,15,4,14),(19,5,20,4),(5,19,6,18),(17,7,18,6),(7,17,8,16),(15,9,16,8),(9,1,10,20),(13,11,14,10)))
d[10_8] = Diagram(((1,12,2,13),(11,2,12,3),(3,10,4,11),(19,5,20,4),(5,15,6,14),(15,7,16,6),(7,17,8,16),(17,9,18,8),(9,19,10,18),(13,20,14,1)))
d[10_9] = Diagram(((1,13,2,12),(7,3,8,2),(3,16,4,17),(13,4,14,5),(5,14,6,15),(15,6,16,7),(17,9,18,8),(9,19,10,18),(19,11,20,10),(11,1,12,20)))
d[10_10] = Diagram(((1,11,2,10),(11,3,12,2),(3,18,4,19),(17,4,18,5),(5,16,6,17),(15,6,16,7),(7,14,8,15),(19,8,20,9),(9,13,10,12),(13,20,14,1)))
d[10_11] = Diagram(((6,2,7,1),(2,15,3,16),(14,3,15,4),(4,13,5,14),(12,5,13,6),(20,8,1,7),(8,18,9,17),(18,10,19,9),(10,20,11,19),(16,12,17,11)))
d[10_12] = Diagram(((10,1,11,2),(2,11,3,12),(16,4,17,3),(4,18,5,17),(14,5,15,6),(6,13,7,14),(12,7,13,8),(8,19,9,20),(20,9,1,10),(18,16,19,15)))
d[10_13] = Diagram(((8,2,9,1),(2,17,3,18),(16,3,17,4),(4,8,5,7),(14,5,15,6),(6,13,7,14),(20,10,1,9),(10,20,11,19),(18,12,19,11),(12,16,13,15)))
d[10_14] = Diagram(((1,14,2,15),(13,2,14,3),(3,17,4,16),(11,5,12,4),(5,11,6,10),(17,7,18,6),(7,19,8,18),(19,9,20,8),(9,1,10,20),(15,13,16,12)))
d[10_15] = Diagram(((6,2,7,1),(2,6,3,5),(14,4,15,3),(4,16,5,15),(12,7,13,8),(8,17,9,18),(18,9,19,10),(10,19,11,20),(20,11,1,12),(16,14,17,13)))
d[10_16] = Diagram(((1,10,2,11),(9,2,10,3),(3,15,4,14),(17,5,18,4),(5,17,6,16),(15,7,16,6),(7,19,8,18),(13,9,14,8),(11,20,12,1),(19,12,20,13)))
d[10_17] = Diagram(((6,2,7,1),(2,12,3,11),(12,4,13,3),(4,14,5,13),(14,6,15,5),(16,7,17,8),(8,17,9,18),(18,9,19,10),(10,19,11,20),(20,15,1,16)))
d[10_18] = Diagram(((12,2,13,1),(2,14,3,13),(20,4,1,3),(4,10,5,9),(18,5,19,6),(6,17,7,18),(16,7,17,8),(8,15,9,16),(10,20,11,19),(14,12,15,11)))
d[10_19] = Diagram(((1,13,2,12),(13,3,14,2),(3,15,4,14),(19,5,20,4),(5,10,6,11),(17,6,18,7),(7,16,8,17),(15,8,16,9),(9,18,10,19),(11,1,12,20)))
d[10_20] = Diagram(((8,2,9,1),(2,8,3,7),(6,4,7,3),(4,15,5,16),(14,5,15,6),(20,10,1,9),(10,18,11,17),(18,12,19,11),(12,20,13,19),(16,14,17,13)))
d[10_21] = Diagram(((1,15,2,14),(13,3,14,2),(3,13,4,12),(15,5,16,4),(5,17,6,16),(17,7,18,6),(7,11,8,10),(19,8,20,9),(9,18,10,19),(11,1,12,20)))
d[10_22] = Diagram(((10,1,11,2),(2,11,3,12),(18,4,19,3),(4,18,5,17),(14,6,15,5),(6,16,7,15),(16,8,17,7),(8,14,9,13),(20,9,1,10),(12,19,13,20)))
d[10_23] = Diagram(((10,1,11,2),(2,13,3,14),(12,3,13,4),(4,11,5,12),(16,6,17,5),(6,18,7,17),(14,7,15,8),(8,19,9,20),(20,9,1,10),(18,16,19,15)))
d[10_24] = Diagram(((14,2,15,1),(2,14,3,13),(10,4,11,3),(4,10,5,9),(8,6,9,5),(6,17,7,18),(16,7,17,8),(18,12,19,11),(12,20,13,19),(20,16,1,15)))
d[10_25] = Diagram(((1,11,2,10),(15,3,16,2),(3,15,4,14),(11,5,12,4),(5,13,6,12),(13,7,14,6),(7,18,8,19),(17,8,18,9),(9,1,10,20),(19,17,20,16)))
d[10_26] = Diagram(((1,12,2,13),(13,2,14,3),(3,14,4,15),(11,4,12,5),(5,17,6,16),(19,7,20,6),(7,19,8,18),(17,9,18,8),(9,1,10,20),(15,11,16,10)))
d[10_27] = Diagram(((1,11,2,10),(11,3,12,2),(3,18,4,19),(15,4,16,5),(5,16,6,17),(17,6,18,7),(7,14,8,15),(19,8,20,9),(9,13,10,12),(13,20,14,1)))
d[10_28] = Diagram(((1,9,2,8),(9,3,10,2),(3,16,4,17),(15,4,16,5),(5,14,6,15),(17,6,18,7),(7,11,8,10),(11,20,12,1),(19,12,20,13),(13,18,14,19)))
d[10_29] = Diagram(((4,2,5,1),(2,15,3,16),(14,3,15,4),(12,5,13,6),(6,11,7,12),(20,8,1,7),(8,18,9,17),(18,10,19,9),(10,20,11,19),(16,14,17,13)))
d[10_30] = Diagram(((1,14,2,15),(13,2,14,3),(3,17,4,16),(11,5,12,4),(5,11,6,10),(19,7,20,6),(7,19,8,18),(17,9,18,8),(9,1,10,20),(15,13,16,12)))
d[10_31] = Diagram(((6,2,7,1),(2,6,3,5),(14,4,15,3),(4,16,5,15),(12,7,13,8),(8,17,9,18),(20,9,1,10),(10,19,11,20),(18,11,19,12),(16,14,17,13)))
d[10_32] = Diagram(((12,2,13,1),(2,14,3,13),(20,4,1,3),(4,10,5,9),(18,5,19,6),(6,15,7,16),(16,7,17,8),(8,17,9,18),(10,20,11,19),(14,12,15,11)))
d[10_33] = Diagram(((6,2,7,1),(2,14,3,13),(12,4,13,3),(4,12,5,11),(14,6,15,5),(16,7,17,8),(8,19,9,20),(18,9,19,10),(10,17,11,18),(20,15,1,16)))
d[10_34] = Diagram(((1,7,2,6),(7,3,8,2),(3,14,4,15),(15,4,16,5),(5,9,6,8),(9,20,10,1),(19,10,20,11),(11,18,12,19),(17,12,18,13),(13,16,14,17)))
d[10_35] = Diagram(((1,11,2,10),(5,3,6,2),(3,18,4,19),(17,4,18,5),(15,6,16,7),(7,14,8,15),(13,8,14,9),(9,12,10,13),(11,1,12,20),(19,17,20,16)))
d[10_36] = Diagram(((16,1,17,2),(2,15,3,16),(20,4,1,3),(4,14,5,13),(12,6,13,5),(6,12,7,11),(10,8,11,7),(8,18,9,17),(18,10,19,9),(14,20,15,19)))
d[10_37] = Diagram(((4,2,5,1),(2,10,3,9),(10,4,11,3),(16,5,17,6),(6,17,7,18),(12,8,13,7),(8,12,9,11),(20,13,1,14),(14,19,15,20),(18,15,19,16)))
d[10_38] = Diagram(((14,2,15,1),(2,16,3,15),(20,4,1,3),(4,12,5,11),(10,6,11,5),(6,10,7,9),(18,7,19,8),(8,17,9,18),(12,20,13,19),(16,14,17,13)))
d[10_39] = Diagram(((1,14,2,15),(13,2,14,3),(3,17,4,16),(17,5,18,4),(5,19,6,18),(11,7,12,6),(7,11,8,10),(19,9,20,8),(9,1,10,20),(15,13,16,12)))
d[10_40] = Diagram(((10,1,11,2),(2,11,3,12),(16,4,17,3),(4,18,5,17),(14,5,15,6),(6,19,7,20),(20,7,1,8),(8,13,9,14),(12,9,13,10),(18,16,19,15)))
d[10_41] = Diagram(((1,14,2,15),(13,2,14,3),(3,17,4,16),(19,5,20,4),(5,10,6,11),(9,6,10,7),(7,19,8,18),(17,9,18,8),(11,1,12,20),(15,13,16,12)))
d[10_42] = Diagram(((1,9,2,8),(9,3,10,2),(3,18,4,19),(15,4,16,5),(5,14,6,15),(19,6,20,7),(7,11,8,10),(11,20,12,1),(17,13,18,12),(13,17,14,16)))
d[10_43] = Diagram(((4,2,5,1),(2,10,3,9),(10,4,11,3),(16,5,17,6),(6,17,7,18),(14,8,15,7),(8,14,9,13),(20,11,1,12),(12,19,13,20),(18,15,19,16)))
d[10_44] = Diagram(((1,14,2,15),(13,2,14,3),(3,17,4,16),(11,5,12,4),(5,20,6,1),(9,7,10,6),(7,19,8,18),(19,9,20,8),(17,10,18,11),(15,13,16,12)))
d[10_45] = Diagram(((4,2,5,1),(2,11,3,12),(10,3,11,4),(12,6,13,5),(6,19,7,20),(14,7,15,8),(8,18,9,17),(16,10,17,9),(20,14,1,13),(18,15,19,16)))
d[10_46] = Diagram(((1,15,2,14),(15,3,16,2),(3,9,4,8),(9,5,10,4),(5,11,6,10),(17,6,18,7),(7,16,8,17),(11,19,12,18),(19,13,20,12),(13,1,14,20)))
d[10_47] = Diagram(((8,1,9,2),(2,9,3,10),(10,3,11,4),(4,11,5,12),(12,5,13,6),(6,17,7,18),(18,7,19,8),(16,14,17,13),(14,20,15,19),(20,16,1,15)))
d[10_48] = Diagram(((6,2,7,1),(2,8,3,7),(8,4,9,3),(4,14,5,13),(14,6,15,5),(16,9,17,10),(10,17,11,18),(18,11,19,12),(12,19,13,20),(20,15,1,16)))
d[10_49] = Diagram(((1,7,2,6),(7,3,8,2),(3,17,4,16),(15,5,16,4),(5,9,6,8),(9,15,10,14),(17,11,18,10),(11,19,12,18),(19,13,20,12),(13,1,14,20)))
d[10_50] = Diagram(((1,10,2,11),(17,3,18,2),(3,19,4,18),(19,5,20,4),(5,13,6,12),(15,7,16,6),(7,15,8,14),(13,9,14,8),(9,17,10,16),(11,20,12,1)))
d[10_51] = Diagram(((16,2,17,1),(2,18,3,17),(20,4,1,3),(4,11,5,12),(14,5,15,6),(6,13,7,14),(12,7,13,8),(8,15,9,16),(18,9,19,10),(10,19,11,20)))
d[10_52] = Diagram(((1,13,2,12),(17,3,18,2),(3,19,4,18),(19,5,20,4),(5,10,6,11),(15,6,16,7),(7,14,8,15),(13,8,14,9),(9,16,10,17),(11,1,12,20)))
d[10_53] = Diagram(((1,7,2,6),(7,3,8,2),(3,17,4,16),(15,5,16,4),(5,9,6,8),(9,15,10,14),(19,11,20,10),(11,19,12,18),(17,13,18,12),(13,1,14,20)))
d[10_54] = Diagram(((14,2,15,1),(2,16,3,15),(20,4,1,3),(4,9,5,10),(10,5,11,6),(6,11,7,12),(18,7,19,8),(8,19,9,20),(12,18,13,17),(16,14,17,13)))
d[10_55] = Diagram(((8,2,9,1),(2,10,3,9),(18,4,19,3),(4,18,5,17),(12,6,13,5),(6,12,7,11),(10,8,11,7),(16,14,17,13),(14,20,15,19),(20,16,1,15)))
d[10_56] = Diagram(((14,2,15,1),(2,16,3,15),(20,4,1,3),(4,10,5,9),(10,6,11,5),(6,12,7,11),(18,7,19,8),(8,17,9,18),(12,20,13,19),(16,14,17,13)))
d[10_57] = Diagram(((1,4,2,5),(15,2,16,3),(3,16,4,17),(5,20,6,1),(9,7,10,6),(7,13,8,12),(13,9,14,8),(17,10,18,11),(11,18,12,19),(19,14,20,15)))
d[10_58] = Diagram(((16,1,17,2),(2,15,3,16),(20,4,1,3),(4,10,5,9),(8,6,9,5),(6,13,7,14),(12,7,13,8),(10,20,11,19),(18,12,19,11),(14,18,15,17)))
d[10_59] = Diagram(((1,4,2,5),(17,3,18,2),(3,17,4,16),(5,20,6,1),(9,7,10,6),(7,14,8,15),(13,8,14,9),(15,11,16,10),(11,19,12,18),(19,13,20,12)))
d[10_60] = Diagram(((16,1,17,2),(2,15,3,16),(20,4,1,3),(4,8,5,7),(12,5,13,6),(6,11,7,12),(8,14,9,13),(18,9,19,10),(10,17,11,18),(14,20,15,19)))
d[10_61] = Diagram(((1,9,2,8),(9,3,10,2),(3,16,4,17),(15,4,16,5),(5,14,6,15),(13,6,14,7),(7,1,8,20),(17,11,18,10),(11,19,12,18),(19,13,20,12)))
d[10_62] = Diagram(((10,1,11,2),(2,11,3,12),(16,4,17,3),(4,18,5,17),(12,5,13,6),(6,13,7,14),(14,7,15,8),(8,19,9,20),(20,9,1,10),(18,16,19,15)))
d[10_63] = Diagram(((1,9,2,8),(9,3,10,2),(3,19,4,18),(17,5,18,4),(5,17,6,16),(15,7,16,6),(7,11,8,10),(11,15,12,14),(19,13,20,12),(13,1,14,20)))
d[10_64] = Diagram(((10,1,11,2),(2,11,3,12),(16,4,17,3),(4,18,5,17),(18,6,19,5),(6,14,7,13),(14,8,15,7),(8,16,9,15),(20,9,1,10),(12,19,13,20)))
d[10_65] = Diagram(((1,9,2,8),(9,3,10,2),(3,16,4,17),(15,4,16,5),(5,14,6,15),(17,6,18,7),(7,11,8,10),(11,18,12,19),(19,12,20,13),(13,20,14,1)))
d[10_66] = Diagram(((1,11,2,10),(11,3,12,2),(3,13,4,12),(9,5,10,4),(5,19,6,18),(19,7,20,6),(7,15,8,14),(15,9,16,8),(13,17,14,16),(17,1,18,20)))
d[10_67] = Diagram(((1,14,2,15),(13,2,14,3),(3,19,4,18),(17,5,18,4),(5,17,6,16),(11,7,12,6),(7,11,8,10),(19,9,20,8),(9,1,10,20),(15,13,16,12)))
d[10_68] = Diagram(((1,11,2,10),(11,3,12,2),(3,16,4,17),(15,4,16,5),(5,14,6,15),(19,6,20,7),(7,18,8,19),(17,8,18,9),(9,13,10,12),(13,20,14,1)))
d[10_69] = Diagram(((6,2,7,1),(2,13,3,14),(12,3,13,4),(4,17,5,18),(16,5,17,6),(10,7,11,8),(8,19,9,20),(20,9,1,10),(14,12,15,11),(18,16,19,15)))
d[10_70] = Diagram(((16,1,17,2),(2,15,3,16),(20,4,1,3),(4,11,5,12),(12,5,13,6),(6,13,7,14),(10,7,11,8),(8,20,9,19),(18,10,19,9),(14,18,15,17)))
d[10_71] = Diagram(((1,4,2,5),(7,2,8,3),(3,8,4,9),(5,13,6,12),(13,7,14,6),(9,19,10,18),(17,11,18,10),(11,15,12,14),(15,20,16,1),(19,16,20,17)))
d[10_72] = Diagram(((16,1,17,2),(2,15,3,16),(20,4,1,3),(4,12,5,11),(12,6,13,5),(6,14,7,13),(10,8,11,7),(8,18,9,17),(18,10,19,9),(14,20,15,19)))
d[10_73] = Diagram(((16,1,17,2),(2,15,3,16),(20,4,1,3),(4,7,5,8),(12,5,13,6),(6,13,7,14),(8,12,9,11),(18,9,19,10),(10,17,11,18),(14,20,15,19)))
d[10_74] = Diagram(((1,12,2,13),(11,2,12,3),(3,15,4,14),(17,5,18,4),(5,17,6,16),(15,7,16,6),(7,1,8,20),(19,9,20,8),(9,19,10,18),(13,11,14,10)))
d[10_75] = Diagram(((1,14,2,15),(13,2,14,3),(3,17,4,16),(7,5,8,4),(5,18,6,19),(17,6,18,7),(11,9,12,8),(9,20,10,1),(19,10,20,11),(15,13,16,12)))
d[10_76] = Diagram(((12,1,13,2),(2,11,3,12),(20,4,1,3),(4,18,5,17),(18,6,19,5),(6,20,7,19),(16,8,17,7),(8,14,9,13),(14,10,15,9),(10,16,11,15)))
d[10_77] = Diagram(((1,7,2,6),(7,3,8,2),(3,14,4,15),(15,4,16,5),(5,9,6,8),(9,18,10,19),(19,10,20,11),(11,20,12,1),(17,12,18,13),(13,16,14,17)))
d[10_78] = Diagram(((1,7,2,6),(7,3,8,2),(3,17,4,16),(15,5,16,4),(5,9,6,8),(9,13,10,12),(19,11,20,10),(11,1,12,20),(13,18,14,19),(17,14,18,15)))
d[10_79] = Diagram(((6,2,7,1),(2,8,3,7),(8,4,9,3),(4,12,5,11),(12,6,13,5),(16,9,17,10),(10,17,11,18),(18,13,19,14),(14,19,15,20),(20,15,1,16)))
d[10_80] = Diagram(((1,17,2,16),(17,3,18,2),(3,11,4,10),(9,5,10,4),(5,19,6,18),(19,7,20,6),(7,13,8,12),(13,9,14,8),(11,15,12,14),(15,1,16,20)))
d[10_81] = Diagram(((4,2,5,1),(2,8,3,7),(8,4,9,3),(12,6,13,5),(6,12,7,11),(16,9,17,10),(10,15,11,16),(18,13,19,14),(14,19,15,20),(20,17,1,18)))
d[10_82] = Diagram(((1,12,2,13),(9,2,10,3),(3,15,4,14),(17,5,18,4),(5,19,6,18),(19,7,20,6),(7,1,8,20),(13,9,14,8),(15,10,16,11),(11,16,12,17)))
d[10_83] = Diagram(((6,1,7,2),(2,7,3,8),(16,3,17,4),(4,10,5,9),(14,6,15,5),(8,16,9,15),(10,17,11,18),(20,11,1,12),(12,19,13,20),(18,13,19,14)))
d[10_84] = Diagram(((4,2,5,1),(2,10,3,9),(10,4,11,3),(18,6,19,5),(6,13,7,14),(16,7,17,8),(8,12,9,11),(12,17,13,18),(14,20,15,19),(20,16,1,15)))
d[10_85] = Diagram(((6,1,7,2),(2,7,3,8),(16,3,17,4),(4,10,5,9),(14,6,15,5),(8,16,9,15),(10,17,11,18),(18,11,19,12),(12,19,13,20),(20,13,1,14)))
d[10_86] = Diagram(((6,1,7,2),(2,7,3,8),(14,4,15,3),(4,10,5,9),(16,5,17,6),(8,15,9,16),(10,18,11,17),(20,12,1,11),(12,20,13,19),(18,14,19,13)))
d[10_87] = Diagram(((6,1,7,2),(2,11,3,12),(18,4,19,3),(4,14,5,13),(20,5,1,6),(10,8,11,7),(8,16,9,15),(16,10,17,9),(12,19,13,20),(14,18,15,17)))
d[10_88] = Diagram(((4,2,5,1),(2,9,3,10),(8,3,9,4),(12,6,13,5),(6,19,7,20),(14,7,15,8),(10,18,11,17),(16,12,17,11),(20,14,1,13),(18,15,19,16)))
d[10_89] = Diagram(((8,1,9,2),(2,7,3,8),(20,4,1,3),(4,13,5,14),(18,5,19,6),(6,12,7,11),(16,9,17,10),(10,15,11,16),(12,19,13,20),(14,18,15,17)))
d[10_90] = Diagram(((14,1,15,2),(2,9,3,10),(10,3,11,4),(4,13,5,14),(20,6,1,5),(6,20,7,19),(18,8,19,7),(8,16,9,15),(16,12,17,11),(12,18,13,17)))
d[10_91] = Diagram(((6,2,7,1),(2,18,3,17),(10,3,11,4),(4,13,5,14),(20,6,1,5),(14,7,15,8),(8,15,9,16),(16,9,17,10),(18,12,19,11),(12,20,13,19)))
d[10_92] = Diagram(((1,9,2,8),(9,3,10,2),(3,19,4,18),(13,4,14,5),(5,12,6,13),(17,7,18,6),(7,11,8,10),(11,17,12,16),(19,15,20,14),(15,1,16,20)))
d[10_93] = Diagram(((16,1,17,2),(2,17,3,18),(12,4,13,3),(4,12,5,11),(10,6,11,5),(6,20,7,19),(14,7,15,8),(8,15,9,16),(20,10,1,9),(18,13,19,14)))
d[10_94] = Diagram(((1,9,2,8),(15,2,16,3),(3,10,4,11),(11,4,12,5),(5,14,6,15),(19,7,20,6),(7,1,8,20),(9,17,10,16),(17,13,18,12),(13,19,14,18)))
d[10_95] = Diagram(((14,2,15,1),(2,16,3,15),(20,4,1,3),(4,11,5,12),(18,5,19,6),(6,17,7,18),(12,7,13,8),(8,13,9,14),(16,9,17,10),(10,19,11,20)))
d[10_96] = Diagram(((1,16,2,17),(15,2,16,3),(3,10,4,11),(9,4,10,5),(5,1,6,20),(13,6,14,7),(7,12,8,13),(19,9,20,8),(11,19,12,18),(17,15,18,14)))
d[10_97] = Diagram(((14,2,15,1),(2,12,3,11),(18,4,19,3),(4,18,5,17),(8,6,9,5),(6,13,7,14),(12,7,13,8),(16,10,17,9),(10,20,11,19),(20,16,1,15)))
d[10_98] = Diagram(((1,10,2,11),(15,3,16,2),(3,17,4,16),(19,5,20,4),(5,13,6,12),(13,7,14,6),(7,19,8,18),(17,9,18,8),(9,15,10,14),(11,20,12,1)))
d[10_99] = Diagram(((6,2,7,1),(2,10,3,9),(10,4,11,3),(4,18,5,17),(18,6,19,5),(14,7,15,8),(8,15,9,16),(16,11,17,12),(12,19,13,20),(20,13,1,14)))
d[10_100] = Diagram(((8,1,9,2),(2,9,3,10),(16,3,17,4),(4,17,5,18),(18,5,19,6),(6,12,7,11),(14,8,15,7),(10,16,11,15),(12,19,13,20),(20,13,1,14)))
d[10_101] = Diagram(((12,2,13,1),(2,12,3,11),(16,4,17,3),(4,18,5,17),(10,6,11,5),(6,14,7,13),(20,8,1,7),(8,20,9,19),(14,10,15,9),(18,16,19,15)))
d[10_102] = Diagram(((14,1,15,2),(2,9,3,10),(18,4,19,3),(4,12,5,11),(12,6,13,5),(6,18,7,17),(16,8,17,7),(8,16,9,15),(10,19,11,20),(20,13,1,14)))
d[10_103] = Diagram(((8,1,9,2),(2,9,3,10),(18,3,19,4),(4,17,5,18),(16,5,17,6),(6,12,7,11),(14,8,15,7),(10,16,11,15),(12,19,13,20),(20,13,1,14)))
d[10_104] = Diagram(((6,2,7,1),(2,16,3,15),(16,4,17,3),(4,12,5,11),(12,6,13,5),(14,7,15,8),(8,17,9,18),(18,9,19,10),(10,19,11,20),(20,13,1,14)))
d[10_105] = Diagram(((1,11,2,10),(11,3,12,2),(3,16,4,17),(15,4,16,5),(5,1,6,20),(13,7,14,6),(7,18,8,19),(17,8,18,9),(9,13,10,12),(19,15,20,14)))
d[10_106] = Diagram(((1,15,2,14),(9,2,10,3),(3,10,4,11),(15,5,16,4),(5,17,6,16),(17,7,18,6),(7,13,8,12),(19,8,20,9),(11,18,12,19),(13,1,14,20)))
d[10_107] = Diagram(((1,11,2,10),(11,3,12,2),(3,16,4,17),(15,4,16,5),(5,1,6,20),(19,7,20,6),(7,14,8,15),(17,8,18,9),(9,13,10,12),(13,18,14,19)))
d[10_108] = Diagram(((1,15,2,14),(9,3,10,2),(3,11,4,10),(19,5,20,4),(5,12,6,13),(17,6,18,7),(7,16,8,17),(15,8,16,9),(11,18,12,19),(13,1,14,20)))
d[10_109] = Diagram(((6,2,7,1),(2,10,3,9),(10,4,11,3),(4,14,5,13),(14,6,15,5),(16,7,17,8),(8,17,9,18),(18,11,19,12),(12,19,13,20),(20,15,1,16)))
d[10_110] = Diagram(((1,14,2,15),(13,2,14,3),(3,10,4,11),(9,4,10,5),(5,1,6,20),(15,7,16,6),(7,17,8,16),(19,9,20,8),(11,19,12,18),(17,13,18,12)))
d[10_111] = Diagram(((1,9,2,8),(9,3,10,2),(3,19,4,18),(17,5,18,4),(5,11,6,10),(15,6,16,7),(7,14,8,15),(11,17,12,16),(19,13,20,12),(13,1,14,20)))
d[10_112] = Diagram(((14,1,15,2),(2,10,3,9),(16,4,17,3),(4,11,5,12),(18,5,19,6),(6,19,7,20),(20,7,1,8),(8,14,9,13),(10,15,11,16),(12,18,13,17)))
d[10_113] = Diagram(((10,2,11,1),(2,8,3,7),(18,4,19,3),(4,14,5,13),(20,5,1,6),(6,11,7,12),(8,16,9,15),(16,10,17,9),(12,19,13,20),(14,18,15,17)))
d[10_114] = Diagram(((1,8,2,9),(17,2,18,3),(3,11,4,10),(19,5,20,4),(5,14,6,15),(13,6,14,7),(7,12,8,13),(9,17,10,16),(11,18,12,19),(15,1,16,20)))
d[10_115] = Diagram(((6,2,7,1),(2,14,3,13),(10,4,11,3),(4,10,5,9),(14,6,15,5),(16,7,17,8),(8,19,9,20),(18,11,19,12),(12,17,13,18),(20,15,1,16)))
d[10_116] = Diagram(((8,1,9,2),(2,16,3,15),(10,4,11,3),(4,17,5,18),(18,5,19,6),(6,12,7,11),(14,8,15,7),(16,9,17,10),(12,19,13,20),(20,13,1,14)))
d[10_117] = Diagram(((1,14,2,15),(15,2,16,3),(3,8,4,9),(11,4,12,5),(5,18,6,19),(13,7,14,6),(7,17,8,16),(9,20,10,1),(19,10,20,11),(17,13,18,12)))
d[10_118] = Diagram(((6,2,7,1),(2,16,3,15),(8,3,9,4),(4,11,5,12),(18,6,19,5),(14,7,15,8),(16,10,17,9),(10,18,11,17),(12,19,13,20),(20,13,1,14)))
d[10_119] = Diagram(((1,16,2,17),(7,2,8,3),(3,10,4,11),(13,4,14,5),(5,1,6,20),(17,7,18,6),(15,8,16,9),(9,14,10,15),(11,19,12,18),(19,13,20,12)))
d[10_120] = Diagram(((16,2,17,1),(2,10,3,9),(8,4,9,3),(4,18,5,17),(20,6,1,5),(6,12,7,11),(14,8,15,7),(10,16,11,15),(12,20,13,19),(18,14,19,13)))
d[10_121] = Diagram(((6,2,7,1),(2,11,3,12),(16,3,17,4),(4,10,5,9),(18,6,19,5),(12,8,13,7),(8,16,9,15),(10,17,11,18),(20,14,1,13),(14,20,15,19)))
d[10_122] = Diagram(((1,8,2,9),(15,2,16,3),(3,11,4,10),(19,5,20,4),(5,12,6,13),(17,6,18,7),(7,16,8,17),(9,15,10,14),(11,18,12,19),(13,1,14,20)))
d[10_123] = Diagram(((8,2,9,1),(2,15,3,16),(10,3,11,4),(4,18,5,17),(12,6,13,5),(6,19,7,20),(14,7,15,8),(16,10,17,9),(18,11,19,12),(20,14,1,13)))
d[10_124] = Diagram(((1,9,2,8),(9,3,10,2),(3,11,4,10),(11,5,12,4),(5,13,6,12),(17,7,18,6),(7,19,8,18),(16,14,17,13),(14,20,15,19),(20,16,1,15)))
d[10_125] = Diagram(((1,5,2,4),(7,3,8,2),(3,9,4,8),(5,15,6,14),(13,7,14,6),(16,9,17,10),(10,17,11,18),(18,11,19,12),(12,19,13,20),(20,15,1,16)))
d[10_126] = Diagram(((1,7,2,6),(7,3,8,2),(16,3,17,4),(4,15,5,16),(5,9,6,8),(14,9,15,10),(10,17,11,18),(18,11,19,12),(12,19,13,20),(20,13,1,14)))
d[10_127] = Diagram(((1,7,2,6),(7,3,8,2),(16,3,17,4),(4,15,5,16),(5,9,6,8),(9,15,10,14),(17,11,18,10),(11,19,12,18),(19,13,20,12),(13,1,14,20)))
d[10_128] = Diagram(((1,9,2,8),(11,3,12,2),(3,11,4,10),(9,5,10,4),(5,13,6,12),(17,7,18,6),(7,19,8,18),(16,14,17,13),(14,20,15,19),(20,16,1,15)))
d[10_129] = Diagram(((1,7,2,6),(7,3,8,2),(3,17,4,16),(15,5,16,4),(5,9,6,8),(14,9,15,10),(10,19,11,20),(18,11,19,12),(12,17,13,18),(20,13,1,14)))
d[10_130] = Diagram(((1,7,2,6),(7,3,8,2),(16,3,17,4),(4,15,5,16),(5,9,6,8),(14,9,15,10),(10,19,11,20),(18,11,19,12),(12,17,13,18),(20,13,1,14)))
d[10_131] = Diagram(((1,7,2,6),(7,3,8,2),(16,3,17,4),(4,15,5,16),(5,9,6,8),(9,15,10,14),(19,11,20,10),(11,19,12,18),(17,13,18,12),(13,1,14,20)))
d[10_132] = Diagram(((1,8,2,9),(9,2,10,3),(3,18,4,19),(17,4,18,5),(5,12,6,13),(11,6,12,7),(7,10,8,11),(16,14,17,13),(14,20,15,19),(20,16,1,15)))
d[10_133] = Diagram(((4,2,5,1),(2,16,3,15),(16,4,17,3),(20,6,1,5),(9,7,10,6),(7,13,8,12),(13,9,14,8),(17,10,18,11),(11,18,12,19),(14,20,15,19)))
d[10_134] = Diagram(((4,2,5,1),(2,16,3,15),(16,4,17,3),(20,6,1,5),(9,7,10,6),(7,13,8,12),(13,9,14,8),(10,18,11,17),(18,12,19,11),(14,20,15,19)))
d[10_135] = Diagram(((1,4,2,5),(15,2,16,3),(3,16,4,17),(5,20,6,1),(9,7,10,6),(7,13,8,12),(13,9,14,8),(10,18,11,17),(18,12,19,11),(19,14,20,15)))
d[10_136] = Diagram(((4,2,5,1),(2,17,3,18),(16,3,17,4),(20,6,1,5),(9,7,10,6),(7,14,8,15),(13,8,14,9),(15,11,16,10),(18,11,19,12),(12,19,13,20)))
d[10_137] = Diagram(((1,15,2,14),(13,3,14,2),(18,4,19,3),(4,8,5,7),(20,5,1,6),(6,19,7,20),(11,8,12,9),(9,17,10,16),(15,11,16,10),(17,12,18,13)))
d[10_138] = Diagram(((1,15,2,14),(13,3,14,2),(18,4,19,3),(4,8,5,7),(20,5,1,6),(6,19,7,20),(8,12,9,11),(16,9,17,10),(10,15,11,16),(12,18,13,17)))
d[10_139] = Diagram(((1,11,2,10),(11,3,12,2),(16,4,17,3),(4,18,5,17),(5,13,6,12),(13,7,14,6),(7,15,8,14),(19,9,20,8),(9,1,10,20),(18,16,19,15)))
d[10_140] = Diagram(((1,15,2,14),(19,3,20,2),(3,10,4,11),(11,4,12,5),(5,12,6,13),(6,18,7,17),(16,8,17,7),(8,16,9,15),(18,10,19,9),(13,1,14,20)))
d[10_141] = Diagram(((10,1,11,2),(2,11,3,12),(12,3,13,4),(4,9,5,10),(5,19,6,18),(19,7,20,6),(7,15,8,14),(15,9,16,8),(13,17,14,16),(17,1,18,20)))
d[10_142] = Diagram(((1,15,2,14),(19,3,20,2),(10,4,11,3),(4,12,5,11),(12,6,13,5),(6,18,7,17),(16,8,17,7),(8,16,9,15),(18,10,19,9),(13,1,14,20)))
d[10_143] = Diagram(((10,1,11,2),(2,11,3,12),(12,3,13,4),(4,9,5,10),(18,5,19,6),(6,19,7,20),(7,15,8,14),(15,9,16,8),(13,17,14,16),(20,17,1,18)))
d[10_144] = Diagram(((1,9,2,8),(9,3,10,2),(3,16,4,17),(15,4,16,5),(5,14,6,15),(17,6,18,7),(7,11,8,10),(18,12,19,11),(12,20,13,19),(20,14,1,13)))
d[10_145] = Diagram(((1,14,2,15),(11,2,12,3),(3,18,4,19),(17,4,18,5),(8,6,9,5),(6,13,7,14),(12,7,13,8),(9,16,10,17),(19,10,20,11),(15,20,16,1)))
d[10_146] = Diagram(((1,14,2,15),(19,3,20,2),(10,4,11,3),(4,10,5,9),(18,5,19,6),(6,14,7,13),(12,8,13,7),(8,17,9,18),(16,11,17,12),(15,20,16,1)))
d[10_147] = Diagram(((10,2,11,1),(2,8,3,7),(3,18,4,19),(13,4,14,5),(20,5,1,6),(6,11,7,12),(8,16,9,15),(16,10,17,9),(19,13,20,12),(14,18,15,17)))
d[10_148] = Diagram(((16,1,17,2),(2,17,3,18),(10,3,11,4),(4,9,5,10),(18,5,19,6),(6,19,7,20),(7,13,8,12),(13,9,14,8),(11,15,12,14),(20,15,1,16)))
d[10_149] = Diagram(((1,17,2,16),(17,3,18,2),(10,3,11,4),(4,9,5,10),(5,19,6,18),(19,7,20,6),(7,13,8,12),(13,9,14,8),(11,15,12,14),(15,1,16,20)))
d[10_150] = Diagram(((1,17,2,16),(15,3,16,2),(3,7,4,6),(19,5,20,4),(5,1,6,20),(10,8,11,7),(8,14,9,13),(14,10,15,9),(11,18,12,19),(17,12,18,13)))
d[10_151] = Diagram(((16,1,17,2),(2,15,3,16),(6,3,7,4),(4,19,5,20),(20,5,1,6),(10,8,11,7),(8,14,9,13),(14,10,15,9),(11,18,12,19),(17,12,18,13)))
d[10_152] = Diagram(((1,7,2,6),(7,3,8,2),(3,9,4,8),(17,5,18,4),(5,19,6,18),(14,10,15,9),(10,16,11,15),(16,12,17,11),(12,20,13,19),(20,14,1,13)))
d[10_153] = Diagram(((16,1,17,2),(2,17,3,18),(3,11,4,10),(9,5,10,4),(18,5,19,6),(6,19,7,20),(7,13,8,12),(13,9,14,8),(11,15,12,14),(20,15,1,16)))
d[10_154] = Diagram(((1,17,2,16),(15,3,16,2),(3,7,4,6),(19,5,20,4),(5,1,6,20),(10,8,11,7),(8,14,9,13),(14,10,15,9),(18,12,19,11),(12,18,13,17)))
d[10_155] = Diagram(((1,11,2,10),(11,3,12,2),(3,13,4,12),(17,4,18,5),(5,14,6,15),(6,19,7,20),(20,7,1,8),(15,8,16,9),(9,16,10,17),(13,19,14,18)))
d[10_156] = Diagram(((1,13,2,12),(19,3,20,2),(3,8,4,9),(17,4,18,5),(5,14,6,15),(13,6,14,7),(7,18,8,19),(16,9,17,10),(10,15,11,16),(11,1,12,20)))
d[10_157] = Diagram(((14,1,15,2),(2,8,3,7),(3,10,4,11),(11,4,12,5),(5,18,6,19),(19,6,20,7),(8,15,9,16),(16,9,17,10),(17,13,18,12),(20,13,1,14)))
d[10_158] = Diagram(((14,1,15,2),(17,3,18,2),(3,9,4,8),(4,11,5,12),(12,5,13,6),(6,20,7,19),(18,8,19,7),(9,17,10,16),(15,11,16,10),(20,13,1,14)))
d[10_159] = Diagram(((14,1,15,2),(2,10,3,9),(16,4,17,3),(4,11,5,12),(5,19,6,18),(19,7,20,6),(7,1,8,20),(8,14,9,13),(10,15,11,16),(12,18,13,17)))
d[10_160] = Diagram(((1,13,2,12),(19,3,20,2),(8,4,9,3),(4,18,5,17),(14,6,15,5),(6,14,7,13),(18,8,19,7),(16,9,17,10),(10,15,11,16),(11,1,12,20)))
d[10_161] = Diagram(((1,13,2,12),(19,3,20,2),(8,4,9,3),(4,18,5,17),(14,6,15,5),(6,14,7,13),(18,8,19,7),(9,17,10,16),(15,11,16,10),(11,1,12,20)))
d[10_162] = Diagram(((14,1,15,2),(2,9,3,10),(18,4,19,3),(11,4,12,5),(5,12,6,13),(6,18,7,17),(16,8,17,7),(8,16,9,15),(10,19,11,20),(20,13,1,14)))
d[10_163] = Diagram(((1,8,2,9),(17,2,18,3),(3,11,4,10),(19,5,20,4),(14,6,15,5),(6,14,7,13),(12,8,13,7),(9,17,10,16),(11,18,12,19),(15,1,16,20)))
d[10_164] = Diagram(((12,2,13,1),(2,12,3,11),(3,16,4,17),(9,5,10,4),(18,5,19,6),(6,14,7,13),(20,8,1,7),(8,15,9,16),(17,10,18,11),(14,19,15,20)))
d[10_165] = Diagram(((1,8,2,9),(7,2,8,3),(3,12,4,13),(4,17,5,18),(18,5,19,6),(13,6,14,7),(9,14,10,15),(19,11,20,10),(11,17,12,16),(15,20,16,1)))

t2 = {}
t2[3] = Diagram(((1,5,2,4),(5,3,6,2),(3,1,4,6)))
t2[5] = Diagram(((1,6,2,7),(7,2,8,3),(3,8,4,9),(9,4,10,5),(5,10,6,1)))
t2[7] = Diagram(((1,8,2,9),(9,2,10,3),(3,10,4,11),(11,4,12,5),(5,12,6,13),(13,6,14,7),(7,14,8,1)))
t2[9] = Diagram(((1,10,2,11),(11,2,12,3),(3,12,4,13),(13,4,14,5),(5,14,6,15),(15,6,16,7),(7,16,8,17),(17,8,18,9),(9,18,10,1)))
t2[11] = Diagram(((12,2,13,1),(2,14,3,13),(14,4,15,3),(4,16,5,15),(16,6,17,5),(6,18,7,17),(18,8,19,7),(8,20,9,19),(20,10,21,9),(10,22,11,21),(22,12,1,11)))
t2[13] = Diagram(((1,15,2,14),(15,3,16,2),(3,17,4,16),(17,5,18,4),(5,19,6,18),(19,7,20,6),(7,21,8,20),(21,9,22,8),(9,23,10,22),(23,11,24,10),(11,25,12,24),(25,13,26,12),(13,1,14,26)))
t2[15] = Diagram(((1,17,2,16),(17,3,18,2),(3,19,4,18),(19,5,20,4),(5,21,6,20),(21,7,22,6),(7,23,8,22),(23,9,24,8),(9,25,10,24),(25,11,26,10),(11,27,12,26),(27,13,28,12),(13,29,14,28),(29,15,30,14),(15,1,16,30)))
t2[17] = Diagram(((1,19,2,18),(19,3,20,2),(3,21,4,20),(21,5,22,4),(5,23,6,22),(23,7,24,6),(7,25,8,24),(25,9,26,8),(9,27,10,26),(27,11,28,10),(11,29,12,28),(29,13,30,12),(13,31,14,30),(31,15,32,14),(14,33,16,32),(33,17,34,16),(17,1,18,34)))
t2[19] = Diagram(((1,21,2,20),(21,3,22,2),(3,23,4,22),(23,5,24,4),(5,25,6,24),(25,7,26,6),(7,27,8,26),(27,9,28,8),(9,29,10,28),(29,11,30,10),(11,31,12,30),(31,13,32,12),(13,33,14,32),(33,15,34,14),(15,35,16,34),(35,17,36,16),(17,37,18,36),(37,19,38,18),(19,1,20,38)))
t2[21] = Diagram(((1,23,2,22),(23,3,24,2),(3,25,4,24),(25,5,26,4),(5,27,6,26),(27,7,28,6),(7,29,8,28),(29,9,30,8),(9,31,10,30),(31,11,32,10),(11,33,12,32),(33,13,34,12),(13,35,14,34),(35,15,36,14),(15,37,16,36),(37,17,38,16),(17,39,18,38),(39,19,40,18),(19,41,20,40),(41,21,42,20),(21,1,22,42)))
t2[23] = Diagram(((1,25,2,24),(25,3,26,2),(3,27,4,26),(27,5,28,4),(5,29,6,28),(29,7,30,6),(7,31,8,30),(31,9,32,8),(9,33,10,32),(33,11,34,10),(11,35,12,34),(35,13,36,12),(13,37,14,36),(37,15,38,14),(15,39,16,38),(39,17,40,16),(17,41,18,40),(41,19,42,18),(19,43,20,42),(43,21,44,20),(21,45,22,44),(45,23,46,22),(23,1,24,46)))

t3 = {}
t3[4] = Diagram(((1,7,2,6),(13,3,14,2),(8,4,9,3),(4,16,5,15),(5,11,6,10),(12,8,13,7),(9,15,10,14),(16,12,1,11)))
t3[5] = Diagram(((14,2,15,1),(2,10,3,9),(3,17,4,16),(11,5,12,4),(18,6,19,5),(6,14,7,13),(7,1,8,20),(15,9,16,8),(10,18,11,17),(19,13,20,12)))
t3[7] = Diagram(((1,11,2,10),(21,3,22,2),(12,4,13,3),(4,24,5,23),(5,15,6,14),(25,7,26,6),(16,8,17,7),(8,28,9,27),(9,19,10,18),(20,12,21,11),(13,23,14,22),(24,16,25,15),(17,27,18,26),(28,20,1,19)))
t3[8] = Diagram(((22,2,23,1),(2,14,3,13),(3,25,4,24),(15,5,16,4),(26,6,27,5),(6,18,7,17),(7,29,8,28),(19,9,20,8),(30,10,31,9),(10,22,11,21),(11,1,12,32),(23,13,24,12),(14,26,15,25),(27,17,28,16),(18,30,19,29),(31,21,32,20)))
t3[10] = Diagram(((1,29,2,28),(2,16,3,15),(30,4,31,3),(17,5,18,4),(5,33,6,32),(6,20,7,19),(34,8,35,7),(21,9,22,8),(9,37,10,36),(10,24,11,23),(38,12,39,11),(25,13,26,12),(13,1,14,40),(14,28,15,27),(29,17,30,16),(18,32,19,31),(33,21,34,20),(22,36,23,35),(37,25,38,24),(26,40,27,39)))
t3[11] = Diagram(((30,2,31,1),(2,18,3,17),(3,33,4,32),(19,5,20,4),(34,6,35,5),(6,22,7,21),(7,37,8,36),(23,9,24,8),(38,10,39,9),(10,26,11,25),(11,41,12,40),(27,13,28,12),(42,14,43,13),(14,30,15,29),(15,1,16,44),(31,17,32,16),(18,34,19,33),(35,21,36,20),(22,38,23,37),(39,25,40,24),(26,42,27,41),(43,29,44,28)))

t4 = {}
t4[5] = Diagram(((16,2,17,1),(9,3,10,2),(3,27,4,26),(4,20,5,19),(5,13,6,12),(29,7,30,6),(22,8,23,7),(15,9,16,8),(10,26,11,25),(11,19,12,18),(28,14,29,13),(21,15,22,14),(17,25,18,24),(27,21,28,20),(23,1,24,30)))
t4[7] = Diagram(((1,13,2,12),(2,24,3,23),(3,35,4,34),(15,5,16,4),(26,6,27,5),(37,7,38,6),(7,19,8,18),(8,30,9,29),(9,41,10,40),(21,11,22,10),(32,12,33,11),(13,25,14,24),(14,36,15,35),(27,17,28,16),(38,18,39,17),(19,31,20,30),(20,42,21,41),(33,23,34,22),(25,37,26,36),(39,29,40,28),(31,1,32,42)))

def print_torus():
	for key in t2:
		print('T(' + str(key) + ',2) = ' + str(t2[key].diameter()))
	for key in t3:
		print('T(' + str(key) + ',3) = ' + str(t3[key].diameter()))
	for key in t4:
		print('T(' + str(key) + ',4) = ' + str(t4[key].diameter()))
		
def print_all():
	for key in d:
		print(str(key) + ' = ' + str(d[key].diameter()))