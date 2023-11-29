import streamlit as st

st.title('title - Geeksforgeeks')                   #title
st.header('header - Geeksforgeeks')                 #header
st.subheader('subheader - Geeksforgeeks')           #subheader
st.text('text - Geeksforgeeks')                     #text

st.markdown('# Hi')                                 #markdown
st.markdown('## Hi')
st.markdown('### Hi')
st.markdown('#### Hi')
st.markdown('Hi')

st.success('Success!')                              #success
st.info('Information!')                             #Information
st.warning('Warning!')                              #Warning
st.error('error!')                                  #error

exp = ZeroDivisionError('Division not possible')    #exception
st.exception(exp)

st.exception(ZeroDivisionError('Division not possible'))

st.help(ZeroDivisionError)                           #help
st.write("range(1,10)")                             #write
st.write(range(1,10))
st.write("1+2+3")
st.write(1+2+3)

st.subheader('Code')
st.code('x = 10 \n'                                 #code
        'for i in range(x) \n'
        '\tprint(i)')

st.subheader('Checkbox')
st.checkbox('Male')                                 #checkbox
st.checkbox('Female')

if(st.checkbox('Adult')):                          #checkbox with validation
    st.write('You are an adult')

st.subheader('Radiobutton')
Radiobutton = st.radio('Select: ', ('Male', 'Female'))     #radio button

if(Radiobutton == 'Male'):
    st.write('You are male')
else:
    st.write('You are female')

st.subheader('Selectbox')
selectbox = st.selectbox('Data Science: ', ['Data analysis','Machine learning','Natural language processing','Computer vision','Deep learning','Image processing','Web scrapping'])
st.write('you have selected: ', selectbox)

st.subheader('Multiselect')
multiselectbox = st.multiselect('Data Science: ', ['Data analysis','Machine learning','Natural language processing','Computer vision','Deep learning','Image processing','Web scrapping'])
st.write('You have selected: ', len(multiselectbox), 'Courses')

st.subheader('Button')
if(st.button('Click me')):
    st.write('Thanks for clicking me')

st.subheader('Slider')
vol = st.slider('Select level',1,10,step = 1)
st.write('Volume is:', vol)

st.subheader('Text Input')                                 #Text Input
name = (st.text_input("Name: "))
password = (st.text_input("Password: ", type = 'password'))
if(name):
    st.write("Hi,",name)

st.subheader('Text area')                                   #text area
st.text_area('Write about urself in 500 words')

st.subheader('Input Number')                                   #text area
st.number_input('Select your age',1,100)

st.subheader('Input Date')                                   #text area
st.date_input('Select Date')

st.subheader('Input Time')                                   #text area
st.time_input('Select Time')
