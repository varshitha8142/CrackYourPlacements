CREATE FUNCTION getNthHighestSalary(N IN NUMBER) RETURN NUMBER IS
result NUMBER;
BEGIN
    /* Write your PL/SQL query statement below */
    select salary into result
from (select distinct salary, dense_rank() over(order by salary desc) r
from employee)
where r = N;
    RETURN result;
END;