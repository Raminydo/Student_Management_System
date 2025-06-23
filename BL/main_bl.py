


import os
from typing import Any
from DAL.data import *

teacher_list_file_path = r'File/teacher_list.text'
student_list_file_path = r'File/student_list.text'


def convert_liststr_listdict(data: list[str]) -> list[dict]:
    return list(map(lambda i: eval(i.strip()), data))

def convert_listdict_liststr(data: list[dict]) -> list[str]:
    return list(map(lambda i: f'{i}\n', data))


def save_person(type: str, person: dict) -> dict:
    
    function_res = {'success': None, 'error_msg': {}, 'success_msg': {}, 'returndata': None}
    
    if type == 'teacher':

        firstname = person['firstname'].strip()
        lastname = person['lastname'].strip()
        username = person['username'].strip()
        password = person['password'].strip()
        email = person['email'].strip()

        #region validation

        #region name
        if (not firstname) or (not firstname.isalpha()) or (not firstname.islower()):
            function_res['error_msg']['firstname'] = f'Firstname Error!!!'
            
        if (not lastname) or (not lastname.isalpha()) or (not lastname.islower()):
            function_res['error_msg']['lastname'] = f'Lastname Error!!!'
        #endregion

        #region username   
        if (not username) or (not username.isalnum()):
            function_res['error_msg']['username'] = f'Username Error!!!'
        #endregion

        #region password
        underscore = []   
        for i in password:
            if i == '_':
                underscore.append('')     

        if (not password) or (len(password) != 8) or (not password.isalnum()) and (not underscore):
            function_res['error_msg']['password'] = f'Password Error!!!'
        #endregion
        
        #region email
        if (not email) or (not email.isprintable()):
            function_res['error_msg']['email'] = f'Email Error!!!'
        #endregion

        #endregion

        #region unique

        #region username
        result = get_person(type='teacher')

        if not result['success']:
            function_res['success'] = False
            function_res['error_msg']['datasource'] = 'Data Source Error!'
            return function_res
        
        teacher_list = result['returndata']

        for ppl in teacher_list:
            if ppl['username'] == username:
                function_res['success'] = False
                function_res['error_msg']['username'] = f'The username: {username} exists.'        
        #endregion

        #region email
        result = get_person(type='teacher')

        if not result['success']:
            function_res['success'] = False
            function_res['error_msg']['datasource'] = 'Data Source Error!'
            return function_res
        
        teacher_list = result['returndata']

        for ppl in teacher_list:
            if ppl['email'] == email:
                function_res['success'] = False
                function_res['error_msg']['email'] = f'The email: {email} exists.'      
        #endregion

        if function_res['error_msg']:
            function_res['success'] = False
            return function_res 
        
        #endregion
            
        #region save teacher
        result = save_data(data=f'{person}\n', file_path=teacher_list_file_path)

        if not result['success']:
            function_res['success'] = False
            function_res['error_msg']['datasource'] = 'Data Source Error!'
            return function_res

        function_res['success'] = True
        function_res['success_msg']['success'] = 'Done!'
        return function_res
        #endregion


    if type == 'student':

        firstname = person['firstname'].strip()
        lastname = person['lastname'].strip()
        std_code = person['std_code'].strip()
        gender = person['gender']
        national_code = person['national_code'].strip()
        phone = person['phone'].strip()

        #region validation

        #region name
        if (not firstname) or (not firstname.isalpha()) or (not firstname.islower()):
            function_res['error_msg']['firstname'] = f'Firstname Error!!!'
        
        if (not lastname) or (not lastname.isalpha()) or (not lastname.islower()):
            function_res['error_msg']['lastname'] = f'Lastname Error!!!'
        #endregion

        #region std code   
        if (not std_code) or (not std_code.isdecimal()) or (len(std_code) != 11):
            function_res['error_msg']['std_code'] = f'Student Code Error!!!' 
        #endregion
  
        #region gender
        if gender == 'None':
            function_res['error_msg']['gender'] = f'Gender Error!!!'  
        #endregion

        #region national code   
        if (not national_code) or (not national_code.isdecimal()) or (len(national_code) != 10):
            function_res['error_msg']['national_code'] = f'National Code Error!!!' 
        #endregion

        #region phone
        if phone:   #doesn't matter if it's empty
            if (not phone.isdecimal()) or (len(phone) != 11):
                function_res['error_msg']['phone'] = f'Phone Error!!!'
        #endregion
            
        #endregion

        #region unique
        
        #region std code
        result = get_person(type='student')

        if not result['success']:
            function_res['success'] = False
            function_res['error_msg']['datasource'] = 'Data Source Error!'
            return function_res
        
        student_list = result['returndata']

        for ppl in student_list:
            if ppl['std_code'] == std_code:
                function_res['success'] = False
                function_res['error_msg']['std_code'] = f'The student code: {std_code} exists.'      
        #endregion

        #region national code
        result = get_person(type='student')

        if not result['success']:
            function_res['success'] = False
            function_res['error_msg']['datasource'] = 'Data Source Error!'
            return function_res
        
        student_list = result['returndata']

        for ppl in student_list:
            if ppl['national_code'] == national_code:
                function_res['success'] = False
                function_res['error_msg']['national_code'] = f'The national code: {national_code} exists.'      
        #endregion

        #region phone
        if phone:   #doesn't matter if it's empty
            result = get_person(type='student')

            if not result['success']:
                function_res['success'] = False
                function_res['error_msg']['datasource'] = 'Data Source Error!'
                return function_res
            
            student_list = result['returndata']

            for ppl in student_list:
                if ppl['phone'] == phone:
                    function_res['success'] = False
                    function_res['error_msg']['phone'] = f'The phone number: {phone} exists.'          
        #endregion

        if function_res['error_msg']:
            function_res['success'] = False
            return function_res
        
        #endregion
            
        #region save student
        result = save_data(data=f'{person}\n', file_path=student_list_file_path)

        if not result['success']:
            function_res['success'] = False
            function_res['error_msg']['datasource'] = 'Data Source Error!'
            return function_res

        function_res['success'] = True
        function_res['success_msg']['success'] = 'Done!'
        return function_res
        #endregion


