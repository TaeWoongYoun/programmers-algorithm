def solution(ineq, eq, n, m):

    a = ineq == "<" and eq == "=" and n <= m 
    b = ineq == ">" and eq == "=" and n >= m 
    c = ineq == "<" and eq == "!" and n < m 
    d = ineq == ">" and eq == "!" and n > m 

    if a or b or c or d:
        return 1
    else :
        return 0