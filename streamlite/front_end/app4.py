import streamlit as st 

def form_components():
    # Input box 
    st.text_input(
        label='Name',
        value="Awnish Kumar",
        # placeholder='Mr Banta',
        max_chars=30,
        type='default',
        key=None, #id 
        help='Enter your full name as per Adhar card',
        autocomplete=None,
        label_visibility='collapsed',
        disabled=False
    )

    # Password Field
    st.text_input(
        label='Enter The Password',
        placeholder='password@123',
        max_chars=15,
        type='password'
    )

    # collpase property works in expander component
    # collapse = True
    with st.expander('Read More',expanded=False):
        st.write('This is Extra Line Hidden')

    # Text Area 
    st.text_area(
        label='Address',
        value='',
        height=50,
        max_chars=None,
        key=None,
        help='Home Address',
        placeholder='Home Address',
        label_visibility='visible',
        disabled=False
    )

    # number input 
    st.number_input(
        label='Quantity',
        min_value=1,
        max_value=5,
        value=2,
        step=1,
        format=None,
        key=None,
        help='Qty : 2',
        label_visibility='visible',
        disabled=False
    )

    # Enter the Percentage
    st.number_input(
        label='Enter the Amount',
        min_value=500.00,
        max_value=5000.00,
        value=None,
        step=100.00,
        format="%.2f",
        key=None,
        help='Enter Amount in INR',
        label_visibility='visible',
        disabled=False
    )

    #select box 
    st.selectbox(
        label='Select the course',
        options=['Btech','MCA','MBA','BCA'],
        index=1,
        key=None,
        placeholder=None,
        label_visibility='visible',
        disabled=False
    )

    #multi select
    st.multiselect(
        label='select skills',
        options=['python','html','css','mern','dsa'],
        max_selections=3,
        default=None,
        format_func=str,
        key=None,
        placeholder=None,
        help=None,
        label_visibility='visible',
        disabled=False
    )

   #Radio is used single selection 
    st.radio(
       label='Select gender',
       options=['male','female','other'],
       horizontal=True, #vertical = True 
       index=0,
       format_func=str,
       key=None,
       help=None,
       label_visibility='visible',
       disabled=False,
   )
   #checkbox is used for Terms and conditions
    remeber_me = st.checkbox('Accept Terms & Conditions')

    st.text('Select Your Hobbies:')
    is_dancing = st.checkbox(
        label='Dancing',
        value=False,
        key=None,
        label_visibility='visible',
        disabled=False
    )

    is_reading = st.checkbox(
        label='reading',
        value=False,
        key=None,
        label_visibility='visible',
        disabled=False
    )

    is_cooking = st.checkbox(
        label='cooking',
        value=False,
        key=None,
        label_visibility='visible',
        disabled=False
    )