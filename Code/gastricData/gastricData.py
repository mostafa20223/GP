################################ Section1 - Importing Class ################################
"""
    gastricData Class
"""
from gasticDataClass import gastricData

gastricDataVar = gastricData("/home/mustafa/Downloads/GP/Data/gastricData/gastricData.mat")
gastricDataVar.set_data()
gastricDataVar.reshape_data(gastricDataVar.y[0][0], gastricDataVar.x[0][0])
MSI_reshaped = gastricDataVar.MSI_reshaped
MassSpec = gastricDataVar.MassSpec

pca_2 = gastricDataVar.dimensionality_reduction("PCA", 2)
pca_3 = gastricDataVar.dimensionality_reduction("PCA", 3)
pca_5 = gastricDataVar.dimensionality_reduction("PCA", 5)

tsne2 = gastricDataVar.dimensionality_reduction("t-SNE", 2)
tsne3 = gastricDataVar.dimensionality_reduction("t-SNE", 3)
gastricDataVar.plot_dimensionality_reduction("t-SNE3", "t-SNE of All Spectra Data and Number of Components is 3 in Scatter Space", gastricDataVar.tsne3, gastricDataVar.MassSpec[:, 5])

KMeans_labels = gastricDataVar.KMeans_clustering(3)
gastricDataVar.plot_KMeans_clustering()

"""
    All Information
"""
gastricDataVar.print_info("pixels_info")
gastricDataVar.print_info("peak_list")
gastricDataVar.print_info("spectra")
gastricDataVar.print_info("MSI")
gastricDataVar.print_info("PCA")
gastricDataVar.print_info("t-SNE")

"""
    Plots
gastricDataVar.plot_images("goodlist", gastricDataVar.pixels_img)
gastricDataVar.plot_images("pixel_sample_id", gastricDataVar.pixel_sample_id)
gastricDataVar.plot_images("HE_image", gastricDataVar.HE_image)
gastricDataVar.plot_MSI()
gastricDataVar.plot_dimensionality_reduction("PCA2", "PCA of All Spectra Data and Number of Components is 2", gastricDataVar.pca_2, gastricDataVar.MassSpec[:, 5])
gastricDataVar.plot_dimensionality_reduction("PCA3", "PCA of All Spectra Data and Number of Components is 3", gastricDataVar.pca_3, gastricDataVar.MassSpec[:, 5])
gastricDataVar.plot_dimensionality_reduction("t-SNE2", "t-SNE of All Spectra Data and Number of Components is 2", gastricDataVar.tsne2, gastricDataVar.MassSpec[:, 5])
gastricDataVar.plot_dimensionality_reduction("t-SNE3", "t-SNE of All Spectra Data and Number of Components is 3 in Scatter Space", gastricDataVar.tsne3, gastricDataVar.MassSpec[:, 5])
"""

"""
self.kmeans_image[self.spectra, :] = self.KMeans_labels
self.kmeans_RGB = np.reshape(self.kmeans_image, (self.y, self.x), order = 'F')

default_cmap = cm.get_cmap(lut = 4)
gnuplot_cmap = cm.get_cmap("gnuplot", lut = 4)
jet_cmap = cm.get_cmap("jet", lut = 4)

plt.figure(figsize = (25, 25))
plt.title('Default K-means Image', loc = 'center', fontsize = 25, color = 'red', fontweight = 'bold')
default_cb = plt.imshow(kmeans_RGB, cmap = default_cmap)
cbar = plt.colorbar(default_cb, ticks = [0, 1, 2, 3], shrink = 0.2)
plt.figure(figsize = (25, 25))
plt.title('Gnuplot K-means Image', loc = 'center', fontsize = 25, color = 'red', fontweight = 'bold')
gnuplot_cb = plt.imshow(kmeans_RGB, cmap = gnuplot_cmap)
cbar = plt.colorbar(gnuplot_cb, ticks = [0, 1, 2, 3], shrink = 0.2)
plt.figure(figsize = (25, 25))
plt.title('Jet K-means Image', loc = 'center', fontsize = 25, color = 'red', fontweight = 'bold')
jet_cb = plt.imshow(kmeans_RGB, cmap = jet_cmap)
cbar = plt.colorbar(jet_cb, ticks = [0, 1, 2, 3], shrink = 0.2)
# cb = imagesc.plot(kmeans_RGB, cmap = cmap, figsize = (20, 20))
"""