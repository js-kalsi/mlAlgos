import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import numpy as np

# Generate some data
from sklearn.datasets.samples_generator import make_blobs
X, y_true = make_blobs( n_samples= 400, centers =4, cluster_std= 0.60, random_state = 0)
X = X[:, :: -1]  # Flip axes for better plotting.

# Plot the data in KMeans Labels.
from sklearn.cluster import KMeans
kmeans = KMeans(4, random_state = 0)
labels = kmeans.fit(X).predict(X)

plt.scatter( X[:, 0], X[:, 1], c= labels, s=40, cmap='viridis')


from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist

def plot_kmeans( kmeans, X, n_clusters= 4, rseed= 0, ax= None):
    labels = kmeans.fit_predict(X)

    # Plot the input data.
    ax = ax or plt.gca()
    ax.axis('equal')
    ax.scatter( X[:, 0], X[:, 1], c= labels, s=40, cmap='viridis', zorder= 2)

    # Plot the representation of the KMeans model.
    centers =  kmeans.cluster_centers_
    
    radii = [ cdist( X[ labels == i ], [ center ] ).max()
              for i, center in enumerate(centers)]

    for c, r in zip( centers, radii):
        ax.add_patch(plt.Circle(c, r, fc = '#CCCCCC', lw=3, alpha= 0.5, zorder=1))


kmeans = KMeans( n_clusters= 4, random_state= 0)
plot_kmeans(kmeans, X)


# In [6]
print(" ####### In [6] #######")
rng = np.random.RandomState(13)
X_stretched = np.dot( X , rng.randn(2, 2) )
kmeans = KMeans( n_clusters=4, random_state = 0 )
plot_kmeans( kmeans, X_stretched )


# In [7]
print(" ####### In [7] #######")
from sklearn.mixture import GMM as gmm
gmm = gmm( n_components = 4).fit(X)
labels = gmm.predict(X)
plt.scatter( X[ :, 0 ], X[ :, 1], c= labels, s= 40, cmap = 'viridis')

# In [8]
print(" ###### In [8] ########")
probs = gmm.predict_proba(X)
print( probs[ :5 ].round(3) )


# In [9]
size = 50 * probs.max(1) ** 2  # Square Emphasizes Differences
plt.scatter( X[:, 0], X[:, 1], c= labels, cmap= 'viridis', s= size)



# In [10]

from matplotlib.patches  import Ellipse
from sklearn.mixture import GMM as gmm

def draw_ellipse( position, covariance, ax=None, **kwargs):
    """ Draw an ellipse with a  given position and covariance """
    ax = ax or plt.gca()

    # Covert covariance to principal axes.
    if covariance.shape == (2, 2):
        U, s, Vt = np.linalg.svd( covariance )
        angle = np.degrees( np.arctan2( U[1, 0], U[0, 0] ))
        width, height = 2 * np.sqrt(s)
    else:
        angle = 0
        width, height = 2 * np.sqrt( covariance )

    # Draw the Ellipse.
    for nsig in range(1, 4):
        ax.add_patch( Ellipse(position, nsig * width, nsig * height, angle, **kwargs))


def plot_gmm( gmm, X, label=True, ax= None):
    ax = ax or plt.gca()
    labels = gmm.fit(X).predict(X)
    if label:
        ax.scatter( X[:, 0], X[:, 1], c= labels, s= 40, cmap= 'viridis', zorder= 2)
    else:
        ax.scatter( X[:, 0], X[:, 1], s= 40, zorder = 2)
    ax.axis('equal')

    w_factor= 0.2/ gmm.weights_.max()
    for  pos, covar, w in zip( gmm.means_, gmm.covars_, gmm.weights_):
        draw_ellipse( pos, covar, alpha= w * w_factor)



# In [11]
from sklearn.mixture import GMM as gmm
gmm = gmm( n_components= 4, random_state= 42)
plot_gmm(gmm, X)


# In [12]
from sklearn.mixture import GMM as gmm
gmm = gmm( n_components =4, covariance_type ='full', random_state= 42)
plot_gmm(gmm, X_stretched)


# In [13]
from sklearn.datasets import make_moons
Xmoon, ymoon = make_moons( 200, noise=0.05, random_statte = 0 )
plt.scatter( Xmoon[:, 0], Xmoon[:, 1] )


# In [14]
from sklearn.mixture import GMM as gmm
gmm2 = gmm( n_components= 2, covariance_type= 'full', random_state= 0)
plt_gmm(gmm2, Xmoon)


# In [15]
gmm16 = gmm( n_components = 16, covariance_type = 'full', random_state = 0)
plot_gmm( gmm16, Xmoon, label= False)


# In [16]
Xnew = gmm16.sample( 400, random_state = 42)
plt.scatter( Xnew[ :, 0], Xnew[:, 1])


# In [17]
n_components  = np.arange( 1, 21)
models = [ gmm(n, covariance_type = 'full', random_state = 0).fit(Xmoon)
           for  n in n_components]

plt.plot( n_components, [ m.bic( Xmoon) for m in models ], label= 'BTC')
plt.plot( n_components, [ m.aic(Xmoon) for m in models ], label = 'AIC')
plt.legend( loc = 'best')
plt.xlabel('n_components')



# In [18]
from sklearn.datasets import load_digits
digits = load_digits()
digits.data.shape



# In [19]
def plot_digits(data):
    fig, ax = plt.subplots( 10, 10 , figsize=(8, 8), subplot_kw = dict( xticks=[], yticks=[]))
    fig.subplots_adjust( hspace = 0.05, wspace= 0.05)
    for i, axi in enumerate( ax.flat ):
        im = axi.imshow( data[i].reshape(8, 8), cmap = 'binary')
        im.set_clim(0, 16)
plot_digits( digits.data )   


# In [20] PCA
from sklearn.decomposition import PCA
pca = PCA(0.99, whiten= True)
data = pca.fit_transform( digits.data )
data.shape




# In [21] Implementing AIC
from sklearn.mixture import GMM as gmm 
n_components = np.arange( 50, 210, 10)
models = [ gmm( n, covariance_type= 'full', random_state = 0 )
           for n in n_components ]
aics = [ model.fit(data).aic(data) for  model in models]
plt.plot( n_components, aics)


# In [22]
from sklearn.mixture import GMM as gmm
gmm = gmm( 110, covariance_type= 'full',random_state = 0)
gmm.fit(data)
print( "gmm.converged_", gmm.converged_ )


# In [23]
data_new = gmm.sample( 100, random_state = 0)
data_new.shape


# In [24]
digits_new = pca.inverse_transform( data_new )
plot_digits( digits_new )
