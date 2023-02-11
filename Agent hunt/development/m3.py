import pandas as pd
import networkx as nx
from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:root@localhost/postgres')

home_info = pd.read_sql('SELECT * FROM home_info',engine)
agent_info = pd.read_sql('SELECT * FROM agent_info',engine)
agent_listing = pd.read_sql('SELECT * FROM agent_listing',engine)

market_id = 1803
market_data = df[df['zipcode_market_id'] == market_id]
print(market_data)
print(market_data.columns)
G = nx.Graph()

for index, row in market_data.iterrows():
    agent1 = row['Nicole']
    agent2 = row['Amy']
    G.add_edge(agent1, agent2)
nx.draw(G, with_labels=True)