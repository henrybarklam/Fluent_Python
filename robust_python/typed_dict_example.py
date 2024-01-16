from typing import TypedDict

'''TypedDict is for the type checker only, will be converted to a dictionary regardless
If the API called at the end ever changes, its easier for a developer to change the types etc
'''
class Range(TypedDict):
    min: float
    max: float

class NutritionInformation(TypedDict):
    value: int
    unit: str
    confidenceRange95Percent: Range
    standardDeviation: float

class RecipeNutritionInformation(TypedDict):
    recipes_used: int
    calories: NutritionInformation
    fat: NutritionInformation
    protein: NutritionInformation
    carbs: NutritionInformation

nutrition_infomation: RecipeNutritionInformation = someApiCall(recipe_name)

def someApiCall(some_recipe):
    # This would have to return a variable of type RecipeNutritionInformation
    return