
import streamlit as st
import torch

from pathlib import Path
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification
)

st.set_page_config(
    page_title="PhishGuard AI",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ PhishGuard AI")
st.subheader("AI-Powered Phishing Email Detection")
st.write(
    "Analyze email content using a fine-tuned "
    "DistilBERT Natural Language Processing model."
)

@st.cache_resource
def load_ai_model():
    model_path = Path(__file__).resolve().parent / "distilbert_model"

    tokenizer = AutoTokenizer.from_pretrained(
        str(model_path)
    )

    model = AutoModelForSequenceClassification.from_pretrained(
        str(model_path)
    )

    model.eval()

    return tokenizer, model

tokenizer, model = load_ai_model()

st.divider()

email_text = st.text_area(
    "Enter email content:",
    placeholder="Paste the email subject and body here...",
    height=200
)

if st.button("Analyze Email", type="primary"):

    if not email_text.strip():
        st.warning("Please enter an email to analyze.")

    else:
        inputs = tokenizer(
            email_text,
            return_tensors="pt",
            truncation=True,
            max_length=256
        )

        with torch.no_grad():
            outputs = model(**inputs)
            probabilities = torch.softmax(
                outputs.logits, dim=1
            )[0]

        phishing_probability = probabilities[1].item()
        prediction = int(torch.argmax(probabilities).item())

        st.divider()
        st.subheader("AI Analysis Result")

        if prediction == 1:
            st.error("⚠️ Phishing Email Detected")
        else:
            st.success("✅ Classified as Safe Email")

        st.metric(
            "Estimated Phishing Probability",
            f"{phishing_probability * 100:.2f}%"
        )

        st.progress(phishing_probability)

        st.info(
            "This AI system analyzes email text only. "
            "It does not verify sender identity, links, "
            "or attachments. Predictions are not guaranteed."
        )

st.divider()
st.caption("Master of Artificial Intelligence | NLP Project")
