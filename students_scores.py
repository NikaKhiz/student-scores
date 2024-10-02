import pandas as pd
import json

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


    def students_with_highest_scores(self):
        # Return students with the highest total scores

        self.data['Total'] = self.data[self.subjects].sum(axis=1)
        total = self.data.groupby('Student')['Total'].sum()
        max_score = total.max()
        top_students = total[total == max_score]
        return top_students
    

    def subject_with_lowest_score(self):
        # Return the subject with the lowest average score

        subjects_avg = self.data[self.subjects].mean()
        worst_score = subjects_avg.min()
        worst_subject = subjects_avg[subjects_avg == worst_score]
        return worst_subject
    

    def students_who_upgraded_result_by_semester(self):
        # Return students who upgraded their scores semester by semester

        grouped_data = self.data.groupby(['Student', 'Semester']).mean(numeric_only=True).reset_index()
        upgraded_students = []
        for student, student_data in grouped_data.groupby('Student'):
            previous_avg = 0
            for row in student_data.itertuples(index=False):
                current_avg = (row.Math + row.Physics + row.Chemistry + row.Biology + row.English) / len(self.subjects)
                if current_avg > previous_avg and student not in upgraded_students:
                    upgraded_students.append(student)
                previous_avg = current_avg

        # shrink generated data
        if len(upgraded_students) > 20:
            display_students = upgraded_students[:20] + ["..."] + upgraded_students[-20:]
        else:
            display_students = upgraded_students
            
        return json.dumps(display_students, indent=4), len(upgraded_students)
    

    def analyze(self):
        # Analyze and store values in properties 

        self.failed_students = self.students_who_failed()
        self.average_scores = self.average_of_scores_by_semesters()
        self.highest_scores = self.students_with_highest_scores()
        self.worst_subject = self.subject_with_lowest_score()
        self.students_upgraded, self.upgraded_count = self.students_who_upgraded_result_by_semester()






    def display_analyzed_data(self):
        # Print the results

        print('Students who didn\'t pass exams:\n', self.failed_students)
        print('-------------------------------')
        print('Average scores by semesters:\n', self.average_scores)
        print('-------------------------------')
        print('Students with highest scores:\n', self.highest_scores)
        print('-------------------------------')
        print('Worst subject:\n', self.worst_subject)
        print('-------------------------------')
        print(f'Students who have upgraded their scores: {self.students_upgraded}')
        print(f'Total number of students who have upgraded their scores: {self.upgraded_count}')
        print('-------------------------------')


def main():
    SUBJECTS = ['Math', 'Physics', 'Chemistry', 'Biology', 'English']
    analyzer = StudentScores('student_scores_random_names.csv', SUBJECTS)
    analyzer.analyze() 
    analyzer.display_analyzed_data() 


if __name__ == '__main__':
    main()
