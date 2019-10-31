1. Where does the Optimization Equation (9.9-9.11) come from?    

_Great question! We briefly discussed digging into Elements of Statistical Learning (the next step up from the introductory text) and you could do a literature review to_

2. Can you provide more detail, or a more intuitive explanation, about how C, the tuning parameter from Equation 9.15, and the Bias-Variance tradeoff are related?

_The paraemter $C$ is related to the number of support vectors the classification ends up being based off of - the smaller $C$ is, the narrower the margin within which, support vectors are defined. You could think about the analogy to a line fit to a stream of points - A small $C$ is realated to the "wiggliness" of the function that is fit to the line, thus the better it fits the data in the sample, but potentially induces more variance for data outside the region observer or from a new sample. Try writing up a statement in your own words to explain this concept to a peer._

3. How exactly does including polynomial terms in Eqn. 9.16 cause a non-linear decision boundary to be formed?

_We discussed this during our last meeting, but it's similar to fitting a linear function (linear in the parameters or $\beta$s) using covariates that are non-linear (i.e., polynomial and/or interaction terms)_ 

4. Why and how does Eqn. 9.23 work correctly?

_This is a question that I do not have the expertise to address. I encourage you to dig into the literature to gain intuition about how it works. Try a Google Scholar or Web of Science Search._ 

5. What is an implicit feature space?

_I belive it is the set of all potential combinations of the $\mathbf{X}$s (i.e., $\mathbf{x_1}$,...,$\mathbf{x_p}$) up to the order you are considering. For instance if you consider just first order terms, there are $2^p$ potential combinations of features that make up the implicit feature space. For certain Kernals for SVMs the implicit feature space would be infintely large, but by using the Kernal, you can explore that space efficiently._ 


6. What is an ROC Curve?

_An ROC curve is a reciever operating characteristic curve that shows the rate of false positives vs. the rate of true positives, and the area under that curve is typically used to assess one measure of performance of a classifier. A perfect classifier would have area = 1 and a random guess would have that equal to 0.5. Check out Section 4.4.3 for more details. We can discuss this on Friday!_

7. For one-versus-one and one-versus-all, what happens if there's a tie between two classes that a point could belong to? 

_In theory, this could happen for any classification method, but it's not somthing that happens often. Sometimes, when an observation is unequivocal (i.e., there is a tie or its "too close to call") that observation receives a label of unequivocal indicating that it does not clearly belong to any of the $K$ classes over the others._

8. Would it be theoretically possible to create or discover an over-arching way to quantify how accurate a method is based on data characteristics? Such as an equation or formula that would take as input the characteristics of the data you want to analyze, and have it output an 'accuracy measure' for each method to determine which method should be used on a set of data? 

_This question has some philosophical underpinnings. There is inherent unknown in data and in processes we are trying to understand that we will never be able to quantify. Thus, there is no "over-arching" way to acheive certainty in any of the decisions we make using data, and it is my opinoin that it should stay that way! For a particular problem, we typically think hard about a reasonable loss function, or a model selection criteria (e.g., LOOCV, AIC, BIC, DIC, etc.) that gets at a characteristic of the data we wish to learn about specifically, but there is no "one-size-fits-all" criteria._ 
