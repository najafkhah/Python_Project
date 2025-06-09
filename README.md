# Financial Fraud Detection Analysis

This project explores patterns in financial transactions to identify potential fraud using a synthetic dataset. It combines exploratory data analysis (EDA), visualisation, and statistical hypothesis testing to investigate whether certain factors (e.g., location, device, payment channel) are associated with fraudulent activity.

---

## Objectives

- Perform exploratory data analysis on transaction records  
- Investigate patterns in fraud across different attributes (e.g., location, transaction type, device used)  
- Conduct statistical hypothesis testing to examine potential relationships between fraud and categorical features  
- Address class imbalance with synthetic data to enable valid comparison and testing  

---

## Exploratory Analysis Highlights

- Fraudulent transactions were evenly distributed across global cities such as Toronto, Berlin, and Sydney.  
- Online and utilities merchant categories showed higher total transaction amounts.  
- Most frauds occurred through ATM and mobile devices.  
- Transaction types like transfer and deposit appeared more frequently in fraudulent activity.  

---

## Hypothesis Testing Results

| Hypothesis                                        | Test       | p-value | Result                   |
|--------------------------------------------------|------------|---------|--------------------------|
| Fraud likelihood differs by payment channel      | Chi-Square | 1.000   | ❌ No significant association |
| Fraud likelihood is associated with transaction location | Chi-Square | 1.000   | ❌ No significant association |

✅ Hypothesis testing used a 5% significance level (α = 0.05)

---

## Conclusion

Despite visible variations in transaction types and merchant categories, statistical analysis showed no significant relationships between fraud and either location or payment channel. This implies that the fraud in this dataset is likely uniformly distributed by design.

---

## Future Directions

- Building predictive models (e.g., logistic regression, decision trees)  
- Analysing temporal or sequential patterns  
- Feature engineering for deeper behavioural insights 
