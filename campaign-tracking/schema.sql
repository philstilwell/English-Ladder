CREATE TABLE IF NOT EXISTS campaigns (
 id TEXT PRIMARY KEY, site TEXT NOT NULL, source TEXT NOT NULL,
 community TEXT NOT NULL, title TEXT NOT NULL, target TEXT NOT NULL,
 status TEXT NOT NULL DEFAULT 'draft' CHECK(status IN ('draft','active','published','test','ended')),
 post_url TEXT NOT NULL DEFAULT '', created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
 published_at TEXT, requests INTEGER NOT NULL DEFAULT 0,
 browser_arrivals INTEGER NOT NULL DEFAULT 0, engaged_visits INTEGER NOT NULL DEFAULT 0,
 internal_requests INTEGER NOT NULL DEFAULT 0, internal_arrivals INTEGER NOT NULL DEFAULT 0,
 test_requests INTEGER NOT NULL DEFAULT 0, test_arrivals INTEGER NOT NULL DEFAULT 0,
 bot_requests INTEGER NOT NULL DEFAULT 0, bot_arrivals INTEGER NOT NULL DEFAULT 0,
 CHECK(site IN ('englishladder.com','slugfester.com'))
);
CREATE TABLE IF NOT EXISTS visits (
 id TEXT PRIMARY KEY, campaign TEXT NOT NULL REFERENCES campaigns(id),
 bucket TEXT NOT NULL CHECK(bucket IN ('audience','internal','test','bot')),
 created_at INTEGER NOT NULL, arrived INTEGER NOT NULL DEFAULT 0,
 engaged INTEGER NOT NULL DEFAULT 0
);
CREATE INDEX IF NOT EXISTS visits_created ON visits(created_at);
CREATE TRIGGER IF NOT EXISTS campaign_request AFTER INSERT ON visits BEGIN
 UPDATE campaigns SET
 requests=requests+(NEW.bucket='audience'),
 internal_requests=internal_requests+(NEW.bucket='internal'),
 test_requests=test_requests+(NEW.bucket='test'),
 bot_requests=bot_requests+(NEW.bucket='bot') WHERE id=NEW.campaign;
END;
CREATE TRIGGER IF NOT EXISTS campaign_arrival AFTER UPDATE OF arrived ON visits
WHEN OLD.arrived=0 AND NEW.arrived=1 BEGIN
 UPDATE campaigns SET
 browser_arrivals=browser_arrivals+(NEW.bucket='audience'),
 internal_arrivals=internal_arrivals+(NEW.bucket='internal'),
 test_arrivals=test_arrivals+(NEW.bucket='test'),
 bot_arrivals=bot_arrivals+(NEW.bucket='bot') WHERE id=NEW.campaign;
END;
CREATE TRIGGER IF NOT EXISTS campaign_test_reclass AFTER UPDATE OF bucket ON visits
WHEN OLD.bucket='audience' AND NEW.bucket='test' AND OLD.arrived=0 BEGIN
 UPDATE campaigns SET requests=requests-1,test_requests=test_requests+1 WHERE id=NEW.campaign;
END;
CREATE TRIGGER IF NOT EXISTS campaign_engagement AFTER UPDATE OF engaged ON visits
WHEN OLD.engaged=0 AND NEW.engaged=1 BEGIN
 UPDATE campaigns SET engaged_visits=engaged_visits+(NEW.bucket='audience') WHERE id=NEW.campaign;
END;
CREATE VIEW IF NOT EXISTS campaign_results AS SELECT
 site, id AS post_id, source, community, title, status, post_url,
 'https://'||site||'/campaign/'||id AS campaign_link,
 'https://'||site||target AS resource,
 published_at, browser_arrivals, engaged_visits,
 requests AS unclassified_link_requests,
 internal_arrivals, test_arrivals, bot_arrivals,
 internal_requests, test_requests, bot_requests
 FROM campaigns;
CREATE VIEW IF NOT EXISTS campaign_dashboard AS SELECT
 title AS post, browser_arrivals AS arrivals, engaged_visits AS engaged,
 internal_arrivals AS internal, test_arrivals AS tests, bot_requests AS bot_requests,
 id AS post_id FROM campaigns;
