/* Baseball.sql */
-- Retrieve teams from the American league
SELECT TeamName 
FROM Team
WHERE League='American'

-- Retrieve Twins player names, calculate their batting averages,
-- and sort the result descending on batting averages
SELECT PlayerName, Hits/AtBats AS BatAvg
FROM Team INNER JOIN Player
  ON Team.TeamID = Player.TeamID
WHERE TeamName='Twins'
ORDER BY BatAvg DESC