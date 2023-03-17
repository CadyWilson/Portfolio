# Prosper Bank Loan Analysis
## How Credit and Other Income Variables Affect Loans


### by Cady Wilson


## Dataset

> This data set contains 113,937 loans with 81 variables on each loan, including loan amount, borrower rate (or interest rate), current loan status, borrower income, and many others. After Dropping duplicate rows and condensing down to only key variables I ended with just 21 features and 113,066 rows.

> Feature descritions can be found at https://s3.amazonaws.com/udacity-hosted-downloads/ud651/prosperLoanData.csv


## Summary of Findings

> I took the approach of a consumer while analyzing this dataset. How might different social constructs like income, credit scores etc. affect the interest rate of a loan. Interest is what you will be paying on top of the loan making it more expensive. The higher the interest, the higher the payback amount.

> From the perspective of Prosper with thier risk assesments it makes sense to create a system approximating the risk of lending to a particular individual. I wanted to see if I could potentially "see the risks" in the system.

>In the end credit score was the highest factor in both loan amount and APR. It was the most well defined category when compared to the other variables. This makes sense, as having a lower credit score tracks with either being uninformed financially or just being bad with money. Both of which would be a bad business decision on Prosper's part.


## Key Insights for Presentation
> The main avenue for this exploration is how different borrower variables affected the APR (interest) of the loans they took out. Particularly I wanted to see if the APR was justified or perhaps a bit predatory. 

> Because credit is more or less the end all be all, I checked to see just how much credit score affected the loan. It was very apparent that the higher the score the lower the APR and vice versa. I also wanted to see if income had an effect on the loan amount. It did, but not as much as I thought it would. It was also suprising to me that people with six-figure incomes also took out loans in higher amounts.