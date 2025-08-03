import streamlit as st 

def tabbed_component():
    st.write('Tabbed component')
    tabs = st.tabs(['Profile','Grades','Attendance','Fees'])
    profile,grades,attendance,fees  = tabs 
    
    #Profile
    with profile:
        st.header('Profile')
        st.text('Name: Awnish Kumar')
        st.text('Class: Btech')
        st.text('Year : 4rth Year')


    #Grades Tabl
    with grades:
        st.header('My Grades')
        grades = {
            'Math' : 'A',
            'Physics' : 'A+',
            'English' :'B',
            'Hindi' : 'B+'
        }
        st.table(grades)

    #attendance Tab
    with attendance:
        st.header('Attendance')
        st.metric('Overall Attendance','80%')
        st.progress(0.80)
    #Fees Tab
    with fees:
        st.header('Fees')
        fees_data = {
            'total' : '1,000,00',
            'paid' : '75,000',
            'due' : '25,000'
        }

        st.table(fees_data)
        st.warning('Pay the Amount Pending before 15th August')
        


