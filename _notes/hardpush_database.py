import csv
#from PIL import Image
#import os
#import random
import psycopg2

'''
Overview:
Script to insert data from a CSV file into Mastodon's database.

Functions:

push_data_to_db(row, cur):

Parameters:
row: Data row from the CSV.
cur: Database cursor.
Description: Inserts a single row of data into Mastodon's database. Uses a CTE to check if a user exists, creates a new account if not, and then inserts a status.
insert_mastodon_data_from_csv(csv_path, db_config):

Parameters:
csv_path: Path to the CSV file.
db_config: Database configuration dictionary.
Description: Connects to the database, reads the CSV file, and inserts each row using push_data_to_db.
Usage:

Set up the database configuration.
Call insert_mastodon_data_from_csv with the path to your CSV file and the database configuration.
Note: Direct database manipulation can bypass application-level checks and validations. Use with caution.

CSV example.csv
id,created_at,updated_at,account_username,text,interaction_type,in_reply_to_id,reblog_of_id,media_attachment_ids,visibility
50,2023-09-12 13:00:00,2023-09-12 13:00:00,Ava,"They can take away our art, but they can't silence our voices. #Resistance 🎨🗣️",toot,Null,Null,"",0
51,2023-09-12 13:05:00,2023-09-12 13:05:00,Viktor,Artistic expression poses a threat to societal order. It must be controlled. #Enforcers 🖌️🚫,reply,50,Null,"",0
52,2023-09-12 13:10:00,2023-09-12 13:10:00,Nora,Reporting on the regime's cultural oppression. We won't let them erase our identity. #FreedomOfExpression 📰💔,toot,Null,Null,"",0
53,2023-09-12 13:15:00,2023-09-12 13:15:00,Ethan,They underestimate the power of creativity. We'll find ways to express ourselves in the shadows. #TechRevolution 💻🌑,toot,Null,Null,"",0
54,2023-09-12 13:20:00,2023-09-12 13:20:00,Harper,The regime's art is the true reflection of our values. Anything else is dangerous. #Propaganda 📢🤐,toot,Null,Null,"",0
56,2023-09-12 13:25:00,2023-09-12 13:25:00,Maya,Infiltrating the regime's art department. Uncovering their dark secrets. #SpyLife 🕵️‍♀️🔍,toot,Null,Null,"",0
57,2023-09-12 13:30:00,2023-09-12 13:30:00,Leo,The Resistance will crumble under the weight of their own ideals. I've seen it firsthand. #Traitor 😈🔪,toot,Null,Null,"",0
58,2023-09-12 13:35:00,2023-09-12 13:35:00,Felix,Resistance scum will pay for their defiance. Torture awaits them in our chambers. #Enforcers ⚡️😈,toot,Null,Null,"",0
59,2023-09-12 13:40:00,2023-09-12 13:40:00,Riley,The sniper's bullet finds its mark. Regime targets eliminated one by one. #SilentJustice 🔫🎯,toot,Null,Null,"",0

here's a breakdown of the CTE logic:
user_check CTE: This checks if a user with the given username exists and returns their account_ID if they do.
new_account CTE: This attempts to insert a new account with the given username and other details. 
If an account with the same username (and domain, if provided) already exists, it performs a dummy update on the username (i.e., it sets the username to its current value). 
Regardless of whether it's an insert or an update, it returns the account_ID.
new_status CTE: This inserts a new status (toot) associated with the account ID determined in the previous steps. 
It uses the COALESCE function to prioritize the account_ID from new_account (if a new account was created or an existing one was updated) and falls back to the account_ID from user_check if no new account was created. 
This means a new status will be created whether the user is new or already exists.
new_user CTE: This inserts a new user associated with the account ID determined in the previous steps. 
Similar to the new_status CTE, it uses the COALESCE function to determine the account_ID.
Final SELECT: This returns the IDs of the newly created or updated account and the newly created status, each with a type label ('account' or 'status').

'''
account_id = 111093256093960762 #dummy
avatar_dir = 'path_to_folder_with_avatars' # Replace with your actual path
output_base_dir = '~/live/public' # Starting point of the path


