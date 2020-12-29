# Tumor Heterogeneity
# Layout
* <a href="#A"> Link to Data </a>
* <a href="#B"> Doctor's Notes </a>
* <a href="#C"> Tasks Accomplished </a>

<h2 id="A"> Link to Data </h2>

[Link to Data (Dropbox)](https://www.dropbox.com/sh/w2yfgnb0u3kragd/AADesjt7IJS873KbPM5so10_a?dl=0)

<h2 id="B"> Doctor's Notes / Useful Links </h2>

[Doctor's Notes](https://github.com/mostafa20223/GP/blob/master/Doctor's%20Notes.md)

<h2 id="C"> Tasks Accomplished </h2>

1. For gastric cancer data: please visualize protein images at the following mass-to-charge (m/z) values:  [3374, 3409, 3445, 4967, and 14021]. I hope you can show it next time.
2. Study the math of PCA. Use Python to implement PCA on one of the publicly available data (e.g. maybe MNIST, or CIFAR-10). It would be great if you can show it next time.
3. Renad has mentioned today that she prepared some slides to explain the PCA. Awesome, thanks Renad! We will start next week with her presentation.
4. Please apply the PCA on the MSI gastric cancer data (please remember to use "goodlist" to guide you accessing only spectral information without including the background). In this task please do the following (this will be part of your thesis):
     * UseApply PCA to perform dimensionality reduction from 82 to 2 dimensions (i.e. n_components=2):
        * i) use scatter plot to show the reduced data.
        * ii) show the amount of explained variance in each of  those 2 principal components.
        * iii) color each point in the PCA scatter plot using the protein intensity value at m/z 3374.
     * Apply the PCA to reduce the MSI data into:
        * i) 3 dimensions and show the explained variance retained in each of those 3 principal components.
        * ii) 5 dimensions and and show the explained variance in each component. 
     * Do you observe any effect on changing the number of principal components on the explained variance?
