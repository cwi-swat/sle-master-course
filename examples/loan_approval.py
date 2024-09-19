from selenium.webdriver.common.by import By
def loan_approval_myql_oracle(driver):
    state = driver.execute_script('return $state;');
    
    assert not True or driver.find_elements(By.ID, 'fullName_div_25')[0].is_displayed(), 'true evaluated to true, however fullName_div_25 was not displayed'
    assert not True or driver.find_elements(By.ID, 'age_div_70')[0].is_displayed(), 'true evaluated to true, however age_div_70 was not displayed'
    assert not True or driver.find_elements(By.ID, 'hasLicense_div_104')[0].is_displayed(), 'true evaluated to true, however hasLicense_div_104 was not displayed'
    assert not (True and (state['age'] < 18)) or driver.find_elements(By.ID, 'inSchool_div_183')[0].is_displayed(), 'true && age < 18 evaluated to true, however inSchool_div_183 was not displayed'
    assert not ((True and (state['age'] < 18)) and state['inSchool']) or driver.find_elements(By.ID, 'grade_div_258')[0].is_displayed(), 'true && age < 18 && inSchool evaluated to true, however grade_div_258 was not displayed'
    assert not ((True and not (((state['age'] < 18)))) and ((state['age'] >= 18) and (state['age'] <= 65))) or driver.find_elements(By.ID, 'employed_div_360')[0].is_displayed(), 'true && !(age < 18) && age >= 18 && age <= 65 evaluated to true, however employed_div_360 was not displayed'
    assert not (((True and not (((state['age'] < 18)))) and ((state['age'] >= 18) and (state['age'] <= 65))) and state['employed']) or driver.find_elements(By.ID, 'jobTitle_div_445')[0].is_displayed(), 'true && !(age < 18) && age >= 18 && age <= 65 && employed evaluated to true, however jobTitle_div_445 was not displayed'
    assert not (((True and not (((state['age'] < 18)))) and ((state['age'] >= 18) and (state['age'] <= 65))) and state['employed']) or driver.find_elements(By.ID, 'yearsInJob_div_496')[0].is_displayed(), 'true && !(age < 18) && age >= 18 && age <= 65 && employed evaluated to true, however yearsInJob_div_496 was not displayed'
    assert not (((True and not (((state['age'] < 18)))) and ((state['age'] >= 18) and (state['age'] <= 65))) and state['employed']) or driver.find_elements(By.ID, 'monthlySalary_div_578')[0].is_displayed(), 'true && !(age < 18) && age >= 18 && age <= 65 && employed evaluated to true, however monthlySalary_div_578 was not displayed'
    assert not (((True and not (((state['age'] < 18)))) and ((state['age'] >= 18) and (state['age'] <= 65))) and state['employed']) or driver.find_elements(By.ID, 'monthlyExpenses_div_640')[0].is_displayed(), 'true && !(age < 18) && age >= 18 && age <= 65 && employed evaluated to true, however monthlyExpenses_div_640 was not displayed'
    assert not (((True and not (((state['age'] < 18)))) and ((state['age'] >= 18) and (state['age'] <= 65))) and state['employed']) or driver.find_elements(By.ID, 'annualSavings_div_713')[0].is_displayed(), 'true && !(age < 18) && age >= 18 && age <= 65 && employed evaluated to true, however annualSavings_div_713 was not displayed'
    assert state['annualSavings'] == (((state['monthlySalary'] - state['monthlyExpenses'])) * 12) if (((True and not (((state['age'] < 18)))) and ((state['age'] >= 18) and (state['age'] <= 65))) and state['employed']) else True, ' annualSavings was not the same as (monthlySalary - monthlyExpenses) * 12, expected ' + (((state['monthlySalary'] - state['monthlyExpenses'])) * 12) + ', got ' + state['annualSavings']
    assert not (((True and not (((state['age'] < 18)))) and ((state['age'] >= 18) and (state['age'] <= 65))) and not ((state['employed']))) or driver.find_elements(By.ID, 'lookingForJob_div_822')[0].is_displayed(), 'true && !(age < 18) && age >= 18 && age <= 65 && !(employed) evaluated to true, however lookingForJob_div_822 was not displayed'
    assert not ((True and not (((state['age'] < 18)))) and not ((((state['age'] >= 18) and (state['age'] <= 65))))) or driver.find_elements(By.ID, 'retired_div_910')[0].is_displayed(), 'true && !(age < 18) && !(age >= 18 && age <= 65) evaluated to true, however retired_div_910 was not displayed'
    assert not (((True and not (((state['age'] < 18)))) and not ((((state['age'] >= 18) and (state['age'] <= 65))))) and state['retired']) or driver.find_elements(By.ID, 'yearsRetired_div_975')[0].is_displayed(), 'true && !(age < 18) && !(age >= 18 && age <= 65) && retired evaluated to true, however yearsRetired_div_975 was not displayed'
    assert not (((True and not (((state['age'] < 18)))) and not ((((state['age'] >= 18) and (state['age'] <= 65))))) and state['retired']) or driver.find_elements(By.ID, 'annualPension_div_1039')[0].is_displayed(), 'true && !(age < 18) && !(age >= 18 && age <= 65) && retired evaluated to true, however annualPension_div_1039 was not displayed'
    assert not (((True and not (((state['age'] < 18)))) and not ((((state['age'] >= 18) and (state['age'] <= 65))))) and state['retired']) or driver.find_elements(By.ID, 'healthcareExpenses_div_1101')[0].is_displayed(), 'true && !(age < 18) && !(age >= 18 && age <= 65) && retired evaluated to true, however healthcareExpenses_div_1101 was not displayed'
    assert not (((True and not (((state['age'] < 18)))) and not ((((state['age'] >= 18) and (state['age'] <= 65))))) and state['retired']) or driver.find_elements(By.ID, 'netPension_div_1180')[0].is_displayed(), 'true && !(age < 18) && !(age >= 18 && age <= 65) && retired evaluated to true, however netPension_div_1180 was not displayed'
    assert state['netPension'] == (state['annualPension'] - state['healthcareExpenses']) if (((True and not (((state['age'] < 18)))) and not ((((state['age'] >= 18) and (state['age'] <= 65))))) and state['retired']) else True, ' netPension was not the same as annualPension - healthcareExpenses, expected ' + (state['annualPension'] - state['healthcareExpenses']) + ', got ' + state['netPension']
    assert not True or driver.find_elements(By.ID, 'seniorDiscount_div_1296')[0].is_displayed(), 'true evaluated to true, however seniorDiscount_div_1296 was not displayed'
    assert state['seniorDiscount'] == ((state['age'] >= 65) and state['retired']) if True else True, ' seniorDiscount was not the same as age >= 65 && retired, expected ' + ((state['age'] >= 65) and state['retired']) + ', got ' + state['seniorDiscount']
    assert not True or driver.find_elements(By.ID, 'income_div_1398')[0].is_displayed(), 'true evaluated to true, however income_div_1398 was not displayed'
    assert not True or driver.find_elements(By.ID, 'monthlyDebts_div_1446')[0].is_displayed(), 'true evaluated to true, however monthlyDebts_div_1446 was not displayed'
    assert not True or driver.find_elements(By.ID, 'hasCoSigner_div_1501')[0].is_displayed(), 'true evaluated to true, however hasCoSigner_div_1501 was not displayed'
    assert not True or driver.find_elements(By.ID, 'loanAmount_div_1564')[0].is_displayed(), 'true evaluated to true, however loanAmount_div_1564 was not displayed'
    assert not True or driver.find_elements(By.ID, 'interestRate_div_1608')[0].is_displayed(), 'true evaluated to true, however interestRate_div_1608 was not displayed'
    assert not True or driver.find_elements(By.ID, 'loanTerm_div_1666')[0].is_displayed(), 'true evaluated to true, however loanTerm_div_1666 was not displayed'
    assert not True or driver.find_elements(By.ID, 'totalInterest_div_1709')[0].is_displayed(), 'true evaluated to true, however totalInterest_div_1709 was not displayed'
    assert state['totalInterest'] == (lambda div: ((((state['loanAmount'] * state['interestRate']) * state['loanTerm'])) // div) if div != 0 else 0)(100) if True else True, ' totalInterest was not the same as (loanAmount * interestRate * loanTerm) / 100, expected ' + (lambda div: ((((state['loanAmount'] * state['interestRate']) * state['loanTerm'])) // div) if div != 0 else 0)(100) + ', got ' + state['totalInterest']
    assert not True or driver.find_elements(By.ID, 'totalRepayment_div_1809')[0].is_displayed(), 'true evaluated to true, however totalRepayment_div_1809 was not displayed'
    assert state['totalRepayment'] == (state['loanAmount'] + state['totalInterest']) if True else True, ' totalRepayment was not the same as loanAmount + totalInterest, expected ' + (state['loanAmount'] + state['totalInterest']) + ', got ' + state['totalRepayment']
    assert not True or driver.find_elements(By.ID, 'monthlyPayment_div_1892')[0].is_displayed(), 'true evaluated to true, however monthlyPayment_div_1892 was not displayed'
    assert state['monthlyPayment'] == (lambda div: (state['totalRepayment'] // div) if div != 0 else 0)(((state['loanTerm'] * 12))) if True else True, ' monthlyPayment was not the same as totalRepayment / (loanTerm * 12), expected ' + (lambda div: (state['totalRepayment'] // div) if div != 0 else 0)(((state['loanTerm'] * 12))) + ', got ' + state['monthlyPayment']
    assert not True or driver.find_elements(By.ID, 'loanApproved_div_1984')[0].is_displayed(), 'true evaluated to true, however loanApproved_div_1984 was not displayed'
    assert state['loanApproved'] == ((((state['income'] > 50000) and (state['monthlyDebts'] < 10000))) or state['hasCoSigner']) if True else True, ' loanApproved was not the same as (income > 50000 && monthlyDebts < 10000) || hasCoSigner, expected ' + ((((state['income'] > 50000) and (state['monthlyDebts'] < 10000))) or state['hasCoSigner']) + ', got ' + state['loanApproved']
    assert not (True and state['loanApproved']) or driver.find_elements(By.ID, 'approvalMessage_div_2114')[0].is_displayed(), 'true && loanApproved evaluated to true, however approvalMessage_div_2114 was not displayed'
    assert state['approvalMessage'] == 'Approved' if (True and state['loanApproved']) else True, ' approvalMessage was not the same as "Approved", expected ' + 'Approved' + ', got ' + state['approvalMessage']
    assert not (True and not ((state['loanApproved']))) or driver.find_elements(By.ID, 'not_approvalMessage_div_2214')[0].is_displayed(), 'true && !(loanApproved) evaluated to true, however not_approvalMessage_div_2214 was not displayed'
    assert state['not_approvalMessage'] == 'Not Approved' if (True and not ((state['loanApproved']))) else True, ' not_approvalMessage was not the same as "Not Approved", expected ' + 'Not Approved' + ', got ' + state['not_approvalMessage']
