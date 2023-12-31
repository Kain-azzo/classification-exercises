import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

def prep_iris(flower):
    flower = flower.rename(columns={"species_name":"species"})
    flower = flower.drop(columns=['species_id','measurement_id'])
    return flower

def clean_titanic(boat):

    boat = boat.drop(columns=['embarked', 'age','deck', 'class'])
    boat.pclass = boat.pclass.astype(object)
    boat.embark_town = boat.embark_town.fillna('Southampton')
    
    return boat



def prep_telco(isp):
    isp = isp.drop(columns = ['payment_type_id','internet_service_type_id','contract_type_id'])
    isp.total_charges = isp.total_charges.str.replace(' ', '0.0')
    return isp

def chop_data(frame, col):

    train, validate_test = train_test_split(frame,
                     train_size=0.6,
                     random_state=123,
                     stratify=frame[col]
                    )

    validate, test = train_test_split(validate_test,
                                     train_size=0.5,
                                      random_state=123,
                                      stratify=validate_test[col]
                        
                                     )
    return train, validate, test

def preprocess_titanic(train, test, validate):
    appendo = []
  
    for stuff in [train, test, validate]:
        stuff['gender'] = stuff['sex'].map({'male': 0, 'female': 1})
        stuff.drop(columns='sex', inplace=True)
        stuff.drop(columns='passenger_id', inplace=True)
        stuff["pclass"] = stuff["pclass"].astype(int)
        stuff['embark_town'].fillna('missing', inplace=True)
        new_embark_town = pd.get_dummies(stuff['embark_town'], drop_first=True).astype(int)
        appendo.append(pd.concat([stuff,new_embark_town],axis=1).drop(columns='embark_town'))
        

    return appendo