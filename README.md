# Mercado Libre Leaderboard with Top Scores
This project is going to track and display the top scores from https://ml-challenge.mercadolibre.com/leaderboard. The main problem with the original leaderboard is that it is only displaying **the most recent scores**, hence, the top scores are not reliable. By using github actions, this repository is constantly tracking the changes in the webpage and storing only the top scores here. In order to visualize the current top scores, refer to the following links:
- https://meli-challenge-leaderboard.herokuapp.com/
- https://github.com/WittmannF/meli-challenge-leaderboard/blob/main/leaderboard/leaderboard.csv

Contributions and suggestions are welcome! You just have to open an issue. Thanks!

## Limitations
The original Meli leaderboard is going to be checked depending every 5 to 10 minutes (minimum cron inteval job available on github actions), hence, submitions that are performed in between those times will not be captured. 
