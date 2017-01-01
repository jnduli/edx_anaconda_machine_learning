import pandas as pd

import random, math

from scipy import misc
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.pyplot as plt

from sklearn.manifold import Isomap
# Look pretty...
matplotlib.style.use('ggplot')



def Plot2D(T, title, x, y, num_to_plot=40):
  # This method picks a bunch of random samples (images in your case)
  # to plot onto the chart:
  fig = plt.figure()
  ax = fig.add_subplot(111)
  ax.set_title(title)
  ax.set_xlabel('Component: {0}'.format(x))
  ax.set_ylabel('Component: {0}'.format(y))
  x_size = (max(T[:,x]) - min(T[:,x])) * 0.08
  y_size = (max(T[:,y]) - min(T[:,y])) * 0.08
  for i in range(num_to_plot):
    img_num = int(random.random() * num_images)
    x0, y0 = T[img_num,x]-x_size/2., T[img_num,y]-y_size/2.
    x1, y1 = T[img_num,x]+x_size/2., T[img_num,y]+y_size/2.
    img = df.iloc[img_num,:].reshape(num_pixels, num_pixels)
    ax.imshow(img, aspect='auto', cmap=plt.cm.gray, interpolation='nearest', zorder=100000, extent=(x0, x1, y0, y1))

  # It also plots the full scatter:
  ax.scatter(T[:,x],T[:,y], marker='.',alpha=0.7)


#
# TODO: Start by creating a regular old, plain, "vanilla"
# python list. You can call it 'samples'.
#
# .. your code here .. 
samples = []
colors =[]

#
# TODO: Write a for-loop that iterates over the images in the
# Module4/Datasets/ALOI/32/ folder, appending each of them to
# your list. Each .PNG image should first be loaded into a
# temporary NDArray, just as shown in the Feature
# Representation reading.
#
for i in range(0,360,5):
    s = 'Datasets/ALOI/32/32_r'+str(i)+'.png'
    img = misc.imread(s)
    img = img[::2, ::2]
    img = img.ravel()
    samples.append(img)
    colors.append('b')

for i in range(110,220,10):
    s = 'Datasets/ALOI/32i/32_i'+str(i)+'.png'
    img = misc.imread(s)
    img = img[::2, ::2]
    img = img.ravel()
    samples.append(img)
    colors.append('r')


# Optional: Resample the image down by a factor of two if you
# have a slower computer. You can also convert the image from
# 0-255  to  0.0-1.0  if you'd like, but that will have no
# effect on the algorithm's results.
#
# .. your code here .. 


#
# TODO: Once you're done answering the first three questions,
# right before you converted your list to a dataframe, add in
# additional code which also appends to your list the images
# in the Module4/Datasets/ALOI/32_i directory. Re-run your
# assignment and answer the final question below.
#
# .. your code here .. 


#
# TODO: Convert the list to a dataframe
#
# .. your code here .. 

df = pd.DataFrame(samples)
del samples
num_images, num_pixels = df.shape
num_pixels = int(math.sqrt(num_pixels))


#
# TODO: Implement Isomap here. Reduce the dataframe df down
# to three components, using K=6 for yo6r neighborhood size
#
# .. your code here .. 

iso = Isomap(n_neighbors=6, n_components=3)
iso.fit(df)
df = iso.transform(df)
#Plot2D(iso.transform(df), 'trial', 0,1);

#
# TODO: Create a 2D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker. Graph the first two
# isomap components
#
# .. your code here .. 
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('Random')
ax.set_xlabel('0')
ax.set_ylabel('1')
ax.scatter(df[:,0],df[:,1], marker='o',c=colors,alpha=0.7)

#df.plot.scatter(x='0', y='01')


#
# TODO: Create a 3D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker:
#
# .. your code here .. 
fig2 = plt.figure()
ax = fig2.add_subplot(111, projection='3d')
ax.set_xlabel('0')
ax.set_ylabel('1')
ax.set_zlabel('2')
ax.scatter(df[:,0],df[:,1],df[:,2], marker='o',c=colors,alpha=0.7)



plt.show()

