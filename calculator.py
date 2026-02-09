import streamlit as st

st.set_page_config(page_title="Calculator")
st.title("Simple Streamlit Calculator")

col1, col2 = st.columns(2)
with col1:
	num1 = st.number_input("First number", value=0.0)
with col2:
	num2 = st.number_input("Second number", value=0.0)

operation = st.selectbox("Operation", ("Add", "Subtract", "Multiply", "Divide"))

if st.button("Calculate"):
	if operation == "Add":
		result = num1 + num2
	elif operation == "Subtract":
		result = num1 - num2
	elif operation == "Multiply":
		result = num1 * num2
	elif operation == "Divide":
		if num2 == 0:
			st.error("Cannot divide by zero")
			result = None
		else:
			result = num1 / num2

	if 'result' in locals() and result is not None:
		st.success(f"Result: {result}")
