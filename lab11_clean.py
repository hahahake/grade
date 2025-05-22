import streamlit as st

grading = {
    'Labs': 5,
    'Assignment 1': 15,
    'Assignment 2': 15,
    'Final Exam': 65
}

# TODO 1: Setup
# 1.1: Give the page a title (and optionally an icon) using set_page_config~
st.set_page_config("title")

# You can also change the title displayed on the app if you want!
st.title("ISOM3400 Grade Calculator")
st.write("Let's see if you will pass this course~")


# TODO 1.2: Create a form to group the input together.
#           You can choose to use the 'with' notation (given) or directly call methods on the form object.
with st.form("input form"):

    # TODO 2: Ask for user input by creating number inputs/sliders. (Please remove the None values!)
    # You may define max/min values to restrict the valid range.
    labs_attended = st.number_input("Number of labs attended (max: 12)", min_value=0, max_value=12, step=1)
    asm1_score = st.number_input("Assignment 1 Score (out of 100)" , min_value=0, max_value=100, step=1)
    asm2_score = st.number_input("Assignment 2 Score (out of 100)" , min_value=0, max_value=100, step=1)
    final_score = st.number_input("Final Score (out of 100)" , min_value=0, max_value=100, step=1)

    # Don't forget the submit button! You can also pass in text to display on the button.
    click_submit = st.form_submit_button("Submit") 


# TODO 3: Calculate scores
if click_submit: 
    # When the click_submit button returns True, all obtained values will be sent to the Streamlit server.
    # Process the obtained values and calculate the total (weighted) score!
    # (You can refer to the grading dictionary at the top for the weights.)
 # Calculate lab score
    if labs_attended >= 10:
        lab_score = grading['Labs']  # Full credit for labs
    else:
        lab_score = grading['Labs'] * (labs_attended * 0.1)  # 10% per lab attended

    # Calculate weighted scores
    total_score = (
        (lab_score * 0.1) +  # Labs contribute 10% of total score
        (asm1_score * (grading['Assignment 1'] / 100)) +  # Assignment 1
        (asm2_score * (grading['Assignment 2'] / 100)) +  # Assignment 2
        (final_score * (grading['Final Exam'] / 100))  # Final Exam
    )




    # You should then display the calculated score on the web app. (e.g. with st.write()/st.markdown()...)

    # TODO 4: Display result
    # Once the total score has been calculated, let the user know if they are likely to pass the course or not.
    # Note that we stay in the indented block under if click_submit.
    # We do not want anything to be displayed if the user has not submitted yet.
    # Display the calculated total score
    st.write("### Calculated Total Course Score:")
    st.write(f"{total_score:.2f} out of 100")

    if total_score < 50:
        st.write("🚨 You may fail the course.")
    else:
        st.write("🎉 You are likely to pass the course!")





    
