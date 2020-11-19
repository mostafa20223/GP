# Tumor Heterogeneity
# Layout
* <a href="#A"> To Do / Tasks </a>
* <a href="#B"> Notes / Useful Links </a>

<h2 id="A"> To Do / Tasks </h2>

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
5. Some of you wanted to work on the MSI data of breast cancer, that is fine and you can work in parallel with the gastric cancer task. 
     * Similarly to what we have discussed today, please access the MSI data and show protein images at m/z = [4965, 4999, 5067]. 
     * Show the average spectrum of patient#1 and Patient#30.
     * Apply the above described PCA analysis but on the breast cancer data (either show it next week or the week after).

<h2 id="B"> Notes / Useful Links </h2>

***PCA and t-SNE Algorithms*** <br>
PCA                         |                        T-SNE
:--------------------------:|:----------------------------:
[Look at direct PCA part](https://www.math.uwaterloo.ca/~aghodsib/courses/f06stat890/readings/tutorial_stat890.pdf) | [Paper](https://lvdmaaten.github.io/publications/papers/JMLR_2008.pdf)
[Python examples](https://www.datacamp.com/community/tutorials/principal-component-analysis-in-python) | [Lecture](https://www.youtube.com/watch?v=RJVL80Gg3lA&list=UUtXKDgv1AVoG88PLl8nGXmw&ab_channel=GoogleTechTalks)
