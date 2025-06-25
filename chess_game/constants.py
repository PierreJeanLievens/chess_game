import pygame
import os

Width, Height = 760,760
Rows, Cols = 8,8
Square = Width//Rows


#Colors
Bg = (47,79,79)
Black = (0,0,0)
White = (255,255,255)
beige = (245,245,220)
brown_chocolate = (210,105,30)
brown = (87,16,16)
cornsilk = (255,248,220)
Green = (0,255,0)


Path = "chess_game/chess_images"


#Black pieces
Black_Knight = pygame.transform.scale(pygame.image.load(os.path.join(Path, "bKN.png" )), (Square, Square ))
Black_Bishop= pygame.transform.scale(pygame.image.load(os.path.join(Path, "bB.png" )), (Square, Square ))
Black_King = pygame.transform.scale(pygame.image.load(os.path.join(Path, "bK.png" )), (Square, Square ))
Black_Queen = pygame.transform.scale(pygame.image.load(os.path.join(Path, "bQ.png" )), (Square, Square ))
Black_Pawn = pygame.transform.scale(pygame.image.load(os.path.join(Path, "bP.png" )), (Square, Square ))
Black_Rook = pygame.transform.scale(pygame.image.load(os.path.join(Path, "bR.png" )), (Square, Square ))

#White pieces
White_Knight = pygame.transform.scale(pygame.image.load(os.path.join(Path, "wKN.png" )), (Square, Square ))
White_Bishop= pygame.transform.scale(pygame.image.load(os.path.join(Path, "wB.png" )), (Square, Square ))
White_King = pygame.transform.scale(pygame.image.load(os.path.join(Path, "wK.png" )), (Square, Square ))
White_Queen = pygame.transform.scale(pygame.image.load(os.path.join(Path, "wQ.png" )), (Square, Square ))
White_Pawn = pygame.transform.scale(pygame.image.load(os.path.join(Path, "wP.png" )), (Square, Square ))
White_Rook = pygame.transform.scale(pygame.image.load(os.path.join(Path, "wR.png" )), (Square, Square ))