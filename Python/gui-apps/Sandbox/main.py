import multiprocessing.process
from ursina import *
# from direct.stdpy import thread
import multiprocessing , threading
from player import Player
from enemy import Enemy, BigEnemy

from mainmenu import MainMenu
# import time

from maps import FloatingIslands, DesertedSands, MountainousValley

from scene_lighting import SceneLighting

from ursina import texture
texture.default_filtering = 'nearest' 

# window.render_mode = 'flat'
# camera.clip_plane_far = 50  # Reduce far clipping distance (default is often 1000+)
# window.vsync = False
mouse.locked = False
Text.default_font = "./assets/Roboto.ttf"
Text.default_resolution = Text.size * 1080

app = Ursina(headless=True)
window.fullscreen = True
window.size = (854,480)
# window.aspect_ratio = 16/9  # Set a custom aspect ratio if needed

window.borderless = False
# window.windowed_size = window.size * 0.75
window.cog_button.disable()
# window.cog_button.enable()

# window.size = window.screen_resolution

# window.collider_counter.disable()
# window.entity_counter.disable()
window.fps_counter.scale = (2,2,2)
window.fps_counter.enable()
# window.exit_button.disable()

scene.fog_density = 0.001
# window.size = window.screen_resolution

# def toggle_fullscreen():
#     window.fullscreen = not window.fullscreen


# def toggle_maxmize():
#     if window.size == (1280, 720):
#         window.size = window.screen_resolution
#     else :
#         window.size = (1280, 720)

# Bind the 'f' key to toggle fullscreen
# key_handler = Entity(ignore_paused=True)
# key_handler.input = lambda key: toggle_fullscreen() if key == 'f' else toggle_maxmize() if key == 'm' else None

# Starting new thread for assets
def load_assets():
    models_to_load = [
        "floatingislands", "desertedsands", "mountainous_valley", "jumppad", "particle", "particles", "enemy", "bigenemy" "pistol", 
        "shotgun", "rifle", "pistol", "minigun", "minigun-barrel", "rocket-launcher", "rocket", "bullet",
    ]

    textures_to_load = [
        "level", "particle", "destroyed", "jetpack", "sky", "rope", "hit"
    ]

    for i, m in enumerate(models_to_load):
        # threading.Thread(target=lambda : load_model(m)).start()
        # multiprocessing.Process(target=lambda : load_model(m)).start()


        threading.Thread(
            target=load_model(m), args=[]).start()
        # load_model(m)

    for i, t in enumerate(textures_to_load):
        # threading.Thread(target=lambda:load_texture(t)).start()
        # multiprocessing.Process(target=lambda:load_texture(t)).start()

        threading.Thread(
            target=load_texture(t), args=[]).start()
        # load_texture(t)

try:
    # thread.start_new_thread(function = load_assets, args = "")
    tt = multiprocessing.Process(target=lambda: threading.Thread(
        target=load_assets, args=[]), args=[])
    # tt = threading.Thread(target=load_assets,args=[])
    # tt = multiprocessing.Process(target=load_assets,args=[])
    tt.start()
    tt.join()
except Exception as e:
    print("error starting thread", e)

player = Player((-60, 50, -16)) # Flat: (-47, 50, -94) # Rope: (-61, 100, 0)
player.disable()

floating_islands = FloatingIslands(player, enabled = True)
deserted_sands = DesertedSands(player, enabled = False)
mountainous_valley = MountainousValley(player, enabled = False)

player.map = floating_islands
player.maps = [floating_islands, deserted_sands, mountainous_valley]

# Enemy
for enemy in range(15):
    i = random.randint(0, 2)
    if i == 0:
        e = BigEnemy(player, position = Vec3(random.randint(-50, 50)))
    else:
        e = Enemy(player, position = Vec3(random.randint(-50, 50)))

    threading.Thread(target=e.disable).start()
    
    threading.Thread(
        target=lambda:player.enemies.append(e)).start()
    # e.disable()
    # player.enemies.append(e)

mainmenu = MainMenu(player, floating_islands, deserted_sands, mountainous_valley)

# Lighting + Shadows
scene_lighting = SceneLighting(ursina = app, player = player, sun_direction = (-0.7, -0.9, 0.5), shadow_resolution = 4096, sky_texture = "sky")

def input(key):
    if key == "g":
        player.reset()
light = DirectionalLight(shadow_map_resolution=(512, 512))
# def update():
#     print(player.position)
if __name__ == "__main__":
    app.run()
