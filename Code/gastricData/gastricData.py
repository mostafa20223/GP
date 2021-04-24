################################ Section1 - Importing Class ################################
"""
    gastricData Class
"""
from gasticDataClass import gastricData

NO_OF_PNTs = 63

gastricDataVar = gastricData("Data/gastricData/gastricData.mat")
gastricDataVar.set_data()
gastricDataVar.reshape_data(gastricDataVar.y[0][0], gastricDataVar.x[0][0])
MSI_reshaped = gastricDataVar.MSI_reshaped
MassSpec = gastricDataVar.MassSpec

# im = readNPY('/path/to/file.npy');

# tsne3 = gastricDataVar.dimensionality_reduction("t-SNE", 3)
# gastricDataVar.plot_dimensionality_reduction("t-SNE3", "t-SNE of All Spectra Data and Number of Components is 3 in Scatter Space", gastricDataVar.tsne3, gastricDataVar.MassSpec[:, 5])
# gastricDataVar.plot_dimensionality_reduction("t-SNE3", "t-SNE of All Spectra Data and Number of Components is 3 in Scatter Space", gastricDataVar.tsne3new, gastricDataVar.MassSpec[:, 5])

"""
    Dimensionality Reduction
pca_2 = gastricDataVar.dimensionality_reduction("PCA", 2)
pca_3 = gastricDataVar.dimensionality_reduction("PCA", 3)
pca_5 = gastricDataVar.dimensionality_reduction("PCA", 5)
tsne2 = gastricDataVar.dimensionality_reduction("t-SNE", 2)
tsne3 = gastricDataVar.dimensionality_reduction("t-SNE", 3)
"""

"""
    Clustering
KMeans_labels = gastricDataVar.KMeans_clustering(3)
"""

"""
    Get Protein Peaks for Each Patient
for i in range(1, NO_OF_PNTs + 1):
    gastricDataVar.getPeaks(i, 0)
"""

"""
    Link to Clinical_data (Survival Analysis)
# gastricDataVar.survival_analysis()
gastricDataVar.Clinical_data("Data/gastricData/Clinical_data.csv")
"""

"""
    All Information
gastricDataVar.print_info("pixels_info")
gastricDataVar.print_info("peak_list")
gastricDataVar.print_info("spectra")
gastricDataVar.print_info("MSI")
gastricDataVar.print_info("PCA")
gastricDataVar.print_info("t-SNE")
"""

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
gastricDataVar.plot_KMeans_clustering()
"""
