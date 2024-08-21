import multiprocessing , threading
from ursina import *
import json 
from ursina.prefabs.health_bar import HealthBar
from panda3d.core import WindowProperties, FrameBufferProperties, GraphicsPipe, Texture, GraphicsOutput, SamplerState, OrthographicLens, Shader, Camera, NodePath, PandaNode, PNMImage
from math import sqrt
import random
# from random import random

def toggle_fullscreen():
    window.fullscreen = not window.fullscreen


def toggle_maxmize():
    if window.size == (1280, 720):
        window.size = window.screen_resolution
    else:
        window.size = (1280, 720)


def sign(x): return -1 if x < 0 else (1 if x > 0 else 0)
def y_dir(y): return -1 if y < 0 else (1 if y > 0 else -1)


colourH = color.rgba(18, 152, 255, 180)
colourN = color.rgba(0, 0, 0, 0.7)
def highlighted(button): return button.color == colourH

class Ability(Entity):
    def __init__(self, player, ability_enabled=True):
        super().__init__(
            parent=player
        )

        self.player = player
        self.ability_enabled = ability_enabled
        self.shift_count = 0


class Rope(Ability):
    def __init__(self, player, enabled=True):
        super().__init__(
            player, enabled
        )

        self.rope_pivot = Entity()
        self.rope = Entity(model=Mesh(vertices=[self.world_position, self.rope_pivot.world_position], mode="line", thickness=15, colors=[
                           color.hex("#ff8c00")]), texture="rope.png", enabled=False)
        self.rope_position = self.position
        self.can_rope = False
        self.rope_length = 1000000
        self.max_rope_length = False
        self.below_rope = False

        # Audio
        self.rope_sound = Audio("rope.wav", False)

    def update(self):
        if self.ability_enabled:
            if self.can_rope and self.player.ability_bar.value > 0:
                if held_keys["right mouse"] and held_keys['shift']:
                    if distance(self.player.position, self.rope_pivot.position) > 10:
                        if distance(self.player.position, self.rope_pivot.position) < self.rope_length and not self.player.grounded:
                            self.player.position += (
                                (self.rope_pivot.position - self.player.position).normalized() * 20) * time.dt
                            self.player.velocity_z += 2 * time.dt
                        self.rope_position = lerp(
                            self.rope_position, self.rope_pivot.world_position, time.dt * 20)
                        self.rope.model.vertices.pop(0)
                        self.rope.model.vertices = [self.player.position - (0, 5, 0) + (
                            self.player.forward * 4) + (self.player.left * 2), self.rope_position]
                        self.rope.model.generate()
                        self.rope.enable()
                        if self.player.y < self.rope_pivot.y:
                            self.player.velocity_y += 40 * time.dt
                        else:
                            self.player.velocity_y -= 60 * time.dt

                        if (self.rope_pivot.y - self.player.y) > self.rope_length:
                            self.below_rope = True
                            invoke(setattr, self, "below_rope", False, delay=5)

                        if self.below_rope:
                            self.player.velocity_y += 50 * time.dt
                    else:
                        self.rope.disable()
                    if distance(self.player.position, self.rope_pivot.position) > self.rope_length:
                        self.max_rope_length = True
                        invoke(setattr, self, "max_rope_length", False, delay=2)
                    if self.max_rope_length:
                        self.player.position += (
                            (self.rope_pivot.position - self.player.position).normalized() * 25 * time.dt)
                        self.player.velocity_z -= 5 * time.dt
                        self.player.velocity_y -= 80 * time.dt

                    self.player.using_ability = True
                    self.player.ability_bar.value -= 2 * time.dt

    def input(self, key):
            if key == "right mouse down" and self.player.ability_bar.value > 0 and held_keys['shift']:
                rope_ray = raycast(camera.world_position, camera.forward, distance=100,
                                   traverse_target=self.player.map, ignore=[self, camera, ])
                if rope_ray.hit:
                    self.can_rope = True
                    rope_point = rope_ray.world_point
                    self.rope_entity = rope_ray.entity
                    self.rope_pivot.position = rope_point
                    self.rope_position = self.position
                    self.rope_sound.pitch = random.uniform(0.7, 1)
                    self.rope_sound.play()
            elif key == "right mouse up":
                self.rope_pivot.position = self.position
                if self.can_rope and self.player.ability_bar.value > 0:
                    self.rope.disable()
                    self.player.velocity_y += 10
                self.can_rope = False
                invoke(setattr, self.player, "using_ability", False, delay=2)


class DashAbility(Ability):
    def __init__(self, player, enabled=True):
        super().__init__(
            player, enabled
        )

        self.dashing = False

        # Audio
        self.dash_sound = Audio("dash.wav", False)
        self.dash_sound.volume = 0.8

    def update(self):
        if self.ability_enabled:
            if self.dashing and not held_keys["right mouse"]:
                if held_keys["a"]:
                    self.player.animate_position(self.player.position + (camera.left * 40), duration=0.2, curve = curve.in_out_quad)
                elif held_keys["d"]:
                    self.player.animate_position(self.player.position + (camera.right * 40), duration=0.2, curve = curve.in_out_quad)
                else:
                    self.player.animate_position(self.player.position + (camera.forward * 40), duration=0.2, curve = curve.in_out_quad)

                camera.animate("fov", 110, duration=0.2, curve = curve.in_quad)
                camera.animate("fov", 100, curve=curve.out_quad, delay = 0.2)

                self.dashing = False
                self.player.velocity_y = 0

                self.player.shake_camera(0.3, 100)

                self.dash_sound.play()

                self.player.movementX = (self.player.forward[0] * self.player.velocity_z +
                                         self.player.left[0] * self.player.velocity_x +
                    self.player.back[0] * -self.player.velocity_z +
                    self.player.right[0] * -self.player.velocity_x) * self.player.speed * time.dt

                self.player.movementZ = (self.player.forward[2] * self.player.velocity_z +
                                         self.player.left[2] * self.player.velocity_x +
                    self.player.back[2] * -self.player.velocity_z +
                    self.player.right[2] * -self.player.velocity_x) * self.player.speed * time.dt

    def input(self, key):
        if self.ability_enabled:
            if key == "left shift":
                self.shift_count += 1
                if self.shift_count >= 2 and self.player.ability_bar.value >= 5:
                    self.dashing = True
                    self.player.ability_bar.value -= 5
                    self.player.using_ability = True
                    invoke(setattr, self.player, "using_ability", False, delay=2)
                invoke(setattr, self, "shift_count", 0, delay=0.2)
            if key == "tab":
                self.shift_count += 1
                if self.shift_count >= 1 and self.player.ability_bar.value >= 10:
                    self.player.health += 200
                    self.player.ability_bar.value -= 7.5
                    self.player.using_ability = True
                    if self.player.health > self.player.max_health:
                        self.player.health = 1000
                    invoke(setattr, self.player,
                           "using_ability", False, delay=2)


class SlowMotion(Ability):
    def __init__(self, player, enabled=True):
        super().__init__(player, enabled)

        self.slow_motion = False
        self.start_slow_motion = False
        self.zoomed = False
        self.vignette = Entity(model="quad", texture = "vignette.png", parent = camera.ui, scale_x = 2, enabled = False)

    def update(self):
        if self.ability_enabled:
            if self.start_slow_motion:
                application.time_scale = 0.5
                self.vignette.enable()
                self.player.using_ability = True
                self.start_slow_motion = False

            if self.slow_motion:
                self.player.ability_bar.value -= 2 * time.dt
                self.player.using_ability = True

            if self.player.ability_bar.value <= 1:
                application.time_scale = 1
                self.vignette.disable()
                self.player.using_ability = False
                self.shift_count = 0

    def input(self, key):
        if key == "right mouse down" and not held_keys['shift']:
            if not self.zoomed:
                camera.animate("fov", 35,
                               duration=0.0625, delay=0, auto_destroy=True)

                # camera.fov = 50
                self.zoomed = True
                self.player.crosshair.scale = 1.5

            else:
                if self.zoomed:
                    # camera.fov = 100
                    camera.animate("fov", 110,
                                   duration=0.0625, delay=0, auto_destroy=True)
                    self.zoomed = False
                    self.player.crosshair.scale = 5
        if key == "right mouse up":
            if self.zoomed:
                # camera.fov = 100
                camera.animate("fov", 110,
                               duration=0.0625, delay=0, auto_destroy=True)
                self.zoomed = False
                self.player.crosshair.scale = 5
        if self.ability_enabled:
            if key == "left shift":
                self.shift_count += 1
                if self.shift_count >= 2 and self.player.ability_bar.value >= 5:
                    self.slow_motion = True
                    self.start_slow_motion = True
                invoke(setattr, self, "shift_count", 0, delay=0.2)
            elif key == "left shift up":
                self.slow_motion = False
                application.time_scale = 1
                self.vignette.disable()
                self.player.using_ability = False


