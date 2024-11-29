import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_digits
import seaborn as sns

# part a

digits = load_digits()

# part b
pixels = pd.DataFrame(digits.data)

labels = digits.target

# part c
single_image = pixels.iloc[0]

# part d
image_array = single_image.to_numpy()

# part e
image_reshaped = image_array.reshape(8, 8)

# part f
plt.figure(figsize=(6, 6))
plt.imshow(image_reshaped, cmap='gray')  
plt.axis('off') 
plt.show()

# part g
scaler = StandardScaler()
pixels_scaled = scaler.fit_transform(pixels)

# part h
pca = PCA(n_components=2)
pixels_pca = pca.fit_transform(pixels_scaled)

# part i
print(f"Explained variance by the first 2 components: {pca.explained_variance_ratio_}")
print(f"Total variance explained by 2 components: {np.sum(pca.explained_variance_ratio_):.2f}")

# part j
plt.figure(figsize=(8, 6))
sns.scatterplot(x=pixels_pca[:, 0], y=pixels_pca[:, 1], hue=labels, palette='tab10', s=100, marker='o', legend='full')
plt.title("PCA of Digits Dataset")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend(title="Digit Label")
plt.show()
