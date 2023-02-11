import pandas as pd
import networkx as nx
from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:root@localhost/postgres')
df = pd.read_sql('SELECT * FROM home_info',engine)
print(df.columns)
market_id = 1803
market_data = df[df['zipcode_market_id'] == market_id]

G = nx.Graph()

for index, row in market_data.iterrows():
    agent1 = row['agent1_name']
    agent2 = row['agent2_name']
    G.add_edge(agent1, agent2)
nx.draw(G, with_labels=True)