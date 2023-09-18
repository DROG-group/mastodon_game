import csv
import psycopg2

def push_data_to_db(row, cur):
    # SQL CTE to insert data
    sql = """
    WITH user_check AS (SELECT id AS account_ID FROM accounts WHERE username = %(account_username)s),
    new_account AS (INSERT INTO accounts (username, created_at, updated_at) VALUES (%(account_username)s, %(created_at)s, %(updated_at)s) WHERE NOT EXISTS (SELECT 1 FROM user_check) RETURNING id AS account_ID),
    new_status AS (INSERT INTO statuses (account_id, text, created_at, updated_at, in_reply_to_id, reblog_of_id, visibility) 
        VALUES (COALESCE((SELECT account_ID FROM new_account), (SELECT account_ID FROM user_check)), %(text)s, %(created_at)s, %(updated_at)s, %(in_reply_to_id)s, %(reblog_of_id)s, %(visibility)s) RETURNING id AS status_id)
    SELECT status_id FROM new_status;
    """
    # Execute the SQL
    cur.execute(sql, row)

def insert_mastodon_data_from_csv(csv_path, db_config):
    # Connect to the database
    conn = psycopg2.connect(**db_config)
    cur = conn.cursor()

    # Read the CSV
    with open(csv_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            push_data_to_db(row, cur)
            conn.commit()

    # Close the database connection
    cur.close()