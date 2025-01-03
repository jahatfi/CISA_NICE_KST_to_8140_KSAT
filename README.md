This is a semantic tool to map CISA NICE cybersecurity tasks, knowledge, and skils, to the corresponding ones (aka KSAT) as implemented in the DoD 8140 framework.

e.g.

```
python semantic_search.py
10      Knowledge of application vulnerabilities
10A     Skill in conducting vulnerability scans and recognizing vulnerabilities in information systems and networks
1157    Ensure that AI design and development activities are properly documented and updated.
142A    Knowledge of the operations and processes for incident, problem, and event management.
Embedding NICE tasks...

8140 KSAT #10: Knowledge of application vulnerabilities
Top 5 most similar CISA NICE tasks:
NICE ID: T1118 (Score: 0.7025) "Identify vulnerabilities"
NICE ID: T0686 (Score: 0.6576) "Identify threat vulnerabilities"
NICE ID: T1690 (Score: 0.6433) "Identify exploitable technical or operational vulnerabilities"
NICE ID: T1028 (Score: 0.6283) "Research new vulnerabilities in emerging technologies"
NICE ID: T1559 (Score: 0.6146) "Resolve vulnerabilities in systems and system components"

8140 KSAT #10A: Skill in conducting vulnerability scans and recognizing vulnerabilities in information systems and networks
Top 5 most similar CISA NICE tasks:
NICE ID: T1118 (Score: 0.6574) "Identify vulnerabilities"
NICE ID: T0686 (Score: 0.6142) "Identify threat vulnerabilities"
NICE ID: T1619 (Score: 0.6113) "Perform risk and vulnerability assessments"
NICE ID: T1690 (Score: 0.5987) "Identify exploitable technical or operational vulnerabilities"
NICE ID: T1747 (Score: 0.5938) "Identify system vulnerabilities within a network"

8140 KSAT #1157: Ensure that AI design and development activities are properly documented and updated.
Top 5 most similar CISA NICE tasks:
NICE ID: T1704 (Score: 0.4816) "Develop intelligence operations plans"
NICE ID: T1750 (Score: 0.4789) "Identify intelligence environment preparation derived production needs"
NICE ID: T1115 (Score: 0.4550) "Oversee the development of design solutions"
NICE ID: T1798 (Score: 0.4516) "Provide intelligence analysis and support"
NICE ID: T1835 (Score: 0.4369) "Determine if intelligence requirements and collection plans are accurate and up-to-date"

8140 KSAT #142A: Knowledge of the operations and processes for incident, problem, and event management.
Top 5 most similar CISA NICE tasks:
NICE ID: T1427 (Score: 0.5890) "Maintain incident tracking and solution databases"
NICE ID: T1977 (Score: 0.5525) "Coordinate with internal and external incident management partners across jurisdictions"
NICE ID: T1333 (Score: 0.5502) "Communicate incident findings to appropriate constituencies"
NICE ID: T1986 (Score: 0.5489) "Develop a continuously updated overview of an incident throughout the incident's life cycle"
NICE ID: T1538 (Score: 0.5427) "Resolve customer-reported system incidents and events"
That took 9.631466150283813 s
```