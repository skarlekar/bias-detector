# Bias Detector
Bias Detector is a machine learning utility built using OpenAI's GPT (Generative Pretrained Transformer). It leverages the power of natural language processing (NLP) to scan through documents and texts to detect various forms of biases, including but not limited to:

- Sexuality
- Neighborhood
- Disability
- Marital status
- Age
- Race
- Ethnicity
- Religion
- Gender
  
The objective of Bias Detector is to foster inclusivity and ensure fairness by identifying potential biases that could unintentionally creep into documents.

## Features

Through an interactive web-based interface, users have the control to select or deselect the types of biases they want to be identified in their documents. This feature ensures a user has the independence to customize the utility's functionality according to their specific needs.

Upon execution, Bias Detector scans the text or document input, detecting any biases based around the categories listed above. It subsequently returns a comprehensive JSON object. This object contains a count of the detected biases, a detailed explanation pinpointing where in the text the bias was found, as well as snippets of the document with the highlighted bias term. The structure of the output makes it easy to trace back the detected biases to their origins in the text.

Eliminate the implicit undertones in your text that might otherwise go unnoticed with **Bias Detector**.

In terms of its tech stack, Bias Detector is engineered with LangChain for methodical prompt control and uses Streamlit for rendering a smooth and interactive user interface.

Join us in our mission of creating a more understanding and inclusive world by eliminating unconscious bias from texts and documents with Bias Detector.

## How to Use
Incorporate Bias Detector into your workflows to stay aware and ensure your language upholds the values of fairness and objectivity. By implementing instant and consistent bias detection, you can critically review and improve your texts in a way that promotes understanding and respect for all.

## Disclaimer
Please be aware that Bias Detector is a tool for assisting in bias detection, and while it attempts to be as accurate as possible, it may not capture all nuances of human language. To help us improve the utility, feedback and contributions are always welcome.
