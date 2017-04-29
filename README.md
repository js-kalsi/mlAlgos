MACHINE LEARNING : It is a sub-field of Artifical Inteligence. It is the study of algorithm which learns from examples and experiences instead of relying upon hardcoded rules.

I will give u an example which sounds easy but it is imposible to solve it without machine learning.
Can you write a code to show the difference between apple and orange?

Image I told you to write a program that takes image file as input and does some analysis and outputs the type fruits.

How can you solve this? You have to start by writing lots of manual rules.

For example : you can write a code to find how many orange pixels are their in orange image and compare that with the number of green once. The ratio should give you a hint about the type of fruit. That works fine for simple images but as you dive deep into the problem you find the real world is messy and the rules you write has start to break...
How to write code to handle black and white photos or images with no apples and oranges in them at all ?
Infact any rule you write I can find an image where it cannot work.You need to write tons of rules just to tell the differnce between apples and orangesAnd if I give you a new problem then you have to start all over again.

Clearly we need something better. To solve this we need an algorithm that can figure out the rules for us so that we do not have to write them by hand and for that we are going to train a classifier as a function	it takes some data as input and assign  a label to it as output for example we could have a picture and we want a classfier as an apple or an orange or I can have an email as a classifier which I can classify as spam and not a spam.

The technique to write a classifier automatically is called Supervised learning.
