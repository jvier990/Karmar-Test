from Models.modelMeal import Meal
import json

def create_meal_objects(meal_data_str):
    meal_list = []
    
    try:
        meal_data = json.loads(meal_data_str)
        
        for item in meal_data:
            if isinstance(item, dict) and 'meals' in item:
                meals = item['meals']
                if isinstance(meals, list):
                    for meal_info in meals:
                        if isinstance(meal_info, dict):
                            #print(f"Processing meal_info: {meal_info}")
                            meal = Meal(
                                idMeal=meal_info.get('idMeal'),
                                strMeal=meal_info.get('strMeal'),
                                strDrinkAlternate=meal_info.get('strDrinkAlternate'),
                                strCategory=meal_info.get('strCategory'),
                                strArea=meal_info.get('strArea'),
                                strInstructions=meal_info.get('strInstructions'),
                                strMealThumb=meal_info.get('strMealThumb'),
                                strTags=meal_info.get('strTags'),
                                strYoutube=meal_info.get('strYoutube'),
                                strIngredient1=meal_info.get('strIngredient1'),
                                strIngredient2=meal_info.get('strIngredient2'),
                                strIngredient3=meal_info.get('strIngredient3'),
                                strIngredient4=meal_info.get('strIngredient4'),
                                strIngredient5=meal_info.get('strIngredient5'),
                                strIngredient6=meal_info.get('strIngredient6'),
                                strIngredient7=meal_info.get('strIngredient7'),
                                strIngredient8=meal_info.get('strIngredient8'),
                                strIngredient9=meal_info.get('strIngredient9'),
                                strIngredient10=meal_info.get('strIngredient10'),
                                strIngredient11=meal_info.get('strIngredient11'),
                                strIngredient12=meal_info.get('strIngredient12'),
                                strIngredient13=meal_info.get('strIngredient13'),
                                strIngredient14=meal_info.get('strIngredient14'),
                                strIngredient15=meal_info.get('strIngredient15'),
                                strIngredient16=meal_info.get('strIngredient16'),
                                strIngredient17=meal_info.get('strIngredient17'),
                                strIngredient18=meal_info.get('strIngredient18'),
                                strIngredient19=meal_info.get('strIngredient19'),
                                strIngredient20=meal_info.get('strIngredient20'),
                                strMeasure1=meal_info.get('strMeasure1'),
                                strMeasure2=meal_info.get('strMeasure2'),
                                strMeasure3=meal_info.get('strMeasure3'),
                                strMeasure4=meal_info.get('strMeasure4'),
                                strMeasure5=meal_info.get('strMeasure5'),
                                strMeasure6=meal_info.get('strMeasure6'),
                                strMeasure7=meal_info.get('strMeasure7'),
                                strMeasure8=meal_info.get('strMeasure8'),
                                strMeasure9=meal_info.get('strMeasure9'),
                                strMeasure10=meal_info.get('strMeasure10'),
                                strMeasure11=meal_info.get('strMeasure11'),
                                strMeasure12=meal_info.get('strMeasure12'),
                                strMeasure13=meal_info.get('strMeasure13'),
                                strMeasure14=meal_info.get('strMeasure14'),
                                strMeasure15=meal_info.get('strMeasure15'),
                                strMeasure16=meal_info.get('strMeasure16'),
                                strMeasure17=meal_info.get('strMeasure17'),
                                strMeasure18=meal_info.get('strMeasure18'),
                                strMeasure19=meal_info.get('strMeasure19'),
                                strMeasure20=meal_info.get('strMeasure20'),
                                strSource=meal_info.get('strSource'),
                                strImageSource=meal_info.get('strImageSource'),
                                strCreativeCommonsConfirmed=meal_info.get('strCreativeCommonsConfirmed'),
                                dateModified=meal_info.get('dateModified')
                            )
                            meal_list.append(meal)
        return meal_list
    
    except json.JSONDecodeError as e:
        print(f"Error al decodificar JSON: {e}")
        return []