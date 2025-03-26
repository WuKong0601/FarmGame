import pygame
from settings import *
from random import randint, choice
from timer import Timer
from support import import_folder
from sprites import Generic

class Animal(pygame.sprite.Sprite):
    def __init__(self, animal_type, pos, groups, collision_sprites, scale=1.0):
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

        # Movement attributes
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = randint(50, 100)

        # Collision
        self.collision_sprites = collision_sprites
        self.hitbox = self.rect.copy().inflate(-self.rect.width * 0.5, -self.rect.height * 0.7)

        # Timers
        self.walk_timer = Timer(randint(2000, 5000))
        self.idle_timer = Timer(randint(1000, 3000))
        self.walk_timer.activate()
        self.is_moving = True
        self.change_direction()

    def change_direction(self):
        """Thay đổi hướng di chuyển ngẫu nhiên"""
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Loại bỏ (0,0) để luôn di chuyển khi không idle
        self.direction = pygame.math.Vector2(choice(directions))
        self.direction = self.direction.normalize() if self.direction.magnitude() > 0 else self.direction
        self.speed = randint(50, 100)

    def collision(self, direction):
        """Xử lý va chạm với vật cản"""
        for sprite in self.collision_sprites:
            if hasattr(sprite, 'hitbox'):
                if sprite.hitbox.colliderect(self.hitbox):
                    if direction == 'horizontal':
                        if self.direction.x > 0:  # moving right
                            self.hitbox.right = sprite.hitbox.left
                        if self.direction.x < 0:  # moving left
                            self.hitbox.left = sprite.hitbox.right
                        self.rect.centerx = self.hitbox.centerx
                        self.pos.x = self.hitbox.centerx
                        self.change_direction()

                    if direction == 'vertical':
                        if self.direction.y > 0:  # moving down
                            self.hitbox.bottom = sprite.hitbox.top
                        if self.direction.y < 0:  # moving up
                            self.hitbox.top = sprite.hitbox.bottom
                        self.rect.centery = self.hitbox.centery
                        self.pos.y = self.hitbox.centery
                        self.change_direction()

    def _scale_image(self):
        """Scale tất cả frame animation theo tỷ lệ"""
        for status in self.animations:
            scaled_frames = []
            for frame in self.animations[status]:
                new_width = int(frame.get_width() * self.scale)
                new_height = int(frame.get_height() * self.scale)
                scaled_frames.append(pygame.transform.scale(frame, (new_width, new_height)))
            self.animations[status] = scaled_frames
        self.image = self.animations[self.status][self.frame_index]

    def _update_hitbox(self):
        """Cập nhật hitbox theo tỷ lệ scale"""
        self.hitbox = self.rect.inflate(
            -self.rect.width * 0.3 * self.scale,
            -self.rect.height * 0.6 * self.scale
        )

    def import_assets(self):
        """Import animation assets"""
        self.animations = {'idle': [], 'walk': []}
        for animation in self.animations.keys():
            full_path = f'../graphics/animals/{self.animal_type}/{animation}'
            self.animations[animation] = import_folder(full_path)

    def animate(self, dt):
        """Xử lý animation"""
        self.frame_index += 6 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        old_center = self.rect.center
        self.image = self.animations[self.status][int(self.frame_index)]
        self.rect = self.image.get_rect(center=old_center)
        self._update_hitbox()

    def move(self, dt):
        """Xử lý di chuyển"""
        self.walk_timer.update()
        self.idle_timer.update()

        # Chuyển đổi giữa các trạng thái di chuyển và idle
        if self.is_moving:
            if not self.walk_timer.active:
                self.is_moving = False
                self.status = 'idle'
                self.direction = pygame.math.Vector2()
                self.idle_timer.activate()
                self.idle_timer.duration = randint(1000, 3000)
        else:
            if not self.idle_timer.active:
                self.is_moving = True
                self.change_direction()
                self.walk_timer.activate()
                self.walk_timer.duration = randint(2000, 5000)

        # Di chuyển nếu đang trong trạng thái di chuyển
        if self.is_moving:
            self.status = 'walk'
            self.pos.x += self.direction.x * self.speed * dt
            self.hitbox.centerx = round(self.pos.x)
            self.rect.centerx = self.hitbox.centerx
            self.collision('horizontal')

            self.pos.y += self.direction.y * self.speed * dt
            self.hitbox.centery = round(self.pos.y)
            self.rect.centery = self.hitbox.centery
            self.collision('vertical')

        # Giới hạn di chuyển trong màn hình
        self.rect.clamp_ip(pygame.Rect(100, 100, SCREEN_WIDTH - 200, SCREEN_HEIGHT - 200))
        self.hitbox.center = self.rect.center

    def update(self, dt):
        """Cập nhật trạng thái mỗi frame"""
        self.move(dt)
        self.animate(dt)


class Fish(Animal):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(
            animal_type='fish',  # Thư mục graphics/animals/fish chứa animation
            pos=pos,
            groups=groups,
            collision_sprites=collision_sprites,
            scale=1.0
        )
        self.speed = randint(50, 80)  # Tốc độ chậm hơn động vật trên cạn
        self.z = LAYERS['water']  # Hiển thị dưới lớp nước

    def change_direction(self):
        """Cá chỉ di chuyển ngang"""
        directions = [(-1, 0), (1, 0)]  # Chỉ di chuyển trái/phải
        self.direction = pygame.math.Vector2(choice(directions))

    def move(self, dt):
        """Ghi đè phương thức move để cá không bị giới hạn bởi clamp_ip"""
        self.walk_timer.update()
        self.idle_timer.update()

        if self.is_moving:
            if not self.walk_timer.active:
                self.is_moving = False
                self.status = 'idle'
                self.direction = pygame.math.Vector2()
                self.idle_timer.activate()
        else:
            if not self.idle_timer.active:
                self.is_moving = True
                self.change_direction()
                self.walk_timer.activate()

        if self.is_moving:
            self.status = 'walk'
            self.pos.x += self.direction.x * self.speed * dt
            self.hitbox.centerx = round(self.pos.x)
            self.rect.centerx = self.hitbox.centerx
            self.collision('horizontal')

    def create_bubble(self):
        bubble = Generic(
            pos=self.rect.midtop,
            surf=pygame.Surface((8, 8), pygame.SRCALPHA),
            groups=self.groups(),
            z=LAYERS['water']
        )
        pygame.draw.circle(bubble.image, (173, 216, 230), (4, 4), 4)
        # Tự hủy sau 1 giây
        Timer(1000, lambda: bubble.kill()).activate()