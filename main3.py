import sys, logging, random, open_color, arcade

#check to make sure we are running the right version of Python
version = (3,7)
assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0],version[1])

#turn on logging, in case we have to leave ourselves debugging messages
logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MARGIN = 20
INITIAL_VELOCITY = 3
NUM_ANIMALS = 5
SCREEN_TITLE = "Collision Exercise"
MASS = 1.05
FRICTION = 0.9

   

class Window(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_mouse_visible(True)
        arcade.set_background_color(open_color.blue_4)
        self.animal_list = arcade.SpriteList()

    def setup(self):
        animals = ['bear','buffalo','chick','chicken','cow','crocodile','dog','duck','elephant','frog','giraffe','goat','gorilla','hippo','horse','monkey','moose','narwhal','owl','panda','parrot','penguin','pig','rabbit','rhino','sloth','snake','walrus','whale','zebra']

        for i in range(NUM_ANIMALS):
            animal = random.choice(animals)
            x = random.randint(MARGIN,SCREEN_WIDTH-MARGIN)
            y = random.randint(MARGIN,SCREEN_HEIGHT-MARGIN)
            dx = random.uniform(-INITIAL_VELOCITY, INITIAL_VELOCITY)
            dy = random.uniform(-INITIAL_VELOCITY, INITIAL_VELOCITY)
            self.animal_sprite = arcade.Sprite("assets/{animal}.png".format(animal=animal), 0.5)
            self.animal_sprite.center_x = x
            self.animal_sprite.center_y = y
            self.animal_sprite.dx = dx
            self.animal_sprite.dy = dy
            self.animal_list.append(self.animal_sprite)            

    def update(self, delta_time):
        for a in self.animal_list:
            a.center_x += a.dx
            a.center_y += a.dy



            collisions = a.collides_with_list(self.animal_list)
            for c in collisions:
                if a.center_x > c.center_x:
                    a.dx = abs(a.dx) * -1 * MASS
                if a.center_x < c.center_x:
                    a.dx = abs(a.dx) * MASS
                if a.center_y > c.center_y:
                    a.dy = abs(a.dy) * MASS
                if a.center_y < c.center_y:
                    a.dy = abs(a.dy) * -1 * MASS



            if a.center_x <= MARGIN:
                a.center_x = MARGIN
                a.dx = abs(a.dx)
                a.dx *= FRICTION
                a.dy *= FRICTION 
            if a.center_x >= SCREEN_WIDTH - MARGIN:
                a.center_x = SCREEN_WIDTH - MARGIN
                a.dx = abs(a.dx)*-1
                a.dx *= FRICTION
                a.dy *= FRICTION 
            if a.center_x <= MARGIN:
                a.center_x = MARGIN
                a.dx = abs(a.dx)
                a.dx *= FRICTION
                a.dy *= FRICTION 
            if a.center_y <= MARGIN:
                a.center_y = MARGIN
                a.dy = abs(a.dy)
                a.dx *= FRICTION
                a.dy *= FRICTION 
            if a.center_y >= SCREEN_HEIGHT - MARGIN:
                a.center_y = SCREEN_HEIGHT - MARGIN
                a.dy = abs(a.dy)*-1
                a.dx *= FRICTION
                a.dy *= FRICTION 


    def on_draw(self):
        arcade.start_render()
        self.animal_list.draw()





def main():
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()