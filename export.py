import sys 
import mysql.connector as mc
from xlwt import Workbook, Formula
import datetime

#Start of programming from here

#Starting of connection of mysql database and data fetch
conn=mc.connect(host="localhost",user="root",password="",database="mfin_db")
cnx=conn.cursor()
query=("""select 
    sp.id as id,
    sp.name as name,
    interest_rate_default,
    tax_on_interest,
    interest_calc_by,
    interest_cal_method,
    ah1.name as 'expense_head',
    ah2.name as 'provision_head',
    ah3.name as 'liabilities_head',
    ah4.name as 'tds_head'
from
    saving_product sp
        left join
    account_head ah1 ON sp.saving_expenditure_id = ah1.id
        left join
    account_head ah2 ON sp.interest_provision_id = ah2.id
        left join
    account_head ah3 ON sp.saving_for_liabilities_id = ah3.id
        left join 
 account_head ah4 ON sp.tds_account_head = ah4.id""")

cnx.execute(query)

#creating workbook 
wb=Workbook()
#Adding new sheet
sheet1=wb.add_sheet("Sheet 1")
#For managing the width of the sheet 
for i in range(10):
    sheet1.col(i).width=7000
    
sheet1.write(0,0,'id')
sheet1.write(0,1,'name')
sheet1.write(0,2,'interest_rate_default')
sheet1.write(0,3,'tax_on_interest')
sheet1.write(0,4,'interest_calc_by')
sheet1.write(0,5,'interest_cal_method')
sheet1.write(0,6,'expense_head')
sheet1.write(0,7,'provision_head')
sheet1.write(0,8,'liabilities_head')
sheet1.write(0,9,'tds_head') 
i=0

temp=datetime.datetime.now().isoformat()
filename=temp.split(".",1)[0]
filename=filename.replace(":","_")
del temp
print(filename)
for (id,name,interest_rate_default,tax_on_interest,interest_calc_by,interest_cal_method,expense_head,provision_head,liabilities_head,tds_head) in cnx:
    i=i+1		
    while (1):
        sheet1.write(i,0,id)
        sheet1.write(i,1,name)
        sheet1.write(i,2,interest_rate_default)
        sheet1.write(i,3,tax_on_interest)
        sheet1.write(i,4,interest_calc_by)
        sheet1.write(i,5,interest_cal_method)
        sheet1.write(i,6,expense_head)
        sheet1.write(i,7,provision_head)
        sheet1.write(i,8,liabilities_head)
        sheet1.write(i,9,tds_head)        
        break
wb.save(filename+"account_tds_saving.xls")

del query
del wb
#initiating new cursor value for writing to check charge profile saving product data

query1=("""select 
    cd.ndate as ndate,
    charge_profile.charge_date as charge_date,
    charge_profile.is_fiscal_year_closing as is_fiscal_year_closing,
    saving_product.name as saving_product_name,
    saving_product.interest_rate_default as interest_rate_default,
    tax_on_interest,
    interest_cal_method,
    interest_calc_by
from
    charge_profile_detail
        inner join
    saving_product ON saving_product.id = charge_profile_detail.saving_product_id
        inner join
    charge_profile ON charge_profile.id = charge_profile_detail.charge_profile_id
        inner join
    calendar_data cd ON cd.edate = charge_profile.charge_date
where
    charge_profile_id in (select 
            id
        from
            charge_profile
        where
            charge_date = '2018-07-16') """)

cnx.execute(query1)

#Starting and creating new workbook
wb1=Workbook()

#Adding new sheet
sheet1=wb1.add_sheet("Sheet 1")
#For managing the width of the sheet 
for i in range(8):
    sheet1.col(i).width=7000

#dEFINING HEADERS

sheet1.write(0,0,'ndate')
sheet1.write(0,1,'charge_date')
sheet1.write(0,2,'is_fiscal_year_closing')
sheet1.write(0,3,'saving_product_name')
sheet1.write(0,4,'interest_rate_default')
sheet1.write(0,5,'tax_on_interest')
sheet1.write(0,6,'interest_cal_method')
sheet1.write(0,7,'interest_calc_by')

i=0
for (ndate,charge_date,is_fiscal_year_closing,saving_product_name,interest_rate_default,tax_on_interest,interest_cal_method,interest_calc_by) in cnx:
    i=i+1
    while(1):
        sheet1.write(i,0,ndate)
        sheet1.write(i,1,charge_date)
        sheet1.write(i,2,is_fiscal_year_closing)
        sheet1.write(i,3,saving_product_name)
        sheet1.write(i,4,interest_rate_default)
        sheet1.write(i,5,tax_on_interest)
        sheet1.write(i,6,interest_cal_method)
        sheet1.write(i,7,interest_calc_by)
        break

wb1.save(filename+"charge_profile_sp.xls")

del wb1
del query1

#initiating query for saving product not set in charge profile  record(in current closing) (send compulsary to client


