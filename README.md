# Circadence Engineer Recruitment Test

## Setup

asdf

## Example Queries

Example command for User Story 1:
curl localhost:8000/rank/ -H "Content-Type: application/json" -H "cache-control: no-cache" -d "{\"player_id\": \"1\", \"battleroom_id\": 30}"

Example command for User Story 2:
curl -X GET localhost:8000/leaderboard/ -H "Content-Type: application/json" -H "cache-control: no-cache" -d "{\"battleroom_id\": \"30\"}"

## Questions

1. How long did you spend on the coding challenge?
Overall, I spent about three weeks working on this but this is because of a lack of free time. I probably only spent about three days working on this project.

2. What would you add to your solution if you had more time?
Currently the ranking system for scores is "hard-coded" meaning that ranks are assigned as a score is added to the database. I would have liked to make it
so that rankings are done automatically based off of the user score.

3. Explain your choice of technologies used.  Discuss any trade-offs.
I chose django primarily because I have prior experience working with it. Django was a great choice because of its simplicity and ability to get a working
"proof of concept" done in a small amount of time. It also provides growing room for taking the project to production.

4. If you were going to test this, how would you do about doing that? What would you test for?
If this is something that would be used directly by a user, I would want to test how different "bad" inputs are handled by the microservice. Testing for SQL
injection would be a big concern and perhaps even load testing if this is something that would be used by a lot of people.

5. How would you handle a new user story to get a player's rank and median battleroom score by username?
Assuming players' usernames would be unique, this would not be hard to implement. First I would add a new attribute to the Player model called "username" and
then add an if statement that parses and looks for "username" in the POST data from localhost:8000/rank/. Next I would find the matching battleroom and get
all the scores that the player has in said battleroom. This could then be used to find the median and return a JSON response just like the other requests.
