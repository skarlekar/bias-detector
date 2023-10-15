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

The objective of Bias Detector is to foster inclusivity and ensure fairness by identifying potential biases that could unintentionally creep into documents. It helps eliminate the implicit undertones in your text that might otherwise go unnoticed without a **Bias Detector**.

## Features

Through an interactive web-based interface, users have the control to select or deselect the types of biases they want to be identified in their documents. This feature ensures a user has the independence to customize the utility's functionality according to their specific needs.

Upon execution, Bias Detector scans the text or document input, detecting any biases based around the categories listed above. It subsequently returns a comprehensive JSON object. This object contains a count of the detected biases, a detailed explanation pinpointing where in the text the bias was found, as well as snippets of the document with the highlighted bias term. The structure of the output makes it easy to trace back the detected biases to their origins in the text.

In terms of its tech stack, Bias Detector is engineered with LangChain for methodical prompt control and uses Streamlit for rendering a smooth and interactive user interface.

Join us in our mission of creating a more understanding and inclusive world by eliminating unconscious bias from texts and documents with Bias Detector.

## Logic

The provided Python script [detect-bias.py](https://github.com/skarlekar/bias-detector/blob/7f48dab7ecc40692055cf22b2f37b02ebd46fecd/detect-bias.py) uses GPT model to detect bias in a given text based on various categories. Here's a step-by-step breakdown of the code:

1. Import the required libraries: `streamlit` for web application, `streamlit_authenticator` for authentication process, `yaml` for reading configuration, `ChatOpenAI` for OpenAI chat model, `ChatPromptTemplate` for generating prompts, `ResponseSchema` and `StructuredOutputParser` for structuring the response from GPT model, and `json` for handling JSON data.
2. Define the function `plot_chart()`. This function is used to display a table and chart which represent the detected bias results based on the categories.
3. In the `process()` function:

   - Prompt the user to enter the text they want to analyze and select the bias categories they want to detect.
   - Define the response schemas for each category, which are used to organize and interpret the response from GPT Model.
   - Create a chat model using `ChatOpenAI` and ask the user to input the text they want to check for bias.
   - Use the provided text to create a prompt for the GPT model using a template string. The prompt asks GPT to identify biases related to the selected categories.
   - Process the GPT model's response, display warnings based on the detected bias, and explain the results. It also highlights area where the biases were found in a markdown format.
   - Finally, it calls `plot_chart()` function to display results in a form of table and chart.
4. The `authenticate()` function takes care of the user authentication process by reading a configuration file that's loaded using `yaml`. It then verifies the user credentials and maintains session state with options to login and logout.
5. `hide_streamlit_menu_and_footer()` is a function to hide the Streamlit’s hamburger menu and footer by injecting a CSS code.
6. The `main()` function sets up Streamlit's parameters such as the title of the page. It also calls `hide_streamlit_menu_and_footer()` to customize the interface, and runs the `authenticate()` function.

In summary, this script uses the instructions provided to GPT-4, a LLM from OpenAI, to count occurrences and highlight biased phrases in the inputted text. It also authenticates users and has a specific UI/UX design setup for the web interface. The final results are shown both in a textual form and visualized as a bar chart and table.

## Call to Action

Incorporate Bias Detector into your workflows to stay aware and ensure your language upholds the values of fairness and objectivity. By implementing instant and consistent bias detection, you can critically review and improve your texts in a way that promotes understanding and respect for all.

## Disclaimer

Please be aware that Bias Detector is a tool for assisting in bias detection, and while it attempts to be as accurate as possible, it may not capture all nuances of human language. To help us improve the utility, feedback and contributions are always welcome.
