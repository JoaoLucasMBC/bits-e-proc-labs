; Faz a soma de RAM[0] com RAM[1]

leaw $R0, %A
movw (%A), %D
leaw $R1, %A
addw (%A), %D, %D
leaw $R2, %A
movw %D, (%A)