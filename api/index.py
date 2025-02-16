from streamlit.web.bootstrap import run
import os

def handler(event, context):
    os.system("streamlit run loop.py --server.address=0.0.0.0 --server.port=8080")
    return {
        'statusCode': 200,
        'body': 'Streamlit app is running'
    } 