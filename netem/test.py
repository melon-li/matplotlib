# import numpy as np
# from matplotlib import pyplot as plt
# from matplotlib import animation
# 
# fig = plt.figure()
# fig.set_dpi(100)
# fig.set_size_inches(7, 6.5)
# 
# ax = plt.axes(xlim=(0, 100), ylim=(0, 100))
# patchs = []
# for i in range(56):
#     patch = plt.Circle((i, -i), 0.75)
#     patchs.append(patch)
#     
# # ax.axis('equal')
# # ax.margins(0)
# def init():
#     for index, patch in enumerate(patchs):
#         patch.center = (index, index)
#         ax.add_patch(patch)
# #     ax.axis('equal')
#     return tuple(patchs)
# 
# def animate(i):
#     for index, patch in enumerate(patchs):
#         x, y = patch.center
#         x = index + 3 * np.sin(np.radians(i))
#         y = index + 3 * np.cos(np.radians(i))
#         patch.center = (x, y)
#     return tuple(patchs)
# 
# anim = animation.FuncAnimation(fig, animate, 
#                                init_func=init, 
#                                frames=360, 
#                                interval=1000,
#                                blit=True)
# 
# ax.margins(0)
# plt.show()

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)

ax = plt.axes(xlim=(0, 10), ylim=(0, 10))
patchs = []

for i in range(5):
    patch = plt.Circle((i, -i), 0.75, fc='y')
    patchs.append(patch)

flag = 0
def init():
    global flag
    if flag == 0:
        flag = 1
    else:
        return tuple(patchs)
    print "hh"
    for patch in patchs:
        patch.center = (i, i)
        ax.add_patch(patch)
    print (len(patchs))
    return tuple(patchs)

def animate(i):
    for index, patch in enumerate(patchs):
        x, y = patch.center
        x = index + 3 * np.sin(np.radians(i))
        y = index + 3 * np.cos(np.radians(i))
        patch.center = (x, y)
    return tuple(patchs)

anim = animation.FuncAnimation(fig, animate, 
                               init_func=init, 
                               frames=360, 
                               interval=20,
                               blit=True)

plt.show()
