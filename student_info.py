grade_scale = {
        80.0: "A",
        75.0: "B+",
        70.0: "B",
        65.0: "C+",
        60.0: "C",
        55.0: "D+",
        50.0: "D",
        45.0: "E",
        # 0 to 44.9 is F
}

def convert_score_to_grade(score: int):
    '''
        converts score to corresponding grade
        params: score
        returns: grade: str
    '''
    for grade_score, grade in grade_scale.items():
        if score >= grade_score:
            return grade
    return "F"

def get_student_data(fname: str, lname: str, score: int):
    ''' 
        input function
        params: fname: str, lname: str, score: int
        returns: fname, lname, score, grade as message: str
    '''
    grade = convert_score_to_grade(score)
    message = print(f"Student Name: {lname},{fname}\nScore: {score}\nGrade: {grade}")
    return message

if __name__ == "__main__":
    get_student_data("Daniel", "Ntiri",79)
