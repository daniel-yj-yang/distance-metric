# Distance_metric
A collection of distance metrics

<hr>

## 1. <a href="https://en.wikipedia.org/wiki/Least_absolute_deviations">L<sup>1</sup> norm</a>

The sum of the absolute differences between corresponding values.
Also known as least absolute deviations (LAD), least absolute errors (LAE)

<img src="./images/L1_distance.png" width="50%" />

<hr>

## 2. L<sup>2</sup> norm / <a href="https://en.wikipedia.org/wiki/Euclidean_distance">Euclidean distance</a>

The square root of the sum of the squares of the differences between corresponding values.

<img src="./images/Euclidean_distance.png" width="50%" />

Using some linear algebra notation, we can express <a href="https://math.stackexchange.com/questions/1236465/euclidean-distance-and-dot-product">Euclidean distance using inner product notation</a>:
<img src="./images/Euclidean_distance_as_inner_product.png" width="500px">
                                                                   
Notes:

(1). <a href="https://stats.stackexchange.com/questions/99171/why-is-euclidean-distance-not-a-good-metric-in-high-dimensions">the Euclidean distance is usually not a good metric in higher dimensional space.</a>

(2). When the square root is removed, it is an <a href="http://www.improvedoutcomes.com/docs/WebSiteDocs/Clustering/Clustering_Parameters/Euclidean_and_Euclidean_Squared_Distance_Metrics.htm">Euclidean Squared distance</a>

<hr>

## 3. <a href="https://en.wikipedia.org/wiki/Mahalanobis_distance">Mahalanobis (Ma-ha-la-nobis) distance</a>

It is a multi-dimensional generalization of the idea of measuring how many standard deviations away P (points) is from the mean of D (distribution). This distance is zero if P is at the mean of D.

The Mahalanobis distance is thus unitless and scale-invariant, and takes into account the correlations of the data set.

A nice explanation can be found <a href="https://stats.stackexchange.com/questions/62092/bottom-to-top-explanation-of-the-mahalanobis-distance">here</a>.<br>

When the distribution (in terms of the covariance matrix) is an identity matrix, the distance is the same as the **Euclidean distance**.

<hr>

## 4. <a href="https://en.wiktionary.org/wiki/Manhattan_distance">Manhattan distance</a>

Imagine a grid-like street geography of the Manhattan borough in NYC.

<img src="./images/Manhattan_distance.png" width="50%" />

<hr>

## 5. <a href="https://en.wikipedia.org/wiki/Cosine_similarity">Cosine distance</a>

cosine distance = 1 - cosine similarity

<img src="./images/cosine_similarity.png" width="300px"><br/>(based on the <a href="https://en.wikipedia.org/wiki/Dot_product">dot product</a> of two vectors)

<a href="https://cmry.github.io/notes/euclidean-v-cosine">Cosine similarity</a>, which is good at measuring the similarity of patterns of feature changes, *independent of* the absolute amplitude of the compared feature vectors.
<br/><br/>
May be used in a number of ML algorithms, including kNN.

<hr>

## 6. <a href="https://en.wikipedia.org/wiki/Minkowski_distance">Minkowski distance</a>

A generalization of both the Euclidean distance and the Manhattan distance in a normed vector space, used in kNN algorithm.

<hr>

## 7. <a href="https://en.wikipedia.org/wiki/Pearson_correlation_coefficient#Pearson's_distance">Pearson's distance</a>

d(x,y) = 1 - Pearson's correlation (x, y)

<hr>

## 8. <a href="https://en.wikipedia.org/wiki/Chebyshev_distance">Chebyshev (chessboard) distance</a>

The Chebyshev distance between two vectors or points x and y, with standard coordinates x<sub>i</sub> and y<sub>i</sub>, respectively, is

D<sub>Chebyshev</sub>(x,y) := max( | x<sub>i</sub> - y<sub>i</sub> | )

That is, the distance between two vectors is the greatest of their differences along <b>any coordinate dimension</b>.

<p align="center"><img src="./images/chessboard_distance_example.png" width="300px"><br/>(<a href="https://en.wikipedia.org/wiki/Chebyshev_distance">image source</a>)</p>

<br/>

May be used in the kNN algorithm.

<hr>

## 9. <a href="https://en.wikipedia.org/wiki/Jaccard_index">Jaccard distance</a>

Dissimilarity between sample sets

<img src="./images/Jaccard_distance.png" width="350px">

Used to provide n x n matrix for <a href="https://en.wikipedia.org/wiki/Multidimensional_scaling">multidimensional scaling</a>.

<hr>

## 10. <a href="https://en.wikipedia.org/wiki/Hamming_distance">Hamming distance</a>

Between two strings of equal length, the number of positions at which the corresponding symbols are different.

Examples (from <a href="https://en.wikipedia.org/wiki/Hamming_distance">wikipedia</a>):<br/>
<img src="./images/Hamming_distance_example.png" width="250px">

<hr>

Some questions:

(1) when to use the Euclidean Squared distance metric?

(2) why it is a bad idea to use Euclidean distance in higher dimensional space?

(3) <a href="https://www.researchgate.net/post/What_is_the_best_distance_measure_for_high_dimensional_data">what distance metric should be used in higher dimensional space?</a>

(4) when to use the cosine distance metric?

