import game_scene

class PlayScene(game_scene.GameScene):
    def __init__(self,width,height):
        super.__init__(self,width,height)

    def draw(self, screen):
        return