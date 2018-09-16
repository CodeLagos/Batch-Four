#JOSEPH OLUWASEGUN 
#PHOLARWALK@GMAIL.COM
#CODELAGOS

#entering personal details
full_name = input("Kindly enter your full name in BLOCK LETTERS :\t")
tin = str(input("Kindly enter tax identification number :\t"))
address =input("Kindly enter your home address :\t")



#import datetime for actual format

import datetime
date_entry = input("Kindly enter your tax return start date in YYYY-MM-DD format:\t")
year, month, day = map(int, date_entry.split('-'))
start_date = datetime.date(year, month, day)

date_entry = input("Kindly enter your tax return end date in YYYY-MM-DD format:\t")
year, month, day = map(int, date_entry.split('-'))
end_date = datetime.date(year, month, day)

#entering duration of vat you wanna file

actual_duration = end_date - start_date


#now calculation sales and income aspect

#define the variable with calculations

sales_income = float(input("Enter your total supplies amount for the period, including tax : "))

zero_rated = float(input("Enter your exempted and zero rated supplies amount :\t"))

total_supplies = sales_income - zero_rated

#vat standard calculation

vat_charged = total_supplies / 1.05

vat_chargd = round(vat_charged, 2)

subtracted_vat = total_supplies - vat_chargd

vat_adjustment = float(input("Enter vat adjustment :\t"))

total_output = subtracted_vat + vat_adjustment

final_total_output = round (total_output, 2)

print ("Your TOTAL OUTPUT TAX is", final_total_output )

#now calculation purchase and expenses aspect

purchase_exp = float(input("Enter your domestic purchases amount for which requirement were met :\t"))

vat_adj_purchase = float(input("Enter vat adjustment on purchases :\t"))

vat_import = float(input("Enter also vat on import if applicable :\t"))

total_payable = purchase_exp + vat_adj_purchase + vat_import

vat_purchase = float(input("Enter vat on purchases not used in supplies :\t"))

vat_taken = float(input("Enter vat taken at source :\t"))

total_deduc = total_payable -vat_purchase - vat_taken

print ("Your TOTAL INPUT TAX is", total_deduc )

amt_payable_refundable = final_total_output - total_deduc

amt_payabl_refundabl = round(amt_payable_refundable, 2)

"\n"


print (full_name, "\t", tin, "\t", address, "\t","\n", actual_duration,"\t", start_date,"\t","-" , end_date)

print("The amount to be return for", actual_duration, "from the FIRS is", amt_payabl_refundabl)
