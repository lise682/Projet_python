#!/usr/bin/pyhton

from math import *
import numpy as np
import matplotlib.pyplot as plt

#debut fonctions
def produitvectoriel(M,r_vecteur):
	E=np.zeros((3,1))
	E[0]=M[1]*r_vecteur[2]-M[2]*r_vecteur[1]
	E[1]=M[2]*r_vecteur[0]-M[0]*r_vecteur[2]	
	E[2]=M[0]*r_vecteur[1]-M[1]*r_vecteur[0]
	return(E)

def produitscalaire(M,r_vecteur):
	E = M[0]*r_vecteur[0]+M[1]*r_vecteur[1]+M[2]*r_vecteur[2]
	return(E)

#def produits_dun_scalaire_et_dun_vecteur():
#	A=np.array([[1],[2],[3]])
#	scalaire=3
#	B=np.array([[scalaire*A[0]],[scalaire*A[1]],[scalaire*A[2]]])
#	return(B)


#fin fonctions

#programme principal

#constantes
permeabilite_magnetique_vide= 4*pi*10e-7 #en ohm.S.m-1

#debut entrees deja definies
resistivite= 500 #en ohm.m
frequence= 2e3 #en Hz

#dipole magnetique
I= 1 #en A
Surface_boucle= 1 #en m^2
Nb_tours= 1 
M_x=1 #dipole perpendiculaire a l axe x
M_y=0
M_z=0
M=np.array([[M_x],[M_y],[M_z]]) # dim 1*3 moments dipolaire selon x y et z

#grille de points de reception
NX= 6 #nombre de points a afficher sur l axe X
NZ= 6 #nombre de points a afficher sur l axe Z
X_min=0
X_max=50 #en m
Z_min=0
Z_max=50

#position du dipole
TX_x= 50 #en m
TX_z= 50
#fin entrees deja definies

#debut calculs
conductivite=1/resistivite #en S.m^-1
pulsation=2*pi*frequence
profondeur_de_peau=503*(resistivite/frequence)**(0.5) #en m
k_carre=complex(0,-conductivite*pulsation*permeabilite_magnetique_vide)
k=complex(1/profondeur_de_peau,-1/profondeur_de_peau)

pas_x= (X_max-X_min)/(NX-1) #en m
pas_z= (Z_max-Z_min)/(NZ-1) #en m

#fin calculs



#debut boucle
for ZZ in range(0,NZ,1): 	#boucle sur les lignes 
	for XX in range(0,NX,1):	#boucles sur les colonnes  
		#calcul de r la distance a la source 
		if XX*pas_x!= TX_x and ZZ*pas_z!=TX_z : #
			r=((TX_x-XX*pas_x)**2+(TX_z-ZZ*pas_z)**2)**(0.5) #norme
			print('r')
			print(r)
			r_x= TX_x-XX*pas_x #coordonnee x vecteur r
			r_z= TX_z-ZZ*pas_z #coordonnee z vecteur r
			r_vecteur=np.array([[r_x],[0],[r_z]])
			print('r_vecteur')
			print(r_vecteur)
			#calcul du champ magnetique		
			#H_teta
			PV1=produitvectoriel(M,r_vecteur)
			H_teta=produitvectoriel(PV1,r_vecteur)/(4*pi*r**5)*complex(1+r/profondeur_de_peau,r/profondeur_de_peau+pulsation*permeabilite_magnetique_vide*r**3)*complex(cos(-r/profondeur_de_peau),sin(-r/profondeur_de_peau))
			#H_teta_norme=((H_teta[0])**2+(H_teta[2])**2)**(0.5)
			#print('H_teta_norme')
			#print(H_teta_norme)
			#H_r
			H_r=2*produitscalaire(M,r_vecteur)*r_vecteur*complex(1+r/profondeur_de_peau,r/profondeur_de_peau)*complex(cos(-r/profondeur_de_peau),sin(-r/profondeur_de_peau))/(4*pi*r**5)
		
			#H
			H=H_r+H_teta
			#print('H')
			#print(H)
			#H_vecteur_norme=((H[0])**2+(H[2])**2)**0.5 #norme du vecteur H (en complexe)
			#print('H_vecteur_norme')
			#print(H_vecteur_norme)
			if ((H[0].real)**2+(H[0].imag)**2)**0.5 != 0:
				X_log_norme_H=log(((H[0].real)**2+(H[0].imag)**2)**0.5)  #log de l intensite de H selon x
			else :
				X_log_norme_H=0 
			if ((H[2].real)**2+(H[2].imag)**2)**0.5	!=0:	
				Z_log_norme_H=log(((H[2].real)**2+(H[2].imag)**2)**0.5)  #log de l intensite de H selon z
			else :
				Z_log_norme_H=0
			print('log norme')
			print(X_log_norme_H)
			print(Z_log_norme_H)
			
			if ((H[0].real)**2+(H[0].imag)**2)**0.5 != 0:
				if ((H[2].real)**2+(H[2].imag)**2)**0.5	!=0:	                
					log_norme_H=log((((H[0].real)**2+(H[0].imag)**2)**0.5)**2+(((H[2].real)**2+(H[2].imag)**2)**2)**0.5)
			print('log_norme_H')
			print(log_norme_H)
            
		else :
			print('on est en position du dipole')
	#axe_x=np.linspace(,
		
#print(r)
		#print(H_r)
		#print(H)


