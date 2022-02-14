'''
Mysql的多表查询

1）左联结（left join），联结结果保留左表的全部数据
2）右联结（right join），联结结果保留右表的全部数据
3）内联结（inner join），取两表的公共数据
写的时候还可以用 as 代指某个表，如下：
select a.学号,a.姓名,b.课程,b.成绩 from 学生 as a left join 成绩 as b on a.学号=b.学号;
'''
select FirstName, LastName, City, State
from Person left join Address
on Person.PersonId = Address.PersonId
;

