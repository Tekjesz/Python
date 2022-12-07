import pandas as pd
import numpy as np
from collections import Counter

def read_data(path_to_txt: str):
    """
    Read in the data of the given txt file
    
    Args:
        path_to_txt(str): path to the txt file
    Returns:
        df(pd.DataFrame): DataFrame created from the data of the read txt file
    """
    
    with open(path_to_txt, "r") as f:
        lines = f.readlines()
        N_lines = len(lines)
        N_block = int(N_lines / 5)
        
        data = []

        for i_block in range(0, N_block):
            release_date   = lines[i_block * 5 + 0].rstrip()
            title          = lines[i_block * 5 + 1].rstrip()
            season_episode = lines[i_block * 5 + 2].rstrip()
            season         = int(season_episode.split("x")[0])
            episode        = int(season_episode.split("x")[1])
            episode_length = float(lines[i_block * 5 + 3].rstrip())
            already_wathced = int(lines[i_block * 5 + 4].rstrip())
            
            data.append([release_date, title, season_episode, season, episode, episode_length, already_wathced])
            
        df = pd.DataFrame(data,
                          columns=["release_date", "title", "season_episode", "season", "episode", "episode_length", "already_wathced"])
        
        #df['release_date']= pd.to_datetime(df['release_date'])
        return df
            
            



if __name__ == "__main__":
    df = read_data(path_to_txt = "2020_09_28/lista.txt")