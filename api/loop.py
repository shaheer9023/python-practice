import streamlit as st
from meta_ai_api import MetaAI

def main():
    # Page config
    st.set_page_config(page_title="Weather Bot", page_icon="🌤️")
    
    # Styling
    st.markdown("""
        <style>
        .big-font {
            font-size:30px !important;
            font-weight: bold;
        }
        .weather-box {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
            margin: 10px 0;
        }
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #f0f2f6;
            padding: 10px;
            text-align: center;
            font-style: italic;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Title with custom styling
    st.markdown('<p class="big-font">Weather Information Bot 🌤️</p>', unsafe_allow_html=True)
    
    # Initialize MetaAI
    llm = MetaAI()
    
    # Create a form
    with st.form(key='weather_form'):
        place = st.text_input("Enter the place (i.e city with country):")
        submit_button = st.form_submit_button(label='Get Weather Info')
        
    if submit_button:
        if place.strip():  # Check if input is not empty
            with st.spinner('Fetching weather information...'):
                instruction = f'''
                you are a custom weather bot. You need to provide the weather information of given place 
                in proper format. Return the response in following format:
                
                Location: [city, country]
                Temperature: [temp in celsius]
                Weather Condition: [condition]
                Humidity: [humidity %]
                Wind Speed: [speed in km/h]
                
                - the given place is {place}
                if user input something else then you have to tell us that you are weather bot and you can only provide weather information
                '''
                response = llm.prompt(instruction)
                
                # Display result in a custom styled box
                st.markdown('<div class="weather-box">', unsafe_allow_html=True)
                st.success("Weather Information")
                # Split the response by lines and format each line
                weather_info = response["message"].split('\n')
                for line in weather_info:
                    if line.strip():  # Only process non-empty lines
                        st.markdown(f"**{line.strip()}**")
                st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.error("Please enter a place name!")
    
    # Add some helpful information at the bottom
    st.markdown("---")
    st.markdown("ℹ️ Enter any city with country to get weather information")
    
    # Add footer with credit
    st.markdown('<div class="footer">Made with ❤️ by Shaheer Ahmad</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main() 