class Enemy(Entity):
    def __init__(self, player, move_speed = 20, position = (0, 0, 0), **kwargs):
        super().__init__(
            model = "enemy.obj",
            texture = "level.png",
            position = position,
            collider = "box",
            **kwargs
        )

        self.player = player
        self.move_speed = move_speed
        self.health = 2
        self.damage = 2

        # Pivots
        self.thruster1 = Entity(parent = self, position = (-0.4, -2, 0))
        self.thruster2 = Entity(parent = self, position = (0.4, -2, 0))

        self.barrel = Entity()

        # Shooting
        self.cooldown_t = 0
        self.cooldown_length = 2

        # Particles
        self.particle_t = 0
        self.particle_amount = 0.4

        self.random = Vec3(random.randrange(-10, 10), random.randrange(0, 3), random.randrange(-10, 10))

        # Audio
        self.gun_sound = Audio("pistol.wav", False)
        self.gun_sound.volume = 0.05

    def update(self):
        if distance(self, self.player) > 20:
            self.position += ((self.player.position + self.random) - self.position).normalized() * self.move_speed * time.dt

        self.look_at(self.player)
        self.rotation_z = 0

        self.barrel.position = self.position + (0, 1, 0) + self.forward
        self.barrel.rotation = self.world_rotation

        # Shooting
        if distance_xz(self, self.player) < 100:
            self.cooldown_t += time.dt
            if self.cooldown_t >= self.cooldown_length:
                self.cooldown_t = 0
                self.cooldown_length = random.uniform(1.5, 3)
                Bullet(self, self.barrel.world_position, 700, color.orange).enemy = self  
                if distance_xz(self, self.player) < 40:
                    self.gun_sound.play()  

        # Particles
        self.particle_t += time.dt
        if self.particle_t >= self.particle_amount:
            self.particle_t = 0
            self.particles1 = Particles(self.thruster1.world_position, Vec3(random.random(), -random.random(), random.random()), 10, texture = "jetpack")
            self.particles2 = Particles(self.thruster2.world_position, Vec3(random.random(), -random.random(), random.random()), 10, texture = "jetpack")

    def reset_pos(self):
        self.position = Vec3(random.randint(-100, 300), random.randint(0, 50), random.randint(-100, 300))

class BigEnemy(Enemy):
    def __init__(self, player, move_speed = 10, position = (0, 0, 0), **kwargs):
        super().__init__(
            player, move_speed, position, **kwargs
        )

        self.model = "bigenemy"
        self.cooldown_length = 3
        self.damage = 4
        self.health = 4




class Gun(Entity):
    def __init__(self, player, equipped = True, **kwargs):
        super().__init__(
            parent = camera,
            scale = 0.3,
            position = (0.5, -0.75, 1.7),
            **kwargs
        )
        
        self.player = player
        self.map = self.player.map
        self.tip = Entity(parent = self, position = (-0.5, 1.3, 1.5))

        self.pos_x = 0.5
        self.pos_y = -0.75

        # Pivot
        self.pivot = Entity(parent = camera, position = (0.5, -0.75, 1.7))

        # Cooldown
        self.cooldown_t = 0
        self.cooldown_length = 0.3
        self.can_shoot = True
        self.started_shooting = False

        # Damage
        self.damage = 2
        # Spring
        self.spring = Spring()
        self.start_spring = False

        # Camera Shake amount
        self.shake_divider = 70

        # Gun type
        self.gun_type = "pistol"
        self.charged = False
        self.equipped = equipped

        # Audio
        self.gun_sound = Audio("pistol.wav", False)
        self.destroyed_enemy = Audio("destroyed.wav", False)
        self.gun_sound.volume = 0.8
        self.destroyed_enemy.volume = 0.1

    def update(self):
        if self.player.enabled:
            if self.equipped:
                self.cooldown_t += time.dt
                if self.cooldown_t >= self.cooldown_length:
                    self.cooldown_t = 0
                    self.can_shoot = True

                    if held_keys["left mouse"] and not self.started_shooting:
                        if self.gun_type == "minigun":
                            if self.charged:
                                self.shoot()
                        else:
                            self.shoot()

                # Springs
                if self.start_spring:
                    gun_movement = self.spring.update(time.dt)
                    self.spring.shove(Vec3(mouse.x, mouse.y, 0))
                    self.x = gun_movement.x + self.pos_x
                    self.y = gun_movement.y + self.pos_y

            if not self.equipped:
                # Pivot Springs
                pivot_movement = self.spring.update(time.dt)
                self.spring.shove(Vec3(mouse.x, mouse.y, 0))
                self.pivot.x = pivot_movement.x + self.pos_x
                self.pivot.y = pivot_movement.y + self.pos_y

    def shoot(self):
        # Spawn bullet
        if self.equipped:
            if self.gun_type == "pistol":
                Bullet(self, self.tip.world_position)
                
                self.gun_sound.clip = "pistol.wav"
                self.gun_sound.volume = 0.8
                self.gun_sound.play()

            elif self.gun_type == "shotgun":
                for i in range(random.randint(2, 4)):
                    b = Bullet(self, self.tip.world_position, randomness = 10)

                self.gun_sound.clip = "shotgun.wav"
                self.gun_sound.volume = 0.8
                self.gun_sound.play()
            elif self.gun_type == "rifle":
                Bullet(self, self.tip.world_position)

                self.gun_sound.clip = "rifle.wav"
                self.gun_sound.volume = 0.8
                self.gun_sound.play()
            elif self.gun_type == "minigun":
                Bullet(self, self.tip.world_position)

                self.shooting = True
                self.gun_sound.clip = "minigun.wav"
                self.gun_sound.volume = 0.8
                self.gun_sound.play()

            # Animate the gun
            if self.gun_type == "pistol" or self.gun_type == "shotgun":
                self.animate_rotation((-30, 0, 0), duration = 0.1, curve = curve.linear)
                self.animate("z", 1, duration = 0.03, curve = curve.linear)
                self.animate("z", 1.5, 0.2, delay = 0.1, curve = curve.linear)
                self.animate_rotation((-15, 0, 0), 0.2, delay = 0.1, curve = curve.linear)
                self.animate_rotation((0, 0, 0), 0.4, delay = 0.12, curve = curve.linear)
            elif self.gun_type == "rifle":
                self.animate_rotation((-20, 0, 0), duration = 0.1, curve = curve.linear)
                self.animate("z", 1.2, duration = 0.03, curve = curve.linear)
                self.animate("z", 1.5, 0.2, delay = 0.1, curve = curve.linear)
                self.animate_rotation((-10, 0, 0), 0.2, delay = 0.1, curve = curve.linear)
                self.animate_rotation((0, 0, 0), 0.4, delay = 0.12, curve = curve.linear)
            elif self.gun_type == "minigun":
                self.animate_rotation((-10, 0, 0), duration = 0.05, curve = curve.linear)
                self.animate("z", 1, duration = 0.015, curve = curve.linear)
                self.animate("z", 1.5, 0.2, delay = 0.05, curve = curve.linear)
                self.animate_rotation((-5, 0, 0), 0.2, delay = 0.05, curve = curve.linear)
                self.animate_rotation((0, 0, 0), 0.4, delay = 0.06, curve = curve.linear)

            self.can_shoot = False
            
            # Camera Shake
            self.player.shake_camera(0.1, self.shake_divider)

    def equip(self):
        self.equipped = True
        self.on_equipped()

    def input(self, key):
        if key == "left mouse down" and self.can_shoot:
            if self.gun_type == "minigun":
                if self.charged:
                    self.shoot()
                    self.started_shooting = True
                    invoke(setattr, self, "started_shooting", False, delay = self.cooldown_length / 2)
                else:
                    self.barrel.animate("rotation_z", self.barrel.rotation_z + 720, 1)
                    invoke(setattr, self, "charged", True, delay = 1)

                self.player.speed = 2
            else:
                self.shoot()
                self.started_shooting = True
                invoke(setattr, self, "started_shooting", False, delay = self.cooldown_length / 2)

        elif key == "left mouse up":
            if hasattr(self, "shooting"):
                self.shooting = False
            self.charged = False
            self.player.speed = 5

    def on_enable(self):
        self.on_equipped()
        
    def on_equipped(self): 
        self.y = -2
        self.rotation_x = 50
        try:
            self.animate("y", self.pos_y, duration = 0.4, curve = curve.linear)
        except AttributeError:
            self.animate("y", -0.5, duration = 0.4, curve = curve.linear)
        self.animate("rotation_x", 0, duration = 0.4, curve = curve.linear)
        invoke(setattr, self, "start_spring", True, delay = 0.4)

    def on_disable(self):
        self.start_spring = False

