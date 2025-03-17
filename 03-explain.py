import random
from typing import List, Callable, Optional, Dict, Any

class KitchenObjectSO:
    def __init__(self, name: str):
        self.name = name

class RecipeSO:
    def __init__(self, kitchen_object_so_list: List[KitchenObjectSO]):
        self.kitchen_object_so_list = kitchen_object_so_list

class RecipeListSO:
    def __init__(self, recipe_so_list: List[RecipeSO]):
        self.recipe_so_list = recipe_so_list

class PlateKitchenObject:
    def __init__(self):
        self._kitchen_object_so_list = []
    
    def get_kitchen_object_so_list(self) -> List[KitchenObjectSO]:
        return self._kitchen_object_so_list

class KitchenGameManager:
    _instance = None
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = KitchenGameManager()
        return cls._instance
    
    def is_game_playing(self) -> bool:
        return True

class DeliveryManager:
    _instance = None
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = DeliveryManager()
        return cls._instance
    
    def __init__(self):
        self.on_recipe_spawned_callbacks = []
        self.on_recipe_completed_callbacks = []
        self.on_recipe_success_callbacks = []
        self.on_recipe_failed_callbacks = []
        
        self.recipe_list_so = None
        self.waiting_recipe_so_list = []
        self.spawn_recipe_timer = 0.0
        self.spawn_recipe_timer_max = 4.0
        self.waiting_recipes_max = 4
        self.successful_recipes_amount = 0
    
    def add_on_recipe_spawned_callback(self, callback: Callable[[], None]):
        self.on_recipe_spawned_callbacks.append(callback)
    
    def add_on_recipe_completed_callback(self, callback: Callable[[], None]):
        self.on_recipe_completed_callbacks.append(callback)
    
    def add_on_recipe_success_callback(self, callback: Callable[[], None]):
        self.on_recipe_success_callbacks.append(callback)
    
    def add_on_recipe_failed_callback(self, callback: Callable[[], None]):
        self.on_recipe_failed_callbacks.append(callback)
    
    def set_recipe_list_so(self, recipe_list_so: RecipeListSO):
        self.recipe_list_so = recipe_list_so
    
    def update(self, delta_time: float):
        self.spawn_recipe_timer -= delta_time
        if self.spawn_recipe_timer <= 0.0:
            self.spawn_recipe_timer = self.spawn_recipe_timer_max
            
            if KitchenGameManager.get_instance().is_game_playing() and len(self.waiting_recipe_so_list) < self.waiting_recipes_max:
                waiting_recipe_so = self.recipe_list_so.recipe_so_list[random.randint(0, len(self.recipe_list_so.recipe_so_list) - 1)]
                
                self.waiting_recipe_so_list.append(waiting_recipe_so)
                
                for callback in self.on_recipe_spawned_callbacks:
                    callback()
    
    # レシピの材料と皿の材料が一致しているかどうかを確認する
    def deliver_recipe(self, plate_kitchen_object: PlateKitchenObject):
        for i in range(len(self.waiting_recipe_so_list)):
            waiting_recipe_so = self.waiting_recipe_so_list[i]
            
            if len(waiting_recipe_so.kitchen_object_so_list) == len(plate_kitchen_object.get_kitchen_object_so_list()):
                plate_contents_matches_recipe = True
                for recipe_kitchen_object_so in waiting_recipe_so.kitchen_object_so_list:
                    ingredient_found = False
                    for plate_kitchen_object_so in plate_kitchen_object.get_kitchen_object_so_list():
                        if plate_kitchen_object_so == recipe_kitchen_object_so:
                            ingredient_found = True
                            break
                    if not ingredient_found:
                        plate_contents_matches_recipe = False
                
                if plate_contents_matches_recipe:
                    self.successful_recipes_amount += 1
                    
                    self.waiting_recipe_so_list.pop(i)
                    
                    for callback in self.on_recipe_completed_callbacks:
                        callback()
                    for callback in self.on_recipe_success_callbacks:
                        callback()
                    return
        
        for callback in self.on_recipe_failed_callbacks:
            callback()
    
    def get_waiting_recipe_so_list(self) -> List[RecipeSO]:
        return self.waiting_recipe_so_list
    
    def get_successful_recipes_amount(self) -> int:
        return self.successful_recipes_amount