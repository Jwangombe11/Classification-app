# Contents of ~/my_app/streamlit_app.py
import streamlit as st

def main_page():
    st.title ("Plant Disease Identifier App")
    st.subheader("The app aids in detecting the diseases affecting your plants.")
    #st.markdown("# Main page")
    #st.sidebar.markdown("# Main page")

def page2():
    col1, col2 = st.columns([3,2])
    with col1:
        st.title ("Plant Disease Identifier App")
        image = st.file_uploader("Upload your photo", type=['jpg', 'png'])
        picture = st.camera_input("Take a picture")
        #if picture:
            #st.image(picture)
    with col2:
        st.title ("Results Panel") 
        if image:
            st.success("Image uploaded sucessfully")
            st.image(image) 
        if picture:
            st.success("Image uploaded sucessfully")
            st.image(picture)   
    #st.markdown("# Page 2 ❄️")
    #st.sidebar.markdown("# Page 2")

def page3():
    st.title ("The Team")
    st.subheader("The App was created by Explore team 11.")
    #st.markdown("# Page 3")
    #st.sidebar.markdown("# Page 3")

page_names_to_funcs = {
    "Main Page": main_page,
    "Plant Disease Identifier": page2,
    "The Team": page3,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()