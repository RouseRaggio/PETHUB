import psycopg2

def get_db_connection():
    return psycopg2.connect(    
        psql= 'postgresql://neondb_owner:npg_knxFCV3Lipw6@ep-bold-wave-ah5ahake-pooler.c-3.us-east-1.aws.neon.tech/prueba?sslmode=require&channel_binding=require',
        host="ep-bold-wave-ah5ahake-pooler.c-3.us-east-1.aws.neon.tech",
        port="5432",
        user="postgres",
        password="psql -h pg.neon.tech",
        dbname="prueba"
    )