class Bullet(Entity):
    def __init__(self, gun, pos, speed = 2000, trail_colour = color.hex("#00baff"), randomness = 0):
        super().__init__(
            model = "bullet.obj",
            texture = "level.png",
            scale = 0.08,
            position = pos
        )

        self.gun = gun
        self.speed = speed
        self.hit_player = False
        self.randomness = Vec3(random.randint(-10, 10) * random.randint(-1, 1), random.randint(-10, 10) * random.randint(-1, 1), random.randint(-10, 10) * random.randint(-1, 1)) * Vec3(randomness)
        self.enemy = None

        self.trail_thickness = 8
        self.trail = TrailRenderer(self.trail_thickness, trail_colour, color.clear, 5, parent = self)

        if hasattr(self.gun, "tip"):
            self.rotation = camera.world_rotation
            self.is_player = True
            self.no_point = False
        else:
            self.world_rotation = self.gun.world_rotation
            self.is_player = False

        if self.is_player:
            if mouse.hovered_entity:
                if mouse.hovered_entity != self.gun.player.map:
                    self.hovered_point = mouse.hovered_entity
                    self.animate("position", Vec3(self.hovered_point.world_position) + (self.forward * 10000) + self.randomness, distance(self.hovered_point.world_position + (self.forward * 10000), self.gun.player) / 150, curve = curve.linear)
                else:
                    self.hovered_point = mouse.world_point
                    self.animate("position", Vec3(self.hovered_point) + self.randomness + (self.forward * 10000), distance(self.hovered_point + (self.forward * 10000), self.gun.player) / 150, curve = curve.linear)
                
            else:
                self.animate("position", self.world_position + (self.forward * 10000) + self.randomness, 5, curve = curve.linear)
                self.no_point = True
            
            destroy(self, 2)

    def update(self):   
        if self.is_player:
            if not self.no_point:
                if self.hovered_point != self.gun.player.map and not isinstance(self.hovered_point, LVector3f):
                    if distance(self, self.hovered_point) < 3 and self.hovered_point != self.gun.player:
                        for i in range(2):
                            p = Particles(self.hovered_point.world_position, Vec3(random.random(), random.randrange(-10, 10, 1) / 10, random.random()), spray_amount = 10, model = "particles")
                            
                        self.hovered_point.health -= self.gun.damage
                        self.hovered_point.texture = "hit.png"
                        invoke(setattr, self.hovered_point, "texture", "level", delay = 0.1)
                        if self.hovered_point.health <= 0:
                            for i in range(6):
                                p = Particles(self.hovered_point.world_position, Vec3(random.random(), random.randrange(-10, 10, 1) / 10, random.random()), spray_amount = 10, model = "particles", texture = "destroyed")
                            self.hovered_point.reset_pos()
                            self.hovered_point.health = 2
                            self.gun.player.shot_enemy()
                            self.gun.destroyed_enemy.play() 
                        
                        destroy(self)
                else:
                    if self.gun.gun_type != "shotgun":
                        if distance(self, self.hovered_point) < 3 and self.hovered_point != self.gun.player:
                            for i in range(2):
                                p = Particles(self.hovered_point - (self.forward * 10), Vec3(random.random(), random.random(), random.random()), 30, model = "particles")

                            destroy(self)
                    else:
                        level_ray = raycast(self.world_position, self.forward, distance = 3, traverse_target = self.gun.player.map, ignore = [self, self.gun, self.gun.player])
                        if level_ray.hit:
                            for i in range(2):
                                p = Particles(self.hovered_point - (self.forward * 10), Vec3(random.random(), random.random(), random.random()), 30, model = "particles")

                            destroy(self)
        else:
            self.position += self.forward * self.speed * time.dt

            level_ray = raycast(self.world_position, self.forward, distance = 3, traverse_target = self.gun.player.map, ignore = [self, self.gun])
            if distance(self, self.gun.player) <= 2:
                if not self.hit_player:
                    self.gun.player.health -= self.enemy.damage
                    self.gun.player.healthbar.value = self.gun.player.health
                    self.hit_player = True
                destroy(self)
            if level_ray.hit:
                destroy(self)
            destroy(self, delay = 2)

class Rocket(Entity):
    def __init__(self, gun, pos, speed = 100, trail_colour = color.hex("#00baff"), randomness = 0, cooldown = 3):
        super().__init__(
            model = "rocket.obj",
            texture = "level.png",
            position = pos,
            parent = gun
        )

        self.gun = gun
        self.speed = speed
        self.randomness = Vec3(random.randint(-10, 10) * random.randint(-1, 1), random.randint(-10, 10) * random.randint(-1, 1), random.randint(-10, 10) * random.randint(-1, 1)) * Vec3(randomness)
        self.pos = pos
        self.trail_colour = trail_colour
        self.no_point = False
        self.cooldown = cooldown

        self.fired = False
        self.gun.ready = True

    def fire(self):
        self.fired = True
        self.parent = scene
        self.gun.ready = False
        self.position = self.gun.world_position
        self.rotation = camera.world_rotation
        
        self.trail_thickness = 8
        self.trail = TrailRenderer(self.trail_thickness, self.trail_colour, color.clear, 5, parent = self)
    
        if mouse.hovered_entity:
            if mouse.hovered_entity != self.gun.player.map:
                self.hovered_point = mouse.hovered_entity
                self.animate("position", Vec3(self.hovered_point.world_position) + (self.forward) + self.randomness, distance(self.hovered_point.world_position + (self.forward), self.gun.player) / 150, curve = curve.linear)
            else:
                self.hovered_point = mouse.world_point
                self.animate("position", Vec3(self.hovered_point) + self.randomness + (self.forward), distance(self.hovered_point + (self.forward), self.gun.player) / 150, curve = curve.linear)
            self.no_point = False
        else:
            self.animate("position", self.world_position + (self.forward * 400) + self.randomness, 1.9, curve = curve.linear)
            self.no_point = True

    def update(self): 
        if self.fired and not self.no_point:
            if self.hovered_point != self.gun.player.map and not isinstance(self.hovered_point, LVector3f):
                if distance(self, self.hovered_point) < 5 and self.hovered_point != self.gun.player:
                    for i in range(2):
                        p = Particles(self.hovered_point.world_position, Vec3(random.random(), random.randrange(-10, 10, 1) / 10, random.random()), spray_amount = 10, model = "particles")
                    
                    for enemy in self.gun.player.enemies:
                        if distance(self, enemy) < 10:
                            enemy.health -= (self.gun.damage - distance(self, enemy))
                            enemy.texture = "hit.png"
                            invoke(setattr, enemy, "texture", "level", delay = 0.1)
                            if enemy.health <= 0:
                                for i in range(6):
                                    p = Particles(enemy.world_position, Vec3(random.random(), random.randrange(-10, 10, 1) / 10, random.random()), spray_amount = 10, model = "particles", texture = "destroyed")
                                enemy.reset_pos()
                                enemy.health = 2
                                self.gun.player.shot_enemy()
                                self.gun.destroyed_enemy.play() 
                    
                    destroy(self)
            else:
                level_ray = raycast(self.world_position, self.forward, distance = 3, traverse_target = self.gun.player.map, ignore = [self, self.gun, self.gun.player])
                if level_ray.hit:
                    for i in range(10):
                        p = Particles(self.hovered_point - (self.forward * 10), Vec3(random.random(), random.random(), random.random()), 30, model = "particles", texture = "jetpack")

                    destroy(self)

class Pistol(Gun):
    def __init__(self, player, equipped = True, **kwargs):
        super().__init__(
            model = "pistol.obj",
            texture = "level.png",
            player = player,
            equipped = equipped,
            **kwargs
        )

        self.gun_type = "pistol"
        self.equip()

