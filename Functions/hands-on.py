import util

def ikpe(insert):
    print("i am not among", insert)
    ikpe_number = util.get_db_credentials_param("ikpe")
    print("my number is,", ikpe_number)

ikpe("ag")
ikpe(1)

