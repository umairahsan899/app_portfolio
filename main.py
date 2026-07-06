import streamlit as st
st.set_page_config(layout="wide")
col1,col2=st.columns(2)
with col1:
    st.image("006 images/photo.JPG",width=300)
with col2:
    st.title("Umair Ahsan")
    content1= """I am a dynamic professional working at the intersection of digital strategy,
     visual design, and technology. With a solid foundation in digital marketing and a
      background in computer science, I specialize in creating impactful online
       experiences—from high-converting social media campaigns to functional
        software applications.I believe that the best digital solutions happen when data
         meets creativity. Whether I am analyzing network concepts, building intelligent
          algorithms, designing a fresh visual layout, or optimizing an ad campaign,
           my goal is always the same: to deliver results that matter."""
    st.info(content1)
content2="""Below you can find some apps i built in python.So feel easy to contact me."""
st.write(content2)