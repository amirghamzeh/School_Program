lessons = []

while True:
 lessonName = input('Enter lesson name: ')
 lessons.append(lessonName)
 stillWant = input('Do you want still add more book ? (y/n) ')
 if stillWant.lower() != 'y':
  if len(lessons) >= 3:
   break
  else:
   print("You have enter 3 lessons or more.")
  

secondChance = int(input("How many second chances does the student have again?"))

totalScore = 0   
for lesson in lessons:
 score = int(input('Enter score for ' + lesson + ': '))
 totalScore += score
 
 if score > 10:
  print(lesson, 'pass')
 elif score > 7 and secondChance > 0:
  print('second chance for ', lesson)
  secondChance -= 1
 else:
  print(lesson, 'faild')

avg = totalScore / len(lessons)

print('your diploma score is:', avg)