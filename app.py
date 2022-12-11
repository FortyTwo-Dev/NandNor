def OR(A, B):
	return A | B

# def XOR(A, B):
# 	return A ^ B

def AND(A, B):
	return A & B

def NOT(A):
	return ~A+2


def NAND(A, B):
	return NOT(AND(A, B))

print("Pour : 0 NAND 0 on a : ", NAND(False, False)) # 0 0
print("Pour : 0 NAND 1 on a : ", NAND(False, True)) # 0 1
print("Pour : 1 NAND 0 on a : ", NAND(True, False)) # 1 0
print("Pour : 1 NAND 1 on a : ", NAND(True, True)) # 1 1


def NOR(A, B):
	return NOT(OR(A, B))

print("\nPour : 0 NOR 0 on a : ", NOR(False, False)) # 0 0
print("Pour : 0 NOR 1 on a : ", NOR(False, True)) # 0 1
print("Pour : 1 NOR 0 on a : ", NOR(True, False)) # 1 0
print("Pour : 1 NOR 1 on a : ", NOR(True, True)) # 1 1
