# Circadence Engineering - Backend Developer

## Intern Coding Challenge

## Instructions

Have you read the README.md file?

Be sure to read these instructions completely before submitting your response.

## Coding Challenge Description

Imagine you are on a team tasked with constructing a constellation of microservices for our flagship product Project Ares.
Existing game functionality allows players to compete in various arenas, called battle rooms, where they are scored on how well they complete various cybersecurity challenges.
You've been assigned to create the microservice that will keep track of leaderboards for the various battle rooms in Project Ares.

Below you will find a set of user stories assigned by your team lead.
Perform the work necessary to satisfy the requirements of the user stories.

In order to complete your challenge, you will need to clone the git repository at <https://gitlab.com/Circadence-Public/code-challenge> and add your solution to the cloned repository.
When you've completed your challenge, email eng_challenge_help@circadence.com with:

- your contact information
- the URL of the git repo containing your solution to the coding challenge.

Please include in your git repository:

1. a single README.md markdown file containing the following:
    - your answers added to the questionaire
    - documentation for building and running your application
2. one folder containing your solution

### Platform Choices

You can create the application in any platform and language of your choice.

### Task requirements

Please return your solution within five days, but don't feel obligated to use the entire five days.

Ensure the following requirements have been met.

- Please complete at least User Story 1 below
- Your code should compile and run in one step
- Feel free to use whatever frameworks / libraries / packages you like
- Please avoid including artifacts from your local build (such as NuGet packages or bin folders) in your solution folder
- You may complete User Story 2 as a bonus question

## User Stories

### User Story 1

As a **system that displays battleroom leaderboards**  
I can **retrieve a player's rank in a battleroom session**  
So that **after playing a battleroom, a player can know their rank**

Acceptance criteria

- Given the following battleroom play:
  - there are 6 players: Mary, James, Jennifer, John, Patricia, Robert
  - all players play 2 battlerooms:  
    battleroom-id 1 has a max score of 500
    battleroom-id 30 has a max score of 300
  - Paticia is player_id: 1

- Executing this curl command will succeed and return the correct results

    curl http://localhost:8080/rank \
    -H 'Content-Type: application/json' \
    -H 'cache-control: no-cache' \
    -d '{"player_id": "1", "battleroom_id": "1", "score":"100" }'

    Note: This is an example and may change based upon your implementation.

- The results will include: player rank and number of total players in battleroom

### User Story 2

As a **system that displays battleroom statistics**  
I can **retrieve the battleroom leaderboard and median score**
So that **we can get insight into player performance in a specific battleroom**

Acceptance criteria

- Given the same battleroom play as User Story 1
- Executing this curl command will succeed and return the correct results

curl -X GET http://localhost:8080/leaderboard \
-H 'Content-Type: application/json' \
-H 'cache-control: no-cache' \
-d '{"battleroom_id":"30"}'

- The results will include: an ordered leaderboard - include player id and score, and battleroom median score

## Questions for You

1. How long did you spend on the coding challenge?
2. What would you add to your solution if you had more time? If you didn't spend much time on the coding test then use this as an opportunity to explain what you would add.
3. Explain your choice of technologies used.  Discuss any trade-offs.
4. If you were going to test this, how would you do about doing that? What would you test for?
5. How would you handle a new user story to get a player's rank and median battleroom score by username?

## Thank you for your time

You may send questions to email: eng_challenge_help@circadence.com
