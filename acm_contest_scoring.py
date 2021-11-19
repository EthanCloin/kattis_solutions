'''
Algorithm to find team score: (kattis runtime 0.05s)
    INPUT DATA FORMAT:  
      input = [
                [time_stamp1, problem_id1, result1],
                 ...
              ]

    STORAGE DATA FORMAT:
      correct_answers = [
                        [time_stamp1, correct_problem_id, result1]
                        ]
                      
      wrong_answers=  [
                      [time_stamp1, wrong_problem_id, result1
                      ]
      time_score = 0
      right_count = 0

---------------------------------------------------------
PSEUDOCODE:

FOR each row of input
  IF input.result == "right"
      PUSH to correct_answers
  PUSH to wrong_answers

FOR each correct_answer
    ADD time_stamp to time_score
    ADD 1 to right_count
    FOR each wrong_answer
        IF wrong_problem_id == correct_problem_id
            time_score += 20
            
---------------------------------------------------------

'''
import sys

# declare storage vars
right_answers = []
wrong_answers = []
right_count = 0
time_score = 0

# read all input lines
for i in sys.stdin:
    input_row = i.split()

    if len(input_row) > 2:
        if input_row[2] == 'right':
            right_answers.append(input_row)
        elif input_row[2] == 'wrong':
            wrong_answers.append(input_row)
    else:
        break
        
# loop thru right_answers and 
for right_ans in right_answers:

    # add time value to total score
    time_score += int(right_ans[0])
    right_count += 1
    
    # search wrong_answers for matching problem_id
    for wrong_ans in wrong_answers:
        if wrong_ans[1] == right_ans[1]:
            time_score += 20

print(f'{right_count} {time_score}')