def get_person(type: str):

    function_res = {'success': None, 'error_msg': {}, 'success_msg': {}, 'returndata': None}

    if type == 'teacher':
        result = load_data(file_path=teacher_list_file_path)

        if not result['success']:
            function_res['success'] = False
            function_res['error_msg']['datasource'] = 'Data Source Error!'
            return function_res
        
        function_res['success'] = True
        function_res['returndata'] = convert_liststr_listdict(result['returndata'])
        return function_res
    
    if type == 'student':
        result = load_data(file_path=student_list_file_path)

        if not result['success']:
            function_res['success'] = False
            function_res['error_msg']['datasource'] = 'Data Source Error!'
            return function_res
        
        function_res['success'] = True
        function_res['returndata'] = convert_liststr_listdict(result['returndata'])
        return function_res


def remove_student(key: str, val: Any):

    function_res = {'success': None, 'error_msg': {}, 'success_msg': {}, 'returndata': None}
    result = get_person(type='student')

    if not result['success']:
        function_res['success'] = False
        function_res['error_msg']['datasource'] = 'Data Source Error!'
        return function_res
    
    std_list = result['returndata']
    

    for ppl in std_list:
        if ppl[key] == val:
            std_list.remove(ppl)


    result = save_data_list(
        data=convert_listdict_liststr(data=std_list),
        file_path=student_list_file_path,
        mode='w'
    )
        

