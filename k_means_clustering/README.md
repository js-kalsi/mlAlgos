a) Implementation of K-nearest-neighbor Algorithm
The `k_means_clustering` folder contains the source code for  "k-nearest-neighbor" Algorithm in javascript as well as in C++. I have learned this algorithm from the [blog](http://burakkanber.com/blog/machine-learning-in-js-k-nearest-neighbor-part-1/)  and also hosted its javascript [version](https://mlalgorithm.herokuapp.com/).
Using the same logic I have created my own C++ version of "k-nearest-neighbor" Alogorithm.
Consider a table for understanding about this algorithm :

| Rooms| Area | Type      |
| -----|:----:| ---------:|
| 1    | 350  | apartment |
| 2    | 300  | apartment |
| 3    | 300  | apartment |
| 4    | 250  | apartment |
| 4    | 500  | apartment |
| 4    | 400  | apartment |
| 5    | 450  | apartment |
| 7    | 850  | house     |
| 7    | 900  | house     |
| 7    | 1200 | house     |
| 8    | 1500 | house     |
| 9    | 1300 | house     |
| 8    | 1240 | house     |
| 10   | 1700 | house     |
| 9    | 1000 | house     |
| 1    | 800  | flat      |
| 3    | 900  | flat      |
| 2    | 700  | flat      |
| 1    | 900  | flat      |
| 2    | 1150 | flat      |
| 1    | 1000 | flat      |
| 2    | 1200 | flat      |
| 1    | 1300 | flat      |

We're going to plot the above as points on a graph in two dimensions, using number of rooms as the x-axis and the area as the y-axis.

When we inevitably run into a new, unlabeled data point ("mystery point"), we'll put that on the graph too. Then we'll pick a number (called "k") and just find the "k" closest points on the graph to our mystery point. If the majority of the points close to the new point are "flats", then we'll guess that our mystery point is a flat.

That's what k-nearest-neighbor means. "If the 3 (or 5 or 10, or 'k') nearest neighbors to the mystery point are two apartments and one house, then the mystery point is an apartment."

[source](http://burakkanber.com/blog/machine-learning-in-js-k-nearest-neighbor-part-1/)

For the Implementation of C++ version, I have taken four arrays :
1) numOfRooms      (type:Integer) Contains the number of the Rooms and is of length 23.
2) areaOfRooms     (type:Integer) Contains the area   of the Rooms and is of length 23.
3) typeOfRoom      (type:String)  Contains the type information i.e(House,Flat & Apartment) and is of length 23.
4) distanceRecords (type:Integer) Contains the minimum distance of each point from the Mystery point and is of length 23.

I am assuming  (numOfRooms,typeOfRoom) as a coordinates of a point.And this way we have 23 points.
Then, I am creating a new random Point(Mystery Point) and calculating using the "k-nearest-neighbor" Alogorithm wheather
that point will be of type House,Flat or Apartment.
