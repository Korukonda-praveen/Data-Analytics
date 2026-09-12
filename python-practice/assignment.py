#crete a dictionary using deatils in codegnan


    # Basic Student & Branch Information
student_info={

"student_id": "CGVI0213",
"name": "Korukonda praveen",
"branch": "Visakhapatnam",
"batch_code": "DA-Vsp-006",
"course_enrolled": "Data Analytics",
#exams avgrages
"daily_exam_avg": 79.67,
"weekly_exam_avg":77.29,
"mock_interview_avg":6.17, # the avg of 3 mock interview till now out of 10
# attendance streak tracker
"attendance_streak": 25, # till 11-09-2026
"streak_broken": 1,# 12-09-2026 due to rainfall the streak is broken
"current_streak":0, # The attendace is currently 0
}


print("=== CODEGNAN VIZAG STUDENT SUMMARY ===")
print(f"Student ID : {student_info['student_id']}")
print(f"Name       : {student_info['name']}")
print(f"Branch     : {student_info['branch']}")
print(f"Batch Code : {student_info['batch_code']}")
print(f"Course     : {student_info['course_enrolled']}")
print("-" * 30)

print("ACADEMIC SCORES:")
print(f"• Daily Exam Avg      : {student_info['daily_exam_avg']}%")
print(f"• Weekly Exam Avg     : {student_info['weekly_exam_avg']}%")
print(f"• Mock Interview Avg  : {student_info['mock_interview_avg']} / 10")
print("-" * 30)

print("ATTENDANCE TRACKER:")
print(f"• Previous Streak     : {student_info['attendance_streak']} Days")
print(f"• Streaks Broken      : {student_info['streak_broken']} time(s)")
print(f"• Current Active Streak: {student_info['current_streak']} Days")
