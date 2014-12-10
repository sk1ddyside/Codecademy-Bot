try:
    import mechanize #tries to import mechanize
except ImportError: #if cant import mechanize
    print 'Oops. It seems as if you do not have mechanize installed'
codecademy = 'www.codecademy.com' #stores codecademy link as a variable
codecademySI = 'http://www.codecademy.com/sign_in' #codecademy sign in link
codecademyJS = 'http://www.codecademy.com/courses/getting-started-v2/0/1?curriculum_id=506324b3a7dffd00020bf661' #Javascript link

br = mechanize.Browser() #make a mechanize browser object, acts as virtual browser, emulator
br.open(codecademy) #opens codecademy

#signing up
#def signUp(username, password, email):
 #   br.select_form(nr=0) #selects first form on the page
    
 #   br["user[email]"] = email #sets value of email field to whatever user entered
  #  br["user[password]"] = password #sets value of username field to whatever user entered
 #   br["user[username]"] = username #sets value of password field to whatever user entered

    #submittionResult = br.submit() #submits data entered above

def logIn(username, password):
    br.open(codecademySI) #opens codecademy

    br.select_form('sign-in-form')#finds login button
    br.form ['q'] = query
    br.submit()#clicks login button

    br["user[login]"] = username #sets value of email/username field to whatever user entered
    br["user[password]"] = password #sets value of password field to whatever user entered

    submittionResult = br.submit() #submits data entered above, local so doesnt overrideother Submittion Result

def _JS():
    br.open(codecamedyJS)
    #ace_text-input ui-inited
    js = 1
    if(js == 1):
        br["ace_text-input ui-inited"] = '"Name"'
        js =+ 1
    elif(js == 2):
        br["ace_text-input ui-inited"] = '"Name".length'
        js =+ 1
    elif(js == 3):
        br["ace_text-input ui-inited"] = '3 + 4'
        js =+ 1
    elif(js == 4):
        br["ace_text-input ui-inited"] = '4 * 4'
        js =+ 1
    elif(js == 5):
        br["ace_text-input ui-inited"] = 'eggplant'
        js =+ 1
    elif(js == 6):
        br["ace_text-input ui-inited"] = '"cake".length'
        js =+ 1
    elif(js == 7):
        br["ace_text-input ui-inited"] = 'confirm("This is an example of using JS to create some interaction on a website. Click OK to continue!");'
        js =+ 1
    elif(js == 8):
        br["ace_text-input ui-inited"] = 'confirm("I fell awesome!")'
        js =+ 1
    elif(js == 9):
        br["ace_text-input ui-inited"] = 'prompt("What is your name?");'
        js =+ 1
    elif(js == 10):
        br["ace_text-input ui-inited"] = '"string with words".length'
        js =+ 1
    elif(js == 11):
        br["ace_text-input ui-inited"] = '"Im coding like a champ".length'
        js =+ 1
    #browser.form = list(browser.forms())[0] #find form with no name
    br.select_form('ui-button ui-button--medium ui-button--blue--on-dark ui-loading js-submit-code')
    br.form ['q'] = query
    br.submit()
#signUp(russ999999, **********, r****@optonline.net)
logIn(russ99999, **********)