class Shotgun(Gun):
    def __init__(self, player, equipped = False, **kwargs):
        super().__init__(
            model = "shotgun.obj",
            texture = "level.png",
            player = player,
            equipped = equipped,
            **kwargs
        )

        self.gun_type = "shotgun"
        self.tip.z = 2

        self.pos_x = 0.6
        self.pos_y = -0.5

        self.damage = 4

        self.shake_divider = 40
        self.cooldown_length = 0.8

class Rifle(Gun):
    def __init__(self, player, equipped = True, **kwargs):
        super().__init__(
            model = "rifle.obj",
            texture = "level.png",
            player = player,
            equipped = equipped,
            **kwargs
        )

        self.gun_type = "rifle"
        self.tip.z = 8
        self.tip.y = 0

        self.pos_x = 0.6
        self.pos_y = -0.5

        self.damage = 0.8

        self.shake_divider = 80
        self.cooldown_length = 0.2
        self.equip()

class MiniGun(Gun):
    def __init__(self, player, equipped = False, **kwargs):
        super().__init__(
            model = "minigun.obj",
            texture = "level.png",
            player = player,
            equipped = equipped,
            **kwargs
        )

        self.barrel = Entity(model = "minigun-barrel", texture = "level", parent = self)
        self.shooting = False

        self.gun_type = "minigun"
        self.tip.z = 7
        self.tip.y = 0

        self.pos_x = 0.9
        self.pos_y = -1.2

        self.damage = 0.5

        self.shake_divider = 70
        self.cooldown_length = 0.1

    def update(self):
        if self.shooting:
            self.barrel.rotation_z += 400 * time.dt
        return super().update()
    
class RocketLauncher(Gun):
    def __init__(self, player, equipped = False, **kwargs):
        super().__init__(
            model = "rocket-launcher.obj",
            texture = "level.png",
            player = player,
            equipped = equipped,
            **kwargs
        )

        self.gun_type = "rocket launcher"
        self.tip.z = 8
        self.tip.y = 0

        self.pos_x = 0.6
        self.pos_y = -0.5

        self.damage = 10
        self.ready = True

        self.shake_divider = 20
        self.cooldown_length = 5

        self.rocket = Rocket(self, (0, 0, 0))

    def input(self, key):
        if key == "left mouse down" and self.ready:
            self.rocket.fire()
            self.animate_rotation((-40, 0, 0), duration = 0.1, curve = curve.linear)
            self.animate("z", 0.5, duration = 0.1, curve = curve.linear)
            self.animate("z", 1.5, 0.2, delay = 0.1, curve = curve.linear)
            self.animate_rotation((-5, 0, 0), 0.5, delay = 0.15, curve = curve.linear)
            self.animate_rotation((0, 0, 0), 0.6, delay = 0.5, curve = curve.linear)
            
            self.player.shake_camera(0.1, self.shake_divider)
            invoke(self.reload, delay = 3)

            self.gun_sound.clip = "rocket_launcher.wav"
            self.gun_sound.play()

    def reload(self):
        self.rocket = Rocket(self, (0, 0, 0))

class Spring:
    def __init__(self, mass = 5, force = 50, damping = 4, speed = 4):
        self.target = Vec3()
        self.position = Vec3()
        self.velocity = Vec3()

        self.iterations = 8

        self.mass = mass
        self.force = force
        self.damping = damping
        self.speed = speed

    def shove(self, force):
        x, y, z = force.x, force.y, force.z

        if x != x:
            x = 0
        if y != y:
            y = 0
        if z != z:
            z = 0

        self.velocity = self.velocity + Vec3(x, y, z)

    def update(self, dt):
        scaledDeltaTime = min(dt,1) * self.speed / self.iterations

        for i in range(self.iterations):
            iterationForce = self.target - self.position
            acceleration = (iterationForce * self.force) / self.mass

            acceleration = acceleration - self.velocity * self.damping

            self.velocity = self.velocity + acceleration * scaledDeltaTime
            self.position = self.position + self.velocity * scaledDeltaTime

        return self.position


