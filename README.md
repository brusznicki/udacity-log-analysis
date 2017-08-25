## Udacity DB Log Analysis Project
This project simulates a SQL based analysis of a 1 million plus row database of logs for a digital publication. Three queries are run to rank articles, authors, and errors for the imagined publication. The project is part of the [Udacity](http://udacity.com) Full Stack Web Developer Nanodegree course. For crossplatform support, it runs on a virtual machine powered by [Vagrant](https://www.vagrantup.com/). We use [PostgreSQL](https://www.postgresql.org/) for the database. [Python 2.7.13](https://www.python.org/ftp/python/2.7.13/) is used for the binary that runs the reports.

## Table of contents

- [Quickstart](#quickstart)
- [Analysis](#analysis)
- [Todos](#todos)

## Quickstart
More detailed instructions are below but those familiar with the above technologies can likely get going with the following:
- [Download and install Python](https://www.python.org/ftp/python/2.7.13/) * 2.7.13 and later versions of Python 2 are supported
- [Download and install VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- [Download and install Vagrant](https://www.vagrantup.com/)
- [Download the news database, newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) ** Must be installed in a subfolder of your /vagrant path, for this quickstart we'll assume `../vagrant/news`
- [Clone this repository]() ** Must be cloned into a subfolder of your /vagrant path, for this quickstart we'll assume `../vagrant/news`
- Now some quick vagrant commands:
  1. `>cd vagrant`
  1. `>vagrant up` (this may take some time if it's your first vagrant up)
  2. `>vagrant ssh`
  3. `>cd news`
  3. `>psql -d news -f newsdata.sql`
  4. `>python log-analysis.py`

## Analysis

By following the quickstart, you will produce three reports that answer the project questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

Reports are rendered in a plain text format that is amenable to pasting into email or as part of a response to be used in other application (JSON, etc.). Reports include the question and responses in the following format:

```
Question to be answered
------------------------------------------------------
response data
------------------------------------------------------
```

If the quickstart is followed exactly, the reponses should be as follows:

```
*****************************************************************
1. What are the most popular three articles of all time?
        
*****************************************************************
Candidate is jerk, alleges rival -- 338,647 views
Bears love berries, alleges bear -- 253,801 views
Bad things gone, say good people -- 170,098 views
=================================================================
```

```
*****************************************************************
2. Who are the most popular article authors of all time?
        
*****************************************************************
Ursula La Multa -- 507,594 views
Rudolf von Treppenwitz -- 423,457 views
Anonymous Contributor -- 170,098 views
Markoff Chaney -- 84,557 views
=================================================================
```

```
***********************************************************************
3. On which days did more than 1% of requests lead to errors?'
        
***********************************************************************
July 17, 2016 -- 2.26% errors
=======================================================================
```

## Todos

The scope of this project was to compose SQL queries that could handle all of the data
analysis within the database environment with minimal python manipulation. In so doing, we take advantage of the power and speed of a relational database.

That said, an interface built on top of this system could empower the user to save queries, and cache responses. This would allow the user to conduct trend analyses. To suppport
such a feature, we would need a minimum of the following projects:
- Create a new table (or database) to store queries and their responses
- Provide a robust interface to allow the user to test and store queries
- Allow the user to export findings to csv, json, or xml for use in other applications
