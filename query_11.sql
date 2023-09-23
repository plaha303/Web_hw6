select t.teacher_name, s.student_name, avg(g.grade) as avg_grade
from teachers t
join subjects sb on t.teacher_id = sb.teacher_id
join grades g on sb.subject_id = g.subject_id
join students s on g.student_id = s.student_id
where t.teacher_id = 3 and s.student_id = 9
group by t.teacher_name, s.student_name;