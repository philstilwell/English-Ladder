import sqlite3
from pathlib import Path
db=sqlite3.connect(':memory:')
db.executescript(Path(__file__).with_name('schema.sql').read_text())
db.execute("INSERT INTO campaigns(id,site,source,community,title,target,status) VALUES('el-test1','englishladder.com','reddit','test','Test','/grammar-concepts/concept-12.html','published')")
for bucket in ['audience','internal','test','bot']:
 db.execute('INSERT INTO visits(id,campaign,bucket,created_at) VALUES(?,?,?,?)',(bucket,'el-test1',bucket,1))
 for _ in range(2):
  db.execute('UPDATE visits SET arrived=1 WHERE id=?',(bucket,))
  db.execute('UPDATE visits SET engaged=1 WHERE id=?',(bucket,))
row=db.execute('SELECT requests,browser_arrivals,engaged_visits,internal_arrivals,test_arrivals,bot_arrivals FROM campaigns').fetchone()
assert row==(1,1,1,1,1,1),row
db.execute("INSERT INTO visits(id,campaign,bucket,created_at) VALUES('reclass','el-test1','audience',1)")
for _ in range(2): db.execute("UPDATE visits SET bucket='test' WHERE id='reclass' AND bucket='audience' AND arrived=0")
assert db.execute('SELECT requests,test_requests FROM campaigns').fetchone()==(1,2)
db.execute('DELETE FROM visits WHERE created_at < 2')
assert db.execute('SELECT browser_arrivals,engaged_visits FROM campaign_results').fetchone()==(1,1)
print('PASS: SQLite totals, duplicate-event prevention, category separation, reclassification and retention')
