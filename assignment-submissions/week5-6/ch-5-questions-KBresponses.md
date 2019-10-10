__Conner, see below for some initial responses to your questions. See additionally, a few exercises from the book that I think would be worth your time!__

1. The book states that k-fold CV is more accurate than LOOCV. Why is that? How would you determine the value of k for which k-fold CV is the most accurate?    
_Good question, and I think this sentence in the book is a bit misleading. I believe they mean that LOOCV is less precise than k-fold CV. That is, there is more variation around the esimator for test MSE from LOOCV (i.e., $k = n$) than there is from k-fold CV when $k < n$. The $k$ for which k-fold CV Is the "most accurate" would be $k = n$, or LOOCV, because it is unbiased._

2. What if you calculated the test MSE for every possible layout of k-fold CV, if this were computationally feasible would it improve the accuracy or precision and if so, by how much? What I mean is, if n = 4, and you do 2-fold CV, you would need to repeat the 2-fold CV process 2 times, once for every group of k=2 you could form.    
_This is a great question, and it's something you could investigate with simulation. As you mention - it could defeat the computational advantage of doing $k$-fold CV instead of $n$-fold cv. Why don't you explore this for a small simulated data set. That is, simulate data under the linear model: $y_i = \beta_0 + \beta_1x_i + \epsilon_i$, where $\epsilon_i \sim N(0_, \sigma^2)$, and $i = 1,2,3,...,10$. Fit the model and use 5-fold CV for every possible combo of folds. Compare that to 5-fold CV on just one randomly selected 5-fold. See what you find. Note that you'll have to pick values for $\beta_0, \beta_1, and \epsilon$ to do the simulation I'll leave that up to you! Additionally, you could think about the additional computational burdon of finding every possible $k$-fold CV from $n$ data points by counting the number of different $k$-fold sets there are from $n$ distinct values._


3. Which approach is the best cross validation approach and why?    
_This is an impossible question to answer because it will be problem specific. Not only are there multiple ways to assess model fit/estimate out of sample predictive error, but there are many critera other than test $MSE$. As we move through the book you'll get exposed to more of these, and you can build your own intuition about what appraoches work well for specific problems. In general, think hard about what the most important characteristic(s) of your model are, then do your best to evaluate how well that piece is doing with respect to the data you have an hypothetical new data - that will provide the "best" evaluation of your model._

4. For bootstrapping, if computational power and time weren't issues, how accurate and precise could bootstrapping potentially be?    
_Typically, bootstratpping is used to find the SE of a quantitiy of interest by repeated sampling (and modeling) with replacement from the data you already have. Thus, bootstrapping can only be as good as the sample you're using to do it from - so in a sense it's not the compuational power that's holding it back, but the way in which the data were collected that's the critical ingredient! To be unbiased, you need a representative sample from the population - for precision, you need a larger sample (typically)._

5. For QDA in chapter 4, could you explain the relationship between the formulas the book gives for QDA and Bayes Theorem?    
_Not sure this is somthing I can do a good job of here, but let's discuss next time we meet!_ 

6. I forgot to ask, from your paper, you said beta coefficients across models hold the same interpretation only when they're orthogonal. What does that mean? Also, how would you interpret a coefficient after you've averaged it across different models?    
_Orthogonal is a term from linear algebra that is equvalent to "independent" in statistics. Thus, for the regression coefficients to remain the same across all models regardless of which Xs are included in the model, all Xs must be mutually independent. This is something we never observe in practice! RE: how to interpret a MA partial regression coefficient - you've hit the nail on the head! There is no clear interpretation, so if explanatory inferernce is the goal model averaging partial regression coefficients to "account for model uncertatinty" doesn't make much sense. It would be analogous to averaging apples and oranges._

#### Text problems to work through

- Problem 2 from the conceptual problems, problem 8 from applied. 