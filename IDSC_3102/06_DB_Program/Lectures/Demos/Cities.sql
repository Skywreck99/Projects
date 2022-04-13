/* Cities.sql */
-- ************************************************************
-- SQL queries to embed into Python code
-- ************************************************************

-- ************************************************************
-- Lect14_01a_States_Cities.py
-- ************************************************************
-- Listbox of State Names
SELECT StateName FROM States

-- Does state have any cities?
SELECT COUNT(*) AS NumCities
FROM States INNER JOIN Cities 
  ON States.StateID = Cities.StateID
WHERE StateName = 'Minnesota'

-- Retrieving City Information
-- Testing for state of Minnesota, state changes dynamically 
-- based on user selection
SELECT CityName, Cities.Pop2020, Pop2010
FROM States INNER JOIN Cities 
  ON States.StateID = Cities.StateID
WHERE StateName = 'Minnesota'

-- ************************************************************ 
-- Lect14_01b_Regions_Divisions.py 
-- ************************************************************

-- Radiobuttons Callback Function
-- Testing for Midwest, region changes dynamically
-- based on user selection
SELECT DISTINCT Division 
FROM States 
WHERE Region='Midwest'
ORDER BY Division

-- Retrieving State Information
-- Testing for West North Central, division changes dynamically
-- based on user selection
SELECT StateName, States.Pop2020 AS StatePop, 
  COUNT(*) AS NumCities, SUM(Cities.Pop2020) AS PopUrban, 
  SUM(Cities.Pop2020)/States.Pop2020 AS PctUrban
FROM States INNER JOIN Cities 
  ON States.StateID = Cities.StateID
WHERE Division='West North Central'
GROUP BY StateName
ORDER BY PctUrban DESC
