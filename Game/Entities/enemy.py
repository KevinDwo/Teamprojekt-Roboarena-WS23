
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Game.gameState import GameState

from pygame.key import ScancodeWrapper
import pygame

from Game.Entities.actor import Actor


class Enemy(Actor):
    def __init__(self, gameState: 'GameState', texturePath: str, position: pygame.Vector2):
        texture = pygame.image.load(texturePath)
        direction = 0
        currentSpeed = 1
        hp = 50
        maxSpeed = 2
        acceleration = 0.05
        brakeAcceleration = 0.02
        rotationalSpeed = 2
        bulletSpeed = 3
        shootCooldown = 500
        shootRange = 200
        super().__init__(gameState, texture, position, direction, currentSpeed, maxSpeed, acceleration,
                         brakeAcceleration, rotationalSpeed, hp, bulletSpeed, shootCooldown, shootRange)

    def move(self):
        if self.isAlive:                                                             # Implement 2 player Support
            targets = [x for x in self.gameState.robots if x.isAlive]
            targets.sort(key=lambda x: (x.position - self.position).length())
            if not targets:
                return
            target = targets[0]

            finalAngle = pygame.Vector2.angle_to(pygame.Vector2(0, 0), target.position - self.position) % 360
            self.direction = finalAngle
            """" Fix me: Smooth turning
            if finalAngle - self.direction < - self.rotationalSpeed:
                self.rotateLeft()
                self.brake()
            elif finalAngle - self.direction > self.rotationalSpeed:
                self.rotateRight()
                self.brake()
            else:
                self.accelerate()
            """
            bullet = self.shoot()
            if bullet:
                self.gameState.entities.append(bullet)
        super().move()
        """"
        for deadlyObstacle in self.gameState.deadlyObstacles:
            if self.getHitBox().colliderect(deadlyObstacle):
                self.hit(1)
        """

    def handleKeyPresses(self, pressed: ScancodeWrapper):
        return

    def kill(self):
        super().kill(False)

    def hit(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.kill()
        else:
            self.hasHealth = (True, self.hp)
        super().updateHp(self.hasHealth)