class MainMenu(Entity):
    def __init__(self, player, floating_islands, deserted_sands, mountainous_valley):
        super().__init__(
            parent = camera.ui
        )

        # Player
        self.player = player

        # Maps
        self.floating_islands = floating_islands
        self.deserted_sands = deserted_sands
        self.mountainous_valley = mountainous_valley

        # Menus
        self.mainmenu = Entity(parent = self, enabled = False)
        self.end_screen = Entity(parent = self, enabled = False)
        self.pause_menu = Entity(parent = self, enabled = False)
        self.maps_menu = Entity(parent = self, enabled = False)

        self.menus = [self.mainmenu, self.pause_menu, self.maps_menu]
        self.index = 0

        self.enable_end_screen = True

        # Animate the Menus
        for menu in self.menus:
            def animate_in_menu(menu = menu):
                for i, e in enumerate(menu.children):
                    e.original_scale = e.scale
                    e.scale -= 0.01
                    e.animate_scale(e.original_scale, delay = i * 0.05, duration = 0.1, curve = curve.out_quad)

                    e.alpha = 0
                    e.animate("alpha", 0.7, delay = i * 0.05, duration = 0.1, curve = curve.out_quad)

                    if hasattr(e, "text_entity"):
                        e.text_entity.alpha = 0
                        e.text_entity.animate("alpha", 1, delay = i * 0.05, duration = 0.1)

            if menu != self.pause_menu:
                menu.on_enable = animate_in_menu

        self.mainmenu.enable()

        # Main Menu
        self.start_button = Button(text = "Start", color = colourH, highlight_color = colourH, scale_y = 0.1, scale_x = 0.3, y = 0.05, parent = self.mainmenu,on_click=self.start)
        self.maps_button = Button(text = "Maps", color = colourN, highlight_color = colourN, scale_y = 0.1, scale_x = 0.3, y = -0.07, parent = self.mainmenu,on_click=self.show_maps_menu)
        self.quit_button = Button(text="Quit", color=colourN, highlight_color=colourN, scale_y=0.1,
                                  scale_x=0.3, y=-0.19, parent=self.mainmenu, on_click=application.quit)

        invoke(setattr, self.start_button, "color", colourH, delay = 0.5)

        # Endscreen
        retry_text = Text("Retry", scale = 4, origin = (0, 0.5), x = 0, y = 0.1, z = -100, parent = self.end_screen)
        press_enter = Text("Press Enter", scale = 2, origin = (0, 0.5), x = 0, y = 0, z = -100, parent = self.end_screen)
        self.highscore_text = Text(text = str(self.player.highscore), origin = (0, 0), size = 0.05, scale = (0.8, 0.8), position = window.top - (0, 0.1), parent = self.end_screen, z = -100)        
        
        camera.overlay.parent = self.end_screen
        camera.overlay.color = color.rgba(220, 0, 0, 100)

        # Pause Menu
        self.resume_button = Button(text = "Resume", color = colourN, highlight_color = colourN, scale_y = 0.1, scale_x = 0.3, y = 0.05, parent = self.pause_menu,on_click=lambda : self.pause(False,False))
        self.retry_button = Button(text = "Retry", color = colourN, highlight_color = colourN, scale_y = 0.1, scale_x = 0.3, y = -0.07, parent = self.pause_menu,on_click=self.retry_game)
        self.mainmenu_button = Button(text = "Main Menu", color = colourN, highlight_color = colourN, scale_y = 0.1, scale_x = 0.3, y = -0.19, parent = self.pause_menu,on_click=self.nav_to_main_menu)
        self.pause_overlay = Entity(parent = self.pause_menu, model = "quad", scale = 99, color = color.rgba(20, 20, 20, 100), eternal = True, z = 10)

        # Maps Menu
        self.back_button = Button(text = "Back To Previes Menu", color = colourN, highlighted_color = colourH, scale_y = 0.1, scale_x = 0.3, y = 0.20, parent = self.maps_menu,on_click=lambda : self.nav_to_main_menu())
        self.floating_islands_button = Button(text = "Floating Islands", color = colourN, highlighted_color = colourH, scale_y = 0.1, scale_x = 0.3, y = 0.05, parent = self.maps_menu,on_click=lambda : self.who_map(0))
        self.deserted_sands_button = Button(text = "Deserted Sands", color = colourN, highlighted_color = colourH, scale_y = 0.1, scale_x = 0.3, y = -0.07, parent = self.maps_menu,on_click=lambda : self.who_map(1))
        self.mountainous_valley_button = Button(text = "Mountainous Valley", color = colourN, highlighted_color = colourH, scale_y = 0.1, scale_x = 0.3, y = -0.19, parent = self.maps_menu,on_click=lambda : self.who_map(2))

    def update(self):
        if self.player.health <= 0:
            if self.enable_end_screen:
                self.end_screen.enable()
                self.enable_end_screen = False
                self.player.check_highscore()
                application.time_scale = 0.1
                mouse.locked = False
                self.player.dead = True
                self.highscore_text.text = "Highscore: " + str(self.player.highscore)

        if held_keys["enter"] and not self.enable_end_screen:
            mouse.locked = True
            self.player.reset()
            self.end_screen.disable()
            self.enable_end_screen = True
            
    def input(self, key):
        if key == "up arrow":
            for menu in self.menus:
                if menu.enabled:
                    self.index -= 1
                    if self.index <= -1:
                        self.index = 0
                    if isinstance(menu.children[self.index], Button):
                        menu.children[self.index].color = colourH
                        menu.children[self.index].highlight_color = colourH
                        for button in menu.children:
                            if menu.children[self.index] != button:
                                button.color = colourN
                                button.highlight_color = colourN
                    else:
                        self.index += 1

        elif key == "down arrow":
            for menu in self.menus:
                if menu.enabled:
                    self.index += 1
                    if self.index > len(menu.children) - 1:
                        self.index = len(menu.children) - 1
                    if isinstance(menu.children[self.index], Button):
                        menu.children[self.index].color = colourH
                        menu.children[self.index].highlight_color = colourH
                        for button in menu.children:
                            if menu.children[self.index] != button:
                                button.color = colourN
                                button.highlight_color = colourN
                    else:
                        self.index -= 1

        if key == "enter":
            # Main Menu
            if self.mainmenu.enabled:
                if highlighted(self.start_button):
                    mouse.locked = True

                    self.start()
                elif highlighted(self.maps_button):
                    self.maps_menu.enable()
                    self.mainmenu.disable()
                    self.update_menu(self.maps_menu)
                elif highlighted(self.quit_button):
                    application.quit()

            # Pause Menu
            elif self.pause_menu.enabled:
                if highlighted(self.resume_button):
                    mouse.locked = True

                    self.pause(False, False)
                elif highlighted(self.retry_button):
                    mouse.locked = True
                    self.player.reset()
                    self.pause_menu.disable()
                elif highlighted(self.mainmenu_button):
                    self.player.disable()
                    self.player.reset()
                    for enemy in self.player.enemies:
                        enemy.disable()
                    self.mainmenu.enable()
                    self.pause_menu.disable()
                    self.update_menu(self.pause_menu)

            # Maps menu
            elif self.maps_menu.enabled:
                if highlighted(self.floating_islands_button):
                    for map in self.player.maps:
                        map.disable()
                    self.floating_islands.enable()
                    mouse.locked = True

                    self.player.map = self.floating_islands
                    self.start()
                if highlighted(self.deserted_sands_button):
                    mouse.locked = True

                    for map in self.player.maps:
                        map.disable()
                    self.deserted_sands.enable()
                    self.player.map = self.deserted_sands
                    self.start()
                if highlighted(self.mountainous_valley_button):
                    self.nav_to_main_menu()
                if highlighted(self.mountainous_valley_button):
                    mouse.locked = True

                    for map in self.player.maps:
                        map.disable()
                    self.mountainous_valley.enable()
                    self.player.map = self.mountainous_valley
                    self.player.position = (-5, 200, -10)
                    self.start() 

            # End Screen
            if self.player.health <= 0:
                mouse.locked = True
                self.end_screen.disable()
                self.enable_end_screen = True
                self.player.reset()

        if key == "escape":
            if self.maps_menu.enabled:
                self.maps_menu.disable()
                self.mainmenu.enable()

            # Pause Menu
            if self.player.enabled:
                self.pause()
                self.update_menu(self.pause_menu)

    def start(self):
        mouse.locked = True

        self.mainmenu.disable()
        self.maps_menu.disable()
        for enemy in self.player.enemies:
            enemy.enable()
        self.player.enable()

    def pause(self, opposite = True, pause = True):
        mouse.locked = False
        if opposite:
            self.pause_menu.enabled = not self.pause_menu.enabled
            if self.pause_menu.enabled:
                application.time_scale = 0.1
            else:
                mouse.locked = True

                application.time_scale = 1
        else:
            if pause:
                self.pause_menu.enable()
                application.time_scale = 0.1
            else:
                mouse.locked = True

                self.pause_menu.disable()
                application.time_scale = 1

    def update_menu(self, menu):
        for c in menu.children:
            c.color = colourN
            c.highlighted_color = colourN
        menu.children[0].color = colourH
        menu.children[0].highlighted_color = colourH
        self.index = 0
    def show_maps_menu(self):
        self.maps_menu.enable()
        self.mainmenu.disable()
        self.update_menu(self.maps_menu)

    def retry_game(self):
        mouse.locked = True
        self.player.reset()
        self.pause_menu.disable()

    def nav_to_main_menu(self):
        mouse.locked = False

        self.player.disable()
        self.player.reset()
        for enemy in self.player.enemies:
            enemy.disable()
        self.mainmenu.enable()
        self.pause_menu.disable()
        self.maps_menu.disable()
        self.update_menu(self.pause_menu)

    def who_map(self,map_index):
        if map_index == 0 :
            mouse.locked = True
            for map in self.player.maps:
                map.disable()
            self.floating_islands.enable()
            self.player.map = self.floating_islands
            self.start()
        elif map_index == 1 :
            mouse.locked = True
            for map in self.player.maps:
                map.disable()
            self.deserted_sands.enable()
            self.player.map = self.deserted_sands
            self.start()
        elif map_index == 2 :
            mouse.locked = True
            for map in self.player.maps:
                map.disable()
            self.mountainous_valley.enable()
            self.player.map = self.mountainous_valley
            self.player.position = (-5, 200, -10)
            self.start() 
        else :
            raise ValueError("The Values On Avrg 0,1,2")


class FloatingIslands(Entity):
    def __init__(self, player, **kwargs):
        super().__init__(
            model = "floatingislands.obj", 
            texture = "level.png", 
            collider = "mesh",
            **kwargs
        )

        self.jumppad1 = JumpPad(player, jump_height = 80, position = (-28, 4, -61), rotation_y = -6, level = self)
        self.jumppad2 = JumpPad(player, jump_height = 30, position = (6.5, 4, 53), rotation_y = 30, level = self)
        self.jumppad3 = JumpPad(player, jump_height = 70, position = (31, 14, 37), rotation_y = 30, level = self)

class DesertedSands(Entity):
    def __init__(self, player, **kwargs):
        super().__init__(
            model = "desertedsands.obj", 
            texture = "level.png", 
            collider = "mesh",
            **kwargs
        )

        self.jumppad1 = JumpPad(player, jump_height = 80, position = (2, -24, 0), level = self, rotation_y = -40, scale = 5, model = None)
        self.jumppad2 = JumpPad(player, jump_height = 80, position = (0, 45, 3), level = self, rotation_y = -40, scale = 5, model = None)

class MountainousValley(Entity):
    def __init__(self, player, **kwargs):
        super().__init__(
            model = "mountainous_valley.obj", 
            texture = "level.png", 
            collider = "mesh",
            scale = 3,
            y = -200,
            **kwargs
        )

        self.jumppad1 = JumpPad(player, jump_height = 100, position = (-6, 26, -44), level = self, rotation_y = -40, scale = 5, model = None)
        self.jumppad2 = JumpPad(player, jump_height = 100, position = (-89, 2, 45), rotation_y = -20, scale = 5, level = self, model = None)
        self.jumppad3 = JumpPad(player, jump_height = 100, position = (58, 39, -1), rotation_y = 40, scale = 4, level = self, model = None)
        self.jumppad4 = JumpPad(player, jump_height = 100, position = (81, -5, 29), rotation_y = 20, scale = 5, level = self, model = None)
        self.jumppad5 = JumpPad(player, jump_height = 100, position = (-49, 115, 27), rotation_y = 0, level = self, model = None)
        self.jumppad6 = JumpPad(player, jump_height = 100, position = (-13, -19, 121), rotation_y = 0, level = self, model = None)

        self.player = player

    def update(self):
        if self.player.y <= -90:
            self.player.position = (-5, 200, -10)
            self.player.rotation_y = -270
            self.player.velocity_x = 0
            self.player.velocity_y = 0
            self.player.velocity_z = 0
            self.player.health -= 5
            self.player.healthbar.value = self.player.health