def push_data_to_db(row, cur):
    for key, value in row.items():
        if value == 'Null':
            row[key] = None
    # SQL CTE to insert data
    sql = """
        WITH 
            user_check AS (
                SELECT id AS account_ID 
                FROM accounts 
                WHERE username = %(account_username)s
            ),
            new_account AS (
                INSERT INTO accounts (username, public_key, created_at, updated_at, note, display_name) 
                VALUES (REPLACE(%(account_username)s, ' ', '_'), 1, '2003-01-01', '2003-01-01', 'TXT', %(account_username)s) 
                    ON CONFLICT (lower(username), COALESCE(lower(domain), ''))
                    DO UPDATE SET username=EXCLUDED.username
                RETURNING id AS account_ID
            ),
            new_status AS (
                INSERT INTO statuses (account_id, text, created_at, updated_at, visibility, in_reply_to_id, reblog_of_id, reply, language) 
                VALUES (
                    COALESCE((SELECT account_ID FROM new_account), (SELECT account_ID FROM user_check)), 
                    %(text)s, 
                    %(created_at)s, 
                    %(updated_at)s, 
                    %(visibility)s,
                    CASE 
                        WHEN CAST(%(in_reply_to_id)s AS TEXT) = 'Null' THEN NULL 
                        ELSE COALESCE((SELECT mastodon_id FROM id_mapping WHERE csv_id = CAST(%(in_reply_to_id)s AS INTEGER)), NULL) 
                    END,
                    CASE 
                        WHEN CAST(%(in_reply_to_id)s AS TEXT) = 'Null' THEN NULL 
                        ELSE COALESCE((SELECT mastodon_id FROM id_mapping WHERE csv_id = CAST(%(reblog_of_id)s AS INTEGER)), NULL) 
                    END,
                    CASE WHEN COALESCE(%(in_reply_to_id)s, 'NULL_VALUE') != 'NULL_VALUE' THEN TRUE ELSE FALSE END,
                    'en'
                )
                RETURNING id AS status_id
            ),
            mapping AS (
                INSERT INTO id_mapping (csv_id, mastodon_id)
                VALUES (%(id)s, (SELECT status_id FROM new_status))
                RETURNING mastodon_id
            ),
            new_status_stats AS (
                INSERT INTO status_stats (status_id, replies_count, reblogs_count, favourites_count, created_at, updated_at)
                SELECT
                    -- Determine which status ID we should be updating stats for
                    CASE 
                        WHEN %(in_reply_to_id)s IS NOT NULL THEN COALESCE((SELECT mastodon_id FROM id_mapping WHERE csv_id = CAST(%(in_reply_to_id)s AS INTEGER)), NULL)
                        WHEN %(reblog_of_id)s IS NOT NULL THEN COALESCE((SELECT mastodon_id FROM id_mapping WHERE csv_id = CAST(%(reblog_of_id)s AS INTEGER)), NULL)
                        ELSE NULL
                    END,
                    CASE WHEN %(in_reply_to_id)s IS NOT NULL THEN 1 ELSE 0 END,  -- Increment reply count if in_reply_to_id is not null
                    CASE WHEN %(reblog_of_id)s IS NOT NULL THEN 1 ELSE 0 END,   -- Increment reblog count if reblog_of_id is not null
                    0,  -- Initial value for favourites_count
                    NOW(),
                    NOW()
                WHERE 
                    (COALESCE((SELECT mastodon_id FROM id_mapping WHERE csv_id = CAST(%(in_reply_to_id)s AS INTEGER)), NULL) IS NOT NULL)
                    OR
                    (COALESCE((SELECT mastodon_id FROM id_mapping WHERE csv_id = CAST(%(reblog_of_id)s AS INTEGER)), NULL) IS NOT NULL)
                ON CONFLICT (status_id) 
                DO UPDATE SET 
                    replies_count = status_stats.replies_count + EXCLUDED.replies_count,
                    reblogs_count = status_stats.reblogs_count + EXCLUDED.reblogs_count,
                    favourites_count = status_stats.favourites_count + EXCLUDED.favourites_count,
                    updated_at = NOW()
                WHERE 
                    (EXCLUDED.replies_count = 1) OR (EXCLUDED.reblogs_count = 1)
            ),
           new_user AS (
                INSERT INTO users (email, account_id, created_at, updated_at, confirmed_at, time_zone)
                SELECT 
                    gen_random_uuid(), 
                    (SELECT account_ID FROM new_account), 
                    '2003-01-01', 
                    '2003-01-01', 
                    '2003-01-01',
                    'Europe/Amsterdam'
                WHERE NOT EXISTS (SELECT 1 FROM user_check)
            )
            SELECT account_ID AS id, 'account' AS type FROM new_account
                UNION ALL
            SELECT status_id AS id, 'status' AS type FROM new_status;
        """
        # Execute the SQL
    cur.execute(sql, row)
    results = cur.fetchall()
    ids = {id_type: id_value for id_value, id_type in results}
    account_id = ids.get('account', 'DefaultAccountValue')
    status_id = ids.get('status', 'DefaultStatusValue')
    return account_id, status_id

