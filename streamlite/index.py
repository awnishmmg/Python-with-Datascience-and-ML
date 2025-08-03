
import sys 
import streamlit as st

from front_end import app1
from front_end import app2


def main():
    
    st.title("My Streamlite App")
    st.markdown('#### Streamlite App')

    print('Main App Running on localhost')
    app2.tabbed_component()

sys.exit(main())
