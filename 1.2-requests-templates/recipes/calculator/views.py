from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


# Напишите ваш обработчик. Используйте DATA как источник данных

def recipe_views(request, recipe):
    meal = recipe
    num = int(request.GET.get('servings', 1))
    if num > 0:
        context = {
                'recipe':
                    {
                    }
            }
        for key, value in DATA.items():
            if key == meal:
                for keys, number in value.items():
                    for recipe, amount in context.items():
                        amount[keys] = number * num
        return render(request, 'calculator/index.html', context)

    # return HttpResponse(f'{meal}')

# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
