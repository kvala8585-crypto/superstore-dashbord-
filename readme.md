# &nbsp;Superstore Management – Data Science \& BI Dashboard Project

## &nbsp;Project Overview

This project converts a Superstore EDA analysis into a complete end-to-end Data Science \& Business Intelligence solution.

It includes:

* Business problem analysis
* SQL database integration
* Machine Learning model training
* Power BI–style interactive dashboard using Streamlit
* Professional UI, slicers, KPIs, and validations

## &nbsp;Business Problems Solved

1. Why profit is negative even when sales are high?
2. Which product categories and sub-categories are most profitable?
3. Which regions and states cause losses?
4. How discounts affect profit margins?
5. How to predict future sales based on quantity and discount?
6. Which customers generate the highest value?

## Key Business Insights

* High discounts (>30%) often result in negative profit
* Technology category generates maximum profit
* Furniture category causes frequent losses
* West \& East regions outperform others
* Corporate customers have higher lifetime value

## &nbsp;Project Architecture

superstore dashbord/
├── data/
│   └── superstore.csv
├── database/
│   └── superstore.db
├── model/
│   └── sales\_model.pkl
├── app.py
├── train\_model.py
├── sql\_setup.py
├── requirements.txt
└── README.md

## &nbsp;Technologies Used

Python, Pandas, NumPy, SQLite, Scikit-learn, Streamlit, Plotly

## &nbsp;Machine Learning Model

RandomForestRegressor for Sales Prediction using Quantity \& Discount.

## Dashboard Features

* Interactive slicers (Region, Category)
* KPIs: Total Sales, Total Profit, Orders
* Sales \& Profit charts
* ML-based Sales Prediction
* Professional dark UI

## &nbsp;Validations

* Column existence checks
* Input range validation
* SQL connection safety
* Model feature validation

## &nbsp;How to Run the Project

pip install -r requirements.txt
python sql\_setup.py
python train\_model.py
streamlit run app.py

## &nbsp;Future Enhancements

* Time-series sales forecasting
* Customer segmentation (K-Means)
* Profit prediction model
* Role-based authentication
* Export reports to PDF / Excel

## &nbsp;Author

Kavi Vala

