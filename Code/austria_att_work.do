*************************************************
* Austrian Bundesliga Work                      *
* Author: Tate Mason         dmason27@uncc.edu  * 
* Collaborators: Dr. Craig Depken and Alex Frei *
* austria_att_work.do              Jan 15, 2024 *
*************************************************

*************************************************
* Environment Setup                             *
*************************************************
	#delimit cr
	clear
	clear all
	set more off
	
	set scheme white_tableau
		*ssc install schemepack*
	
	//Data Paths//
	
	local data "/Users/tate/Library/CloudStorage/Dropbox/Austrian_Bundesliga/Data"
	local output "/Users/tate/Library/CloudStorage/Dropbox/Austrian_Bundesliga/Output"
	
	local summTotal = 1
	local summModern = 0
	local summFirst = 0
	
	
	
*************************************************
* Summary Stats (Full Time Horizon)             *
*************************************************

	if `summTotal' {
		
		use `data'/original-playoff-att-data.dta, clear
	
		local vars "Rank Total Matches Average"
		
		foreach v of local vars {
			destring(`v'), replace
		}
		gen Playoff = 0
		replace Playoff = 1 if Year>=1985 & Year<=1992
		replace Playoff = 1 if Year>=2018 & Year<=2022

		collapse (sum) Total, by(Year)
				
		tsset Year
		tsline Total, title("Total Average Attendance: 1974-2023") xtitle("Year") ytitle("Average Total Attendance")
			
			
			graph export "`output'/total-average-att.pdf", replace
	}

*************************************************
* Summary Stats (Modern Playoff Era)            *
*************************************************	

	if `summModern' {
		use `data'/modern-playoff-att-data.dta, clear
		
		local vars "Rank Total Matches Average"
		
		foreach v of local vars {
			destring(`v'), replace
		}
		
	
	collapse Total, by(Year)
	
	tsset Year
	tsline Total
		
	}

	