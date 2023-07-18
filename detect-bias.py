import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser
import json

def plot_chart(prohibited_phrases, result):
    response = {}
    for p in prohibited_phrases:
        if p in result:
            val = result[p]
            response.update({p: val})
        else:
            response.update({p: 0})
    st.markdown('*Table*')
    st.dataframe(response, use_container_width = True)
    st.markdown('*Chart*')
    st.bar_chart(response)

def process():
    st.header("Enter text to detect bias")
    prohibited_phrases = ['sexuality','neighborhood', 'disability', 'marital status', 'age', 'race', 'ethnicity', 'religion', 'gender']
    options = st.sidebar.multiselect('Bias to Detect', prohibited_phrases, prohibited_phrases )
    options_str = str.join(',', options)
    options_str_key = options_str.replace(" ", "_") + ", bias_type_count, highlighted_text, explanation"

    sexuality_schema = ResponseSchema(name = "sexuality", description = "Total number of sexual bias found in the given text. Examples of sexual bias is: male-dominated, women-owned", type = "number")

    neighborhood_schema = ResponseSchema(name = "neighborhood", description = "Total number of neighborhood bias found in the given text. Examples of neighborhood bias is: highly sought-after neighborhood, good schools, rich community, poor neighborhood.", type = "number")

    disability_schema = ResponseSchema(name = "disability", description = "Total number of disability bias found in the given text. Examples of disability bias is: mental disorder, blind, deaf, bipolar disorder, ADHD, hearing loss, epilepsy.", type = "number")

    marital_status_schema = ResponseSchema(name = "marital_status", description = "Total number of marital status bias found in the given text. Examples of marital status bias is: single, married, separated, divorced, widowed", type = "number")

    age_schema = ResponseSchema(name = "age", description = "Total number of age bias found in the given text. Examples of age bias is: elderly, old person, old people, very young.", type = "number")

    race_schema = ResponseSchema(name = "race", description = "Total number of race bias found in the given text. Examples of race bias is: white, black, hispanic, asian, native american.", type = "number")

    ethnicity_schema = ResponseSchema(name = "ethnicity", description = "Total number of ethnicity bias found in the given text. Examples of ethnicity bias is: mexican, african-american, chinese, japanese, indian, french-canadian, indigenous-people, pacific-islander, filipino, cuban.", type = "number")

    religion_schema = ResponseSchema(name = "religion", description = "Total number of religious bias found in the given text. Examples of religious bias is: hindu temple, church, synagogue, mosque, christian, muslim, hindu, jew.", type = "number")

    gender_schema = ResponseSchema(name = "gender", description = "Total number of gender bias found in the given text. Examples of gender bias is: male, female, gay, lesbian, transgender, gender neutral, non-binary, agender, pangender, genderqueer, two-spirit, third gender, and all combination of these.", type = "number")

    bias_type_count_schema = ResponseSchema(name = 'bias_type_count', description="Total count of all type of biases found.", type = "number")

    highlighted_text_schema = ResponseSchema(name = 'highlighted_text', description="Add the highlighted section where the biased phrases are found in the given text. Use Markdown for highlighting the biased phrases that were detected. If no biases are found, leave this empty")

    explanation_schema = ResponseSchema(name = 'explanation', description= "Explain the response and your reasoning here")

    schemas = {'sexuality': sexuality_schema,'neighborhood': neighborhood_schema, 'disability': disability_schema, 'marital status': marital_status_schema, 'age': age_schema, 'race': race_schema, 'ethnicity': ethnicity_schema, 'religion': religion_schema, 'gender': gender_schema, 'total_count': bias_type_count_schema, 'highlighted_text': highlighted_text_schema, 'explanation_text': explanation_schema}

    response_schemas = [explanation_schema, bias_type_count_schema,highlighted_text_schema]
    for option in options:
        response_schemas.append(schemas[option])

    output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
    format_instructions = output_parser.get_format_instructions()

    chat = ChatOpenAI(temperature=0.0, model='gpt-4')

    user_input = st.text_area("Text to analyze:")
    if user_input:
        
        template_string = f"""
            For the following text find the total number of biases that indicates a reference to prohibited terms such as: {options_str}.
            Example of what is not a bias: "white fence", "black door", "brown pen".
            
            """         
        template_string = template_string + """
        text: {text} 

        {format_instructions}
        """
        prompt_template = ChatPromptTemplate.from_template(template_string)

        ## Create a prompt from user input
        prompt = prompt_template.format_messages (text=user_input, 
                                format_instructions=format_instructions)
        ## Call OpenAI LLM with prompt and receive response
        response = chat(prompt)

        ## Process response
        print(response.content)
        # Convert response content to JSON
        response_content = output_parser.parse(response.content)
        # Get individual elements from JSON
        bias_type_count = response_content['bias_type_count']
        highlighted_text = response_content['highlighted_text']
        explanation = response_content['explanation']

        ## Display result
        # Display no of bias types found
        st.warning(f"There were {bias_type_count} types of biases found in the given text")
        st.markdown('*Explanation*')
        st.write(explanation)
        st.markdown('*Highlights*')
        st.markdown(highlighted_text)

        # Plot table and barchart
        plot_chart(prohibited_phrases=options, result=response_content)
        # Display highlighted text from response


def authenticate():
    with open('./config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )
    name, authentication_status, username = authenticator.login('Login', 'main')
    if st.session_state["authentication_status"]:
        authenticator.logout('Logout', 'main', key='unique_key')
        st.write(f'Welcome *{st.session_state["name"]}*')
        process()
    elif st.session_state["authentication_status"] is False:
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password')
    return name, authentication_status, username

def hide_streamlit_menu_and_footer():
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            footer:after {
                content:'Made by Multifamily Architecture'; 
                visibility: visible;
                display: block;
                position: relative;
                #background-color: red;
                padding: 5px;
                top: 2px;
            }
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="Bias Detector")
    st.title("Detect bias in given text")
    hide_streamlit_menu_and_footer()
    name, authstatus, username = authenticate() 

if __name__ == '__main__':
    main()


    

