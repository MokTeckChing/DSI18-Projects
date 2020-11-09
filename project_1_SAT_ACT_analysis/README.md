# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 1: Standardized Testing, Statistical Summaries and Inference

### Problem Statement

Which states should the college board focus funding on to increase participation rates in the future?

### Executive Summary

The format of the SATs was changed in 2016 to better reflect the academic curriculum of US high schools. 

This notebook aims to determine if the format change improved participation rates for the SATs from 2017 to 2018 by cross-examining the data with the data from the ACTs, another national-level exam, from the same period. This notebook also aims to make recommendations on what states the colleage board should focus on in the future to imporve SAT participation rates.

The data reveals that participation rates for the SATs are independant of SAT scores. Instead, they are dependant on state policy, which is in turn influenced by the political ideology of that state.

### Data Dictionary

|Feature|Type|Dataset|Description|
|---|---|---|---|
|2017_SAT_state|string|sat_2017|participating state for SAT 2017| 
|2017_SAT_participation|float|sat_2017|participation percentage for SAT 2017| 
|2017_SAT_ebrw|float|sat_2017|evidence-based reading and writing score for SAT 2017 | 
|2017_SAT_math|float|sat_2017|Math score for SAT 2017| 
|2017_SAT_total|float|sat_2017|Total score for SAT 2017| 
|2017_ACT_participation |float|act_2017|participation percentage for ACT 2017| 
|2017_ACT_english|float|act_2017|English score for ACT 2017| 
|2017_ACT_math|float|act_2017|Math score for ACT 2017| 
|2017_ACT_reading|float|act_2017|Reading score for ACT 2017| 
|2017_ACT_science|float|act_2017|Science score for ACT 2017| 
|2017_ACT_composite |float|act_2017|Composite score for ACT 2017| 
|2018_SAT_participation|float|sat_2018|participation percentage for SAT 2018| 
|2018_SAT_ebrw|float|sat_2018|evidence-based reading and writing score for SAT 2018 | 
|2018_SAT_math|float|sat_2018|Math score for SAT 2018| 
|2018_SAT_total|float|sat_2018|Total score for SAT 2018| 
|2018_ACT_participation |float|act_2018|participation percentage for ACT 2018| 
|2018_ACT_english|float|act_2018|English score for ACT 2018| 
|2018_ACT_math|float|act_2018|Math score for ACT 2018| 
|2018_ACT_reading|float|act_2018|Reading score for ACT 2018| 
|2018_ACT_science|float|act_2018|Science score for ACT 2018| 
|2018_ACT_composite |float|act_2017|Composite score for ACT 2018| 

### Conclusion

It is suggested that the College Board target left-leaning states that require a mandatory ACT examination, such as Nevada, Utah and Wisconsin, and attempt to "flip" them.