class JumpPad(Entity):
    def __init__(self, player, jump_height = 100, model = "jumppad.obj", position = (0, 0, 0), level = None, scale = 6, **kwargs):
        super().__init__(
            model = model,
            texture = "level",
            position = position,
            scale = scale,
            **kwargs
        )

        self.player = player
        self.jump_height = jump_height
        self.level = level

        if not self.show:
            self.visible = False

    def update(self):
        if self.visible and distance(self, self.player) < 10:
            self.player.velocity_y = self.jump_height

    def input(self, key):
        if self.level.enabled:
            self.visible = True
        elif not self.level.enabled:
            self.visible = False


class Particles(Entity):
    def __init__(self, position, direction = Vec3(random.random(), random.random(), random.random()), spray_amount = 30, **kwargs):
        super().__init__(
            model = "particle.obj",
            texture = "particle.png",
            scale = 0.2,
            position = position, 
            rotation_y = random.random() * 360
        )
        
        self.direction = direction
        self.spray_amount = spray_amount
        self.prev_spray_amount = self.spray_amount

        self.destroy(1)

        for key, value in kwargs.items():
            setattr(self, key ,value)

    def update(self):
        self.position += self.direction * self.spray_amount * time.dt
        self.spray_amount -= self.prev_spray_amount * time.dt

    def destroy(self, delay = 1):
        self.fade_out(duration = 0.2, delay = 0.7, curve = curve.linear)
        destroy(self, delay)
        del self



def sign(x): return -1 if x < 0 else (1 if x > 0 else 0)
def y_dir(y): return -1 if y < 0 else (1 if y > 0 else -1)


