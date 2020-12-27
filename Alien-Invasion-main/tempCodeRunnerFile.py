self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.background.image, self.background.rect)
        self.ship.blitme()