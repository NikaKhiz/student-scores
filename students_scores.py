import pandas as pd

class StudentScores:
    def __init__(self, filepath, subjects):
        self.data = pd.read_csv(filepath)
        self.subjects = subjects
        self.clean_data()
        self.failed_students = None
        self.average_scores = None
        self.highest_scores = None
        self.worst_subject = None
        self.students_upgraded = None
        self.upgraded_count = None


    def clean_data(self):
        # Convert subject scores to numeric and fill NaN values with 0
        self.data[self.subjects] = self.data[self.subjects].apply(pd.to_numeric, errors='coerce')
        self.data.fillna(0, inplace=True)


    def students_who_failed(self):
        # Return students who failed in any subject
        condition = (self.data[self.subjects] < 50).any(axis=1)
        failed_students = self.data[condition]
        return failed_students.drop_duplicates(subset='Student')
    

    def average_of_scores_by_semesters(self):
        # Return average scores grouped by semester

        return self.data.groupby('Semester').mean(numeric_only=True)


    def analyze(self):
        # Analyze and store values in properties 

        self.failed_students = self.students_who_failed()
        self.average_scores = self.average_of_scores_by_semesters()



    def display_analyzed_data(self):
        # Print the results

        print('Students who didn\'t pass exams:\n', self.failed_students)
        print('-------------------------------')
        print('Average scores by semesters:\n', self.average_scores)
        print('-------------------------------')


def main():
    SUBJECTS = ['Math', 'Physics', 'Chemistry', 'Biology', 'English']
    analyzer = StudentScores('student_scores_random_names.csv', SUBJECTS)
    analyzer.analyze() 
    analyzer.display_analyzed_data() 


if __name__ == '__main__':
    main()
