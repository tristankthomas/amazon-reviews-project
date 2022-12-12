# Amazon Product Data Analysis
This project was part of a data processing and machine learning subject and required analysing a dataset that contained different Amazon products from different categories. The reviews of each product were analysed to determine what word bi-grams are indicative of a positive or negative review. It was split up into 7 parts, each part outputting certain information.
### **Task 1**
This simply creating a JSON file representing the total number of products and categories in the dataset.
### **Task 2/3**
This averages the review score and cost of each product and represents this data in CSV files.
### **Task 4/5**
This creates a plot of the average cost against the average score of all products in the 'Pet Supplies' category. Task 5 then creates a plot to compare the means of each review score in each category
### **Task 6**
This section pre-processes the review bodies of each review by:
- Converting all non-alphabetic characters to single-space characters
- Converting all spacing characters (tabs/newlines) into single-space characters and ensuring only one whitespace character exists between each word
- Converting all uppercase to lowercase
- Removing all stopwords
- Removing all words less than 3 characters long
- Generating all sequential pairs of words into bi-grams

The bi-grams for each review are then represented in a JSON file.
### **Task 7**
The aim of this task was to discover which bi-grams from task 6 are the most indicative of positive and negative reviews using the log-odds ratio metric, which involves first finding the probability that a bi-gram is in a positive or negative review using $p_b(b) = \frac{num\ positive\ reviews\ containing\ bigram\ b}{num\ positive\ reviews}$ where b is a bigram. This can then be converted to odds using $o_p(b) = \frac{p_b(b)}{1 - p_b(b)}$. Computing this for each bi-gram in the data yields $o_p(b)$ and $o_n(b)$ which can then be converted to a ratio using $o_r(b) = \frac{o_p(b)}{o_n(b)}$. Finally the log-odds ratio is generated using $log_{10}{(o_r(b))}$.

This information is then used to generate the two plots, one showing the frequency distribution of log-odds ratios and the other showing the top 10 most and least indicative bi-grams.

## Running the Script
The python files generate the output files with the corresponding name, already included in this repo. However to generate this files from scratch the following command can be ran:
```
python main.py <task-num>
```
For example:
```
python main.py task3
```
will generate the task 3 CSV file. This can all be done at once by replacing task-num with `all`.
