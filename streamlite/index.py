
import sys 
import streamlit as st

from front_end import app1
from front_end import app2
from front_end import app3
from front_end import app4


def main():
    
    st.title("My Streamlite App")
    st.markdown('#### Streamlite App')

    print('Main App Running on localhost')
    #app1.first_app()
    #app2.tabbed_component()
    # app3.markdown_app()
    app4.form_components()


sys.exit(main())
