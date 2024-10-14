"""
Created on Mon Mar  4 13:58:58 2024

We consider here two metasurfaces in series (bi-layer metasurfaces), 
typically where the first one has a weakly focusing phase profile and 
the second one has a strongly focusing phase profile.The script adjusts 
the substrate thickness to optimize the parabolic phase profile.
of the second lens and focus at a desired position ('focus'). The two 
curves that the script outputs should align to ensure paraxial design

Input: spacing between the two optical layers
Output:phase profile of the second lens

@author: Louis Martin
"""

import numpy as np
import matplotlib.pyplot as plt

wavelength=0.940;
#wavelength=1.122
deg2rad = np.pi / 180;
angle_resolve_degree=0.001;
angle_resolve=angle_resolve_degree*deg2rad;
angle=[angle_resolve*i for i in range(int(90/angle_resolve_degree)+1)];
N_angle=len(angle)
k = 2 * np.pi / wavelength
subspace = 0.1; # metasurface phase profile radial resolution
integration_resolve=subspace/100;
size = 904;  # size of metasurface, unit um
l_substrate=370; # substrate thickness
n_substrate=1.45; # substrate index
n_f=1.45; # index between metasurface and focal plane
# d_object=1000;#distance to object
# focal_inf=470; # focal length, ie back focal length
#focus = 470;  
#focus= n_f*(((focal_inf/n_f)**(-1)-(d_object+(l_substrate/n_substrate))**(-1))**(-1))#distance to image plane
focus=449;

print("focus")
print(focus)

N_atom = round(size / subspace)  # number of atoms
N_middle = round(N_atom / 2)

s=[]
for i in range(N_angle):
    alpha=angle[i]
    s.append(l_substrate*np.sin(alpha)/np.sqrt(n_substrate**2-np.sin(alpha)**2))

phase=[0 for i in range(N_middle)]
d=[0 for i in range(N_angle)]

d_temp=0
for i in range(N_angle):
    d[i]=d_temp
    alpha=angle[i]
    integral=((s[i]-d_temp)**2+focus**2)**1.5*np.cos(alpha)/focus**2/n_f # equation 2
    d_temp+=integral*angle_resolve

phase_temp=0
i_s_temp=0
for i in range(N_middle):
    for j in range(round(subspace/integration_resolve)):
        if j==0:
            phase[i]=phase_temp
        x=i*subspace+(j+1)*integration_resolve
        for i_s in range(i_s_temp,len(s)):
            if s[i_s]>x:
                break
        i_s_temp=i_s
        alpha=angle[i_s]
        d_temp=d[i_s]
        length_diff=-integration_resolve*(np.sin(alpha)+n_f*(x-d_temp)/np.sqrt(focus**2+(x-d_temp)**2)) # equation 5
        phase_diff=length_diff*2*np.pi/wavelength
        phase_temp+=phase_diff

position_plot=[subspace*i/1e3 for i in range(-N_middle+1,N_middle)]
phase_plot=[0 for i in range(-N_middle+1,N_middle)]
for i in range(-N_middle+1,N_middle):
    if i<0:
        phase_plot[i+N_middle-1]=phase[-i]
    else:
        phase_plot[i+N_middle-1]=phase[i]

position_array=np.array(position_plot)
phase_array=np.array(phase_plot)
poly = np.polyfit(position_array, phase_array, 22)
poly = poly[::-2]
poly = poly[1:]
print(f'metasurface polynomials: {poly}')
