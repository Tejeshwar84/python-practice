if __name__ == '__main__':
    students = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    unq_score = sorted({score for score , score in students})
    second_lowest_score = unq_score[1]
    students_lowest_score = sorted(name for name , score in students if score == second_lowest_score)
    
    for name in students_lowest_score:
        print(name)
