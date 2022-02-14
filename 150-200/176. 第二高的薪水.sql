'''
https://leetcode-cn.com/problems/second-highest-salary/solution/tu-jie-sqlmian-shi-ti-ru-he-cha-zhao-di-ngao-de-sh/

1.Mysql 使用 limit 和 offset

limit n子句表示查询结果返回前n条数据, offset n表示跳过x条语句, limit y offset x 分句表示查询结果跳过 x 条数据，
读取前 y 条数据,使用limit和offset，降序排列再返回第二条记录可以得到第二大的值。

select distinct 成绩
from 成绩表
where 课程='语文'
order by 课程,成绩 desc
limit 1,1;          # 跳过1条数据，取当前位置的--前1条。该行的,可以换成offset。 offest : 英译，偏移量。

2.Mysql: IFNULL(expression, alt_value)
如果第一个参数的表达式 expression 为 NULL，则返回第二个参数的备用值。

3.没有查询结果就返回NUll的另一个方法：将查询结果作为临时表。
SELECT
    (SELECT DISTINCT
            Salary
        FROM
            Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary
;
'''
