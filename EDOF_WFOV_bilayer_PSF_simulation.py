#This script should be used after the correct phase profile of the 2nd lens 
#is determined with the 'EDOF_WFOV_Bilayer_Paraxial_phaseProfileExtraction.py' script
#The script characterizes the Point Spread Function as a point source propagates through the bi-layer to the imaging plane

import csv, time
import numpy as np
import matplotlib.pyplot as plt
from numba import njit,prange

# variables [unit in um]
mm=1e3
wavelength=0.94
k=2*np.pi/wavelength
deg2rad=np.pi/180
pitch=1.4 # resolution of the wavefront
size=1000 # size of the wavefront
N=int(size/pitch)-1
N_middle=N/2
size_lens=2000 # diameter of WFOV metasurface
N_lens=int(size_lens/pitch)-1
N_middle_lens=N_lens/2
eff_f=2000 # focal length of WFOV when object is at infinity
depth_center=5000 #normal distance of EDOF to object
distance=2366 # substrate thickness
n=1.45 # substrate index
focus=1/(1/eff_f-1/(depth_center+distance/n)) #back focal length of WFOV
AOI=0*deg2rad
angle_substrate=np.arcsin(np.sin(AOI)/n)
center=distance*np.tan(angle_substrate)
img_range=1000 # image plane size
img_resolve=1.67 # resolution
img_size=int(img_range/img_resolve)
amp=np.ones((N,N)) # surface amplitude distribution, modify this
#phase=np.zeros((N,N)) # surface phase distribution, modify this
depth=10000

# EDOF phase profile
phase=np.zeros((N,N))
for i in range(N):
    x=(i-N_middle)*pitch
    for j in range(N):
        y=(j-N_middle)*pitch
        phase[i][j]=1000*np.pi/(size**3)*(x**3+y**3)

# lens phase profile
poly=np.array([-1.669279163975940E+003,7.592269753136122E+000,-6.705995305204940E+000,1.303638243779945E+001,-7.390330699017709E+000,2.082710611487795E+000,-3.015150238570076E-001,1.581363311667552E-002,1.238235525927042E-003,-2.028621253800335E-004,7.611795160760097E-006])
N_poly=len(poly)
@njit
def phase_lens_func(r):
    phase=0
    for i in range(N_poly):
        phase+=poly[i]*(r/mm)**(2*(i+1))
    return phase
phase_lens=np.zeros((N_lens,N_lens))
for i in range(N_lens):
    x=(i-N_middle_lens)*pitch+center
    for j in range(N_lens):
        y=(j-N_middle_lens)*pitch
        r=np.sqrt(x**2+y**2)
        phase_lens[i][j]=phase_lens_func(r)
trans_lens=np.exp(1j*phase_lens)

# incident phase
phase_incident=np.zeros((N,N))
for i in range(N):
    x=(i-N_middle)*pitch
    for j in range(N):
        y=(j-N_middle)*pitch
        r = np.sqrt((x + depth * np.sin(AOI)) ** 2 + y ** 2 + (depth * np.cos(AOI)) ** 2)
        phase_incident[i][j] = k * r
        #phase_incident[i][j] = k * x * np.sin(AOI)

phase_EDOF=phase+phase_incident
#phase_DH=phase_incident
trans_EDOF=np.exp(1j*phase_EDOF)

@njit(parallel=True)
# light field at focusing lens
def u1(i_lens,j_lens):
    wave = 0
    x_i = (i_lens-N_middle_lens)*pitch+center
    y_i = (j_lens-N_middle_lens)*pitch
    for i in prange(N):
        x = (i-N_middle) * pitch
        for j in prange(N):
            y=(j-N_middle)*pitch
            xy_f = np.sqrt((x - x_i) ** 2 + (y - y_i) ** 2)
            theta_i = angle_substrate
            theta_f = np.arctan(xy_f / distance)
            r_f = np.sqrt(xy_f ** 2 + distance ** 2)
            wave+=amp[i][j]*trans_EDOF[i][j]*0.5*(np.cos(theta_i)+np.cos(theta_f))*np.exp((0+1j)*k*n*r_f)*pitch**2/((0 + 1j) * wavelength * r_f)
    return wave

start=time.time()
u_lens = np.zeros((N_lens, N_lens)).astype(complex)
for i in prange(N_lens):
    for j in prange(N_lens):
        u_lens[i][j]=u1(i,j)
    end = time.time()
    #print(f'step 1 process: {i+1}/{N_lens}')
    print(f'step 1 remaining time: {(end - start) / (i + 1) * (N_lens - i - 1)} s')

u_lens *= trans_lens


@njit(parallel=True)
# light field at image plane
def u2(x_i,y_i):
    wave = 0
    for i in prange(N_lens):
        x = (i-N_middle_lens) * pitch
        for j in prange(N_lens):
            y=(j-N_middle_lens)*pitch
            xy_i = np.sqrt(x ** 2 + y ** 2)
            xy_f = np.sqrt((x - x_i) ** 2 + (y - y_i) ** 2)
            theta_i = np.arctan(xy_i / focus)
            theta_f = np.arctan(xy_f / focus)
            r_f = np.sqrt(xy_f ** 2 + focus ** 2)
            wave+=u_lens[i][j]*0.5*(np.cos(theta_i)+np.cos(theta_f))*np.exp((0+1j)*k*r_f)*pitch**2/((0 + 1j) * wavelength * r_f)
    return wave

@njit
# intensity at image plane
def intensity(x,y):
    return abs(u2(x,y))**2

start=time.time()

intensity_img=np.zeros((img_size,img_size))
for i in range(img_size):
    x=i*img_resolve-img_range/2-50#+17.473090529568136
    for j in range(img_size):
        y=j*img_resolve-img_range/2
        intensity_img[i][j]=intensity(x,y)
    end = time.time()
    print(f'step 2 remaining time: {(end - start) / (i + 1) * (img_size - i - 1)} s')

# save intensity distribution
with open(f'EDOF_WFOV_1mmPSF_imResolveArducam_depth_{int(depth)}_AOI_{round(AOI/deg2rad)}_20230107.csv', 'w', newline='') as file:
    mywriter = csv.writer(file, delimiter=',')
    mywriter.writerows(intensity_img)

# plot figure
im = plt.imshow(intensity_img, cmap=plt.cm.Greys_r, origin='lower', extent=(-img_range / 2, img_range / 2, -img_range / 2, img_range / 2))
plt.savefig(f'EDOF_WFOV_1mmPSF_imResolveArducam_depth_{int(depth)}_AOI_{round(AOI/deg2rad)}_20230107.png', bbox_inches=0,dpi=300)
plt.close()
