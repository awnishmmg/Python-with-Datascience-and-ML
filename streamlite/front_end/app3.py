import streamlit as st 
import os

def markdown_app():
    # Heading h1 to h6
    st.text('-- Heading --')
    st.markdown("# This heading h1") #h1 
    st.markdown("## This heading h2") #h2 
    st.markdown("### This heading h3") #h3 
    st.markdown("#### This heading h4") #h4 
    st.markdown("##### This heading h5") #h5 
    st.markdown("###### This heading h6") #h6 

    # Text Formatting bold,italic,deleted,inline code
    st.text('-- text formatting --')
    st.markdown("**Bold**")
    st.markdown("*italic*")
    st.markdown("~~deleted~~")
    st.markdown("`inline code`") 

    #ordered list and un-ordered list 
    st.text('-- un-ordered list--')
    st.markdown('''
        - Apple
        - Banana 
            - Yellow Banana 
            - Green Banana
        - Mango       
                ''')

    st.text('-- ordered list--')
    st.markdown('''
        1. step 1
        2. step 2
            1. sub step A 
            2. sub step B 
            3. sub step C
        3. another step 3
        4. last step 4 
                ''')
    
    st.text('-- ordered list with abc--')
    st.markdown('''
        1. step 1
        2. step 2
            a. sub step A 
            b. sub step B 
            c. sub step C
        3. another step 3
        4. last step 4 
                ''')
    

    # Marquee tag 
    st.text('-- marquee Tag--')
    st.markdown('''
    <marquee style="color:red">This is Marquue Tag</marquee>
                ''',unsafe_allow_html=True)
    
    st.text('-- Rendered HTML--')
    current_path = os.path.abspath(__file__)
    front_end_path = os.path.dirname(current_path)
    file_path=os.path.join(front_end_path,'templates','index.html')
    #st.text(file_path)
    with open(file_path,'r') as index_html:
        content = index_html.read()
        st.markdown(content,unsafe_allow_html=True)


    #code blocks with copy paste
    st.text('-- code blocks--')
    st.code('''
            import sys
            def main():
                ...
                ...
            sys.exit(main())
            
    ''')


    #tables using markdown
    st.text('-- Table using markdown--')
    st.markdown('''
     | name | class | marks |
     |------|-------|-------|
     |ram   | Btech | 100   |
     |shyam | mca   | 80    |
     |aman  | bba   | 70    |                    
                ''')