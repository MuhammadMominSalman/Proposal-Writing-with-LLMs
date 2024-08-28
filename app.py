import streamlit as st

st.title("Proposal Writing Assistant")
topic = st.text_input("Enter the proposal topic:")

if st.button("Generate Proposal"):
    proposal = proposal_chain.run({"topic": topic})
    st.write("Generated Proposal:")
    st.text(proposal)