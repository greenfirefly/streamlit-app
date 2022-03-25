import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


@st.cache
def load_data(file, nrows=100):
    data = pd.read_csv(file, nrows=nrows)
    return data


header = st.container()
dataset = st.container()
features = st.container()
details = st.container()
model_training = st.container()
data_predicting_container = st.container()
data_predicting = st.expander(label='Click here')


with header:
    st.title('To fail or not to fail')
    st.header('Predicting hard drive failure ahead of time.')
    st.write('Hard Drive failure can have a negative impact, be it for a private persons loss of valuable memories or technical failure of mass storage companies. While individual persons mostly only rely on one individual hard drive and might not possess a back-up of their data, data storage facilities apply regular backup measures to prevent loss of data.')

   
   
with dataset:
    st.header('Accessing our data set')
     
    data_load_state = st.text('Loading data...')
    data = load_data('https://raw.githubusercontent.com/greenfirefly/streamlit-app/main/data/ST4000DM000_failure.csv', nrows=1000)
    
    st.subheader('Raw data')
    st.dataframe(data)
    data_load_state.text('Loading data...done!')

    labels = 'failure', 'no failure'
    pie_data = data['failure'].value_counts()
    st.write(pie_data)

    fig, ax = plt.subplots(1,1)
    ax.set_title('Pie Chart')
    ax.pie(pie_data, labels=labels)
    st.pyplot(fig)

    

with features:
    st.header('Features we created')

    st.session_state['type'] = st.radio('Which feature do you want to look at?', ['smart_5_raw', 'smart_183_raw', 'smart_184_raw', 'smart_187_raw'])

    fig, ax = plt.subplots()
    ax.set_title(st.session_state['type'])
    ax.hist(data[st.session_state['type']], bins=20)
    st.pyplot(fig)
    
    chart_data = pd.DataFrame(data[st.session_state['type']], data['date'])
    st.line_chart(chart_data)


with details:
    serial = data.sample(1)['serial_number'].to_list()[0]
    test_data = data[data['serial_number'] == serial]
    st.write(test_data)

    fig, ax = plt.subplots()
    ax.plot(test_data['date'], test_data['smart_5_raw'])
    st.pyplot(fig)
    

with model_training:
    st.header('Time to train')

with data_predicting_container:
    with data_predicting:
        st.header('Wanna check it out?')
        st.text('Try uploading your data and we predict you how long your hard drive will last')


        uploaded_file = st.file_uploader("Choose a file")
        
        if uploaded_file is not None:
            dataframe = pd.read_csv(uploaded_file)
            st.write(dataframe.head(3))
            st.balloons()

        st.button('Predict')


st.sidebar.title('Fail or not to Fail!')
st.sidebar.header("Gurdians of the Memroy")
st.sidebar.text('Felix, Chang Ming, Andreas & Daniela')

