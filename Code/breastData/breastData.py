################################ Section1 - Importing Class ################################
"""
    breastData Class
"""
from breastDataClass import breastData

breastDataVar = breastData("/home/mustafa/Downloads/GP/Data/breastData/breastData.mat")
breastDataVar.set_data()
breastDataVar.reshape_data(breastDataVar.y[0][0], breastDataVar.x[0][0])
MSI_reshaped = breastDataVar.MSI_reshaped
MassSpec = breastDataVar.MassSpec

pca_2 = breastDataVar.dimensionality_reduction("PCA", 2)
pca_3 = breastDataVar.dimensionality_reduction("PCA", 3)
pca_5 = breastDataVar.dimensionality_reduction("PCA", 5)

tsne2 = breastDataVar.dimensionality_reduction("t-SNE", 2)
tsne3 = breastDataVar.dimensionality_reduction("t-SNE", 3)
breastDataVar.plot_dimensionality_reduction("t-SNE3", "t-SNE of All Spectra Data and Number of Components is 3 in Scatter Space", breastDataVar.tsne3, breastDataVar.MassSpec[:, 5])

"""
    All Information
"""
breastDataVar.print_info("pixels_info")
breastDataVar.print_info("peak_list")
breastDataVar.print_info("spectra")
breastDataVar.print_info("MSI")
breastDataVar.print_info("PCA")
breastDataVar.print_info("t-SNE")

"""
    Plots
"""
"""
    breastDataVar.plot_images("goodlist", breastDataVar.pixels_img)
    breastDataVar.plot_images("pixel_sample_id", breastDataVar.pixel_sample_id)
    breastDataVar.plot_images("HE_image", breastDataVar.HE_image)
    breastDataVar.plot_MSI()
    breastDataVar.plot_dimensionality_reduction("PCA2", "PCA of All Spectra Data and Number of Components is 2", breastDataVar.pca_2, breastDataVar.MassSpec[:, 5])
    breastDataVar.plot_dimensionality_reduction("PCA3", "PCA of All Spectra Data and Number of Components is 3", breastDataVar.pca_3, breastDataVar.MassSpec[:, 5])
    breastDataVar.plot_dimensionality_reduction("t-SNE2", "t-SNE of All Spectra Data and Number of Components is 2", breastDataVar.tsne2, breastDataVar.MassSpec[:, 5])
    breastDataVar.plot_dimensionality_reduction("t-SNE3", "t-SNE of All Spectra Data and Number of Components is 3 in Scatter Space", breastDataVar.tsne3, breastDataVar.MassSpec[:, 5])
"""




