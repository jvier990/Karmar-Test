def replace_category_id(mealjson, mapper):
    # Verificar si 'strCategory' existe en 'mealjson'
    if "data" in mealjson and "strCategory" in mealjson["data"]:
        # Obtener el valor actual de 'strCategory'
        category = mealjson["data"]["strCategory"]
        
        # Reemplazar el valor si existe en el mapper
        if category in mapper:
            mealjson["data"]["strCategory"] = mapper[category]
    
    return mealjson