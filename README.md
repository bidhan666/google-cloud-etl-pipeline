Key Steps:

1. Data Extraction & Masking: Extracted employee data from multiple sources (databases, CSVs, APIs), and applied masking techniques to sensitive information like salaries and passwords using Cloud Data Fusion.

2. Data Transformation: Using Cloud Data Fusion, I transformed and cleaned the data, combining first and last names, masking sensitive columns, and securely storing the data in Google Cloud Storage.

3. Data Loading into BigQuery: The transformed data was securely loaded into Google BigQuery, where it’s available for further analysis. This process was optimized for performance and reliability.

4. Automation with Cloud Composer & Apache Airflow: All workflows were orchestrated with Google Cloud Composer (powered by Apache Airflow) to ensure smooth, repeatable processes with task dependencies, scheduling, and error handling.

5. Data Visualization in Looker Studio: Finally, the data was visualized in Looker Studio, providing clear and insightful dashboards for analysis and decision-making.

Why This Matters:

By automating this entire pipeline, I was able to create a scalable, efficient, and secure workflow for handling large datasets. The integration between Google Cloud services like BigQuery, Cloud Data Fusion, Google Cloud Storage, and Looker Studio allowed seamless data flow from extraction to visualization, all while ensuring data integrity and security.

Tools and Technologies:

1. Python for data extraction and handling.

2. Google Cloud Storage for secure raw data storage.

3. Cloud Data Fusion for transformation and data integration.

4. BigQuery for scalable data warehousing and analytics.

5. Looker Studio for dynamic data visualization.

6. Cloud Composer with Apache Airflow for workflow orchestration and automation.
