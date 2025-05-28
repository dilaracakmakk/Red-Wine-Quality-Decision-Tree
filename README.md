### Wine Quality Prediction with Decision Tree
This project uses the UCI Red Wine Quality Dataset (Kaggle) to predict wine quality based on physicochemical properties using a Decision Tree Classifier.

### Project Workflow
1. Exploratory Data Analysis (EDA)
Checked for missing values and data distribution.

Visualized the distribution of wine quality scores.

Generated a correlation heatmap to identify features that influence wine quality.

2. Data Preparation
The quality column was converted into quality groups (e.g., low, medium, high).

Features (X) and target (y) were separated.

Data was split into training and testing sets (75% training, 25% testing).

3. Model Training
A DecisionTreeClassifier was trained on the processed training data.

Model performance was evaluated on the test data.

4. Model Evaluation
Accuracy score, confusion matrix, and classification report were generated.

Feature importance was visualized to interpret model decisions.

