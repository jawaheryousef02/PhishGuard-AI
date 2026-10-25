\# PhishGuard AI

\### AI-Powered Phishing Email Detection Using Natural Language Processing



\## Project Overview



PhishGuard AI is a Natural Language Processing (NLP) project developed to identify potentially malicious phishing emails.



The project compares two machine learning approaches:



1\. TF-IDF with Logistic Regression

2\. Fine-tuned DistilBERT Transformer



A Streamlit web application allows users to paste email content and receive an AI-generated classification with an estimated phishing probability.



\## Problem Statement



Phishing emails remain a significant cybersecurity threat. Attackers use deceptive messages to persuade recipients to disclose credentials, visit malicious websites, or reveal sensitive information.



This project investigates whether transformer-based NLP can improve phishing email classification compared with a traditional machine learning baseline.



\## Dataset



\*\*Source:\*\* Hugging Face



\*\*Dataset:\*\* `zefang-liu/phishing-email-dataset`



\*\*Original records:\*\* 18,650



The dataset contains two primary fields:



\- Email Text

\- Email Type (Safe Email or Phishing Email)



After cleaning and removing duplicate email text, the dataset was divided into training, validation, and testing subsets.



\## Methodology



The project follows these stages:



1\. Dataset collection and exploration

2\. Data cleaning and preprocessing

3\. Stratified train/validation/test splitting

4\. TF-IDF feature extraction

5\. Logistic Regression training

6\. DistilBERT tokenization and fine-tuning

7\. Performance evaluation

8\. Error analysis

9\. Streamlit prototype development



\## Model Performance



The final evaluation was conducted using an independent test set.



| Metric | Logistic Regression | DistilBERT |

|---|---:|---:|

| Accuracy | 97.72% | 98.29% |

| Precision | 95.92% | 97.76% |

| Phishing Recall | 98.07% | 97.66% |

| F1-score | 96.98% | 97.71% |

| False Positives | 41 | 22 |

| False Negatives | 19 | 23 |



DistilBERT achieved higher overall accuracy and precision, while Logistic Regression achieved slightly higher phishing recall.



\## Technologies Used



\- Python

\- Hugging Face Transformers

\- DistilBERT

\- Scikit-learn

\- PyTorch

\- Pandas and NumPy

\- Google Colab

\- Streamlit



\## Running the Application



Install the required dependencies:



```bash

python -m pip install -r requirements.txt

```



Place the trained DistilBERT model files in a folder named `distilbert\_model` next to `app.py`.



Start the application:



```bash

python -m streamlit run app.py

```



Open `http://localhost:8501` in your browser.



\*\*Note:\*\* The trained model weights are not included in this repository. They must be supplied separately.



\## Prototype Testing



Two manually written demonstration emails were tested:



| Scenario | Predicted Result | Estimated Phishing Probability |

|---|---|---:|

| Suspicious account verification email | Phishing | 99.64% |

| Legitimate project meeting reminder | Safe | 0.03% |



Both examples produced their expected classifications.



\## Ethical Considerations and Limitations



The system processes email text and does not independently verify sender identity, malicious URLs, or attachments.



Model predictions may contain false positives and false negatives. Probability scores are model estimates and should not be interpreted as guaranteed or calibrated risk measurements.



Real or confidential emails should not be included in a public repository. The system is intended as a research prototype rather than a replacement for enterprise email security controls.



\## Future Improvements



\- Explainable AI techniques

\- Additional multilingual datasets

\- Evaluation on newer phishing campaigns

\- URL and sender reputation analysis

\- Improved phishing recall

\- Deployment through a secure hosting platform



\## Academic Context



Developed as an individual Natural Language Processing project for a Master of Artificial Intelligence programme at the University of Wollongong in Dubai.

