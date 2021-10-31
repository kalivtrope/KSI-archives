import sqlite3


def prepare_table(licks):
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.execute('''
    create table licks (
      l integer not null,
      r integer not null,
      check (l <= r),
      unique(l, r)
    )
    ''')

    c.executemany('insert into licks values (?,?)', licks)
    return conn, c


def main():
    licks = (
        (1, 5),
        (2, 3),
        (4, 6),
    )

    prep = '''
CREATE TEMPORARY TABLE temp AS
    SELECT l, r FROM licks ORDER by l;
'''
    query = '''
WITH RECURSIVE
    cover(iter, total, ende) as (
        SELECT 1, 0, 0
        UNION ALL
        SELECT 
            iter + 1,
            total + max(0, r - ende) - max(0, l - ende),
            max (r, ende)
        FROM cover, temp WHERE temp.rowid = iter
    )
SELECT total from cover ORDER BY iter DESC LIMIT 1;
'''

    conn, c = prepare_table(licks)
    c.executescript(prep)
    c.execute(query)
    result = c.fetchone()
    print(result[0])

    c.close()
    conn.close()


if __name__ == '__main__':
    main()
