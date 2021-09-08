>“Wealth, like a tree, grows from a tiny seed. The first copper you save is the seed from which your tree of wealth shall grow. The sooner you plant that seed the sooner shall the tree grow. And the more faithfully you nourish and water that tree with consistent savings, the sooner may you bask in contentment beneath its shade.”
​
### ― George S. Clason, The Richest Man in Babylon
​
________________________________
​
​
​
## TL;DR:
​
I loathe that every budget app, credit monitor, and financial tool exists with the sole purpose of pushing financially illiterate products. Credit cards, consolidation loads, personal loans, reverse morgage scams, etc. The goal is to handle as little user data as possible and be able to provide an opportunity to identify areas of financial fault in a budget. 
​
________________
​
​
​
​
## tools for the job
​
The goal is to use Django with python for anything that is non responsive, and javascript for anything that needs active response. 
Materialize will be the style/structuring of the page and we will likely use amCharts for data visualization. 
​
_______________
​
## "But Kaylen", you say, somehow spelling my name wrong verbally. "What will this app do?"
Good question, 
- The goal is to have a landing page to describe the service,
- Offer the user to create a budget using non identifying details. We need to know your finances and likely zipcode (more on that later), nothing else. 
- filling out the details will present you with a screen of detailed information as far as national averages spent in catagories and financial rules of thumb for expenses. 
- provide the user a reference number to be able to come back to this information anytime in the next three months, allowing the user to have a rolling 90 day back-reference. 
- allow the user to edit the budget and review the effects on the advice. 
- our newly minted budgeteer will have access to a resource center that holds links to as many free or low cost financial literacy tools as can be safely reccomended. including books, podcasts, quotes, and more.
​
________
​
## Well what data DO you need for this online budget template app. 
​
Great question again, I like you. 
​
We will need to store data on a few things, but nothing too intrusive. 
there will be a master model that holds key data like:
​
### master model 
Key | Value
------------ | -------------
Reference number | 69420
budget name | x_fortnite_hater_x's budget for july. 
hourly income est. | $20 (entered or calculated by monthly total)
monthly income est. | $4000 (entered or calculated by hourly total)
yearly income est. | $48,000 (entered or calculated by monthly/hourly total)
Bonus income (investments, etc) | $45 (Wow! Thats seems less than the national 4% inflation of the USD, you should really consider reviewing something like mid-growth mutual funds to keep yourself on track for better investment)
Savings | $20,000
expenses common | [Pet care, healthcare, Food (monthly/weekly), car payment, car insurance, debt repayment, familial assistance, tithing]
uncommon expenses (no advice available) | [ state-wide mandatory sky diving classes?, house party savings fund contributions ] (weird stuff that would not be classically catagorized)
home_owner? | False / {'zip': 97223, 'homestyle': '2b2ba', 'zillow_value': 500,000, 'purchase_price': 'declined to enter', remaining_balance': 400,000, 'monthly_min': 1945.00, 'PMI': True} This allows us to have enough data to make advice. 
​
​
​
​
Example of advice we could give based on the limited info above:
>We see you have private morgage insurance. This is required by banks to cover their loan in the eventuality of a default. You wouldnt pay your bosses car insurance, why pay your banks morgage insurance. Your loan is less than 80% of the stated value of the home since the value of your home increased so much, this means you can refinance for an estimated $3,969 in closing costs added to your loan or paid out of pocket (cash prefered), saving you $230 a month in PMI. That cost is recouped in 19 months and its just savings from there on out! (closing costs sources https://www.businessinsider.com/personal-finance/average-refinance-closing-costs)
​
​
____________
​
​
## Sign me up! When can I start using the template? 
You are killing me here, there is no signing up. thats the whole point. 
but lets review what needs to be done:
​
week one:
 <!-- - be overwhelmed by the project. (dont worry this we would do this for even small projects) -->
 <!-- - tackle small things like getting django setup -->
 <!-- - get the landing page setup -->
 <!-- - color scheme time.jpg -->
 <!-- - setup headers, footers, landing page beautification (this is easy and makes the project feel further along. ) -->
<!-- - setup the model(s) -->
<!-- - make blank pages and setup the url structure for the details, edit, resources, more info, and FAQ pages -->
​
week two: 
<!-- - back-end time, display a default model on our details page and show access to the data -->
<!-- - be able to reference different budgets with different ref-numbers -->
- create a POST edit form for adjusting values in the model.  (ooh, maybe lock this with a model specific pin)
<!-- - r/dataisbeautiful time, source a low cost or free visualization library like AMcharts.  -->
- get some graphs working on the detail screen, experiment with keeping the data live with javascript.
​
week three:
<!-- - compile resources on financial literacy. -->
<!-- - add resource links to resource library -->
- compile advice options for simple budget pitfalls
​
week four:
<!-- - cry because class is almost over. -->
- polish things up. make the landing page pop.
- make the details screen UX friendly. 
- make the edit page clean.
- review device advert like a display of the the budget tool on a sleek new macbook pro for the front page. 
- final sweep to ensure everything looks good on mobile and desktop. 