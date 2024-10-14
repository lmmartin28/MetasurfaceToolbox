import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

deg2rad=np.pi/180
img = mpimg.imread('image_pol1/44.bmp')[:,:,0]
H,W = img.shape
img_fft = np.fft.fftshift(np.fft.fft2(img))

figsize = 12, 9
figure, ax1 = plt.subplots(figsize=figsize)
font = {'family': 'Times New Roman', 'weight': 'normal', 'size': 45}
font2 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 30}
plt.tick_params(labelsize=35,width=4,length=10)
labels = ax1.get_xticklabels() + ax1.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
im = plt.imshow(np.log(abs(img_fft)), cmap='gray', origin='lower',aspect='auto')
plt.savefig(f'image_ft_pol1_20221219.jpg',bbox_inches = 'tight',dpi=300)
plt.close()

#r=63
r=60
#angle_list=np.linspace(0,170,18)
#angle_list=np.linspace(-20,0,11)
angle_list=np.linspace(120,160,5)
N_angle=len(angle_list)
for i_angle in range(N_angle):
    angle = angle_list[i_angle]*deg2rad
    #angle=20*deg2rad
    x=r/2*np.cos(angle)
    y=r/2*np.sin(angle)
    '''
    u=np.linspace(0,H-1,H)
    v=np.linspace(0,W-1,W)
    U,V=np.meshgrid(u,v)
    psf_fft=np.cos(2*np.pi*(x*U+y*V)).T
    '''
    psf=np.zeros((H,W))
    psf[round(H/2+x)][round(W/2+y)]=1
    psf[round(H/2-x)][round(W/2-y)]=1
    psf_fft = np.fft.fftshift(np.fft.fft2(psf))
    snr=0.1
    #snr_list=np.linspace(0.01,0.1,10)
    #N_snr=len(snr_list)
    #for i_snr in range(N_snr):
    #snr=snr_list[i_snr]
    img_dec_fft=img_fft*psf_fft/(psf_fft**2+snr)
    img_dec = np.fft.fftshift(np.fft.fft2(img_dec_fft))
    '''
    figsize = 12, 9
    figure, ax1 = plt.subplots(figsize=figsize)
    font = {'family': 'Times New Roman', 'weight': 'normal', 'size': 45}
    font2 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 30}
    plt.tick_params(labelsize=35,width=4,length=10)
    labels = ax1.get_xticklabels() + ax1.get_yticklabels()
    [label.set_fontname('Times New Roman') for label in labels]
    im = plt.imshow(abs(psf_fft), cmap='gray', origin='lower',aspect='auto')
    plt.savefig(f'psf_ft_20221219.jpg',bbox_inches = 'tight',dpi=300)
    plt.close()
    '''
    '''
    figsize = 12, 9
    figure, ax1 = plt.subplots(figsize=figsize)
    font = {'family': 'Times New Roman', 'weight': 'normal', 'size': 45}
    font2 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 30}
    plt.tick_params(labelsize=35,width=4,length=10)
    labels = ax1.get_xticklabels() + ax1.get_yticklabels()
    [label.set_fontname('Times New Roman') for label in labels]
    im = plt.imshow(abs(img_dec), cmap='gray', origin='lower',aspect='auto')
    plt.savefig(f'image_deconvolution_pol1/image_deconvolution_angle_{round(angle_list[i_angle])}_20221219.jpg',bbox_inches = 'tight',dpi=300)
    #plt.savefig(f'image_deconvolution/image_deconvolution_snr_{snr}_20221219.jpg',bbox_inches='tight', dpi=300)
    plt.close()
    '''
    fig = plt.figure(frameon=False)
    fig.set_size_inches(W,H)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.imshow(abs(img_dec), cmap='gray',aspect='equal')
    fig.savefig(f'image_deconvolution_pol1/image_deconvolution_angle_{round(angle_list[i_angle])}_20221219.png', dpi=1)
    plt.close()

    print(f'process: {i_angle+1}/{N_angle}')
    #print(f'process: {i_snr + 1}/{N_snr}')

deg2rad=np.pi/180
img = mpimg.imread('image_pol2/44.bmp')[:,:,0]
H,W = img.shape
img_fft = np.fft.fftshift(np.fft.fft2(img))

#r=63
r=60
angle_list=90-angle_list
angle_list=np.where(angle_list<0,angle_list+180,angle_list)
N_angle=len(angle_list)
for i_angle in range(N_angle):
    angle = angle_list[i_angle]*deg2rad
    #angle=20*deg2rad
    x=r/2*np.cos(angle)
    y=r/2*np.sin(angle)
    '''
    u=np.linspace(0,H-1,H)
    v=np.linspace(0,W-1,W)
    U,V=np.meshgrid(u,v)
    psf_fft=np.cos(2*np.pi*(x*U+y*V)).T
    '''
    psf=np.zeros((H,W))
    psf[round(H/2+x)][round(W/2+y)]=1
    psf[round(H/2-x)][round(W/2-y)]=1
    psf_fft = np.fft.fftshift(np.fft.fft2(psf))
    snr=0.1
    #snr_list=np.linspace(0.01,0.1,10)
    #N_snr=len(snr_list)
    #for i_snr in range(N_snr):
    #snr=snr_list[i_snr]
    img_dec_fft=img_fft*psf_fft/(psf_fft**2+snr)
    img_dec = np.fft.fftshift(np.fft.fft2(img_dec_fft))

    fig = plt.figure(frameon=False)
    fig.set_size_inches(W,H)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.imshow(abs(img_dec), cmap='gray',aspect='equal')
    fig.savefig(f'image_deconvolution_pol2/image_deconvolution_angle_{round(angle_list[i_angle])}_20221219.png', dpi=1)
    plt.close()

    print(f'process: {i_angle+1}/{N_angle}')
    #print(f'process: {i_snr + 1}/{N_snr}')
