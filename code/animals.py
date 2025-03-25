import pygame
from timer import Timer
from settings import *
from random import randint, choice
from timer import Timer
from support import import_folder

class Animal(pygame.sprite.Sprite):
    def __init__(self, animal_type, pos, groups, scale=1.0):
        super().__init__(groups)
        self.animal_type = animal_type
        self.scale = scale
        self.import_assets()
        self.status = 'idle'
        self.frame_index = 0
        self.image = self.animations[self.status][self.frame_index]
        self._scale_image()
        self.rect = self.image.get_rect(center=pos)
        self.z = LAYERS['main']
        self._update_hitbox()
        self.walk_timer = Timer(2000, self.change_direction)  # 2000ms = 2 giây
        self.walk_timer.activate()
        self.direction = pygame.math.Vector2()
        self.speed = randint(50, 100)

    def change_direction(self):
        """Thay đổi hướng di chuyển ngẫu nhiên"""
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]  # Thêm (0,0) để có lúc đứng yên
        self.direction = pygame.math.Vector2(choice(directions))
        # Đặt lại timer với thời gian ngẫu nhiên
        self.walk_timer.duration = randint(1000, 3000)  # 1-3 giây
        self.walk_timer.activate()

    def _scale_image(self):
        """Scale tất cả frame animation theo tỷ lệ"""
        for status in self.animations:
            scaled_frames = []
            for frame in self.animations[status]:
                # Tính toán kích thước mới
                new_width = int(frame.get_width() * self.scale)
                new_height = int(frame.get_height() * self.scale)
                # Scale hình ảnh
                scaled_frames.append(pygame.transform.scale(frame, (new_width, new_height)))
            self.animations[status] = scaled_frames

        # Cập nhật hình ảnh hiện tại
        self.image = self.animations[self.status][self.frame_index]
    # def _scale_image(self):
    #     """Scale tất cả frame animation theo tỷ lệ"""
    #     for status, frames in self.animations.items():
    #         self.animations[status] = [
    #             pygame.transform.scale(
    #                 frame,
    #                 (int(frame.get_width() * self.scale),
    #                  int(frame.get_height() * self.scale))
    #             ) for frame in frames
    #         ]
    #     self.image = self.animations[self.status][self.frame_index]

    def _update_hitbox(self):
        """Cập nhật hitbox theo tỷ lệ scale"""
        self.hitbox = self.rect.inflate(
            -self.rect.width * 0.3 * self.scale,
            -self.rect.height * 0.6 * self.scale
        )

    def animate(self, dt):
        self.frame_index += 6 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0

        # Scale lại ảnh mỗi frame nếu cần
        old_center = self.rect.center
        self.image = self.animations[self.status][int(self.frame_index)]
        self.rect = self.image.get_rect(center=old_center)
        self._update_hitbox()

    def import_assets(self):
        self.animations = {'idle': [], 'walk': []}
        for animation in self.animations.keys():
            full_path = f'../graphics/animals/{self.animal_type}/{animation}'
            self.animations[animation] = import_folder(full_path)

    def change_direction(self):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]
        self.direction = pygame.math.Vector2(choice(directions))
        self.walk_timer.duration = randint(1000, 3000)
        self.walk_timer.activate()

    def animate(self, dt):
        self.frame_index += 4 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        self.image = self.animations[self.status][int(self.frame_index)]

    def move(self, dt):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
            self.status = 'walk'
        else:
            self.status = 'idle'

        self.rect.center += self.direction * self.speed * dt
        self.rect.clamp_ip(pygame.Rect(100, 100, SCREEN_WIDTH - 200, SCREEN_HEIGHT - 200))

    def update(self, dt):
        self.walk_timer.update()
        self.move(dt)
        self.animate(dt)