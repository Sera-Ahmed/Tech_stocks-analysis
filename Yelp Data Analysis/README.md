Yelp provieds platform to customers to search for restaurants and various other services and for them to write or read reviews before/ after booking a service. Yelp was founded in 2004 and since then has gotten attention of millions of users. 

The analysis shows the top business categories, the number of reviews per year and if the customer reviews if they have a positive or negative experience with the business. 

Now we will get a little technical and discuss the tools and techniques used for the analysis. 

The Yelp dataset is huge and is more than 10GB, consists of more than 8million reviews, 2 million users, 160k plus business and 200k plus pictures which is certainly very hard to store on a computer and gets even more difficult when processing of the data needs to be done. So to avoid the slowness and constant crashing of the file the below tools and technologies have been used. 

A EMR (ElasticMapReduce cluster was spun) and the analysis was done using spark and jupyter notebook using python. The data has been loaded in s3 and the data was being pulled directly from s3 which means there is no need to store it locally on the computer. The jupyer notebook was connected directly to the EMR cluster. The EMR had 1 master node and 2 worker nodes (we could select the option for auto scaling). 

This is the screenshot of the EMR cluseter which was used for the analysis

![cluster_configuration](/Users/sera/Desktop/Baruch Books/CIS 9760 Big Data/Project 2 Spark/project02/assets/cluster_configuration.png)

This is the screenshot of the notebook configuration used for the analysis

![notebook_configuration](/Users/sera/Desktop/Baruch Books/CIS 9760 Big Data/Project 2 Spark/project02/assets/notebook_configuration.png)

**Conclusion:**

The analysis shows that recently the interest of customers in posting reviews on Yelp has gone down. It could be because of the amount of competition in this area. A decade ago we could only think of Yelp as the platform to find restaurants and other services but now there are Ubereats, doordash, seamless, grubhub and many more. Well we wish good luck to Yelp and hopefully people continue to like them and use their service. 

