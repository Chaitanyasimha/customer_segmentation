# Customer Segmentation Project

This project focuses on segmenting customers based on their purchasing behavior and other relevant features using clustering algorithms. The goal is to identify distinct customer groups to enable targeted marketing strategies and enhance business decision-making.

## Key Features
- **Data Cleaning and Preprocessing**: Handled missing values, normalized numerical features, and prepared the dataset for analysis.
- **Feature Engineering**: Created new features to capture more information about customer behavior.
- **Clustering Algorithms**: Implemented K-means clustering to identify distinct customer segments.
- **Visualization**: Used Matplotlib and Seaborn to visualize the segmentation results, providing clear insights into the customer groups.

## Technologies Used
- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Matplotlib**
- **Seaborn**
- **MySQL**
- **Git**

## Project Structure
customer_segmentation_project/
│
├── data_preprocessing.py # Data Preprocessing Module
├── apply_clustering.py # Apply Clustering Algorithms
├── determine_clusters.py # Determine Optimal Clusters
├── eda.py # Exploratory Data Analysis
├── model_validation.py # Model Validation
├── visualize_clusters.py # Visualization of Clusters
├── data/ # Data files
│ ├── ecom_customer_data.xlsx # E-commerce customer data
│ ├── Mall_Customers.csv # Mall customer data
│
├── requirements.txt # List of required packages
├── README.md # Project documentation
└── .gitignore # Git ignore file for ignoring unnecessary files

## How to Run
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/customer_segmentation_project.git
    cd customer_segmentation_project
    ```

2. **Set Up Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate for Windows
    ```

3. **Install Required Packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run Data Preprocessing**:
    ```bash
    python data_preprocessing.py
    ```

5. **Perform Exploratory Data Analysis**:
    ```bash
    python eda.py
    ```

6. **Determine Optimal Clusters**:
    ```bash
    python determine_clusters.py
    ```

7. **Apply Clustering Algorithm**:
    ```bash
    python apply_clustering.py
    ```

8. **Validate the Model**:
    ```bash
    python model_validation.py
    ```

9. **Visualize Clusters**:
    ```bash
    python visualize_clusters.py
    ```

## Project Overview
This project aims to identify distinct customer groups within two datasets: an e-commerce dataset and a mall customer dataset. Through data preprocessing, exploratory data analysis, and clustering using the K-means algorithm, we successfully identified optimal clusters for both datasets. These insights can help in targeted marketing and personalized customer service strategies.

### Exploratory Data Analysis (EDA)
- Analyzed distributions of orders, purchases, age, and spending scores.
- E-commerce data insights revealed high-frequency buyers and niche market behavior for certain products.
- Mall customer data insights showed varied age and income distributions among different spending levels.

### Clustering with K-Means
- Determined that 5 clusters were optimal for both datasets using the Elbow Method and Silhouette Score.
- Clear segmentation of customers with unique characteristics was revealed, validating the effectiveness of our approach.

### Actionable Insights
- **Targeted Campaigns**: Personalized offers for high spenders and loyalty programs for low spenders.
- **Inventory Management**: Align stock with cluster preferences to optimize inventory turnover.

### Future Work
- Explore other clustering techniques like hierarchical clustering or DBSCAN to compare results.
- Incorporate more features and external data to enhance segmentation and provide deeper insights.

## Conclusion
This project demonstrates the value of customer segmentation in understanding and serving different customer groups more effectively. The integration of data preprocessing, exploratory data analysis, and clustering techniques provided a comprehensive view of customer behavior and preferences.

---

By following this README, users can understand the project's purpose, the technologies used, and how to run the project step-by-step. This README is designed to be clear, concise, and professional, ensuring it is well-received by everyone.
