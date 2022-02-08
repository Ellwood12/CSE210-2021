# from Chicken_Crossing.game import handle_food_collisions
from game import constants
import random
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.chicken import Chicken
from game.seed import Seed
from game.eagle import Eagle
from game.cars import Cars
from game.trucks import Trucks
from game.score import Score
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService
from game.move_actors_action import MoveActorsAction
from game.handle_off_screen_action import HandleOffScreenAction
from game.control_actors_action import ControlActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.handle_food_collisions import Handle_Food_Collision
import os
import raylibpy

#https://opengameart.org/content/top-view-car-truck-sprites


def main():

    cast = {}

    cast["seeds"] = []
    seed = Seed()
    seed_info = []
    seed.set_image(constants.IMAGE_SEED)
    seed.set_height(10)
    seed.set_width(10)
    seed_position = Point(750,300)
    seed.set_position(seed_position)
    seed_info.append(seed)
    cast["seeds"] = seed_info

    cast["cars"] = []
    all_cars = []
    x = 175
    y = [0, 150, 300, 450]
    for i in range(len(y)):
        car = Cars()
        car.set_image(constants.IMAGE_CAR_RED)
        car.set_height(40)
        car.set_width(20)
        car_position = Point(x, y[i])
        car.set_position(car_position)
        car_velocity = Point(0, 2.5)
        car.set_velocity(car_velocity)
        all_cars.append(car)
    x = 470
    y = [100, 250, 400, 550]
    for i in range(len(y)):
        car = Cars()
        car.set_image(constants.IMAGE_CAR_RED_UP)
        car.set_height(40)
        car.set_width(20)
        car_position = Point(x, y[i])
        car.set_position(car_position)
        car_velocity = Point(0, -2.5)
        car.set_velocity(car_velocity)
        all_cars.append(car)

    cast["cars"] = all_cars

    cast["trucks"] = []
    all_trucks = []
    x = 255
    y = [50, 250, 450]
    for i in range(len(y)):
        truck = Trucks()
        truck.set_image(constants.IMAGE_TRUCK)
        truck.set_height(20)
        truck.set_width(20)
        truck_position = Point(x, y[i])
        truck.set_position(truck_position)
        truck_velocity = Point(0, 3)
        truck.set_velocity(truck_velocity)
        all_trucks.append(truck)

    x = 560
    y = [50, 250, 450]
    for i in range(len(y)):
        truck = Trucks()
        truck.set_image(constants.IMAGE_TRUCK_UP)
        truck.set_height(50)
        truck.set_width(20)
        truck_position = Point(x, y[i])
        truck.set_position(truck_position)
        truck_velocity = Point(0, -3)
        truck.set_velocity(truck_velocity)
        all_trucks.append(truck)

    cast["trucks"] = all_trucks

    cast["semi_trucks"] = []
    all_big_trucks = []
    x = 360
    y = [30, 230, 430, 630]
    for i in range(len(y)):
        big_truck = Trucks()
        big_truck.set_image(constants.IMAGE_SEMI)
        big_truck.set_height(110)
        big_truck.set_width(20)
        big_truck_position = Point(x, y[i])
        big_truck.set_position(big_truck_position)
        big_truck_velocity = Point(0, 1.5)
        big_truck.set_velocity(big_truck_velocity)
        all_big_trucks.append(big_truck)

    x = 645
    y = [0, 200, 400]
    for i in range(len(y)):
        big_truck = Trucks()
        big_truck.set_image(constants.IMAGE_SEMI_UP)
        big_truck.set_height(100)
        big_truck.set_width(20)
        big_truck_position = Point(x, y[i])
        big_truck.set_position(big_truck_position)
        big_truck_velocity = Point(0, -2.5)
        big_truck.set_velocity(big_truck_velocity)
        all_big_trucks.append(big_truck)

    cast["semi_trucks"] = all_big_trucks

    x = 800
    y1 = (random.randint(1,550))
    y2 = (random.randint(1,550))
    y = [y1,y2]
    eagle_info = []
    cast["eagle"] = []
    for i in range(len(y)):
        eagle = Eagle()
        eagle.set_image(constants.IMAGE_EAGLE)
        eagle.set_height(20)
        eagle.set_width(20)
        eagle_position = Point(x, y[i])
        eagle.set_position(eagle_position)
        eagle_velocity = Point(-2,0)
        eagle.set_velocity(eagle_velocity)
        eagle_info.append(eagle)
    cast["eagle"] = eagle_info
  
    cast["chicken"] = []
    chicken = Chicken()
    chick_info = []
    chicken.set_image(constants.IMAGE_CHICKEN)
    chicken.set_height(20)
    chicken.set_width(20)
    chicken_position = Point(80,300)
    chicken.set_position(chicken_position)
    chicken_velocity = Point(constants.CHICK_DX,constants.CHICK_DY)
    chicken.set_velocity(chicken_velocity)
    chick_info.append(chicken)
    cast["chicken"] = chick_info

    cast["score"] = []
    score = Score()
    score_info = []
    position = Point(1, 0)
    points = 0
    score.set_height(20)
    score.set_width(20)
    position = Point(1, 0)
    score.set_position(position)
    score.set_text(f"Score: {points}")
    score_info.append(score)
    cast["score"] = score_info

    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    move_actors_action = MoveActorsAction()
    handle_off_screen_action = HandleOffScreenAction()
    handle_food_collisions = Handle_Food_Collision()
    control_actors_action = ControlActorsAction(input_service)
    handle_collisions_action = HandleCollisionsAction()
    physics_service = PhysicsService()
    audio_service = AudioService()
    draw_actors_action = DrawActorsAction(output_service)

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_off_screen_action, handle_food_collisions, handle_collisions_action]
    script["output"] = [draw_actors_action]

    # Start the game
    output_service.open_window("Chicken Crossing")
    audio_service.start_audio()
    audio_service.play_sound(constants.TRAFFIC_START)
    
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()

if __name__ == "__main__":
    main()

