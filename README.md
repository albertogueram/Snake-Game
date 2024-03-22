## Snake Class
#### Initialize: 
Snake body creation with three segments
with 20 pixels per segment. In addition, we define the
head of the snake as first segment whole_snake[0]. 
We will use the head for moving and detect collisions
#### Move:
Move 20 pixels (one segment) the head of the snake
and move the next segment to the prior segment position
#### Up, Right, Left, Down:
Change the heading of the snake head
#### Grow: 
Increase the size of the snake adding one extra segment 
and placing it in the last segment position.

## Food Class
Inheritance of Turtle class from turtle package
#### Refresh:
Takes new x,y random position from the board and assign it
to the next piece when the head of the snake collission with
food.

## ScoreBoard Class 
Inheritance of Turtle class from turtle package
#### Refresh:
Update the score and call update_scoreboard method
whenever the head of the snake collission
with food.
#### Update Scoreboard:
Delete the previous score and update it
### Reset:
When the snake collission with itself of the edges
it´s update the highest score and create a new snake.

# Main Function
While variable game_is_on is True it will continue running the program till:
1. Snake Head collision with wall
2. Snake Head collision with another segment of the snake

During that while loop the snake grows when it detects
that the head collision with food.

Collision is done using the .distance method 