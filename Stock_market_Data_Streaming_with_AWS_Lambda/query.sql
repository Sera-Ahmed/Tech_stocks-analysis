select
distinct name as "Name",
hour as "Hour",
ts as "Time",
max_high as "Max High"

from 
(select
 raw1.name, 
 raw1.hour,
 raw1.ts,
 raw2.max_high
 
 from
 (select
  distinct name,
  high,
  ts,
  substring(ts,12,2) as hour
  
  from
  "stocks8"."04"
  ) raw1
 
 
 INNER JOIN 
 
 (select
 distinct name,
 substring(ts,12,2) as hour,
 max(high) as max_high
 
 from 
 "stocks8"."04"
 
 group by name,substring(ts,12,2)
 ) raw2
 
 on raw1.name = raw2.name and raw1.hour = raw2.hour and raw1.high = raw2.max_high)
 
 order by name, hour
 
 ;
 
 
 