query2=("""select 
    id,
    name,
    interest_rate_default,
    tax_on_interest,
    interest_cal_method,
    interest_calc_by
from
    saving_product
where
    id not in (select 
            saving_product_id
        from
            charge_profile_detail
                inner join
            saving_product ON saving_product.id = charge_profile_detail.saving_product_id
                inner join
            charge_profile ON charge_profile.id = charge_profile_detail.charge_profile_id
        where
            charge_profile_id in (select 
                    id
                from
                    charge_profile
                where
                    charge_date = '2018-10-17')) """)

cnx.execute(query2)

#Starting and creating new workbook
wb2=Workbook()

#Adding new sheet
sheet1=wb2.add_sheet("Sheet 1")

#For managing the width of the sheet 
for i in range(6):
    sheet1.col(i).width=7000

#dEFINING HEADERS

sheet1.write(0,0,'id')
sheet1.write(0,1,'name')
sheet1.write(0,2,'interest_rate_default')
sheet1.write(0,3,'tax_on_interest')
sheet1.write(0,4,'interest_cal_method')
sheet1.write(0,5,'interest_calc_by')

i=0
for (id,name,interest_rate_default,tax_on_interest,interest_cal_method,interest_calc_by) in cnx:
    i=i+1
    while(1):
        sheet1.write(i,0,id)
        sheet1.write(i,1,name)
        sheet1.write(i,2,interest_rate_default)
        sheet1.write(i,3,tax_on_interest)
        sheet1.write(i,4,interest_cal_method)
        sheet1.write(i,5,interest_calc_by)
        break

wb2.save(filename+"charge_profile_record.xls")

del wb2
del query2

#Query for identifying the things To display organization type (either taxable,not taxable or tax beyond limit)
query3=(""" select id,name ,location_type from organization """)
cnx.execute(query3)

#Starting and creating new workbook
wb3=Workbook()

#Adding new sheet
sheet1=wb3.add_sheet("Sheet 1")

#For managing the width of the sheet 
for i in range(3):
    sheet1.col(i).width=7000

#dEFINING HEADERS
sheet1.write(0,0,'id')
sheet1.write(0,1,'name')
sheet1.write(0,2,'location_type')

i=0
for (id,name,location_type ) in cnx:
    i=i+1
    while(1):
        sheet1.write(i,0,id)
        sheet1.write(i,1,name)
        sheet1.write(i,2,location_type)
        break

wb3.save(filename+"_org_tax_type.xls")
del wb3
del query3

#Last file to check account head  set up for Loan with initialization start of query

query4=("""select 
    lp.id as id,
    lp.name as name,
    lp.alias_name as alias_name,
    lpd.Interestratedefault as Interestratedefault,
    lpd.interestRateMaximum as interestRateMaximum,
    lpd.interestRateMinimum as interestRateMinimum,
    lpd.interestcalculation as interestcalculation,
    lpd.amortization as amortization,
    ah.name as income,
    ah1.name as assets,
    ah2.name as rebate
from
    loan_product lp
        left join
    loan_product_detail lpd ON lp.id = lpd.id
        left join
    account_head ah ON lp.account_head_income_id = ah.id
        left join
    account_head ah1 ON lp.account_head_assets_id = ah1.id
        left join
    account_head ah2 ON lp.account_head_rebate_id = ah2.id """)
cnx.execute(query4)

#Starting and creating new workbook
wb4=Workbook()

#Adding new sheet
sheet1=wb4.add_sheet("Sheet 1")

#For managing the width of the sheet 
for i in range(11):
    sheet1.col(i).width=7000

#dEFINING HEADERS
sheet1.write(0,0,'id')
sheet1.write(0,1,'name')
sheet1.write(0,2,'alias_name')
sheet1.write(0,3,'Interestratedefault')
sheet1.write(0,4,'interestRateMaximum')
sheet1.write(0,5,'interestRateMinimum')
sheet1.write(0,6,'interestcalculation')
sheet1.write(0,7,'amortization')
sheet1.write(0,8,'income')
sheet1.write(0,9,'assets')
sheet1.write(0,10,'rebate') 

i=0
for (id,name,alias_name,Interestratedefault,interestRateMaximum,interestRateMinimum,interestcalculation,amortization,income,assets,rebate) in cnx:
    i=i+1
    while(1):
        sheet1.write(i,0,id)
        sheet1.write(i,1,name)
        sheet1.write(i,2,alias_name)
        sheet1.write(i,3,Interestratedefault)
        sheet1.write(i,4,interestRateMaximum)
        sheet1.write(i,5,interestRateMinimum)
        sheet1.write(i,6,interestcalculation)
        sheet1.write(i,7,amortization)
        sheet1.write(i,8,income)
        sheet1.write(i,9,assets)
        sheet1.write(i,10,rebate) 
        break

wb4.save(filename+"_set_up_Loan.xls")
del wb4
del query4

#CLOsing the connection of cursor
cnx.close()

#closing the connection parameters
conn.close()



