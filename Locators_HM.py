mainurl = 'https://attabotics-hivemind-test.azurewebsites.net'
##mainurl = 'https://attabotics-hivemind-test-feature.azurewebsites.net'

class ri_locators():
    ri_page = mainurl+'/manufacturing/robot_identities'
    create = '//*[@id="application"]/div[3]/div/div[1]/div[1]/button'
    generate = '/html/body/div[2]/div/div[2]/div/form/div[1]/div/button'
    GUIDfield = '/html/body/div[2]/div/div[2]/div/form/div[1]/div/input'
    GeneralAssembly = 'body > div.ui.dimmer.modals.page.transition.visible.active > div > div.scrolling.content > div > form > div:nth-child(2) > div > i.dropdown.icon'
    ant5_2 = '/html/body/div[2]/div/div[2]/div/form/div[2]/div/div[2]/div[9]'
    ant5_1 = '/html/body/div[2]/div/div[2]/div/form/div[2]/div/div[2]/div[8]'
    ant4_3 = '/html/body/div[2]/div/div[2]/div/form/div[2]/div/div[2]/div[6]'
    v4namefield = '/html/body/div[2]/div/div[2]/div/form/div[3]/input'
    RINgenerate ='/html/body/div[2]/div/div[2]/div/form/div[3]/div/button' 
    RINfield = '/html/body/div[2]/div/div[2]/div/form/div[3]/div'
    WOnumberfld = '/html/body/div[2]/div/div[2]/div/form/div[4]/input'
    radioID = '/html/body/div[2]/div/div[2]/div/form/div[5]/input' 
    saveRI = '/html/body/div[2]/div/div[3]/button[2]'
    searchbox = '//*[@id="application"]/div[3]/div/div[1]/div[2]/div/div[1]/div/input'
    searchBtn = '//*[@id="application"]/div[3]/div/div[1]/div[2]/div/div[1]/div/button'
    viewassemblyBtn = '//*[@id="application"]/div[3]/div/div[1]/div[3]/table/tbody/tr/td[9]/a/button'

class assemblies_locators():
    assign_page = mainurl+'/manufacturing/assemblies/assign_serial_number'
    subassembly_page = mainurl+"/manufacturing/assemblies/{0}#hierarchy"
    comm_ant_page = mainurl+"/commissioning/ants/{0}#comm"
    comm_assm_page = mainurl+"/commissioning/assemblies/{0}#comm"
    parent_page = mainurl+'/manufacturing/assemblies/parent_serial_number'  
    serial_number = '//*[@id="application"]/div[3]/div/div[1]/div/div/div[1]/div[1]/div/input'
    part_number = '//*[@id="application"]/div[3]/div/div[1]/div/div/div[1]/div[2]/div/input'
    WOnumber = '//*[@id="application"]/div[3]/div/div[1]/div/div/div[1]/div[3]/div/input'
    BOM_rev = '//*[@id="application"]/div[3]/div/div[1]/div/div/div[1]/div[4]/input'
    assign_but = '//*[@id="application"]/div[3]/div/div[1]/div/div/button'      
    sn1_field = '//*[@id="application"]/div[3]/div/div[1]/div/div/div[1]/div[1]/div/input'
    sn2_field = '//*[@id="application"]/div[3]/div/div[1]/div/div/div[1]/div[2]/div/input'
    parentchild_but = '//*[@id="application"]/div[3]/div/div[1]/div/div/div[2]/div/button' 

class capbanks_locators():
    cb_page = mainurl+'/commissioning/cap_banks'
    create = '//*[@id="application"]/div[3]/div/div[1]/div/div[1]/div[1]/div/button'
    serial_f = '/html/body/div[2]/div/div[2]/div/form/div[1]/input'
    hwvers_dd = 'body > div.ui.dimmer.modals.page.transition.visible.active > div > div.scrolling.content > div > form > div:nth-child(2) > div > i'
    hwvers_5 = '/html/body/div[2]/div/div[2]/div/form/div[2]/div/div/div[3]'
    loc_dd = 'body > div.ui.dimmer.modals.page.transition.visible.active > div > div.scrolling.content > div > form > div:nth-child(3) > div > i'
    loc_atta = '/html/body/div[2]/div/div[2]/div/form/div[3]/div/div/div[4]'
    save_b = '/html/body/div[2]/div/div[3]/button[2]'
    details_b = '//*[@id="application"]/div[3]/div/div[1]/div/div[3]/div/table/tbody/tr/td[1]/a/i'
    search = '//*[@id="application"]/div[3]/div/div[1]/div/div[1]/div[3]/div/input'
    link = '//*[@id="application"]/div[3]/div/div[1]/div/div/div[1]/div[1]/div[2]/div/button'
    antselect = '/html/body/div[2]/div[3]/div[2]/div/form/div[2]/div/input'
    matchedant = '/html/body/div[2]/div[3]/div[2]/div/form/div[2]/div/div[2]/div'
    saveant = '/html/body/div[2]/div[3]/div[3]/button[2]'
    
class tsb_locators():
    tsb_page = mainurl+'/commissioning/bulletins'
    create = '//*[@id="application"]/div[3]/div/div[1]/div[1]/div[1]/div[2]/button'    
    id_box = '/html/body/div[2]/div/div[2]/div/form/div[1]/div[1]/input'
    link_box = '/html/body/div[2]/div/div[2]/div/form/div[1]/div[2]/input'
    save_tsb = '/html/body/div[2]/div/div[3]/button[2]'
    first_option = 'body > div.ui.dimmer.modals.page.transition.visible.active > div > div.scrolling.content > div > form > div:nth-child(4) > div > div > div > div:nth-child(3) > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > input[type=checkbox]'
    search = '//*[@id="application"]/div[3]/div/div[1]/div[2]/div[1]/div[3]/div/input'
    details = '//*[@id="application"]/div[3]/div/div[1]/div[2]/div[3]/div/table/tbody/tr[1]/td[2]/a/i'
    details_tsb = '//*[@id="application"]/div[3]/div/div[1]/div/div/div[3]/div[2]/div/div/div[3]/div/table/tbody/tr/td[1]/a/i'
    update_tsb = '//*[@id="application"]/div[3]/div/div[1]/div[1]/div/div[3]/div[2]/div[7]/div[2]/table/tbody/tr[1]/td[9]/button'
    status_tsb = 'body > div.ui.dimmer.modals.page.transition.visible.active > div.ui.modal.transition.visible.active.front > div.content > form > div:nth-child(1) > div.ui.selection.dropdown > i'
    complete_tsb = '/html/body/div[2]/div[14]/div[2]/form/div[1]/div[1]/div[2]/div[4]'
    save_status = '/html/body/div[2]/div[12]/div[3]/button[2]' 

class struct_antmaint_locators():
    pass
