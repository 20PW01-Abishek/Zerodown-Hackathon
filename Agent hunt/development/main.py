from flask import Flask, render_template, request
import psycopg2
from collections import Counter

app = Flask(__name__)

# Connect to the database
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="root"
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def results():
    market_id = request.form.get("market_id")
    n = request.form.get("num_results")
    market_id = int(market_id)
    n = int(n)
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT agent_info.id, agent_info.first_name, brokerage.id, brokerage.name
        FROM agent_listing
        JOIN agent_info ON agent_listing.agent_id = agent_info.id
        JOIN home_info ON agent_listing.home_id = home_info.id
        JOIN brokerage ON agent_info.brokerage_id = brokerage.id
        WHERE home_info.zipcode_market_id = %s
        ORDER BY agent_listing.listing_price DESC
        LIMIT %s
        """, (market_id, n)
    )
    agents = cursor.fetchall()
    l = []
    for i in range(n):
        l.append(agents[i][1])
    c = Counter(l)
    x = c.keys()
    y = c.values()

    lb = []
    for i in range(n):
        lb.append(agents[i][3])
    cb = Counter(lb)
    xb = cb.keys()
    yb = cb.values()
    print(xb,yb,x,y)

    return render_template("results.html", agents=agents, market_id=market_id, n=n, xl=list(x), yl=list(y), xb=list(xb), yb=list(yb))

if __name__ == '__main__':
    app.run(debug=True)
