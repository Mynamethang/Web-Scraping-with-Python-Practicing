drop_largest_companies_table ="""DROP TABLE IF EXISTS largest_companies"""
create_largest_companies_table = (
                                """
                                CREATE TABLE largest_companies(
                                rank SMALLINT,
                                name VARCHAR(50),
                                industry VARCHAR(50),
                                revenue MONEY,
                                revenue_growth DECIMAL(5,3),
                                employees INT,
                                headquarters VARCHAR(50)
                                    )
                                """
                                )    

insert_largest_companies_table = ("""INSERT INTO largest_companies(rank, name, industry, revenue, revenue_growth, employees, headquarters) 
                                  VALUES(%s, %s, %s, %s, %s, %s, %s)""")           
