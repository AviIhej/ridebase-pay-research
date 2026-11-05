"""Adds the 19 transportation network companies on the California CPUC TNC permits-issued page (page read 2026-11-05)."""
import sys; sys.path.insert(0, __file__.rsplit('/',1)[0]); from common import *
S='https://www.cpuc.ca.gov/regulatory-services/licensing/transportation-licensing-and-analysis-branch/transportation-network-companies/tnc-permits-issued'
R='California Public Utilities Commission TNC permit'
L=[('Silver Ride, Inc','Silver Ride','https://silverride.com','niche','Senior and accessible rides','TCP 21471'),
('Lyft, Inc','Lyft','https://www.lyft.com/','national platform','Ride-hail','TCP 32513'),
('Wingz, Inc','Wingz','https://www.wingz.com/','niche','Non-emergency medical and airport rides','TCP 32514'),
('Executive Ride LLC','Opoli','https://www.opoli.com/','regional platform','Ride-hail and car service','TCP 34171'),
('Ride Plus, LLC','Provado Mobile Health','','niche','Health ride service','TCP 36311'),
('Nomad Transit LLC','VIA','https://ridewithvia.com','white-label operator','Shared on-demand transit','TCP 37983'),
('Uber Technologies Inc','Uber','https://www.uber.com/','national platform','Ride-hail','TCP 38150'),
('Alto Operations California LLC','Alto','https://ridealto.com','regional platform','Employed-driver ride-hail','TCP 39432'),
('Onward Health Inc','Onward','','niche','Health ride service','TCP 40034'),
('HUM, Inc.','HUM','https://humrides.com','startup','Ride-hail','TCP 40925'),
('UZURV Holdings, Inc','Uzurv Holdings','https://uzurv.com','niche','Assisted mobility rides','TCP 41023'),
('Daytrip, Inc','Daytrip','','startup','Ride-hail','TCP 43824'),
('Ride Share Admin Services LLC','Prime Time Rideshare','https://www.primetimerideshare.com/','startup','Ride-hail','TCP 47643'),
('Ridein Technologies, Inc.','Ridenroll','https://ridenroll.com','startup','Event rideshare','TCP 43972'),
('The Pick N Drop LLC','Pick N Drop','','startup','Ride-hail','TCP 49694'),
('Local Driver Tech Inc.','Fare Co-op','https://farecoop.com','niche','Driver-owned ride-hail','TCP 44843'),
('Zietra Technologies inc','Dollar.ai','','startup','Ride-hail','TCP 50982'),
('HopSkipDrive, Inc','HopSkipDrive','https://www.hopskipdrive.com/','niche','Student rides (TNC permit, charter-party carrier section)','TCP 34668'),
('Dolightful, Inc','Kango','','niche','Kids rides','TCP 35591')]
rows=[mk(n,t,'US','CA',web=w,ride=r,reg=R,pid=p,ev=f"Listed on the CPUC TNC permits-issued page under the name {d}. The page lists carrier name, dba name and TCP number only.",src=S,mk_='California',parent='',score='3' if t=='national platform' else '2') for n,d,w,t,r,p in [(a[0],a[1],a[2],a[3],a[4],a[5]) for a in L]]
add_rows(rows)
