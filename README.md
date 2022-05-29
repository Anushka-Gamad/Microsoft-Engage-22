<a href="https://myanimelist.net/">
    <img src="https://github.com/Anushka-Gamad/Microsoft-Engage-22/blob/main/images/Logo1.png" alt="toyokoto" title="toyokoto" align="right" height="100" />
</a>

# TOYOKOTO - Anime Recommendation System
Viewers often waste hours scrolling through hundreds, if not thousands, of anime episodes before finding anything they enjoy. In order to build a better streaming environment that promotes income and increases the time spent on a website, businesses must be given advice based on their likes and wants.


<h2>Objective</h2>
We use machine learning to analyse the information in order to construct a recommendation system that can assist someone in deciding what to watch next.

<h2>Dataset</h2>
The dataset is downloaded fron Kaggle. The dataset contains two CSV files anime.csv and ratings.csv 
<p>Link to dataset : <a href="https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database">Download</a></p>

<h2>Problem Statement</h2>
Using an anime dataset, to create a recommendation system based on two famous algorithms:
<li>content based filtering </li>
<li>collaborative filtering</li>

<h2>Technologies</h2>
Used Python libraries such as streamlit, numpy, sklearn, pandas , cosine similarity

<h2>Website UI</h2>
<img src="https://github.com/Anushka-Gamad/Microsoft-Engage-22/blob/main/images/image1.png" alt="toyokoto" title="image1" align="centre"/>
<img src="https://github.com/Anushka-Gamad/Microsoft-Engage-22/blob/main/images/image2.png" alt="toyokoto" title="image2" align="centre"/>
<img src="https://github.com/Anushka-Gamad/Microsoft-Engage-22/blob/main/images/image3.png" alt="toyokoto" title="image3" align="centre"/>

<h2>Video Demo</h2>
<a href="">Click me</a>

<h2>Algorithms</h2>
<h3>Content Based Recommendation System<h3>
This algorithm recommends products which are similar to the ones that a user has liked in the past. The content of each
item is represented as a set of descriptors or terms, typically the words that occur in a document.A content based recommender
works with data that the user provides, either explicitly (rating) or implicitly (clicking on a link). Based on that data, a user profile is
generated, which is then used to make suggestions to the user. As the user provides more inputs or takes actions on the
recommendations, the engine becomes more and more accurate
    
Here, there are various approaches to solve this problem and I have applied them keeping in mind their usage in theindustry.
They are broadly based on 2 category:
1) User Based: Takes user_id to get recommendation
2) Item Based: Give recommendation based on the serch
We use cosine similarity to find the relation
Cosine similarity metric measures the cosine of the angle between two n-dimensional vectors projected in a
multi-dimensional space. The Cosine similarity of two documents will range from 0 to 1.

 <h3>Collaborative Filtering Recommender System</h3>
Collaborative filtering is a technique that can filter out items that a user might like on the basis of reactions by similar users. It works by
searching a large group of people and finding a smaller set of users with tastes similar to a particular user.
1) User Based collaborative filtering- This algorithm first finds the similarity score between users. Based on this
similarity score, it then picks out the most similar users and recommends products which these similar users have liked
or bought previously.
2) Item Based collaborative filtering: In this algorithm, we compute the similarity between each pair of items. So in our
case we will find the similarity between each movie pair and based on that, we will recommend similar movies which
are liked by the users in the past.

  
 <h2>Discussion</h2>
<li>A major drawback of content based filtering algorithm is that it is limited to recommending items that are of the same type. It will never
recommend products which the user has not bought or liked in the past. So if a user has watched or liked only action movies in
the past, the system will recommend only action movies. It’s a very narrow way of building an engine.
To improve on this type of system, we need an algorithm that can recommend items not just based on the content, but the
  behavior of users as well.</li>
<li>In practice, many commercial recommender systems are based on large datasets. As a result, the user-item matrix used
for collaborative filtering could be extremely large and sparse, which brings about challenges in the performance of the
recommendation.One typical problem caused by the data sparsity is the cold start problem. As collaborative filtering
methods recommend items based on users' past preferences, new users will need to rate a sufficient number of items to
enable the system to capture their preferences accurately and thus provides reliable recommendations.</li>
<li>Similarly, new items also have the same problem. When new items are added to the system, they need to be rated by a
substantial number of users before they could be recommended to users who have similar tastes to the ones who
rated them. The new item problem does not affect content-based recommendations, because the recommendation of
  an item is based on its discrete set of descriptive qualities rather than its ratings.</li>
  
  
 
  <h2>Future Possible Ideas</h2>
Creating a hybrid recommendation system that that combines content-based filtering and collaborative filtering could
potentially take advantage from both the representation of the content as well as the similarities among users and
negates the limitations.