def edit_student(
        new_firstname, new_lastname, stdcode, new_class_,
        new_gender, national_code, new_phone, new_address
        ):
    
    function_res = {'success': None, 'error_msg': {}, 'success_msg': {}, 'returndata': None}

    new_firstname = new_firstname.strip()
    new_lastname = new_lastname.strip()
    stdcode = stdcode.strip()
    new_class_ = new_class_
    new_gender = new_gender
    national_code = national_code.strip()
    new_phone = new_phone.strip()
    new_address = new_address

    
    #region validation

    #region name
    if (not new_firstname) or (not new_firstname.isalpha()) or (not new_firstname.islower()):
        function_res['error_msg']['firstname'] = f'Firstname Error!!!'
    
    if (not new_lastname) or (not new_lastname.isalpha()) or (not new_lastname.islower()):
        function_res['error_msg']['lastname'] = f'Lastname Error!!!'
    #endregion

    #region std code   
    if (not stdcode) or (not stdcode.isdecimal()) or (len(stdcode) != 11):
        function_res['error_msg']['std_code'] = f'Student Code Error!!!' 
    #endregion

    #region gender
    if new_gender == 'None':
        function_res['error_msg']['gender'] = f'Gender Error!!!'  
    #endregion

    #region national code   
    if (not national_code) or (not national_code.isdecimal()) or (len(national_code) != 10):
        function_res['error_msg']['national_code'] = f'National Code Error!!!' 
    #endregion

    #region phone
    if new_phone:   #doesn't matter if it's empty
        if (not new_phone.isdecimal()) or (len(new_phone) != 11):
            function_res['error_msg']['phone'] = f'Phone Error!!!'
    #endregion

    #endregion

    #region unique phone
    if new_phone:   #doesn't matter if it's empty
        result = get_person(type='student')

        if not result['success']:
            function_res['success'] = False
            function_res['error_msg']['datasource'] = 'Data Source Error!'
            return function_res
        
        student_list = result['returndata']

        for ppl in student_list:
            if (ppl['phone'] == new_phone) and ppl['std_code'] != stdcode:
                function_res['success'] = False
                function_res['error_msg']['phone'] = f'The phone number: {new_phone} exists.'
                

    if function_res['error_msg']:
        function_res['success'] = False
        return function_res
    #endregion

    #region editting
    result = get_person(type='student')

    if not result['success']:
        function_res['success'] = False
        function_res['error_msg']['datasource'] = 'Data source error!'
        return function_res

    std_list = result['returndata']

    for ppl in std_list:
        if ppl['std_code'] == stdcode:
            
            ppl['firstname'] = new_firstname
            ppl['lastname'] = new_lastname
            ppl['class_'] = new_class_
            ppl['gender'] = new_gender
            ppl['national_code'] = national_code
            ppl['phone'] = new_phone
            ppl['address'] = new_address

            break
    #endregion
        

    result = save_data_list(
        data=convert_listdict_liststr(data=std_list),
        file_path=student_list_file_path,
        mode='w'
    )

    if not result['success']:
            function_res['success'] = False
            function_res['error_msg']['datasource'] = 'Data Source Error!'
            return function_res

    function_res['success'] = True
    function_res['success_msg']['success'] = 'Done!'
    return function_res


def check_login(username: str, password: str):

    function_res = {'success': None, 'error_msg': {}, 'success_msg': {}, 'returndata': None}

    username = username.strip()
    password = password.strip()   

    if (not username) or (not password):
        function_res['error_msg']['login'] = f'Please fill both gaps!!!'

    if function_res['error_msg']:
        function_res['success'] = False
        return function_res


    result = get_person(type='teacher')
    teacher_list = result['returndata']

    if teacher_list:
        for ppl in teacher_list:
            if (ppl['username'] == username) and (ppl['password'] == password):
                function_res['success'] = True
                function_res['success_msg']['login'] = f'Welcome'
                return function_res
            
                  
    if not function_res['success']:
        function_res['success'] = False
        function_res['error_msg']['login'] = f'Username and password does not match!!!'
        return function_res