class Player(Entity):
    def __init__(self, position, speed=5, jump_height=20):
        super().__init__(
            model="cube",
            position=position,
            scale=(1.3, 1, 1.3),
            visible_self=False,
            rotation_y=-270
        )

        # Camera
        # mouse.locked = True
        camera.parent = self
        camera.position = (0, 2, 0)
        camera.rotation = (0, 0, 0)
        camera.fov = 110

        # Crosshair
        # self.crosshair = Entity(model="quad", color=color.black, parent=camera, rotation_z=45, position=(
        #     0, 0, 1), scale=1, z=100, always_on_top=True,)
        crosshair_texture = load_texture('crosshair.png')

        # Create the crosshair entity
        self.crosshair = Entity(model="quad", color=color.black, parent=camera, position=(
            0, 0, 1), scale=5, z=100, always_on_top=True, texture=crosshair_texture)

        # Player values
        self.speed = speed
        self.jump_count = 0
        self.jump_height = jump_height
        self.jumping = False
        self.can_move = True
        self.grounded = False

        # Velocity
        self.velocity = (0, 0, 0)
        self.velocity_x = self.velocity[0]
        self.velocity_y = self.velocity[1]
        self.velocity_z = self.velocity[2]

        # Movement
        self.movementX = 0
        self.movementZ = 0

        self.mouse_sensitivity = 50

        # Map
        self.map = None
        self.maps = []

        # Camera Shake
        self.can_shake = False
        self.shake_duration = 0.1
        self.shake_timer = 0
        self.shake_divider = 70  # the less, the more camera shake

        # Guns
        self.rifle = Rifle(self, True, enabled=True)
        self.shotgun = Shotgun(self, True, enabled=False)
        self.pistol = Pistol(self, True, enabled=False)
        self.minigun = MiniGun(self, True, enabled=False)
        self.rocket_launcher = RocketLauncher(self, True, enabled=False)
        

        self.guns = [self.rifle, self.shotgun, self.pistol,
                     self.minigun, self.rocket_launcher]
        self.current_gun = 0

        # Abilities
        self.rope = Rope(self)
        self.dash_ability = DashAbility(self)
        self.slow_motion = SlowMotion(self, False)

        self.primary_abilities = [self.rope]
        self.secondary_abilities = [self.dash_ability, self.slow_motion]

        # Sliding
        self.sliding = False
        self.slope = False
        self.slide_pivot = Entity()
        self.set_slide_rotation = False

        # Enemies
        self.enemies = []

        # Health
        self.health = 1000
        self.max_health = 1000
        self.healthbar = HealthBar(1000, bar_color=color.hex(
            "#ff1e1e"), roundness=0, y=window.bottom_left[1] + 0.1, scale_y=0.03, scale_x=0.3)
        self.healthbar.text_entity.disable()
        self.ability_bar = HealthBar(25, bar_color=color.hex(
            "#50acff"), roundness=0, position=window.bottom_left + (0.12, 0.05), scale_y=0.007, scale_x=0.2)
        self.ability_bar.text_entity.disable()
        self.ability_bar.animation_duration = 0

        self.using_ability = False
        self.dead = False

        # Score
        self.score = 0
        self.score_text = Text(text=str(self.score), origin=(
            0, 0), size=0.05, scale=(1, 1), position=window.top_right - (0.1, 0.1))
        self.score_text.text = str(self.score)

        # Get highscore from json file
        path = os.path.dirname(sys.argv[0])
        self.highscore_path = os.path.join(path, "./highscores/highscore.json")

        try:
            with open(self.highscore_path, "r") as hs:
                highscore_file = json.load(hs)
                self.highscore = highscore_file["highscore"]
        except FileNotFoundError:
            with open(self.highscore_path, "w+") as hs:

                json.dump({"highscore": 0}, hs, indent=4)
                self.highscore = 0

        # Audio
        self.fall_sound = Audio("fall.wav", False)

    def jump(self):
        self.jumping = True
        self.velocity_y = self.jump_height
        self.jump_count += 1

    def update(self):
        movementY = self.velocity_y / 75
        self.velocity_y = clamp(self.velocity_y, -70, 100)

        direction = (0, sign(movementY), 0)

        # Main raycast for collision
        y_ray = raycast(origin=self.world_position, direction=(
            0, y_dir(self.velocity_y), 0), traverse_target=self.map, ignore=[self, ])

        if y_ray.distance <= self.scale_y * 1.5 + abs(movementY):
            if not self.grounded:
                self.velocity_y = 0
                self.grounded = True
                self.fall_sound.play()

            # Check if hitting a wall or steep slope
            if y_dir(self.velocity_y) == -1:
                if y_ray.world_normal.y > 0.7 and y_ray.world_point.y - self.world_y < 0.5:
                    # Set the y value to the ground's y value
                    if not held_keys["space"]:
                        self.y = y_ray.world_point.y + 1.4
                    self.jump_count = 0
                    self.jumping = False
        else:
            if not self.rope.can_rope:
                self.velocity_y -= 40 * time.dt
                self.grounded = False
                self.jump_count = 1

            self.y += movementY * 50 * time.dt

        # Sliding
        if self.sliding:
            camera.y = 0
            if y_ray.distance <= 2:
                slide_ray = raycast(self.world_position + self.forward, self.forward,
                                    distance=8, traverse_target=self.map, ignore=[self, ])
                if not slide_ray.hit:
                    if hasattr(y_ray.world_point, "y"):
                        self.y = y_ray.world_point.y + 1.4

                        if y_ray.world_normal[2] * 10 < 0:
                            self.velocity_z -= y_ray.world_normal[2] * \
                                10 * time.dt
                        if y_ray.world_normal[2] * 10 > 0:
                            self.velocity_z += y_ray.world_normal[2] * \
                                10 * time.dt
                elif slide_ray.hit:
                    self.velocity_z = -10
                    if self.velocity_z <= -1:
                        self.velocity_z = -1
                    if hasattr(y_ray.world_point, "y"):
                        self.y = y_ray.world_point.y + 1.4

                if self.set_slide_rotation:
                    self.slide_pivot.rotation = camera.world_rotation
                    self.set_slide_rotation = False
        else:
            camera.y = 2

        # Velocity / Momentum
        if not self.sliding:
            movement = 10 if y_ray.distance < 5 and not self.rope.can_rope else 5

            if held_keys["w"] or held_keys["up arrow"]:
                self.velocity_z += movement * time.dt
            else:
                self.velocity_z = lerp(
                    self.velocity_z, 0 if y_ray.distance < 5 else 1, time.dt * 3)
            if held_keys["a"] or held_keys["left arrow"]:
                self.velocity_x += movement * time.dt
            else:
                self.velocity_x = lerp(
                    self.velocity_x, 0 if y_ray.distance < 5 else 1, time.dt * 3)
            if held_keys["s"] or held_keys["down arrow"]:
                self.velocity_z -= movement * time.dt
            else:
                self.velocity_z = lerp(
                    self.velocity_z, 0 if y_ray.distance < 5 else 1, time.dt * 3)
            if held_keys["d"] or held_keys["right arrow"]:
                self.velocity_x -= movement * time.dt
            else:
                self.velocity_x = lerp(
                    self.velocity_x, 0 if y_ray.distance < 5 else -1, time.dt * 3)

        # Movement
        if y_ray.distance <= 5 or self.rope.can_rope:
            if not self.sliding:
                self.movementX = (self.forward[0] * self.velocity_z +
                                  self.left[0] * self.velocity_x +
                                  self.back[0] * -self.velocity_z +
                                  self.right[0] * -self.velocity_x) * self.speed * time.dt

                self.movementZ = (self.forward[2] * self.velocity_z +
                                  self.left[2] * self.velocity_x +
                                  self.back[2] * -self.velocity_z +
                                  self.right[2] * -self.velocity_x) * self.speed * time.dt
        else:
            air_movementX = 0.5 if self.movementX < 0.5 and self.movementX > -0.5 else 0.2
            air_movementZ = 0.5 if self.movementZ < 0.5 and self.movementZ > -0.5 else 0.2

            self.movementX += (self.forward[0] * held_keys["w"] * air_movementX +
                               self.left[0] * held_keys["a"] * air_movementX +
                               self.back[0] * held_keys["s"] * air_movementX +
                               self.right[0] * held_keys["d"] * air_movementX) / 2 * time.dt

            self.movementZ += (self.forward[2] * held_keys["w"] * air_movementZ +
                               self.left[2] * held_keys["a"] * air_movementZ +
                               self.back[2] * held_keys["s"] * air_movementZ +
                               self.right[2] * held_keys["d"] * air_movementZ) / 2 * time.dt

        # Collision Detection
        if self.movementX != 0:
            direction = (sign(self.movementX), 0, 0)
            x_ray = raycast(origin=self.world_position, direction=direction,
                            traverse_target=self.map, ignore=[self, ])

            if x_ray.distance > self.scale_x / 2 + abs(self.movementX):
                self.x += self.movementX

        if self.movementZ != 0:
            direction = (0, 0, sign(self.movementZ))
            z_ray = raycast(origin=self.world_position, direction=direction,
                            traverse_target=self.map, ignore=[self, ])

            if z_ray.distance > self.scale_z / 2 + abs(self.movementZ):
                self.z += self.movementZ

        # Camera
        camera.rotation_x -= mouse.velocity[1] * self.mouse_sensitivity
        self.rotation_y += mouse.velocity[0] * self.mouse_sensitivity
        camera.rotation_x = min(max(-90, camera.rotation_x), 90)

        # Camera Shake
        if self.can_shake:
            camera.position = self.prev_camera_pos + \
                Vec3(random.randrange(-10, 10), random.randrange(-10, 10),
                     random.randrange(-10, 10)) / self.shake_divider

        # Abilities
        n = clamp(self.ability_bar.value, 0, self.ability_bar.max_value)
        self.ability_bar.bar.scale_x = n / self.ability_bar.max_value

        if not self.using_ability and self.ability_bar.value < 30:
            self.ability_bar.value += 15 * time.dt
        if self.ability_bar.value <= 0:
            self.rope.rope_pivot.position = self.rope.position
            self.rope.rope.disable()
            self.rope.can_rope = False

        # Resets the player if falls of the map
        if self.y <= -100:
            self.position = (-60, 15, -16)
            self.rotation_y = -270
            self.velocity_x = 0
            self.velocity_y = 0
            self.velocity_z = 0
            self.health -= 5
            self.healthbar.value = self.health

    def input(self, key):
        if key == "space":
            if self.jump_count < 1:
                self.jump()

        if key == "left shift":
            self.sliding = False  # turned sliding off for now
            self.set_slide_rotation = True
        elif key == "left shift up":
            self.sliding = False

        if key == "1":
            if not self.rifle.enabled:
                for gun in self.guns:
                    gun.disable()
                self.rifle.enable()
        elif key == "2":
            if not self.shotgun.enabled:
                for gun in self.guns:
                    gun.disable()
                self.shotgun.enable()
        elif key == "3":
            if not self.pistol.enabled:
                for gun in self.guns:
                    gun.disable()
                self.pistol.enable()
        elif key == "4":
            if not self.minigun.enabled:
                for gun in self.guns:
                    gun.disable()
                self.minigun.enable()
        elif key == "5":
            if not self.rocket_launcher.enabled:
                for gun in self.guns:
                    gun.disable()
                self.rocket_launcher.enable()

        if key == "scroll up":
            self.current_gun = (self.current_gun - 1) % len(self.guns)
            for i, gun in enumerate(self.guns):
                if i == self.current_gun:
                    gun.enable()
                else:
                    gun.disable()

        if key == "scroll down":
            self.current_gun = (self.current_gun + 1) % len(self.guns)
            for i, gun in enumerate(self.guns):
                if i == self.current_gun:
                    gun.enable()
                else:
                    gun.disable()

    def shot_enemy(self):
        if not self.dead:
            self.score += 1
            self.score_text.text = str(self.score)
            if self.score > self.highscore:
                self.animate_text(self.score_text, 1.8, 1)

    def reset(self):
        if self.map == self.maps[0] or self.map == self.maps[1]:
            self.position = (-60, 15, -16)
        elif self.map == self.maps[2]:
            self.position = (-5, 200, -10)
        self.rotation = (0, -270, 0)
        self.velocity_x = 0
        self.velocity_y = 0
        self.velocity_z = 0
        self.health = 1000
        self.healthbar.value = self.health
        self.ability_bar.value = 30
        self.dead = False
        self.score = 0
        self.score_text.text = self.score
        application.time_scale = 1
        for enemy in self.enemies:
            enemy.reset_pos()

    def shake_camera(self, duration=0.1, divider=70):
        self.can_shake = True
        self.shake_duration = duration
        self.shake_divider = divider
        self.prev_camera_pos = camera.position
        invoke(setattr, self, "can_shake", False, delay=self.shake_duration)
        invoke(setattr, camera, "position",
               self.prev_camera_pos, delay=self.shake_duration)

    def check_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(self.highscore_path, "w") as hs:
                json.dump({"highscore": int(self.highscore)}, hs, indent=4)

    def animate_text(self, text, top=1.2, bottom=0.6):
        """
        Animates the scale of text
        """
        text.animate_scale((top, top, top), curve=curve.out_expo)
        invoke(text.animate_scale, (bottom, bottom, bottom), delay=0.4)



