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

dial_colors = np.concatenate([
    (np.random.rand(200) * 20 + 10) / 100,
    (np.random.rand(200) * 20 + 10) / 100,
    (np.random.rand(200) * 20 + 10) / 100,
    (np.random.rand(200) * 20 + 40) / 100,
    (np.random.rand(200) * 20 + 50) / 100,
    (np.random.rand(200) * 20 + 60) / 100,
    (np.random.rand(200) * 20 + 50) / 100,
    (np.random.rand(200) * 20 + 40) / 100,
    (np.random.rand(200) * 20 + 30) / 100,
    (np.random.rand(200) * 20 + 20) / 100,
])

print(dial_colors.shape)
hist, bins = np.histogram(dial_colors)
print(hist, bins)
figname = 'myDial'

# specify which index you want your arrow to point to
arrow_index = 750

# create labels at desired locations
# note that the pie plot plots from right to left
labels = [' ']*len(dial_colors)
labels[0] = '90'
labels[250] = '45'
labels[500] = '0'
labels[750] = '315'
labels[1000] = '270'
labels[1250] = '225'
# 180だけ位置がおかしいのであとで入れる
# labels[1499] = '180'
labels[1750] = '135'

# function plotting a colored dial
def dial(color_array, arrow_index, labels, ax):
    # Create bins to plot (equally sized)
    size_of_groups=np.ones(len(color_array))

    cs=cm.RdYlBu(color_array)
    pie_wedge_collection = ax.pie(size_of_groups, colors=cs, labels=labels)

    i=0
    print("pie wedge collection", len(pie_wedge_collection[0]))
    for pie_wedge in pie_wedge_collection[0]:
        pie_wedge.set_edgecolor(cm.RdYlBu(color_array[i]))
        i=i+1

    # create a white circle to make the pie chart a dial
    my_circle=plt.Circle( (0,0), 0.3, color='white')
    ax.add_artist(my_circle)


# create figure and specify figure name
fig, ax = plt.subplots()

# make dial plot and save figure
dial(dial_colors, arrow_index, labels, ax)
ax.set_aspect('equal')
plt.savefig(figname + '.png', bbox_inches='tight') 

# create a figure for the colorbar (crop so only colorbar is saved)
fig, ax2 = plt.subplots()
cmap = cm.ScalarMappable(cmap='RdYlBu')
cmap.set_array([min(dial_colors), max(dial_colors)])
cbar = plt.colorbar(cmap, orientation='horizontal')
cbar.ax.set_xlabel("Risk")
plt.savefig('cbar.png', bbox_inches='tight')
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
