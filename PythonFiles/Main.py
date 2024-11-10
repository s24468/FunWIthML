import sys
sys.path.append("D:/PROJECTS/PythonProjects/FunWIthML")
from PythonFiles.ImportMechanism import setup_imports

st, pd, np, px, pipeline = setup_imports()


st.title("Simple Streamlit App")
st.write("This app demonstrates basic Streamlit functionality.")

# Slider for user input
user_input = st.slider("Select a number", 0, 100)

# Display input and a random chart
st.write(f"User input: {user_input}")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
st.line_chart(chart_data)
