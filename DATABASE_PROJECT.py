import psycopg2
hostname="localhost"
port_id=5432
pwd="LEVIACKERMANFD1234"
database_name="GITHUB_PROJECT"
username="postgres"
conn=psycopg2.connect(
    host=hostname,
    password=pwd,
    user=username,
    dbname=database_name,
    port=port_id
)
curr=conn.cursor()
def create_table_github():
    curr.execute(''' CREATE TABLE IF NOT EXISTS GIT_HUB_USER_INFO(
                    username varchar(100),
                    name  varchar(100),
                    followers int,
                    following int,
                    repositories int
)      ''')
    conn.commit()
def insert_github_info(username,name,followers,following,repos):
    curr.execute('''        
    INSERT INTO GIT_HUB_USER_INFO
    VALUES
    (%s,%s,%s,%s,%s)    ''',(username,name,followers,following,repos)
    )
    conn.commit()
def show_user_info():
    curr.execute('''SELECT *FROM GIT_HUB_USER_INFO''')
    return curr.fetchall()
