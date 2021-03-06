# PongEvolution
Neural nets learn to play pong using the genetic algorithm.

## How to use

### Edit the values in `config.py` to your liking:

- `SCREENSIZE` *(tuple)*: The size of the screen (w,h)
- `PADDLESIZE` *(tuple)*: The default paddle dimensions
- `PLAYERSPEED` *(number)*: The maximum speed the paddles can travel at
- `HIDDENNODES` *(int)*: The number of hidden nodes each player's neural net contains
- `BALLRADIUS` *(number)*: The radius of the balls
- `DEFAULT_BALLSPEED` *(number)*: The base speed the balls start at
- `DIFFICULTY_RATE` *(number)*: The rate at which the ball speed increases each frame
- `POPULATION_SIZE` *(number)*: The size of the population
- `MUTATION_RATE` *(number)*: The rate at which the organisms mutate
- `FPS_CAP` *(number)*: The maximum FPS to run at. -1 for no max

### Run main.py

- Use `alt` to show the neural net of the winner of the previous generation
- Use `shift` to kill every organism in the current generation
- Hold `w` to only show the previous generation's best player
