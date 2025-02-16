from streamlit.web.bootstrap import run
import sys
import os

def handler(event, context):
    # Set the correct path for the streamlit app
    current_dir = os.path.dirname(os.path.abspath(__file__))
    app_path = os.path.join(current_dir, "loop.py")
    
    # Configure Streamlit
    sys.argv = [
        "streamlit",
        "run",
        app_path,
        "--server.address=0.0.0.0",
        "--server.port=8080",
        "--server.headless=true"
    ]
    
    # Run the app
    run()
    
    return {
        'statusCode': 200,
        'body': 'Streamlit app is running'
    } 