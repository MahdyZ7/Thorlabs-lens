import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 1_000_000)
# y = np.sqrt(1 - x**2 / 3.3)
# y = np.sqrt(1 - x**2 / 4.41)
# phase shift
#δ = 2π(n2 - n1)t/λ
# n2 = 1.5168 n1 = 1 λ= 587.6 nm default
# n2 = 1.5131 n1 = 1 λ= 700 nm red
# n2 = 1.5185 n1 = 1 λ= 550 nm green
n_d = 1.5168 - 1
wavlen_d = (587.6 * 10**-9)
y_d = 2 * np.pi * n_d * np.sqrt(1 - x**2 / 3.3) / wavlen_d

n_red = 1.5131 - 1
wavlen_red = (700 * 10**-9)
y_red = 2 * np.pi * n_red * np.sqrt(1 - x**2 / 3.3) / wavlen_red

n_green = 1.5185 - 1
wavlen_green = (550 * 10**-9)
y_green = 2 * np.pi * n_green * np.sqrt(1 - x**2 / 3.3) / wavlen_green

# a phase multiplier is used to avoid diffraction grating instead of 2pi
phase_x = 16384 # 2^14
for i in range(len(y_d)):
	# reduce phase
	y_d[i] = y_d[i] - (phase_x * np.pi * np.floor(y_d[i]/(phase_x * np.pi)))
	y_red[i] = y_red[i] - (phase_x * np.pi * np.floor(y_red[i]/(phase_x * np.pi)))
	y_green[i] = y_green[i] - (phase_x * np.pi * np.floor(y_green[i]/(phase_x * np.pi)))
	# calculate new thicknes
	y_d[i] = y_d[i] * wavlen_d / (2 * np.pi * n_d)
	y_red[i] = y_red[i] * wavlen_red / (2 * np.pi * n_red)
	y_green[i] = y_green[i] * wavlen_green / (2 * np.pi * n_green)

# plt.subplot(x, y_d)
# plt.title('Lens Cross Section')
# plt.xlabel('Radius (r)')
# plt.ylabel('lens hight (mm)')

fig, axs = plt.subplots(3)
fig.suptitle('fresnel lenses (588, 700, 500 nm)')
axs[0].plot(x, y_d)
axs[1].plot(x, y_red,'red')
axs[2].plot(x, y_green,'green')

for ax in axs.flat:
    ax.set(xlabel='radius (r)', ylabel='thickneds (mm)')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()
plt.show()

