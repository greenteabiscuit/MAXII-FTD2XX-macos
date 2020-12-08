import matplotlib.pyplot as plt
from matplotlib import cm, gridspec
import numpy as np
import math
from PIL import Image
from mpl_toolkits.axes_grid1 import make_axes_locatable

# set your color array and name of figure here:
# dial_colors2 = np.linspace(0,1,1000) # using linspace here as an example
# dial_colors = (np.random.rand(2000) * 20 + 50) / 100

# best change it to 3600
# 
"""
dial_colors = np.concatenate([
    (np.random.rand(300) * 20 + 40) / 100, #1, 0 to 30
    (np.random.rand(300) * 20 + 50) / 100, #2, 30 to 60
    np.full(300, 0.7), #3, 60 to 90
    np.full(300, 0.7), #4, 90 to 120
    (np.random.rand(300) * 20 + 50) / 100, #5, 120 to 150
    (np.random.rand(300) * 20 + 45) / 100, #6, 150 to 180
    (np.random.rand(300) * 20 + 45) / 100, #7, 180 to 210
    (np.random.rand(300) * 5 + 40) / 100, #8, 210 to 240
    (np.random.rand(300) * 5 + 30) / 100, #9, 240 to 270
    (np.random.rand(300) * 20 + 40) / 100, #10, 270 to 300
    (np.random.rand(300) * 10 + 30) / 100, #11, 300 to 330
    (np.random.rand(300) * 20 + 40) / 100, #12, 330 to 360
])

dial_colors = np.concatenate([
    np.full(300, 530), #1, 0 to 30
    np.full(300, 535), #2, 30 to 60
    np.full(300, 540), #3, 60 to 90
    np.full(300, 543), #4, 90 to 120
    np.full(300, 535), #5, 120 to 150
    np.full(300, 530), #6, 150 to 180
    np.full(300, 520), #7, 180 to 210
    np.full(300, 515), #8, 210 to 240
    np.full(300, 510), #9, 240 to 270
    np.full(300, 515), #10, 270 to 300
    np.full(300, 520), #11, 300 to 330
    np.full(300, 525), #12, 330 to 360
])
"""

# dial_colors = np.concatenate([np.full(300, i) for i in range(1, 37, 1)])
dial_colors_0_90 = np.concatenate([np.full(300, 530+i) for i in range(1, 10, 1)])
dial_colors_90_270 = np.concatenate([np.full(300, 539-i) for i in range(1, 19, 1)])
dial_colors_270_360 = np.concatenate([np.full(300, 520+i) for i in range(1, 10, 1)])

dial_colors = np.concatenate([
    dial_colors_0_90,
    dial_colors_90_270,
    dial_colors_270_360,
])

print("min", dial_colors.min())

numer = dial_colors - dial_colors.min()
denom = dial_colors.max() - dial_colors.min() + 0.1

dial_colors = numer / denom


print(dial_colors.shape)
hist, bins = np.histogram(dial_colors)
print(hist)
print(bins)
figname = 'myDial'

# create labels at desired locations
# note that the pie plot plots from right to left
labels = [' ']*len(dial_colors)
labels[0] = '90'
labels[(len(dial_colors) // 8) * 1] = '45'
labels[(len(dial_colors) // 8) * 2] = '0'
labels[(len(dial_colors) // 8) * 3] = '315'
labels[(len(dial_colors) // 8) * 4] = '270'
labels[(len(dial_colors) // 8) * 5] = '225'
# 180だけ位置がおかしいのであとで入れる
# labels[2700] = '180'
labels[(len(dial_colors) // 8) * 7] = '135'

# function plotting a colored dial
def dial(color_array, labels, ax):
    # Create bins to plot (equally sized)
    size_of_groups=np.ones(len(color_array))

    cs = cm.jet(color_array)
    pie_wedge_collection = ax.pie(size_of_groups, colors=cs, labels=labels)

    i=0
    print("pie wedge collection", len(pie_wedge_collection[0]))
    for pie_wedge in pie_wedge_collection[0]:
        pie_wedge.set_edgecolor(cm.jet(color_array[i]))
        i=i+1

    # create a white circle to make the pie chart a dial
    my_circle=plt.Circle( (0,0), 0.3, color='white')
    ax.add_artist(my_circle)
    ax.set_title("Sound Imaging 360 Degrees")


# create figure and specify figure name
fig, ax = plt.subplots()

# make dial plot and save figure

dial(dial_colors, labels, ax)
print("saving")
ax.set_aspect('equal')
plt.savefig(figname + '.png', bbox_inches='tight') 

# create a figure for the colorbar (crop so only colorbar is saved)
print("setting scalar mappable")
fig, ax2 = plt.subplots()
cmap = cm.ScalarMappable(cmap="jet")
print(min(dial_colors), max(dial_colors))
cmap.set_array([min(dial_colors), max(dial_colors)])
cbar = plt.colorbar(cmap, orientation='horizontal')
cbar.ax.set_xlabel("Accumulated Sum")
plt.savefig('cbar.png', bbox_inches='tight')
print("cropping")
cbar = Image.open('cbar.png')
c_width, c_height = cbar.size
cbar = cbar.crop((0, .8*c_height, c_width, c_height)).save('cbar.png')

# open figure and crop bottom half
im = Image.open(figname + '.png')
width, height = im.size

# crop bottom half of figure
# function takes top corner &lt;span                data-mce-type="bookmark"                id="mce_SELREST_start"              data-mce-style="overflow:hidden;line-height:0"              style="overflow:hidden;line-height:0"           &gt;&amp;#65279;&lt;/span&gt;and bottom corner coordinates
# of image to keep, (0,0) in python images is the top left corner
# im = im.crop((0, 0, width+c_width, int(height/2.0))).save(figname + '.png')