def ensure_id_mapping_table_exists(db_config):
    """
    Ensures that the id_mapping table exists and is empty.
    If the table exists, it truncates it. If it doesn't, it creates it.

    The `id_mapping` table serves as an essential bridge between the original CSV data and the Mastodon database:
    1. **ID Mismatch**: Mastodon may assign new auto-incremented IDs different from the original CSV IDs.
    2. **Maintain Relationships**: Fields in the CSV, like `in_reply_to_id`, refer to other records. We need to update these references with new Mastodon IDs to preserve relationships.
    3. **Avoid Duplications**: If importing data multiple times, the mapping table helps identify already imported records and prevents duplications.
    4. **Data Auditing**: After data insertion, the table assists in verifying the migration by mapping Mastodon IDs back to their original CSV IDs.

    The function `ensure_id_mapping_table_exists` ensures that this table is ready for each import, either by truncating existing data or creating the table if it doesn't exist.    
    Parameters:
    - db_config: Dictionary containing database connection parameters.
    """
    
    # PL/pgSQL block to ensure the id_mapping table exists and is empty
    sql = """
    DO $$
    BEGIN
        -- If the table exists, truncate it
        IF EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'id_mapping') THEN
            TRUNCATE TABLE id_mapping;
        ELSE
            -- If the table doesn't exist, create it
            CREATE TABLE id_mapping (
                csv_id INT PRIMARY KEY,
                mastodon_id BIGINT
            );
        END IF;
    END $$;
    """
    
    # Connect to the database and execute the SQL
    conn = psycopg2.connect(**db_config)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()

def insert_mastodon_data_from_csv(csv_path, db_config):
    # Connect to the database
    ensure_id_mapping_table_exists(db_config)
    conn = psycopg2.connect(**db_config)
    cur = conn.cursor()

    # Read the CSV
    with open(csv_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            account_id, status_id = push_data_to_db(row, cur)
            # saved_avatar_path = avatar_pusher(account_id, avatar_dir, output_base_dir)
            #Refactor reply_to_id in rest of the code...
            print(f"Account ID: {account_id}, Status ID: {status_id}")
            conn.commit()

    # Close the database connection
    cur.close()
    conn.close()


def clean_csv_data(input_path, output_path):
    cleaned_data = []
    print("Importing data...")
    with open(input_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            # Convert empty strings to None for integer fields
            for field in ['id', 'in_reply_to_id', 'reblog_of_id']:
                if not row[field]:
                    row[field] = Null
            cleaned_data.append(row)

    # Write cleaned data to a new CSV
    with open(output_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=cleaned_data[0].keys())
        writer.writeheader()
        writer.writerows(cleaned_data)

# Example usage
#clean_csv_data('_notes/example.csv', '_notes/example.csv')

# Example usage:
db_config = {
    'dbname': 'mastodon_production',
    'user': 'mastodon',
    'password': '',
    'host': '127.0.0.1',
    'port': '5432'
}
insert_mastodon_data_from_csv('_notes/example.csv', db_config)
