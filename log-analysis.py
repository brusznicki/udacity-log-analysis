#!/usr/bin/env python2.7
#
# Udacity Logs Analysis Project
import psycopg2
DBNAME = 'news'


class LogAnalysis():
    '''LogAnalysis class that creates reports for 3 project questions'''

    def __init__(self):
        self.dbName = DBNAME

    def main(self):
        '''Runs the SQL scripts to generate answers to questions.'''

        questions = self.get_questions()

        for key in sorted(questions.keys()):
            self.print_result(
                questions[key]['question'],
                self.execute_query(questions[key]['query']),
                questions[key]['label'])

    def get_questions(self):
        '''Contains a list of user provided questions and queries
        to get answers'''
        questions = {}  # Hash of questions and associated queries

        # LOG ANALYSIS QUESTION 1
        question1 = """1. What are the most popular three articles of all time?
        """

        query1 = """
            SELECT a.title, TO_CHAR(views, 'FM999,999,999')
                FROM articles a
                    LEFT JOIN (SELECT path, count(log.path) AS views
                               FROM log
                               WHERE status = '200 OK'
                               GROUP BY PATH) AS l
                    ON REPLACE(l.path, '/article/', '') LIKE a.slug
                ORDER BY views DESC
                LIMIT 3;
        """
        questions[1] = {'question': question1,
                        'query': query1,
                        'label': ' views'}

        # LOG ANALYSIS QUESTION 2
        question2 = """2. Who are the most popular article authors of all time?
        """
        query2 = """
            SELECT authors.name, TO_CHAR(sum(views), 'FM999,999,999')
                FROM articles
                    JOIN authors on articles.author = authors.id
                        LEFT JOIN (SELECT path, count(*) AS views
                                   FROM log
                                   WHERE status = '200 OK'
                                   GROUP BY PATH) AS l
                        ON REPLACE(l.path, '/article/', '')
                        LIKE articles.slug
                GROUP BY authors.name
                ORDER BY SUM(views) DESC;
        """
        questions[2] = {'question': question2,
                        'query': query2,
                        'label': ' views'}

        # LOG ANALYSIS QUESTION 3
        question3 = """3. On which days did more than 1% of requests lead to errors?'
        """
        query3 = """
            SELECT TO_CHAR(date_trunc('day', day), 'FMMonth DD, YYYY'),
                   round(fail*100.0 / (fail + success),2)
                   AS quotient
                FROM (
                    SELECT
                        date_trunc('day', log.time) AS day,
                        sum(case when status = '200 OK' THEN 1 ELSE 0 end)
                        AS success,
                        SUM(CASE WHEN status = \
                        '404 NOT FOUND' THEN 1 ELSE 0 END)
                        AS fail
                    FROM log
                    GROUP BY date_trunc('day', log.time)
                   ) AS derivedTable
                WHERE cast(fail AS decimal(12,2)) / (fail + success) > 0.01
                GROUP BY date_trunc('day', day), success, fail;
        """
        questions[3] = {'question': question3,
                        'query': query3,
                        'label': '% errors'}

        return questions

    def execute_query(self, query):
        """Executes query, returns result"""

        if query:
            db = self.db_connect(self.dbName)
            c = db.cursor()
            c.execute(query)
            result = c.fetchall()
            db.close()
            return result
        else:
            return

    def db_connect(self, db_name):
        """Connect to database, db_name, return connection """
        try:
            db = psycopg2.connect("dbname={}".format(db_name))
            return db
        except psycopg2.Error as e:
            print "Unable to connect to {}, check your connection"\
                  .format(db_name)
            return None

    def print_result(self, question, result, label):
        '''Produces text only output of query result'''
        print "\n"
        print "*" * len(question)
        print question
        print "*" * len(question)
        for row in result:
            print " -- ".join([str(x) for x in row]) + label
        print "=" * len(question)


if __name__ == '__main__':

    la = LogAnalysis()
    la.main()
