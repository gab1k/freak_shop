from interface_setup import *
from facade import ClientRequests

class MenuView:
    def show_enter_menu(self, DataBaseRequester):
        ReturnToMenu = 0
        LoginText = RegistrationFont.render("Логин :", False, (0, 0, 0))
        PassowrdText = RegistrationFont.render("Пароль : ", False, (0, 0, 0))
        ConfirmText = RegistrationFont.render("Войти", False, (0, 0, 0))
        LoginButton = Rect(ScreenWidth * 5 / 38, ScreenHeight / 5, 1000, 150)
        PasswordButton = Rect(ScreenWidth * 5 / 38, ScreenHeight * 6 / 10, 1000, 150)
        ConfirmButton = Rect(ScreenWidth * 27 / 38, ScreenHeight / 3 - 40, 400, 400)
        EyeIconButton = Rect(ScreenWidth / 80, ScreenHeight * 6 / 10 - 20, 220, 180)
        BackButton = Rect(ScreenWidth * 6 / 7, ScreenHeight * 1 / 30, 180, 180)
        LoginInput = ""
        PasswordInput = ""
        active = 0
        password_show = False
        while True:
            screen.fill(RegistrationBackgroundColor)
            for event in pygame.event.get():
                if event.type == QUIT:
                    ReturnToMenu = 1
                if event.type == MOUSEBUTTONDOWN:
                    MousePosition = pygame.mouse.get_pos()
                    if LoginButton.collidepoint(MousePosition):
                        active = 1
                    elif PasswordButton.collidepoint(MousePosition):
                        active = 2
                    else:
                        active = 0
                    if ConfirmButton.collidepoint(MousePosition):
                        LoginSuccess = DataBaseRequester.login_user(LoginInput,  PasswordInput)
                        if (LoginSuccess):
                            ReturnToMenu = 2
                        else:
                            ReturnToMenu = 1
                        #add real checks later
                    if EyeIconButton.collidepoint(MousePosition):
                        password_show = not password_show
                    if BackButton.collidepoint(MousePosition):
                        ReturnToMenu = 1
                if event.type == KEYDOWN:
                    if active == 1:
                        if event.key == K_BACKSPACE:
                            LoginInput = LoginInput[:-1]
                        elif len(LoginInput) < MaxLoginLength:
                            LoginInput += event.unicode
                    if active == 2:
                        if event.key == K_BACKSPACE:
                            PasswordInput = PasswordInput[:-1]
                        elif len(PasswordInput) < MaxPasswordLength:
                            PasswordInput += event.unicode

            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_ESCAPE]:
                ReturnToMenu = 1

            pygame.draw.rect(screen, RegistrationButtonColor, LoginButton)
            pygame.draw.rect(screen, RegistrationButtonColor, PasswordButton)
            pygame.draw.rect(screen, RegistrationButtonColor, ConfirmButton)
            screen.blit(LoginText, (LoginButton.midtop[0] - 100, LoginButton.midtop[1] - 80))
            screen.blit(PassowrdText, (PasswordButton.midtop[0] - 120, PasswordButton.midtop[1] - 80))
            screen.blit(ConfirmText, (ConfirmButton.center[0] - 100, ConfirmButton.center[1] - 60))

            LoginInputText = RegistrationFont.render(LoginInput, False, (0, 0, 0))
            screen.blit(LoginInputText, (LoginButton.left, LoginButton.center[1] - 55))

            if password_show:
                EyeIconImage = pygame.image.load("src/img/EyeIcon.png").convert_alpha()
                screen.blit(pygame.transform.scale(EyeIconImage, (220, 180)),
                            (ScreenWidth / 80, ScreenHeight * 6 / 10 - 20))
                PassowrdInputText = RegistrationFont.render(PasswordInput, False, (0, 0, 0))
                screen.blit(PassowrdInputText, (PasswordButton.left, PasswordButton.center[1] - 55))
            else:
                EyeIconImage = pygame.image.load("src/img/EyeIconCrossed.png").convert_alpha()
                screen.blit(pygame.transform.scale(EyeIconImage, (250, 160)),
                            (ScreenWidth / 80 - 10, ScreenHeight * 6 / 10 - 10))
                PassowrdInputText = RegistrationFont.render('*' * len(PasswordInput), False, (0, 0, 0))
                screen.blit(PassowrdInputText, (PasswordButton.left, PasswordButton.center[1] - 30))

            BackIconImage = pygame.image.load("src/img/BackIcon.png").convert_alpha()
            screen.blit(pygame.transform.scale(BackIconImage, (180, 180)),
                        (ScreenWidth * 6 / 7, ScreenHeight * 1 / 30))
            pygame.display.update()

            if ReturnToMenu == 1:
                return "menu"
            elif ReturnToMenu == 2:
                return "gameplay"

    def show_resgistration_menu(self, DataBaseRequester):
        ReturnToMenu = 0
        LoginText = RegistrationFont.render("Логин :", False, (0, 0, 0))
        NicknameText = RegistrationFont.render("Имя :", False, (0, 0, 0))
        PassowrdText = RegistrationFont.render("Пароль : ", False, (0, 0, 0))
        RepeatPasswordText = RegistrationFont.render("Повторите пароль : ", False, (0, 0, 0))
        ConfirmText = RegistrationFont.render("Регистрация", False, (0, 0, 0))
        LoginButton = Rect(ScreenWidth * 5 / 38, ScreenHeight / 12 + 20, 1000, 150)
        NicknameButton = Rect(ScreenWidth * 5 / 38, ScreenHeight / 4 + 60, 1000, 150)
        PasswordButton = Rect(ScreenWidth * 5 / 38, ScreenHeight / 2 + 20, 1000, 150)
        RepeatPasswordButton = Rect(ScreenWidth * 5 / 38, ScreenHeight * 7 / 10 + 40, 1000, 150)
        ConfirmButton = Rect(ScreenWidth * 27 / 38, ScreenHeight / 3 - 40, 400, 400)
        EyeIconButton1 = Rect(ScreenWidth / 80, ScreenHeight / 2 - 20, 220, 180)
        EyeIconButton2 = Rect(ScreenWidth / 80, ScreenHeight * 7/ 10 - 20, 220, 180)
        BackButton = Rect(ScreenWidth * 6 / 7, ScreenHeight * 1 / 30, 180, 180)
        LoginInput = ""
        PasswordInput = ""
        RepeatPasswordInput = ""
        NicknameInput = ""
        password_show = False
        repeat_password_show = False
        active = 0
        while True:
            screen.fill(RegistrationBackgroundColor)
            for event in pygame.event.get():
                if event.type == QUIT:
                    ReturnToMenu = 1
                if event.type == MOUSEBUTTONDOWN:
                    MousePosition = pygame.mouse.get_pos()
                    if LoginButton.collidepoint(MousePosition):
                        active = 1
                    elif PasswordButton.collidepoint(MousePosition):
                        active = 2
                    elif RepeatPasswordButton.collidepoint(MousePosition):
                        active = 3
                    elif NicknameButton.collidepoint(MousePosition):
                        active = 4
                    else:
                        active = 0
                    if ConfirmButton.collidepoint(MousePosition):
                        RegisterSuccess = DataBaseRequester.register_user(LoginInput, NicknameInput, PasswordInput,
                                                                          RepeatPasswordInput)
                        #add checker later
                        ReturnToMenu = 1
                    if EyeIconButton1.collidepoint(MousePosition):
                        password_show = not password_show
                    if EyeIconButton2.collidepoint(MousePosition):
                        repeat_password_show = not repeat_password_show
                    if BackButton.collidepoint(MousePosition):
                        ReturnToMenu = 1

                if event.type == KEYDOWN:
                    if active == 1:
                        if event.key == K_BACKSPACE:
                            LoginInput = LoginInput[:-1]
                        elif len(LoginInput) < MaxLoginLength:
                            LoginInput += event.unicode
                    if active == 2:
                        if event.key == K_BACKSPACE:
                            PasswordInput = PasswordInput[:-1]
                        elif len(PasswordInput) < MaxPasswordLength:
                            PasswordInput += event.unicode
                    if active == 3:
                        if event.key == K_BACKSPACE:
                            RepeatPasswordInput = RepeatPasswordInput[:-1]
                        elif len(RepeatPasswordInput) < MaxPasswordLength:
                            RepeatPasswordInput += event.unicode
                    if active == 4:
                        if event.key == K_BACKSPACE:
                            NicknameInput = NicknameInput[:-1]
                        elif len(NicknameInput) < MaxPasswordLength:
                            NicknameInput += event.unicode

            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_ESCAPE]:
                ReturnToMenu = 1

            pygame.draw.rect(screen, RegistrationButtonColor, LoginButton)
            pygame.draw.rect(screen, RegistrationButtonColor, NicknameButton)
            pygame.draw.rect(screen, RegistrationButtonColor, PasswordButton)
            pygame.draw.rect(screen, RegistrationButtonColor, RepeatPasswordButton)
            pygame.draw.rect(screen, RegistrationButtonColor, ConfirmButton)
            screen.blit(LoginText, (LoginButton.midtop[0] - 100, LoginButton.midtop[1] - 80))
            screen.blit(NicknameText, (NicknameButton.midtop[0] - 80, NicknameButton.midtop[1] - 80))
            screen.blit(PassowrdText, (PasswordButton.midtop[0] - 120, PasswordButton.midtop[1] - 80))
            screen.blit(RepeatPasswordText, (RepeatPasswordButton.midtop[0] - 270, RepeatPasswordButton.midtop[1] - 80))
            screen.blit(ConfirmText, (ConfirmButton.center[0] - 175, ConfirmButton.center[1] - 60))

            LoginInputText = RegistrationFont.render(LoginInput, False, (0, 0, 0))
            NicknameInputText = RegistrationFont.render(NicknameInput, False, (0, 0, 0))
            screen.blit(LoginInputText, (LoginButton.left, LoginButton.center[1] - 55))
            screen.blit(NicknameInputText, (NicknameButton.left, NicknameButton.center[1] - 55))

            if password_show:
                EyeIconImage = pygame.image.load("src/img/EyeIcon.png").convert_alpha()
                screen.blit(pygame.transform.scale(EyeIconImage, (220, 180)),
                            (ScreenWidth / 80, ScreenHeight / 2 + 10))
                PassowrdInputText = RegistrationFont.render(PasswordInput, False, (0, 0, 0))
                screen.blit(PassowrdInputText, (PasswordButton.left, PasswordButton.center[1] - 55))
            else:
                EyeIconImage = pygame.image.load("src/img/EyeIconCrossed.png").convert_alpha()
                screen.blit(pygame.transform.scale(EyeIconImage, (250, 160)),
                            (ScreenWidth / 80 - 10, ScreenHeight  / 2 + 20))
                PassowrdInputText = RegistrationFont.render('*' * len(PasswordInput), False, (0, 0, 0))
                screen.blit(PassowrdInputText, (PasswordButton.left, PasswordButton.center[1] - 30))

            if repeat_password_show:
                EyeIconImage = pygame.image.load("src/img/EyeIcon.png").convert_alpha()
                screen.blit(pygame.transform.scale(EyeIconImage, (220, 180)),
                            (ScreenWidth / 80, ScreenHeight * 7 / 10 + 20))
                RepeatPassowrdInputText = RegistrationFont.render(RepeatPasswordInput, False, (0, 0, 0))
                screen.blit(RepeatPassowrdInputText, (RepeatPasswordButton.left, RepeatPasswordButton.center[1] - 55))
            else:
                EyeIconImage = pygame.image.load("src/img/EyeIconCrossed.png").convert_alpha()
                screen.blit(pygame.transform.scale(EyeIconImage, (250, 160)),
                            (ScreenWidth / 80 - 10, ScreenHeight * 7 / 10 + 30))
                RepeatPassowrdInputText = RegistrationFont.render('*' * len(RepeatPasswordInput), False, (0, 0, 0))
                screen.blit(RepeatPassowrdInputText, (RepeatPasswordButton.left, RepeatPasswordButton.center[1] - 30))

            BackIconImage = pygame.image.load("src/img/BackIcon.png").convert_alpha()
            screen.blit(pygame.transform.scale(BackIconImage, (180, 180)),
                        (ScreenWidth * 6 / 7, ScreenHeight * 1 / 30))
            pygame.display.update()

            if ReturnToMenu == 1:
                return "menu"

    def show_start_menu(self, DataBaseRequester):
        while True:
            screen.fill(RegistrationBackgroundColor)
            EnterButton = Rect(ScreenWidth * 11 / 38, ScreenHeight / 6, 800, 250)
            RegistrationButton = Rect(ScreenWidth * 11 / 38, ScreenHeight / 2, 800, 250)
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if EnterButton.collidepoint(pygame.mouse.get_pos()):
                        return self.show_enter_menu(DataBaseRequester)
                    if RegistrationButton.collidepoint(pygame.mouse.get_pos()):
                        return self.show_resgistration_menu(DataBaseRequester)
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_ESCAPE]:
                sys.exit()
            pygame.draw.rect(screen, RegistrationButtonColor, EnterButton)
            pygame.draw.rect(screen, RegistrationButtonColor, RegistrationButton)
            EnterText = RegistrationFont.render("Войти", False, (0, 0, 0))
            RegistrationText = RegistrationFont.render("Зарегестрироваться", False, (0, 0, 0))
            screen.blit(EnterText, (EnterButton.center[0] - 80, EnterButton.center[1] - 40))
            screen.blit(RegistrationText, (RegistrationButton.center[0] - 270, RegistrationButton.center[1] - 40))
            pygame.display.update()
