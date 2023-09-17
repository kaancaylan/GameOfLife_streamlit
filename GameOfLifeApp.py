import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.title("Conway's Game Of Life")

class ConwaysGameApp:
    def __init__(self):
        pass
    
    def initialize_matrix(self, square_size, prob_alive):
        return np.random.binomial(1, prob_alive, size=(square_size, square_size))   

    def initialize_game(self):
        matrix_shape = st.sidebar.slider("Shape of Square Matrix", 10, 600, step=10, value=200)
        alive_cells = st.sidebar.slider("Proportion of Alive Cells at the Beginning", 0.0, 1.0, step=0.01, value=0.5)
        stopping_time = st.sidebar.slider("Time in between rounds", 0.0, 3.0, value=0.01)
        # number_of_rounds = number = st.number_input('Number of Rounds to run the Game: ', value=100, min_value=1, max_value=10000)
        # st.write('The Game will run for ', number_of_rounds, "rounds")

        initialize = st.sidebar.button("Start Game")
        stopping_button = st.sidebar.button("Stop Game")
        if initialize:
            self.matrix = self.initialize_matrix(matrix_shape, alive_cells)
            i = 0
            plot_placeholder = st.empty()
            while not stopping_button:
                neighbors = self.find_neighbors(self.matrix)
                self.matrix = self.update_array(self.matrix, neighbors)
                fig, ax = plt.subplots()
                ax.set_title(f"round number = {i+1}")
                plt.axis("off")
                ax.imshow(self.matrix)
                plot_placeholder.pyplot(fig)
                i += 1
                time.sleep(stopping_time)
                plt.close()
        if stopping_button:
            st.subheader(f"The Game has ended. Press Start to play again.")
                    

    def run_rounds_streamlit(self):
        plot_placeholder = st.empty()
        for i in range(self.n_iter):        
            neighbors = self.find_neighbors(self.matrix)
            self.matrix = self.update_array(self.matrix, neighbors)
            fig, ax = plt.subplots()
            ax.set_title(f"round number = {i+1}")
            ax.imshow(self.matrix)
            # st.pyplot(fig, clear_figure=True)
            plot_placeholder.pyplot(fig)
            time.sleep(0.001)
            plt.close()

    def find_neighbors(self, arr):
        neighbors = []
        for i in range(len(arr)):
            for j, value in enumerate(arr[i]):

                if i == 0 or i == len(arr) - 1 or j == 0 or j == len(arr[i]) - 1:
                    # corners
                    new_neighbors = []
                    if i != 0:
                        new_neighbors.append(arr[i - 1][j])  # top neighbor
                    if j != len(arr[i]) - 1:
                        new_neighbors.append(arr[i][j + 1])  # right neighbor
                    if i != len(arr) - 1:
                        new_neighbors.append(arr[i + 1][j])  # bottom neighbor
                    if j != 0:
                        new_neighbors.append(arr[i][j - 1])  # left neighbor
                    if i != 0 and j != 0:
                        new_neighbors.append(arr[i-1][j-1])  # top-left
                    if i != 0 and j != len(arr) - 1:
                        new_neighbors.append(arr[i-1][j+1])  # bottom-left
                    if i != len(arr) - 1 and j != 0:
                        new_neighbors.append(arr[i+1][j-1])  # top-right
                    if i != len(arr) - 1 and j != len(arr) - 1:
                        new_neighbors.append(arr[i-1][j-1])  # bottom-right
                    
                else:
                    # add neighbors
                    new_neighbors = [
                        arr[i - 1][j],  # top neighbor
                        arr[i][j + 1],  # right neighbor
                        arr[i + 1][j],  # bottom neighbor
                        arr[i][j - 1],  # left neighbor
                        arr[i-1][j-1],  # top-left
                        arr[i-1][j+1],  # bottom-left
                        arr[i+1][j-1],  # top-right
                        arr[i+1][j+1]   # bottom-right
                    ]

                neighbors.append({
                    "index": (i, j),
                    "state": value,
                    "neighbors":sum(new_neighbors)})

        return neighbors
    

    def update_array(self, arr, neighbor_counts):
        for i in neighbor_counts:
            if i["state"] == 1:
                if i["neighbors"] < 2 or i["neighbors"] > 3:
                    arr[i['index']] = 0
            elif i["state"] == 0:
                if i["neighbors"] == 3:
                    arr[i["index"]] = 1
        return arr

"""
**Welcome To Conway's Game Of Life!**

---
In the Game of Life each grid cell can have either one of two states: dead or alive. The Game of Life is controlled by four simple rules which are applied to each grid cell in the simulation domain:

- A live cell dies if it has fewer than two live neighbors.
- A live cell with two or three live neighbors lives on to the next generation.
- A live cell with more than three live neighbors dies.
- A dead cell will be brought back to live if it has exactly three live neighbors.
---

To Start the Game, press the Start button on the left. To stop it, simply press the Stop. 
You can also adjust the proportion of alive cells and the size of the playing field below the start and stop button.
"""

ConwaysGameApp().initialize_game()