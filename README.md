# Game Of Life Application

This repository is the implementation of Conway's Game of Life in a Streamlit Application.

## Rules of the Game

In the Game of Life each grid cell can have either one of two states: dead or alive. The Game of Life is controlled by four simple rules which are applied to each grid cell in the simulation domain:

- A live cell dies if it has fewer than two live neighbors.
- A live cell with two or three live neighbors lives on to the next generation.
- A live cell with more than three live neighbors dies.
- A dead cell will be brought back to live if it has exactly three live neighbors.


## Requirements

To install requirements:

```setup
pip install -r requirements.txt
```

## Build and run the Docker

The repository contains a Dockerfile which is ready to use for deploying the Stramlit application after downloading the project.

To build the Docker image, run the following command in the Terminal:

```setup
docker build -t streamlit .
```

Then, to run the Docker image in a container, run the following command:

```setup
docker run -p 8503:8503 streamlit
```


