import streamlit as st
import streamlit.components.v1 as components
 



components.html(
    """
    <script src="https://www.gstatic.com/dialogflow-console/fast/messenger/bootstrap.js?v=1"></script>
    <style>#GithubIcon {  visibility: hidden;}</style>
    <df-messenger
        chat-title="AIClub"
        agent-id="3cb41952-578d-43df-a37d-f1f12bcc12e1"
        language-code="en"></df-messenger>
    """,
    height=400, # try various values to see what works best (maybe use st.slider)

)
#st.markdown(hide_github_icon, unsafe_allow_html=True)