class SceneLighting(Entity):
    def __init__(self, ursina, player, sun_direction = (0.75, -1, 0.5), sun_color = (1.0, 0.7, 0.3, 1.0), ambient_color = (0.6, 0.65, 0.7, 0.5), 
                 shadow_resolution = 2048, shadow_size = 100, shadow_height = 200, shadow_bias = 0.0, shadow_camera_direction_offset = True, 
                 shadow_filter_radius = 3.0, shadow_filter_samples = 10.0, soft_shadows = True,
                 sky_texture = None, sky_color = (1.0, 1.0, 1.0, 1.5), gamma = 2.0):

        self.player = player
        self.shadow_camera_direction_offset = (shadow_size / 2.0) * shadow_camera_direction_offset

        # noise texture creation for random values in shader
        def createNoiseTexture(tex_size):
            noise_img = PNMImage(tex_size, tex_size)

            for x in range(tex_size):
                for y in range(tex_size):
                    noise_img.setRed(x, y, random.random())

            noise_texture = Texture("noise texture")
            noise_texture.load(noise_img)
            noise_texture.setMagfilter(SamplerState.FT_nearest)
            noise_texture.setMagfilter(SamplerState.FT_nearest)
            return noise_texture


        # sky
        if (sky_texture):
            self.sky_shader = Shader.load(lang = Shader.SL_GLSL, vertex = "shaders/sky_vert.glsl", fragment = "shaders/sky_frag.glsl")
            self.sky = Entity(model = "sphere", texture = sky_texture, scale = 5000, double_sided = True, color = sky_color)
            self.sky.setShader(self.sky_shader)
            self.sky.setShaderInput("gamma", gamma)

        # bufffer creation
        win_prop = WindowProperties(size = (shadow_resolution, shadow_resolution))
        fb_prop = FrameBufferProperties()
        fb_prop.setRgbColor(1)
        fb_prop.setAlphaBits(1)
        fb_prop.setDepthBits(1)
        shadow_buffer = ursina.graphicsEngine.makeOutput(ursina.pipe, "shadow buffer", -100, fb_prop, win_prop, GraphicsPipe.BFRefuseWindow, ursina.win.getGsg(), ursina.win)

        shadow_tex = Texture()
        shadow_buffer.addRenderTexture(shadow_tex, GraphicsOutput.RTM_bind_or_copy,
                                 GraphicsOutput.RTP_depth_stencil)
        shadow_tex.setMinfilter(SamplerState.FT_nearest)
        shadow_tex.setMagfilter(SamplerState.FT_nearest)
        shadow_tex.setWrapU(Texture.WM_border_color)
        shadow_tex.setWrapV(Texture.WM_border_color)
        shadow_tex.setBorderColor((1.0, 1.0, 1.0, 1.0))

        shadow_buffer.setClearActive(GraphicsOutput.RTP_depth, True)
        shadow_buffer.setClearValue(GraphicsOutput.RTP_depth, 1.0)

        # shadow camera creation
        self.shadow_cam = Camera("shadow camera")
        shadow_cam_lens = OrthographicLens()
        shadow_cam_lens.setFilmSize(shadow_size, shadow_size)
        shadow_cam_lens.setFilmOffset(0, 0)
        shadow_cam_lens.setNearFar(-shadow_height, shadow_height)
        self.shadow_cam.setLens(shadow_cam_lens)

        self.shadow_cam_np = ursina.render.attachNewNode(self.shadow_cam)
        self.shadow_cam_np.lookAt(sun_direction)

        display_region = shadow_buffer.makeDisplayRegion()
        display_region.disableClears()
        display_region.setActive(True)
        display_region.setCamera(self.shadow_cam_np)

        # main shader
        self.main_shader = Shader.load(lang = Shader.SL_GLSL, vertex = "shaders/main_vert.glsl", fragment = "shaders/main_frag.glsl")

        ursina.render.setShaderInput("shadowMap", shadow_tex)
        ursina.render.setShaderInput("shadowCam", self.shadow_cam_np)
        ursina.render.setShaderInput("shadowDir", sun_direction)
        ursina.render.setShaderInput("shadowSize", (shadow_size, shadow_height, shadow_resolution))
        ursina.render.setShaderInput("shadowBias", shadow_bias)
        ursina.render.setShaderInput("shadowFilterResolution", (shadow_filter_radius, shadow_filter_samples))
        ursina.render.setShaderInput("softShadows", soft_shadows)

        shadow_texel_size = shadow_size / shadow_resolution
        shadow_texel_radius = sqrt(shadow_texel_size**2 + shadow_texel_size**2) / 2.0
        ursina.render.setShaderInput("shadowTexelRadius", shadow_texel_radius)

        ursina.render.setShaderInput("sunColor", sun_color)
        ursina.render.setShaderInput("ambientColor", ambient_color)

        noise_tex = createNoiseTexture(128)
        ursina.render.setShaderInput("noiseTex", noise_tex)

        ursina.render.setShaderInput("gamma", gamma)

        main_camera_initializer = NodePath(PandaNode("main camera initializer"))
        main_camera_initializer.setShader(self.main_shader)
        ursina.cam.node().setInitialState(main_camera_initializer.getState())

        # shadow shader
        self.shadow_shader = Shader.load(lang = Shader.SL_GLSL, vertex = "shaders/shadow_vert.glsl", fragment = "shaders/shadow_frag.glsl")

        shadow_camera_initializer = NodePath(PandaNode("shadow camera initializer"))
        shadow_camera_initializer.setShader(self.shadow_shader)
        self.shadow_cam.setInitialState(shadow_camera_initializer.getState())

        # debug shadow buffer
        # ursina.accept("v", ursina.bufferViewer.toggleEnable)


    def update(self):
        self.shadow_cam_np.setPos(self.player.world_position + camera.forward.normalized() * self.shadow_camera_direction_offset)


class TrailRenderer(Entity):
    def __init__(self, thickness=10, color=color.white, end_color=color.clear, length=6, **kwargs):
        super().__init__(**kwargs)
        self.renderer = Entity(
            model=Mesh(
                vertices=[self.world_position for i in range(length)],
                colors=[lerp(end_color, color, i/length*2)
                        for i in range(length)],
                mode='line',
                thickness=thickness,
                static=False
            )
        )
        self._t = 0
        self.update_step = .025

    def update(self):
        self._t += time.dt
        if self._t >= self.update_step:
            self._t = 0
            self.renderer.model.vertices.pop(0)
            self.renderer.model.vertices.append(self.world_position)
            self.renderer.model.generate()

    def on_destroy(self):
        destroy(self.renderer)


# if __name__ == '__main__':
#     app = Ursina()
#     window.color = color.black
#     mouse.visible = False
#     player = Entity()
#     player.graphics = Entity(parent=player, scale=.1, model='circle')
#     trail_renderer = TrailRenderer(
#         parent=player, thickness=100, color=color.yellow, length=6)

#     pivot = Entity(parent=player)
#     trail_renderer = TrailRenderer(
#         parent=pivot, x=.1, thickness=20, color=color.orange)
#     trail_renderer = TrailRenderer(
#         parent=pivot, y=1, thickness=20, color=color.orange)
#     trail_renderer = TrailRenderer(
#         parent=pivot, thickness=2, color=color.orange, alpha=.5, position=(.4, .8))
#     trail_renderer = TrailRenderer(
#         parent=pivot, thickness=2, color=color.orange, alpha=.5, position=(-.5, .7))

#     def update():
#         player.position = lerp(player.position, mouse.position*10, time.dt*4)

#         if pivot:
#             pivot.rotation_z -= 3
#             pivot.rotation_x -= 2

#     def input(key):
#         if key == 'space':
#             destroy(pivot)

#     app.run()
mouse.locked = False
Text.default_font = "./assets/Roboto.ttf"
Text.default_resolution = Text.size * 1080
# Set the desired frame rate
target_fps = 60

# Adjust the time.dt value to achieve the target frame rate
time.dt = 1 / target_fps
app = Ursina()
window.fullscreen = True
window.borderless = False
window.windowed_size = window.size * 0.75
window.cog_button.disable()

# window.size = window.screen_resolution
# window.collider_counter.disable()
# window.entity_counter.disable()
window.fps_counter.enable()
window.exit_button.disable()
window.fps_counter.scale = (2,2,2)
scene.fog_density = 0.001
window.size = window.screen_resolution

def toggle_fullscreen():
    window.fullscreen = not window.fullscreen


def toggle_maxmize():
    if window.size == (1280, 720):
        window.size = window.screen_resolution
    else :
        window.size = (1280, 720)

# Bind the 'f' key to toggle fullscreen
key_handler = Entity(ignore_paused=True)
key_handler.input = lambda key: toggle_fullscreen() if key == 'f' else toggle_maxmize() if key == 'm' else None

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
        load_model(m)

    for i, t in enumerate(textures_to_load):
        load_texture(t)

try:
    threading.Thread.join().start(load_assets)
    # .start_new_thread(function = load_assets, args = "")
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
for enemy in range(20):
    i = random.randint(0, 2)
    if i == 0:
        e = BigEnemy(player, position = Vec3(random.randint(-50, 50)))
    else:
        e = Enemy(player, position = Vec3(random.randint(-50, 50)))

    e.disable()
    player.enemies.append(e)

mainmenu = MainMenu(player, floating_islands, deserted_sands, mountainous_valley)

# Lighting + Shadows
scene_lighting = SceneLighting(ursina = app, player = player, sun_direction = (-0.7, -0.9, 0.5), shadow_resolution = 4096, sky_texture = "sky")

def input(key):
    if key == "g":
        player.reset()

# def update():
#     print(player.position)

app.run()