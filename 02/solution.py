mass = {'H': 1.01, 'He': 4.0, 'Li': 6.94, 'Be': 9.01, 'B': 10.81, 'C': 12.01, 'N': 14.01, 'O': 16.0, 'F': 19.0, 'Ne': 20.18, 'Na': 22.99, 'Mg': 24.31, 'Al': 26.98, 'Si': 28.09, 'P': 30.97, 'S': 32.07, 'Cl': 35.45, 'Ar': 39.95, 'K': 39.1, 'Ca': 40.08, 'Sc': 44.96, 'Ti': 47.87, 'V': 50.94, 'Cr': 52.0, 'Mn': 54.94, 'Fe': 55.85, 'Co': 58.93, 'Ni': 58.69, 'Cu': 63.55, 'Zn': 65.39, 'Ga': 69.72, 'Ge': 72.61, 'As': 74.92, 'Se': 78.96, 'Br': 79.9, 'Kr': 83.8, 'Rb': 85.47, 'Sr': 87.62, 'Y': 88.91, 'Zr': 91.22, 'Nb': 92.91, 'Mo': 95.94, 'Tc': 98.0, 'Ru': 101.07, 'Rh': 102.91, 'Pd': 106.42, 'Ag': 107.87, 'Cd': 112.41, 'In': 114.82, 'Sn': 118.71, 'Sb': 121.76, 'Te': 127.6, 'I': 126.9, 'Xe': 131.29, 'Cs': 132.91, 'Ba': 137.33, 'La': 138.91, 'Ce': 140.12, 'Pr': 140.91, 'Nd': 144.24, 'Pm': 145.0, 'Sm': 150.36, 'Eu': 151.96, 'Gd': 157.25, 'Tb': 158.93, 'Dy': 162.5, 'Ho': 164.93, 'Er': 167.26, 'Tm': 168.93, 'Yb': 173.04, 'Lu': 174.97, 'Hf': 178.49, 'Ta': 180.95, 'W': 183.84, 'Re': 186.21, 'Os': 190.23, 'Ir': 192.22, 'Pt': 195.08, 'Au': 196.97, 'Hg': 200.59, 'Tl': 204.38, 'Pb': 207.2, 'Bi': 208.98, 'Po': 209.0, 'At': 210.0, 'Rn': 222.0, 'Fr': 223.0, 'Ra': 226.0, 'Ac': 227.0, 'Th': 232.04, 'Pa': 231.04, 'U': 238.03, 'Np': 237.0, 'Pu': 244.0, 'Am': 243.0, 'Cm': 247.0, 'Bk': 247.0, 'Cf': 251.0, 'Es': 252.0, 'Fm': 257.0, 'Md': 258.0, 'No': 259.0, 'Lr': 262.0, 'Rf': 261.0, 'Db': 262.0, 'Sg': 266.0, 'Bh': 264.0, 'Hs': 269.0, 'Mt': 268.0}

def calcMass(chem):
	m = 0
	i = 0
	br = 0
	n = len(chem)
	while i<n:
		if chem[i]=='(':
			br += 1
			ele = ''
			i += 1
			num = ''
			while br:
				if chem[i]=='(':
					br += 1
				elif chem[i]==')':
					br -= 1
				if br==0:
					i += 1
					break
				ele += chem[i]
				i += 1
			while i<n and chem[i].isdigit():
				num += chem[i]
				i += 1
			if(num):
				m += (calcMass(ele)*int(num))
			else:
				m += calcMass(ele)

		else:
			ele = chem[i]
			i += 1
			num = ''
			while i<n and chem[i].islower():
				ele += chem[i]
				i += 1
			while i<n and chem[i].isdigit():
				num += chem[i]
				i += 1
			if(num):
				m += (mass[ele]*int(num))
			else:
				m += mass[ele]
	return m	
		
chem = input()
m = calcMass(chem)
print(m)
