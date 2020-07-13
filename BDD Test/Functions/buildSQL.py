#! /usr/bin/python3
# -*- coding: utf-8 -*-


import pymysql


def createRequestTextAon(column, criterias_and, criterias_not, criterias_or):
    """Write the end of SQL request for a search with AND (or basic), OR and NOT. Corresponding structure :
    (((column LIKE '%~%' AND column LIKE '%~%') OR (column LIKE '%~%' AND column LIKE '%~%')) AND (column NOT LIKE '~'))
    Return the request as a list."""
    request = [" (((%s LIKE '%%%s%%'" %(column, criterias_and[0])]
    lrequesta = len(criterias_and)
    lrequesto = len(criterias_or)
    lrequestn = len(criterias_not)
    
    for nb in range(1,lrequesta):
        request.append(" AND %s LIKE '%%%s%%'" %(column, criterias_and[nb]))

    request.append(") OR (%s LIKE '%%%s%%'" % (column, criterias_or[0]))
    
    for nb in range(1, lrequesto):
        request.append(" AND %s LIKE '%%%s%%'" % (column, criterias_or[nb]))
    
    request.append(")) AND (%s NOT LIKE '%%%s%%'" % (column, criterias_not[0]))
    
    for nb in range(1, lrequestn):
        request.append(" AND %s NOT LIKE '%%%s%%'" % (column, criterias_not[nb]))
    
    request.append("))")
    print(request)
    print("".join(request))
    return(request)


def createRequestTextAo(column, criterias_and, criterias_or):
    """Write the end of SQL request for a search with AND (or basic) and OR. Corresponding structure :
    ((column LIKE '%~%' AND column LIKE '%~%') OR (column LIKE '%~%' AND column LIKE '%~%'))
    Return the request as a list."""
    request = [" ((%s LIKE '%%%s%%'" %(column, criterias_and[0])]
    lrequesta = len(criterias_and)
    lrequesto = len(criterias_or)
    
    for nb in range(1,lrequesta):
        request.append(" AND %s LIKE '%%%s%%'" %(column, criterias_and[nb]))    
    
    request.append(") OR (%s LIKE '%%%s%%'" % (column, criterias_or[0]))
    
    for nb in range(1, lrequesto):
        request.append(" AND %s LIKE '%%%s%%'" % (column, criterias_or[nb]))
    
    request.append(")) ")

    print(request)
    print("".join(request))
    return(request)


def createRequestTextAn(column, criterias_and, criterias_not):
    """Write the end of SQL request for a search with AND (or basic) and NOT. Corresponding structure :
    ((column LIKE '%~%' AND column LIKE '%~%') AND (column NOT LIKE '%~'%))
    Return the request as a list."""
    request = [" ((%s LIKE '%%%s%%'" %(column, criterias_and[0])]
    lrequesta = len(criterias_and)
    lrequestn = len(criterias_not)
    
    for nb in range(1,lrequesta):
        request.append(" AND %s LIKE '%%%s%%'" %(column, criterias_and[nb]))
    
    request.append(") AND (%s NOT LIKE '%%%s%%'" % (column, criterias_not[0]))
    
    for nb in range(1, lrequestn):
        request.append(" AND %s NOT LIKE '%%%s%%'" % (column, criterias_not[nb]))
    
    request.append("))")
    print(request)
    print("".join(request))
    return(request)


def createRequestTextA(column, criterias_and):
    """Write the end of SQL request for a search with AND (or basic). Corresponding structure :
    (column LIKE '%~%' AND column LIKE '%~%')
    Return the request as a list."""
    request = [" (%s LIKE '%%%s%%'" %(column, criterias_and[0])]
    lrequesta = len(criterias_and)
    
    for nb in range(1,lrequesta):
        request.append(" AND %s LIKE '%%%s%%'" %(column, criterias_and[nb]))
    
    request.append(")")
    print(request)
    print("".join(request))
    return(request)
