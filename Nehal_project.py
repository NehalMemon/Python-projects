# Function to recommend fields based on criteria
def recommend_fields(intermediate_marks, percentage, field_of_interest):
    recommended_fields = []

    # Engineering
    if intermediate_marks >= 825 and percentage >= 75 and field_of_interest == 'engineering':
        recommended_fields.append(' BS Computer Science')
        recommended_fields.append(' Software Engineering')
        recommended_fields.append(' Biomedical Engineering')

    if intermediate_marks >= 715 and percentage >= 65 and field_of_interest == 'engineering':
        recommended_fields.append(' Mechanical Engineering')
        recommended_fields.append(' Electrical Engineering')
        recommended_fields.append(' Textile Engineering')

    if intermediate_marks >= 550 and percentage >= 50 and field_of_interest == 'engineering':
        recommended_fields.append(' Civil Engineering')
        recommended_fields.append(' Chemical Engineering')
    if intermediate_marks <= 550 and percentage <= 50 and field_of_interest == 'engineering':
        recommended_fields.append(' Enviromental Engineering')
        recommended_fields.append(' Enviromental Engineering')
        recommended_fields.append(' Architecture Engineering')

    # Medicine
    if intermediate_marks >= 935 and percentage >= 85 and field_of_interest == 'medicine':
        recommended_fields.append(' Medicine(MBBS)')
        recommended_fields.append(' Dentistry(BDS)')
    if intermediate_marks >= 825 and percentage >= 75 and field_of_interest == 'medicine':
        recommended_fields.append(' BS Micro Biology')
        recommended_fields.append(' BS Biochemistry')
        recommended_fields.append(' DR of Pharmacy')
    if intermediate_marks >= 660 and percentage >= 60 and field_of_interest == 'medicine':
        recommended_fields.append(' BS Physiology')
        recommended_fields.append(' BS Biostatics')
    if intermediate_marks <= 660 and percentage <= 60 and field_of_interest == 'medicine':
        recommended_fields.append(' BS Zoology')
        recommended_fields.append(' BS Botany')
    # Buisness
    if intermediate_marks >= 935 and percentage >= 85 and field_of_interest == 'commerce':
        recommended_fields.append(' ACCA')
        recommended_fields.append(' CA')
    if intermediate_marks >= 770 and percentage >= 70 and field_of_interest == 'commerce':
        recommended_fields.append(' Buisness Administration')
        recommended_fields.append(' B.Sc. in Economics')
    if intermediate_marks >= 660 and percentage >= 60 and field_of_interest == 'commerce':
        recommended_fields.append(' Certified Public Accountant')
        recommended_fields.append(' Bachelor in Foreign Trade')

    if intermediate_marks <= 660 and percentage <= 60 and field_of_interest == 'commerce': 
         recommended_fields.append(' Journalism and Mass Communication')
         recommended_fields.append(' Digital Marketing')
        

    # Display recommendations
    if recommended_fields:
        print("Recommended fields:")
        for i in recommended_fields:
            print(">"+ i)
    else:
        print("Sorry, no fields recommended based on the provided criteria.")

# Example usage
intermediate_marks = int(input("Enter intermediate marks: "))
percentage = intermediate_marks/11
field_of_interest = input("Enter field of interest: ")
recommend_fields(intermediate_marks, percentage, field_of_interest)
