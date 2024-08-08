import os
from APIZohoCreator import ApiZoho
from APImeals import ApiMeal
from Credentials.getZohoToken import get_access_token
from Helpers.mapperCategoryMeal import mealsMapper
from Helpers.getMealsList import create_meal_objects
from Helpers.mapperZohoCategories import replace_category_id
from Helpers.getCategoriesList import mapperCategoriestoZoho, create_category_json
import json
from dotenv import load_dotenv
load_dotenv()

#CARGAR VARIABLES DE ENTORNO
refresh_token = os.getenv('REFRESH_TOKEN')
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
username = os.getenv('USERNAME_ZOHO')
app = os.getenv('APP')
base_url = os.getenv('BASE_URL')
environment = os.getenv('ENVIRONMENT')
meal_url = os.getenv('MEAL_BASE_URL')
by_categories = os.getenv('BY_CATEGORY')
by_id  = os.getenv('BY_ID')
by_name = os.getenv('BY_NAME')
categories = os.getenv('CATEGORIES')


#GENERAR TOKEN PARA ACCEDER A ZOHO
auth_token = get_access_token(refresh_token, client_id, client_secret)
print(auth_token)

#OBTENER INFOMRACIOND DE MEALS ATRAVES DE LA API
def getMealData(by,value,meal_url):
    meals = ApiMeal(meal_url)
    meals_data = meals.get_meals(by,value)
    if meals_data:
        #print("Datos obtenidos:", meals_data)
        return meals_data
    else:
        print("No se pudo obtener datos.")

def getMealCategories():
    meals = ApiMeal(meal_url)
    meals_data = meals.get_categories()
    if meals_data:
        #print("Datos obtenidos:", meals_data)
        return meals_data
    else:
        print("No se pudo obtener datos.")


#OBTENER LA DATA GENERAL DE LOS CATEGORIES GENERADOS (Para obtener el ID)
def getGeneralZohoMealsData(base_url):
    base_url = f"{base_url}/{username}/{app}/report"
    mealsInZoho = ApiZoho(base_url, auth_token, environment)
    dataZoho = mealsInZoho.get_general_data()
    if dataZoho:
        #print("Datos obtenidos:", dataZoho)
        return dataZoho
    else:
        print("No se pudo obtener datos.")

#OBTENER LA DATA GENERAL DE LOS MEALS GENERADOS (Para obtener el ID)
def getGeneralZohoMealsCategories(base_url):
    base_url = f"{base_url}/{username}/{app}/report"
    mealsInZoho = ApiZoho(base_url, auth_token, environment)
    dataZoho = mealsInZoho.get_general_categories_data()
    if dataZoho:
        #print("Datos obtenidos:", dataZoho)
        return dataZoho
    else:
        print("No se pudo obtener datos.")

#AGREGAR REGISTROS DE MEALs
def addMeal(base_url,meal):
    base_url = f"{base_url}/{username}/{app}/form"
    mealsInZoho = ApiZoho(base_url, auth_token, environment)
    dataZoho = mealsInZoho.add_meals(meal)
    if dataZoho:
        #print("Datos obtenidos:", dataZoho)
        return dataZoho
    else:
        print("No se pudo obtener datos.")
#AGREGAR REGISTROS DE CATEGORIESs
def addCategories(base_url,meal):
    base_url = f"{base_url}/{username}/{app}/form"
    mealsInZoho = ApiZoho(base_url, auth_token, environment)
    dataZoho = mealsInZoho.add_categories(meal)
    if dataZoho:
        #print("Datos obtenidos:", dataZoho)
        return dataZoho
    else:
        print("No se pudo obtener datos.")

#Obtener la lista de IDs de meals por categoria, y obtener la info de esos Meals por su id
def fetchMealsDetails(id_list,by,meal_url):
    # Obtener los detalles de cada comida
    meals_details = []
    for meal_id in id_list:
        meal_details = getMealData(by, meal_id, meal_url)
        meals_details.append(meal_details)
    
    # Convertir la lista de detalles de comidas a formato JSON
    json_output = json.dumps(meals_details, indent=4)
    return json_output

#getMealData(by_id,'52771',meal_url)

def getCategoriesList(base_url):
    
    data = getGeneralZohoMealsCategories(base_url)
    
   
    if not data or "data" not in data:
        print("No se obtuvieron datos o el formato de datos es incorrecto.")
        return None
    
    
    categories_dict = {}
    for item in data["data"]:
       
        category_name = item.get("strCategory")
        category_id = item.get("ID")
        
        if category_name and category_id:  
            categories_dict[category_name] = category_id

    return categories_dict

def actCatagoriesinZho(base_url):
    categoriesList = getMealCategories()

    catagorieList = mapperCategoriestoZoho(categoriesList)
    print(len(catagorieList))  

    
    category_jsons = [create_category_json(category) for category in catagorieList]

    
    for category_json in category_jsons:
        category_json_str = json.dumps(category_json, indent=4)
        addCategories(base_url, category_json_str)




idList = mealsMapper(getMealData(by_categories,'Breakfast',meal_url))

zohoIDsList = getGeneralZohoMealsData(base_url)
zohoIDsList = zohoIDsList['data']
zohoIDsList = [meal['idMeal'] for meal in zohoIDsList]

idList = [id for id in idList if id not in zohoIDsList]


dataList = fetchMealsDetails(idList,by_id,meal_url)

meals = create_meal_objects(dataList)


# Procesar los primeros 10 meals
for i, meal in enumerate(meals[:10]):  # Solo los primeros 10 elementos
    mealjson = {"data": meal.dict()}
    updated_mealjson = replace_category_id(mealjson, getCategoriesList(base_url))
    mealjson_str = json.dumps(updated_mealjson, indent=4)
    addMeal(base_url, updated_mealjson)
    print(f"Inserted meal {i + 1}:\n{mealjson_str}")


"""
#Obtener un meal de prueba
meal1 = meals[0]
#Formatear a dict
mealjson = {"data": meal1.dict()}
#reemplazar el valor de la categoria
replace_category_id(mealjson,getCategoriesList(base_url))
#mealjson["data"]["strCategory"] = "4676181000000021003"
#formatear a un formato json
mealjson_str = json.dumps(mealjson, indent=4) 

#insertar en formulario zoho
addMeal(base_url,mealjson)

"""








