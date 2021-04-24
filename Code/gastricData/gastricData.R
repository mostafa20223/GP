library(RcppCNPy)
library(Rtsne)
library(scatterplot3d)
library(ggplot2)

MassSpec <- npyLoad("Data/gastricData/MassSpec_Gastric.npy")

set.seed(42)
tsne_out <- Rtsne(as.matrix(MassSpec), dims = 3)
tsne_out1 <- Rtsne((MassSpec), dims = 3)
df <- data.frame(matrix(unlist(tsne_out), nrow=length(tsne_out), byrow=TRUE))

ggplot(df)
# print(typeof(tsne_out))
# print(typeof(tsne_out1))

# scatterplot3d(tsne_out, y = NULL, z = NULL)

# library(samr)

# set.seed(100)
# samfit <- SAM(MassSpec_R, tsne3_R, resp.type = "Two class unpaired")

# # examine significant gene list
# print(samfit)

# # plot results
# plot(samfit)