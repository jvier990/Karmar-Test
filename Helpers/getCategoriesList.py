from Models.modelCategories import Category
from typing import List


def mapperCategoriestoZoho(json_data: dict) -> List[Category]:
    categories = [Category(**category) for category in json_data['categories']]
    return categories

def create_category_json(category: Category) -> dict:
    return {
        "data": {
            "strCategory": category.strCategory,
            "strCategoryDescription": category.strCategoryDescription,
            "idCategory": category.idCategory,
            "strCategoryThumb": category.strCategoryThumb
        }
    }