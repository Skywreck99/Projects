/* Loans.sql */
-- **************************************************
-- Slide #09: Basic SQL
-- **************************************************
SELECT * FROM Customer

-- **************************************************
-- Slide #12: Basic SQL (cont.)
-- **************************************************
SELECT custID, firstName, lastName 
FROM Customer

-- **************************************************
-- Slide #15: Basic SQL (cont.)
-- **************************************************
SELECT loanID, amount, loanType, mthPmt
FROM Loan WHERE custID=106

-- **************************************************
-- Slide #16: Querying Multiple Tables
-- **************************************************
SELECT firstName, lastName, amount, mthPmt
FROM Customer INNER JOIN Loan
  ON Customer.custID = Loan.custID
WHERE city = 'Santa Fe' and loanType = 'Mortg'

-- **************************************************
-- Slide #18: Basic Summary Queries
-- **************************************************
SELECT loanType, COUNT(*) AS NumLoans
FROM Loan
GROUP BY loanType

SELECT city, ROUND(AVG(mthPmt),2) AS avgMthPmt
FROM Customer INNER JOIN Loan
  ON Customer.custID = Loan.custID
WHERE loanType = 'Mortg'
GROUP BY city
